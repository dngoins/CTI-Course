# LAB 10: Planning and Gathering Data from Threat Intelligence Sources

## Objective

This lab reinforces the concepts of planning and gathering data from threat intelligence sources. The focus will be on utilizing Google Dorks for OSINT and [Exploit DB](https://www.exploit-db.com/google-hacking-database), specifically targeting the Advanced Persistent Threat (APT28) group. Students will apply these techniques using a sample dataset for analysis.

---

## Prerequisites

Students should be familiar with the basics of Cyber Threat Intelligence (CTI) and possess foundational knowledge of:

- The intelligence cycle (Planning, Gathering, Analysis, Dissemination)
- Google Dorks and its use in OSINT

---

## Lab Setup

### Materials Needed

- Computers with internet access
- Kali Linux virtual machine (username: kali, password: kali)
- Google Dorks queries
- Sample dataset (ADFA Intrusion Detection Datasets)

### Duration

Approximately 90 minutes

---

## Instructions

### 🕐 Task 1: Introduction to Threat Intelligence (10 Minutes)

**Steps:**

1.1 Instructor provides an overview of threat intelligence and its significance.  
1.2 Discuss the intelligence cycle: Planning, Gathering, Analysis, and Dissemination.  
1.3 Explain the focus of the lab: using Google Dorks for OSINT and Nessus for vulnerability scanning to investigate APT28.
1.4 Instructor Demo how to create a Google Dork query.


---

### 🧠 Task 2: Planning Phase (20 Minutes)

**Objective:** Plan the intelligence gathering process by identifying key requirements and resources.

**Steps:**

2.1 **Identifying Intelligence Requirements:**  
   - Define what information is needed, such as potential threats, vulnerabilities, and attack vectors related to APT28.  
   - Example: Identify TTPs of APT28 targeting the financial sector.  

2.2 **Setting Objectives:**  
   - Define clear and measurable goals.  
   - Example: Identify specific attack vectors and tools used by APT28.

2.3 **Resource Allocation:**  
   - Allocate necessary resources including personnel, tools (Google Dorks, [Exploit DB](https://www.exploit-db.com/google-hacking-database)), and datasets.  

2.4 **Developing a Collection Plan:**  
   - Outline methods and sources for gathering intelligence (OSINT, TECHINT).  
   - Methods could include Google Dorks queries for OSINT and Nessus for vulnerability scanning.

---

### 🔍 Task 3: Gathering Phase (30 Minutes)

**Objective:** Gather data using OSINT and TECHINT techniques.

**Steps:**

3.1 **OSINT with Google Dorks:**  
   - Introduction to Google Dorks and how it can be used for OSINT.  
   - Example queries for APT28 investigation:  
   - `site:pastebin.com APT28`  
   - `intitle:"APT28" filetype:pdf`  
   - `inurl:APT28 report`
   - `related:apt28.com`
   - `intext:"APT28" "vulnerability"`
   - `filetype:docx "APT28" "attack vector"`
   - `ext:pdf "APT28" "TTPs"`
   - `cache:apt28.com`
   - `before:2023-01-01 APT28`
   - `after:2022-01-01 APT28`
   - Operators: `AND` `&`, `OR` `|`, `NOT`, `*` (wildcard), `..` (range), etc.

[**Google Dorks Cheatsheet:**](https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06)

3.2 **Practical Exercise:**  
   - Use Google Dorks to gather publicly available data related to APT28.  
   - Document findings in the "OSINT Findings" section of the worksheet.

3.3 **Evaluating Credibility and Reliability:**  
   - Assess the credibility of the sources (authoritative vs non-authoritative).  
   - Cross-reference information and check the reputation of the sources.

3.4 **TECHINT with Nessus:**  
   - Introduction to Nessus and how it is used for vulnerability scanning.  
   - Setup and configuration of Nessus for scanning.
   - Navigate to [Trial Nessus](https://www.tenable.com/try#expert) and create an account if needed.
   - Nessus is installed on the Kali Linux VM, however it's trial version has not been activated yet.

3.5 **Practical Exercise:**  
   - Launch Kali Linux and open Nessus. Open the Nessus web interface in a browser (usually `https://localhost:8834`).  
   - Import the sample dataset (e.g., ADFA Intrusion Detection Datasets) into Nessus.  
   - The sample dataset can be found in your Downloads folder ~/Downloads/ADFA-IDS_datasets.zip
   - Unzip the dataset and import it into Nessus.
   - Configure the scan settings (e.g., scan type, target IPs, etc.).
   - Run a vulnerability scan on the dataset and analyze the results.  
   - Ensure the trial version of Nessus is activated to access all features.  

---


#### 🛠️ Updated Task 3.4–3.5: Using Nessus for TECHINT (Vulnerability Scanning)

**Objective:** Perform a vulnerability scan using Nessus to identify potential attack vectors in relation to APT28-style threats.

---

### Step-by-Step Guide:

#### 🧰 A. Setup Nessus on Kali Linux
1. **Start Kali Linux** and ensure it’s connected to the internet.
2. Launch a web browser and open the Nessus interface at:
   ```
   https://localhost:8834
   ```
3. If prompted with a security warning (self-signed cert), proceed to the site.

#### 🔐 B. Activate Nessus
1. If this is the first time launching Nessus, complete the initial setup wizard:
   - Select **Nessus Essentials** (free version for students).
   - Register at [https://www.tenable.com/products/nessus/nessus-essentials](https://www.tenable.com/products/nessus/nessus-essentials) to get an activation code.
   - Enter the activation code in Nessus.
   - Let Nessus download plugins (~15–20 minutes).

#### 📁 C. Import and Prepare Sample Data
1. Locate the provided ADFA dataset at:
   ```
   ~/Downloads/ADFA-IDS_datasets.zip
   ```
2. Unzip it:
   ```bash
   unzip ~/Downloads/ADFA-IDS_datasets.zip -d ~/Downloads/ADFA-IDS
   ```
3. If the dataset contains virtual machines or IPs, take note of the local IP addresses.

#### 🖥️ D. Create a New Scan
1. From the Nessus Dashboard, click **New Scan** > **Advanced Scan**.
2. Name the scan: `APT28 Vulnerability Scan`.
3. In the **Targets** field, enter the IP address or hostname of the machine hosting the ADFA dataset.
4. Click the **Discovery** tab:
   - Use default settings, or set **Port Scan Range** to `default`.
5. Click the **Credentials** tab (optional):
   - Leave blank unless you have login credentials for authenticated scanning.
6. Click **Save**.

#### ▶️ E. Run and Monitor the Scan
1. Go back to the **My Scans** tab.
2. Click the **Play** (▶️) button next to your scan.
3. Wait for the scan to complete (duration depends on target and scope).

#### 📊 F. Analyze the Results
1. After the scan, click the completed scan to view:
   - **Total vulnerabilities**
   - Categorized by **Critical**, **High**, **Medium**, **Low**, **Info**
2. Click on individual vulnerabilities to view:
   - Description and plugin ID
   - CVSS score
   - Affected services and ports
   - Recommended remediation steps

#### 🧩 G. Correlate with OSINT
1. Cross-reference discovered vulnerabilities with APT28 TTPs:
   - Are any CVEs known to be exploited by APT28?
   - Do any detected weaknesses match OSINT findings from your Google Dork queries?

#### 📝 H. Document Findings
1. Record the following in your worksheet or lab report:
   - List of discovered vulnerabilities
   - Severity levels
   - Any direct or indirect relation to APT28 activity
   - Suggested mitigations or alerts to raise


### 📊 Task 4: Analysis and Reporting (20 Minutes)

**Objective:** Analyze the collected data, identify patterns, and create a report.

**Steps:**

4.1 **Analyze the Collected Data:**  
   - Identify any patterns or correlations between the OSINT data and vulnerabilities identified by Nessus.  

4.2 **Reporting Findings:**  
   - Create a report summarizing the findings. Include key threats, vulnerabilities, and insights gained from the OSINT and TECHINT phases.  
   - Present recommendations for mitigating identified threats.

---

### 📣 Task 5: Discussion and Q&A (10 Minutes)

**Objective:** Review the results of the lab, discuss findings, and address questions.

**Steps:**

5.1 Each team presents their findings, highlighting the identified threats and vulnerabilities.  
5.2 Discuss the use of OSINT and TECHINT tools in the context of real-world cyber threat intelligence.  
5.3 Instructor provides feedback and answers any questions.

---

### ✅ Task 6: Conclusion (5 Minutes)

**Steps:**

6.1 Summarize the key takeaways from the lab, emphasizing the importance of planning, gathering, and analyzing threat intelligence.  
6.2 Reinforce the role of OSINT and TECHINT in enhancing cybersecurity posture.  
6.3 Provide a brief overview of how to use the results for proactive defense and intelligence dissemination.

---

## Key Takeaways

- Planning and gathering are critical steps in the threat intelligence cycle.
- OSINT tools like Google Dorks provide valuable insights into potential threats.
- Vulnerability scanning with tools like Nessus helps identify and prioritize system weaknesses.
- Collaboration and documentation are key to ensuring thorough analysis and effective defense strategies.

### References
- Google Dorks: [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
- Nessus: [Tenable Nessus](https://www.tenable.com/products/nessus-vulnerability-scanner)
- [Google Dorks youtube](https://www.youtube.com/watch?v=GlIG37uZSjQ)
