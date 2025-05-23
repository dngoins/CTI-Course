# LAB 20: Adversary Emulation with Atomic Red Team

## Objective

In this lab, students will dive into adversary emulation using Atomic Red Team tests on Windows and Linux systems. Through hands-on experience, students will learn to execute adversarial tactics, assess detection mechanisms, and refine response capabilities in a fun, engaging, and adversarial manner.

---

## Prerequisites

Before beginning, ensure you have:

- Windows Sever 2016 and Linux (Kali) virtual machines set up.
- Administrative privileges on both operating systems.
- Internet connectivity to download Atomic Red Team and additional dependencies.
- Familiarity with basic command-line operations.

---

## Scenario

Your adversarial team, "Cyber Avengers," has been tasked to emulate threat actors using the Atomic Red Team framework. The objective is to attack simulated enterprise targets, evade detection systems, and provide recommendations for improving defensive tactics.

---

## Lab Setup

### Materials Needed

- Computers or VMs with internet access.
- Atomic Red Team repository.
- Windows (Sysmon/Event Viewer) and Linux (ELK/Kibana) monitoring tools.
- Digital notebook or documentation tools (e.g., OneNote, Markdown editors).

### Duration

60 minutes total

---

## Instructions

### 🚀 Task 1: Prepare Your Attack Arsenal (10 Minutes)

**Objective:** Setup and prepare Atomic Red Team framework.

**Steps:**

1.1 **Clone Atomic Red Team Repository:**
  - Execute on both OS:
    ```bash
    git clone https://github.com/redcanaryco/atomic-red-team.git AtomicRedTeam
    ```
1.2 **Install Dependencies:**
  - Ensure Python 3.x is installed on Windows/Linux.
  - Navigate into the repository:
    ```bash
    cd AtomicRedTeam
    python -m venv venv
    source .venv/bin/activate  # Linux
    pip3 install invoke
    pip3 install -r requirements.txt
    ```

1.3 Open another terminal Install Invoke-Atomic (Tool to run Atomic tests):
  ```bash
  cd ~
  git clone https://github.com/redcanaryco/invoke-atomicredteam.git
  cd invoke-atomicredteam
  python -m venv venv
  source .venv/bin/activate  # Linux
  pip3 install invoke

  pwsh # starts Powershell on Linux
  Install-Module -Name Invoke-AtomicRedTeam -Force -Scope CurrentUser
  Import-Module ./Invoke-AtomicRedTeam

  Invoke-AtomicTest T1059.001 -TestNumbers 1 # Sample test to verify installation
  Get-AtomicTest -TestNumbers 1 # List all tests
    ```


---

### 🎯 Task 2: Setting Up the Cyber Battlefield (10 Minutes)

**Objective:** Configure execution environments for attack simulation.

**Steps:**

2.1 **Windows Environment Setup:**
  - Launch PowerShell with admin privileges.
  - Navigate to cloned repository:
    ```powershell
    cd C:\path\to\atomic-red-team
    ```

2.2 **Linux Environment Setup:**
  - Open terminal with admin privileges.
  - Navigate to cloned repository:
    ```bash
    cd /path/to/atomic-red-team
    ```

---

### 🧨 Task 3: Launch the Attacks (15 Minutes)

**Objective:** Execute selected Atomic tests on both operating systems.

**Steps:**

3.1 **Atomic Test Selection:**
  - Choose two tests that represent different tactics (e.g., persistence, lateral movement, privilege escalation).

3.2 **Execute on Windows (Sample Test - Process Creation):**
  - Run Atomic test from PowerShell:
    ```powershell
    Invoke-AtomicTest T1059.001 -TestNumbers 1
    ```
  - Observe execution feedback carefully.

3.3 **Execute on Linux (Sample Test - File Modification):**
  - From terminal, run test:
    ```bash
    ./atomics/T1074.001/T1074.001.yaml
    ```
  - Verify test execution successfully.

---

### 🔎 Task 4: Detection & Defense Challenge (15 Minutes)

**Objective:** Monitor and detect your adversarial actions.

**Steps:**

4.1 **Windows System Monitoring:**
  - Launch Event Viewer or Sysmon.
  - Check event logs generated by Atomic test executions (process creations, network activities).

4.2 **Linux System Monitoring:**
  - Open Kibana dashboard in ELK stack.
  - Filter and analyze logs for Atomic test artifacts (file changes, unusual system behavior).

4.3 **Adversarial Analysis:**
  - Document any observed detection gaps.
  - Suggest evasion techniques or improved detection rules.

---

### 📝 Task 5: Intelligence Briefing & Recommendations (5 Minutes)

**Objective:** Compile a short adversarial report highlighting successes, detections, and recommendations.

**Steps:**

5.1 **Draft Report:**
  - Summarize attack steps executed.
  - Identify which tactics were detected and which went unnoticed.
  - Propose enhancements to detection and response strategies.

---

### 🎤 Task 6: Present Your Adversarial Success (5 Minutes)

**Objective:** Present and discuss your adversarial achievements and lessons learned.

**Steps:**

6.1 **Team Presentation:**
  - Briefly present your actions, detections, and recommendations.
  - Discuss key adversarial insights.

6.2 **Class Discussion:**
  - Share your thoughts on improving enterprise defense strategies.

---

## Key Takeaways

- Hands-on adversarial testing enhances cybersecurity skills.
- Atomic Red Team tests provide realistic attack simulations.
- Effective defense relies on robust detection and response mechanisms.
- Continuous improvement and collaboration strengthen defensive capabilities.

---