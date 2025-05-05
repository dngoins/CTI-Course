# LAB 16_03: Using the MITRE ATT&CK Framework for Cyber Threat Intelligence (CTI)

---

## Objective

In this lab, students will explore the use of the MITRE ATT&CK framework to enhance their Cyber Threat Intelligence (CTI) capabilities. Participants will learn how to identify, map, analyze, and mitigate adversary behaviors through practical application of the framework in simulated scenarios.

---

## Prerequisites

Before beginning this lab, students should have completed:

- Introduction to Cyber Threat Intelligence concepts.
- Familiarity with the MITRE ATT&CK Framework and navigation basics.
- Basic cybersecurity principles including knowledge of SIEM and threat intelligence platforms.
- Understanding of threat actors, Tactics, Techniques, and Procedures (TTPs).

---

## Scenario

An ongoing malware campaign named "SmartApeSG" has been targeting multiple organizations through fake browser updates. Recent intelligence suggests the use of the NetSupport RAT and StealC malware. Your team's task is to use the MITRE ATT&CK framework to identify and map adversarial TTPs, create relevant detection rules, generate comprehensive reports, and effectively communicate findings to various stakeholders.

---

## Lab Setup

### Materials Needed

- Computers with internet access
- MITRE ATT&CK Framework website access ([MITRE ATT&CK® Navigator](https://mitre-attack.github.io/attack-navigator/))
- SIEM and threat intelligence platform access (simulation/demo environment recommended)
- Report templates (provided by instructor or pre-made by students)

### Duration

1 Hour

---

## Instructions

### 🕐 Task 1: Introduction to MITRE ATT&CK Framework (10 Minutes)

**Objective:** Understand the structure, components, and value of the MITRE ATT&CK framework.

**Steps:**

1.1 Instructor presents a brief overview of MITRE ATT&CK:
- Purpose and use cases in Cyber Threat Intelligence.
- Explanation of Tactics, Techniques, and Procedures (TTPs).

1.2 Briefly explore the [MITRE ATT&CK website](https://attack.mitre.org/) and highlight key navigation points:
- Tactics and Techniques tabs.
- ATT&CK Navigator.
- Use the ATT&CK Data locally for offline use.
    ```bash
    cd attack-navigator/nav-app
    npm start
    ```
    - Navigate to the local server (http://localhost:4200) to access the ATT&CK Navigator locally.
    - Showcase how to create a new layer, add techniques, and export the layer.
    - Demonstrate the use of the ATT&CK Data locally for offline use.
    
---

### 🔍 Task 2: Mapping Adversary Tactics and Techniques (15 Minutes)

**Objective:** Identify adversary TTPs from provided sample threat data and map them using ATT&CK Navigator.

**Steps:**

2.1 Access and review the provided sample threat data:
- Malware-Traffic-Analysis.net – [2025-03-26 SmartApeSG fake browser update](https://malware-traffic-analysis.net/2025/03/26/index.html).

2.2 Document initial observations and indicators of compromise (IoCs).

2.3 Navigate to the ATT&CK Navigator:
- Create a new layer in ATT&CK Navigator.
- Identify and select relevant tactics and techniques used by SmartApeSG malware campaign.

2.4 Document your mapping clearly, including rationale for selecting each TTP.

---

### 🛡️ Task 3: Creating Detection and Analytics (15 Minutes)

**Objective:** Develop practical detection rules based on mapped TTPs.

**Steps:**

3.1 Use your mapped TTPs to define specific detection strategies.

3.2 Within your simulated SIEM and threat intelligence platforms:
- Create at least three (3) detection rules.
- Explain the logic and expected outputs of each rule.

3.3 Document the detection rules clearly for inclusion in your final intelligence report.

---

### 📄 Task 4: Report Creation (10 Minutes)

**Objective:** Produce a comprehensive intelligence report.

**Steps:**

4.1 Use the provided template or your own format to create an intelligence report with the following sections:

- **Executive Summary:** A concise overview of the threat and recommendations.
- **Threat Landscape:** Clear description of identified TTPs and adversary behaviors.
- **Detection and Mitigation Strategies:** Detailed documentation of created detection rules, analytics logic, and recommended mitigations.
- **Recommendations:** Actionable insights based on your analysis.
- **Supporting Data:** Screenshots, graphs, and ATT&CK Navigator exports illustrating findings.

4.2 Ensure clarity, readability, and suitability for different audiences (technical and non-technical stakeholders).

---

### 📣 Task 5: Dissemination of Reports (5 Minutes)

**Objective:** Tailor and disseminate intelligence findings effectively.

**Steps:**

5.1 Discuss as a team the differences in communication needs among:
- Security Teams (detailed technical analysis and mitigations)
- Executives (high-level, strategic implications)
- External Partners (collaborative threat intelligence sharing and compliance aspects)

5.2 Prepare distinct brief summaries appropriate for each audience.

---

### ✅ Task 6: Feedback and Improvement (5 Minutes)

**Objective:** Refine your intelligence delivery based on feedback.

**Steps:**

6.1 Simulate dissemination by briefly presenting your report summaries to peers.

6.2 Collect feedback on clarity, technical accuracy, and effectiveness of communication.

6.3 Document feedback and discuss potential areas of improvement.

---

## Lab Wrap-Up

**Discussion:**

- Summarize how the MITRE ATT&CK framework aids the CTI lifecycle.
- Share insights on practical application challenges and lessons learned.

**Reflection:**

- Encourage students to reflect on the utility of structured frameworks in enhancing proactive defense strategies.
- Discuss the importance of continuous improvement through feedback integration.

---

## Assessment

**Evaluation Criteria:**

Students will be evaluated on their ability to:

- Accurately map adversary TTPs using MITRE ATT&CK Navigator.
- Effectively create detection and analytics strategies.
- Clearly document and communicate their analysis in intelligence reports.
- Demonstrate effective communication tailored to varied stakeholder groups.
- Incorporate feedback constructively.

**Instructor Feedback:**

Provide personalized constructive feedback to students, highlighting strengths and offering actionable suggestions for improvement in applying the MITRE ATT&CK framework.

---

## Key Takeaways

- The MITRE ATT&CK framework is integral to identifying and responding to cyber threats.
- Accurate mapping of TTPs facilitates targeted detection and mitigation.
- Tailored, clear communication enhances stakeholder understanding and actionability.
- Feedback-driven improvement is crucial to effective CTI practice.

---
