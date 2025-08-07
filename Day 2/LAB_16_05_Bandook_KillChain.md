# LAB 16_05: Using the Cyber Kill Chain to Analyze the Bandook RAT Attack

---

## Objective

In this lab, students will use the Cyber Kill Chain framework to analyze a real-world malware infection involving the Bandook Remote Access Trojan (RAT). Students will trace each stage of the attack, analyze packet captures, and develop detection strategies.

---

## Prerequisites

- Wireshark installed
- Browser access to:
  - [Malware Traffic Analysis - Bandook Sample (2023-08-01)](https://www.malware-traffic-analysis.net/2023/08/01/index.html)
- Basic knowledge of the Cyber Kill Chain
- Familiarity with analyzing PCAP files

---

## Duration

1 Hour

---

## Instructions

### 🔍 Task 1: Download and Open the PCAP File (10 Minutes)

**Steps:**

1. Visit [https://www.malware-traffic-analysis.net/2023/08/01/index.html](https://www.malware-traffic-analysis.net/2023/08/01/index.html)
2. Download the ZIP archive containing the PCAP and password ("infected").
3. Extract the contents and open the `.pcap` file in **Wireshark**.

---

### 🔗 Task 2: Identify Kill Chain Stages (30 Minutes)

**Objective:** Use Wireshark and your knowledge of the Cyber Kill Chain to identify which packets correspond to each phase.

| Kill Chain Phase      | Your Observations |
|-----------------------|-------------------|
| Reconnaissance        |                   |
| Weaponization         |                   |
| Delivery              |                   |
| Exploitation          |                   |
| Installation          |                   |
| Command and Control   |                   |
| Actions on Objectives |                   |

**Tips:**
- Use `http.request`, `dns`, and `tcp.stream eq N` filters to isolate interesting traffic.
- Look for unusual downloads (e.g., `.exe`, `.dll`, `.bat`) or unexpected external connections.

---

### 🛡️ Task 3: Detection Rule Creation (15 Minutes)

**Objective:** Translate observed behavior into a basic detection rule.

**Steps:**

1. Choose one behavior such as:
   - Unusual parent-child process chain (e.g., `chrome.exe` launching unknown exe)
   - Outbound connection to known C2 IPs
2. Draft a detection rule using the following format:

**Sample Detection Rule:**
```
Technique: C2 Communication (C2)
Log Source: Firewall / Netflow
Query:
  dst_ip == 185.10.68.52 AND dst_port == 6591
Logic: Detects outbound traffic to known Bandook C2 server
Response: Trigger alert, isolate host
```

3. Save your detection rule as a `.md` or `.txt` file.

---

### 📄 Task 4: Report and Discussion (5 Minutes)

**Objective:** Summarize your findings in a short report or discussion.

**Sections to Include:**

- Kill Chain Mapping Summary
- Notable Observations in the PCAP
- Detection Logic and Rationale
- Recommended Mitigation Actions

---

## Deliverables

- Completed Kill Chain table with observations
- Screenshot of Wireshark filtered views
- One detection rule in markdown format
- 1-paragraph threat summary

---

## Reflection Questions

1. What stage of the kill chain was hardest to identify?
2. How can this framework assist in proactive defense?
3. How would you brief a non-technical stakeholder about this threat?

---

