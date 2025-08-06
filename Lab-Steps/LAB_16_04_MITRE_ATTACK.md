# LAB 16_04: Deep Dive - ATT&CK Navigator Mapping and Detection Rule Creation

---

## Objective

This lab guides students through hands-on use of the MITRE ATT&CK Navigator. Students will:
- Map real-world adversary techniques from the 2025-03-26 SmartApeSG malware report
- Create a new Navigator layer
- Develop one practical detection rule
- Export and print the Navigator output

---

## Prerequisites

- Completion of LAB 16_03
- Browser access to:
  - [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
  - [SmartApeSG Report](https://malware-traffic-analysis.net/2025/03/26/index.html)

---

## Duration

45 Minutes

---

## Instructions

### 🔍 Task 1: Navigate and Create an ATT&CK Layer (15 Minutes)

**Objective:** Create a Navigator layer and begin mapping threat techniques.

**Steps:**

1. Open the ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
2. Click `New Layer` > `Enterprise` to start a fresh mapping.
3. From the SmartApeSG report, identify 2–3 initial behaviors. Common examples:
   - Command and Control (e.g., T1219 - Remote Access Tools)
   - Initial Access via Fake Software (T1189 - Drive-by Compromise)

4. In the Navigator:
   - Use the search bar to find these techniques by ID or keyword.
   - Click each technique cell to color it (e.g., red for confirmed behavior).
   - Optionally add comments (e.g., "Observed in packet dump from 2025-03-26")

5. Click `Export > Save Layer as JSON` and name it `SmartApeSG_Mapping.json`.

6. Optional: Click `Print` to export a PDF of the visual mapping.

---

### 🛡️ Task 2: Write a Detection Rule (20 Minutes)

**Objective:** Translate mapped behavior into 1 actionable detection rule.

**Steps:**

1. Choose one of your mapped techniques (e.g., `T1219 - Remote Access Tools`).
2. Imagine you are writing a rule for a SIEM (like Splunk or Sentinel).

**Sample detection rule format:**

- **Technique:** T1219 - Remote Access Tools
- **Log Source:** Windows Event Logs
- **Query:**
  ```plaintext
  EventID=4688 AND (NewProcessName="*nstray.exe" OR ParentImage="*chrome.exe")
  ```
- **Logic Explanation:** Detects suspicious RAT processes spawned by browsers.
- **Response:** Alert, isolate host, collect memory image.

3. Save your rule in a markdown file or paste it into a team shared doc.

---

### 📤 Task 3: Present and Save Output (10 Minutes)

**Objective:** Share your work and prepare for submission.

**Steps:**

1. Attach your `.json` layer file and screenshot of the Navigator.
2. Submit your markdown file with detection rule, technique ID, and rationale.
3. Optionally print the Navigator output or generate a report using the "Export to PDF" plugin if available.

---

## Assessment

**Grading Rubric:**

| Task | Points |
|------|--------|
| Accurate technique mapping in Navigator | 10 pts |
| Detection rule created with correct logic | 10 pts |
| Exported JSON layer and printed screenshot | 5 pts |
| Rationale documented clearly | 5 pts |
| **Total** | **30 pts** |

---

## Reflection Questions

1. What challenges did you face while identifying techniques?
2. How does this mapping assist detection engineering?
3. What changes would you make to improve your detection logic?
