# LAB 16: WMI and Sysmon for System Monitoring and Threat Detection

## Objective

In this lab, students will learn how to utilize Windows Management Instrumentation (WMI) and Sysmon for effective system monitoring and threat detection on Windows machines.

---

## Prerequisites

Students should have:

- A Windows system (Windows 10 or later recommended)
- Administrative privileges on the system
- Internet access to download Sysmon and related resources
- Basic familiarity with Windows Command Prompt and PowerShell

---

## Lab Setup

### Materials Needed

- Windows computer with administrative privileges
- Internet connection for downloading software
- Sysmon executable file from Microsoft Sysinternals
- A basic Sysmon configuration XML file (available from Sysinternals)

### Duration

Approximately 30–40 minutes

---

## Step-by-Step Instructions

### 🛠️ Task 1: Setup Sysmon (5-10 Minutes)

#### Steps:

**1.1 Download Sysmon:**

- Go to [Microsoft Sysinternals Sysmon Page](https://docs.microsoft.com/sysinternals/downloads/sysmon).
- Download the latest Sysmon executable file.

**1.2 Install Sysmon:**

- Open Command Prompt with administrative privileges.
- Navigate to the downloaded Sysmon executable location.
- Run the following command to install Sysmon with the provided or a basic configuration:
  
```cmd
sysmon -accepteula -i sysmonconfig.xml
```

> **Note**: Ensure `sysmonconfig.xml` is in the same directory or provide a full path.

**1.3 Verify Installation:**

- Confirm Sysmon is running by executing:
  
```cmd
sc query sysmon
```

- Verify that the service status indicates "Running".

---

### ⚙️ Task 2: Configure Sysmon (5 Minutes)

#### Steps:

**2.1 Create or Obtain a Configuration File:**

- Acquire a Sysmon configuration XML file from the official Sysinternals website, or create your custom file to log relevant events (e.g., process creation, file changes, network connections).

**2.2 Apply the Configuration:**

- Apply your configuration by running:
  
```cmd
sysmon -c sysmonconfig.xml
```

---

### 🖥️ Task 3: Use WMI for System Queries (10 Minutes)

#### Steps:

**3.1 Query Running Processes:**

- Open PowerShell with administrative rights.
- List active processes by running:

```powershell
Get-WmiObject Win32_Process | Select-Object Name, ProcessId
```

**3.2 Query Installed Software:**

- List installed applications with:

```powershell
Get-WmiObject Win32_Product | Select-Object Name, Version
```

**3.3 Automate WMI Queries:**

- Create a PowerShell script named `monitor.ps1` to automate system monitoring:
  
```powershell
$processes = Get-WmiObject Win32_Process | Select-Object Name, ProcessId
$software = Get-WmiObject Win32_Product | Select-Object Name, Version
$processes | Out-File "C:\Monitoring\processes.txt"
$software | Out-File "C:\Monitoring\software.txt"
```

- Save and schedule or manually execute this script as needed.

---

### 📈 Task 4: Analyze Sysmon Logs (5-10 Minutes)

#### Steps:

**4.1 Open Event Viewer:**

- Press `Win + R`, type `eventvwr`, and press Enter.

**4.2 Navigate to Sysmon Logs:**

- In Event Viewer, navigate to:
  - `Applications and Services Logs` → `Microsoft` → `Windows` → `Sysmon`

**4.3 Identify Suspicious Activities:**

- Inspect logs for suspicious events related to process creations, network activities, and file modifications.
- Cross-reference events with WMI queries to identify potential threats.

---

### 📋 Task 5: Generate Reports (5 Minutes)

#### Steps:

**5.1 Export Sysmon Logs:**

- Right-click `Sysmon` in Event Viewer, select `Save All Events As...`, and save as `.evtx`.

**5.2 Compile Findings:**

- Summarize your observations in a report using any text editor or documentation tool, including details about suspicious events, potential threats, and security implications.

---

### 🗣️ Task 6: Discussion and Review (5 Minutes)

#### Steps:

**6.1 Review Findings:**

- Discuss your analysis with peers or instructor.
- Highlight strengths and identify any detection gaps or weaknesses.

**6.2 Improve Your Configuration:**

- Refine your Sysmon configuration based on the lab insights to enhance detection capabilities.
- Adjust your WMI queries or monitoring scripts to address identified gaps.

---

## Key Takeaways

- Effective use of Sysmon and WMI greatly enhances Windows threat detection.
- Regular configuration and refinement of monitoring tools increase cybersecurity readiness.
- Automation of queries through scripts ensures consistent and efficient system monitoring.
- Collaborative analysis and sharing findings improve overall security posture.

---
