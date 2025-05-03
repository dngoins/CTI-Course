
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load CSV file
df = pd.read_csv('AttackedNetworkTraffic.csv')

# Display first few rows of the dataframe
print(df.head())

# Encode IP addresses
df['Source'] = df['Source'].astype('category').cat.codes
df['Destination'] = df['Destination'].astype('category').cat.codes

# Extract relevant features
features = df[['Source', 'Destination', 'Length']]


# Apply KMeans clustering
kmeans = KMeans(n_clusters=2)
df['Cluster'] = kmeans.fit_predict(features)

# Visualize clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Source', y='Destination', hue='Cluster', palette='viridis')
plt.title('Network Traffic Clustering')
plt.show()


# Visualize packet lengths
plt.figure(figsize=(10, 6))
sns.histplot(df['Length'], bins=50, kde=True)
plt.title('Packet Length Distribution')
plt.xlabel('Packet Length')
plt.ylabel('Frequency')
plt.show()

# Visualize clusters with packet lengths
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Source', y='Length', hue='Cluster', palette='viridis')
plt.title('Cluster Analysis with Packet Lengths')
plt.show()
