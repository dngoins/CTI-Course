# LAB 04: Threat Hunting with AI Simulation

## Objective

In this lab, students will learn how to perform threat hunting using Artificial Intelligence (AI) in a Kali Linux virtual environment. They will deploy pre-trained AI models to analyze captured network traffic, distinguish between normal and attack patterns, and document their findings.

---

## Prerequisites

Students should have:

- Kali Linux Virtual Machine with internet access
- Familiarity with basic Linux terminal commands
- Basic understanding of Python and virtual environments

---

## Lab Setup

### Materials Needed

- Kali Linux virtual machine (username: `kali`, password: `kali`)
- Internet connection (initially)
- The provided [files](https://github.com/dngoins/CTI-Course):
  - `SimulateNetworkAttack.py`
  - `NormalNetworkTraffic.csv`
  - `AttackedNetworkTraffic.csv`
  - `AIThreatHunting.py`

### Duration

40–50 minutes total

---

## Instructions

### 🕐 Task 1: Kali Linux VM Setup (5 Minutes)

**Steps:**

1.1 Boot up the Kali Linux Virtual Machine.  
1.2 Login using credentials:  
- **Username:** kali  
- **Password:** kali  

---

### 📥 Task 2: Download & Deploy AI Models (10 Minutes)

**Objective:** Obtain and set up AI models required for threat analysis.

#### K-Means Clustering Model Setup

2.1 Open the terminal and update system packages:
```bash
sudo apt-get update
```

2.2 Ensure Python and Pip3 are installed:
```bash
sudo apt-get install python3-pip
```

2.3 Clone the scikit-learn repository:
```bash
git clone https://github.com/scikit-learn/scikit-learn.git
```

2.4 Navigate to the cloned directory:
```bash
cd scikit-learn
```

2.5 Create a Python virtual environment:
```bash
python3 -m venv threat-hunt-env
```

2.6 Activate the virtual environment:
```bash
source threat-hunt-env/bin/activate
```

2.7 Install scikit-learn and dependencies:
```bash
pip3 install -U scikit-learn pandas matplotlib seaborn
```

2.8 Return to the home directory:
```bash
cd ~
```

#### Gradient Boosting Model Setup

2.9 Clone the XGBoost repository:
```bash
git clone https://github.com/dmlc/xgboost.git
```

2.10 Confirm the virtual environment is activated; if not, activate it again:
```bash
source ~/scikit-learn/threat-hunt-env/bin/activate
```

2.11 Install XGBoost:
```bash
pip3 install xgboost
```

---

### 📡 Task 3: Network Traffic Capture (5 Minutes)

**Objective:** Capture baseline normal network traffic.

**Steps:**

3.1 Open a new terminal window and start Wireshark:
```bash
wireshark
```

3.2 Select the `eth0` LAN network interface.

3.3 Capture normal traffic for **1 minute**.

3.4 Export captured traffic as CSV:
- `FILE -> Export Packet Dissections -> As CSV`
- Select all packets.
- Save as `NormalNetworkTraffic.csv`.

---

### 🚨 Task 4: Simulate Network Attack (10 Minutes)

**Objective:** Simulate a network attack scenario to generate anomalous traffic data.

**Steps:**

4.1 Obtain the provided `SimulateNetworkAttack.py` file and copy it into your home directory.

4.2 Identify the IP address:
```bash
ifconfig
```
- Note down `inet` from the `eth0` interface.

4.3 Edit `SimulateNetworkAttack.py`:
- Replace the placeholder `target_ip` with your identified IP address.

4.4 Run the simulation (for about 5 seconds initially):
```bash
python SimulateNetworkAttack.py
```

4.5 While running, capture traffic with Wireshark:
- Stop the script with `CTRL+C` after a short burst (5–10 seconds).
- Allow Wireshark and VM performance to stabilize between bursts.
- Repeat bursts until you capture about 600–1000 packets.

4.6 Save captured traffic as CSV:
- `FILE -> Export Packet Dissections -> As CSV`
- Save as `AttackedNetworkTraffic.csv`.

---

### 🧪 Task 5: Threat Hunting with AI Models (10 Minutes)

**Objective:** Utilize AI models to hunt for threats within network data.

**Steps:**

5.1 Activate your Python virtual environment:
```bash
source ~/scikit-learn/threat-hunt-env/bin/activate
```

5.2 Obtain `AIThreatHunting.py` from your instructor and ensure it's placed in your home directory.

5.3 Execute AI threat hunting script:
```bash
python AIThreatHunting.py
```

5.4 Analyze outputs from the script to detect anomalies.

---

### 📊 Task 6: Analysis & Reporting (10 Minutes)

**Objective:** Interpret AI model outputs to identify and document threats.

**Steps:**

6.1 Document your findings clearly, identifying potential threats.

6.2 Classify threats based on identified patterns:
- Normal vs. Attack clusters.

6.3 Create visualizations (if applicable) to represent anomalies detected.

6.4 Report should include:
- Cluster Analysis Summary
- SYN Flood Attack characteristics
- Packet Length Distribution Visualization

---

## Reasoning & Visualization Techniques

### Cluster Analysis:
- Identify normal vs. anomalous traffic patterns.
- Use AI clustering to distinguish benign from malicious activities.

### SYN Flood Attack Identification:
- Analyze packets for repetitive SYN requests.
- Detect potential SYN flood attacks through packet frequency and sources.

### Packet Length Visualization:
- Use graphical plots to visualize packet length distributions.
- Identify deviations indicative of attack traffic.

---

## Key Takeaways

- Threat hunting can be greatly enhanced with AI and ML techniques.
- Capturing and analyzing network traffic provides actionable threat intelligence.
- AI clustering methods efficiently segregate normal from malicious traffic.
- Visualization assists in rapid detection and understanding of anomalies.

---

## References

- [Malware-Traffic-Analysis.net - Training Exercises](https://www.malware-traffic-analysis.net)
- [Detecting Network Attacks with Wireshark - InfosecMatter](https://www.infosecmatter.com/detecting-network-attacks-wireshark)

--- 

