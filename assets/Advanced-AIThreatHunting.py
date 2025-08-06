import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

plt.ion()

def load_and_aggregate_data():
    \"\"\"Load both normal and attack traffic data and create aggregated dataset\"\"\"
    try:
        # Load normal traffic data
        normal_df = pd.read_csv('NormalNetworkTraffic.csv')
        normal_df['Label'] = 0  # Normal traffic
        
        # Load attack traffic data
        attack_df = pd.read_csv('AttackedNetworkTraffic.csv')
        attack_df['Label'] = 1  # Attack traffic
        
        # Combine datasets
        combined_df = pd.concat([normal_df, attack_df], ignore_index=True)
        
        # Save aggregated dataset
        combined_df.to_csv('AggregateNetworkTraffic.csv', index=False)
        
        print(f\"Normal traffic samples: {len(normal_df)}\")
        print(f\"Attack traffic samples: {len(attack_df)}\")
        print(f\"Total samples: {len(combined_df)}\")
        
        return combined_df
    except FileNotFoundError as e:
        print(f\"Error loading files: {e}\")
        print(\"Please ensure both NormalNetworkTraffic.csv and AttackedNetworkTraffic.csv exist\")
        return None

def preprocess_data(df):
    \"\"\"Preprocess the data for machine learning\"\"\"
    # Make a copy to avoid modifying original
    processed_df = df.copy()
    
    # Encode IP addresses as categorical codes
    processed_df['Source'] = processed_df['Source'].astype('category').cat.codes
    processed_df['Destination'] = processed_df['Destination'].astype('category').cat.codes
    
    # Select features for modeling
    feature_columns = ['Source', 'Destination', 'Length']
    
    # Add additional features if they exist in the data
    if 'Protocol' in processed_df.columns:
        processed_df['Protocol'] = processed_df['Protocol'].astype('category').cat.codes
        feature_columns.append('Protocol')
    
    if 'Time' in processed_df.columns:
        # Convert time to seconds since start
        processed_df['Time'] = pd.to_datetime(processed_df['Time'], errors='coerce')
        if not processed_df['Time'].isna().all():
            processed_df['TimeSeconds'] = (processed_df['Time'] - processed_df['Time'].min()).dt.total_seconds()
            feature_columns.append('TimeSeconds')
    
    return processed_df, feature_columns

def perform_clustering_analysis(df, feature_columns):
    \"\"\"Perform enhanced clustering analysis with multiple cluster numbers\"\"\"
    features = df[feature_columns].fillna(0)
    
    # Test different numbers of clusters
    cluster_numbers = [2, 3, 4, 5]
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.ravel()
    
    for i, n_clusters in enumerate(cluster_numbers):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(features)
        
        # Plot clustering results
        scatter = axes[i].scatter(df['Source'], df['Destination'], c=clusters, cmap='viridis', alpha=0.6)
        axes[i].set_title(f'Network Traffic Clustering (k={n_clusters})')
        axes[i].set_xlabel('Source (encoded)')
        axes[i].set_ylabel('Destination (encoded)')
        plt.colorbar(scatter, ax=axes[i])
    
    plt.tight_layout()
    plt.show()
    
    # Return optimal clustering (k=2 for binary classification comparison)
    kmeans_optimal = KMeans(n_clusters=2, random_state=42)
    df['Cluster'] = kmeans_optimal.fit_predict(features)
    
    return df

def create_correlation_heatmap(df, feature_columns):
    \"\"\"Create correlation heatmap of network features\"\"\"
    features = df[feature_columns + ['Label']].fillna(0)
    
    plt.figure(figsize=(10, 8))
    correlation_matrix = features.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True)
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.show()

def train_classification_models(df, feature_columns):
    \"\"\"Train multiple classification models and compare performance\"\"\"
    features = df[feature_columns].fillna(0)
    labels = df['Label']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.3, random_state=42, stratify=labels
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize models
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42)
    }
    
    results = {}
    
    # Train and evaluate each model
    for name, model in models.items():
        print(f\"\\nTraining {name}...\")
        
        # Train model
        if name == 'Logistic Regression':
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test_scaled)
            y_prob = model.predict_proba(X_test_scaled)[:, 1]
        else:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]
        
        # Store results
        results[name] = {
            'model': model,
            'y_pred': y_pred,
            'y_prob': y_prob,
            'y_test': y_test
        }
        
        # Print classification report
        print(f\"\\n{name} Classification Report:\")
        print(classification_report(y_test, y_pred))
    
    return results, feature_columns

def plot_confusion_matrices(results):
    \"\"\"Create confusion matrix heatmaps for all models\"\"\"
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    for i, (name, result) in enumerate(results.items()):
        cm = confusion_matrix(result['y_test'], result['y_pred'])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[i])
        axes[i].set_title(f'{name}\\nConfusion Matrix')
        axes[i].set_xlabel('Predicted')
        axes[i].set_ylabel('Actual')
    
    plt.tight_layout()
    plt.show()

def plot_roc_curves(results):
    \"\"\"Create ROC curves for all models\"\"\"
    plt.figure(figsize=(10, 8))
    
    for name, result in results.items():
        fpr, tpr, _ = roc_curve(result['y_test'], result['y_prob'])
        roc_auc = auc(fpr, tpr)
        
        plt.plot(fpr, tpr, linewidth=2, 
                label=f'{name} (AUC = {roc_auc:.3f})')
    
    plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves - Model Performance Comparison')
    plt.legend(loc=\"lower right\")
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_feature_importance(results, feature_columns):
    \"\"\"Plot feature importance for tree-based models\"\"\"
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    tree_models = ['Random Forest', 'Gradient Boosting']
    
    for i, model_name in enumerate(tree_models):
        if model_name in results:
            model = results[model_name]['model']
            importance = model.feature_importances_
            
            # Create feature importance plot
            indices = np.argsort(importance)[::-1]
            
            axes[i].bar(range(len(importance)), importance[indices])
            axes[i].set_title(f'{model_name}\\nFeature Importance')
            axes[i].set_xlabel('Features')
            axes[i].set_ylabel('Importance')
            axes[i].set_xticks(range(len(importance)))
            axes[i].set_xticklabels([feature_columns[j] for j in indices], rotation=45)
    
    plt.tight_layout()
    plt.show()

def create_advanced_visualizations(df):
    \"\"\"Create additional advanced visualizations\"\"\"
    
    # 1. Packet length distribution by label
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    sns.histplot(data=df, x='Length', hue='Label', bins=50, alpha=0.7)
    plt.title('Packet Length Distribution by Traffic Type')
    plt.xlabel('Packet Length')
    plt.ylabel('Frequency')
    
    # 2. Box plot of packet lengths
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df, x='Label', y='Length')
    plt.title('Packet Length Box Plot by Traffic Type')
    plt.xlabel('Traffic Type (0=Normal, 1=Attack)')
    plt.ylabel('Packet Length')
    
    plt.tight_layout()
    plt.show()
    
    # 3. Source-Destination relationship
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df['Source'], df['Destination'], c=df['Label'], 
                         cmap='coolwarm', alpha=0.6, s=30)
    plt.colorbar(scatter, label='Traffic Type (0=Normal, 1=Attack)')
    plt.xlabel('Source (encoded)')
    plt.ylabel('Destination (encoded)')
    plt.title('Source-Destination Relationship Colored by Traffic Type')
    plt.show()

def create_time_series_analysis(df):
    \"\"\"Create time-series analysis if time data is available\"\"\"
    if 'Time' in df.columns:
        try:
            df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
            if not df['Time'].isna().all():
                # Group by time intervals and count packets
                df_time = df.set_index('Time').resample('10S').agg({
                    'Label': 'sum',  # Count of attack packets
                    'Length': 'count'  # Total packet count
                }).fillna(0)
                
                fig, axes = plt.subplots(2, 1, figsize=(15, 8))
                
                # Plot total traffic over time
                axes[0].plot(df_time.index, df_time['Length'], linewidth=2)
                axes[0].set_title('Total Network Traffic Over Time')
                axes[0].set_ylabel('Packet Count')
                axes[0].grid(True, alpha=0.3)
                
                # Plot attack traffic over time
                axes[1].plot(df_time.index, df_time['Label'], color='red', linewidth=2)
                axes[1].set_title('Attack Traffic Over Time')
                axes[1].set_ylabel('Attack Packet Count')
                axes[1].set_xlabel('Time')
                axes[1].grid(True, alpha=0.3)
                
                plt.tight_layout()
                plt.show()
        except Exception as e:
            print(f\"Time series analysis failed: {e}\")

def main():
    \"\"\"Main function to run the advanced threat hunting analysis\"\"\"
    print(\"Advanced AI Threat Hunting Analysis\")
    print(\"=\" * 50)
    
    # Load and aggregate data
    print(\"\\n1. Loading and aggregating data...\")
    df = load_and_aggregate_data()
    if df is None:
        return
    
    # Preprocess data
    print(\"\\n2. Preprocessing data...\")
    df, feature_columns = preprocess_data(df)
    print(f\"Features used: {feature_columns}\")
    
    # Create correlation heatmap
    print(\"\\n3. Creating correlation heatmap...\")
    create_correlation_heatmap(df, feature_columns)
    
    # Perform clustering analysis
    print(\"\\n4. Performing clustering analysis...\")
    df = perform_clustering_analysis(df, feature_columns)
    
    # Train classification models
    print(\"\\n5. Training classification models...\")
    results, feature_columns = train_classification_models(df, feature_columns)
    
    # Create visualizations
    print(\"\\n6. Creating performance visualizations...\")
    plot_confusion_matrices(results)
    plot_roc_curves(results)
    plot_feature_importance(results, feature_columns)
    
    # Create advanced visualizations
    print(\"\\n7. Creating advanced traffic visualizations...\")
    create_advanced_visualizations(df)
    
    # Create time-series analysis
    print(\"\\n8. Creating time-series analysis...\")
    create_time_series_analysis(df)
    
    # Model performance summary
    print(\"\\n9. Model Performance Summary:\")
    print(\"=\" * 30)
    for name, result in results.items():
        fpr, tpr, _ = roc_curve(result['y_test'], result['y_prob'])
        roc_auc = auc(fpr, tpr)
        print(f\"{name}: AUC = {roc_auc:.3f}\")
    
    print(\"\\nAnalysis complete! Check the generated visualizations to understand:\")
    print(\"- Feature correlations and importance\")
    print(\"- Model performance comparisons\")
    print(\"- Traffic pattern differences\")
    print(\"- Clustering effectiveness\")
    print(\"- Time-based traffic patterns\")

if __name__ == \"__main__\":
    main()
