# LAB 16_04: Answer Key - ATT&CK Navigator and Detection Rule Creation

---

## Task 1: Technique Mapping

**Mapped Techniques from SmartApeSG Campaign:**

1. **T1189 - Drive-by Compromise**  
   - Rationale: Malware delivered via fake browser update link.
2. **T1219 - Remote Access Tools**  
   - Rationale: NetSupport RAT observed in traffic dump.
3. **T1059.003 - Command and Scripting Interpreter: Windows Command Shell**  
   - Rationale: Powershell-based scripts initiating download commands.

---

## Task 2: Sample Detection Rule

- **Technique:** T1219 - Remote Access Tools  
- **Log Source:** Windows Security Event Logs (Sysmon/EventID 4688)  
- **Query:**
  ```plaintext
  EventID=4688 AND (NewProcessName="*nstray.exe" OR ParentImage="*chrome.exe")
  ```
- **Logic:** Monitors for suspicious RAT processes initiated from browser processes.
- **Response:**  
  - Trigger alert  
  - Isolate affected host  
  - Perform memory dump for malware analysis

---

## Task 3: Export

Expected files:
- `SmartApeSG_Mapping.json`
- PDF or screenshot of Navigator layer view

---

