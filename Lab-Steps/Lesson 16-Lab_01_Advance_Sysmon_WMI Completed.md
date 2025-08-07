---

# 🎯 Advanced Lab: WMI and SYSMON with MITRE ATT&CK TTPs

## Objective

Enhance Sysmon configuration and WMI queries to specifically detect MITRE ATT&CK techniques:
- **T1566.001**: Phishing - Spearphishing Attachment
- **T1204.001**: User Execution - Malicious Link

### Duration: 25-30 minutes

---

### 🛡️ Task 7: Enhanced Sysmon Configuration for TTP Detection (10 Minutes)

#### Steps:

**7.1 Create Advanced Sysmon Configuration:**

Create a new file `sysmonconfig-ttp.xml` with enhanced rules:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Sysmon schemaversion="4.82">
  <!-- Enhanced Sysmon configuration for T1566.001 and T1204.001 detection -->
  
  <EventFiltering>
    
    <!-- T1566.001: Spearphishing Attachment Detection -->
    <!-- Event ID 1: Process Creation - Focus on email attachment execution -->
    <RuleGroup name="T1566.001-SpearphishingAttachment" groupRelation="or">
      <ProcessCreate onmatch="include">
        <!-- Suspicious processes spawned from email clients -->
        <ParentImage condition="end with">outlook.exe</ParentImage>
        <ParentImage condition="end with">thunderbird.exe</ParentImage>
        <ParentImage condition="end with">winmail.exe</ParentImage>
        <!-- Suspicious file extensions commonly used in attachments -->
        <Image condition="end with">.scr</Image>
        <Image condition="end with">.pif</Image>
        <Image condition="end with">.com</Image>
        <!-- Executables from temp/download directories -->
        <Image condition="contains">\Temp\</Image>
        <Image condition="contains">\Downloads\</Image>
        <Image condition="contains">\AppData\Local\Temp\</Image>
        <!-- Office applications spawning suspicious processes -->
        <ParentImage condition="end with">winword.exe</ParentImage>
        <ParentImage condition="end with">excel.exe</ParentImage>
        <ParentImage condition="end with">powerpnt.exe</ParentImage>
        <!-- Command line with suspicious patterns -->
        <CommandLine condition="contains">powershell -enc</CommandLine>
        <CommandLine condition="contains">powershell -e </CommandLine>
        <CommandLine condition="contains">cmd /c echo</CommandLine>
        <CommandLine condition="contains">bitsadmin</CommandLine>
        <CommandLine condition="contains">certutil -decode</CommandLine>
      </ProcessCreate>
    </RuleGroup>

    <!-- T1204.001: Malicious Link Execution Detection -->
    <!-- Event ID 3: Network Connection - Suspicious outbound connections -->
    <RuleGroup name="T1204.001-MaliciousLink" groupRelation="or">
      <NetworkConnect onmatch="include">
        <!-- Browser processes connecting to suspicious TLDs -->
        <Image condition="end with">chrome.exe</Image>
        <Image condition="end with">firefox.exe</Image>
        <Image condition="end with">msedge.exe</Image>
        <Image condition="end with">iexplore.exe</Image>
        <!-- Non-standard ports from browsers -->
        <DestinationPort condition="is">443</DestinationPort>
        <DestinationPort condition="is">80</DestinationPort>
        <DestinationPort condition="is">8080</DestinationPort>
        <DestinationPort condition="is">8443</DestinationPort>
      </NetworkConnect>
    </RuleGroup>

    <!-- Event ID 11: File Created - Malicious downloads -->
    <RuleGroup name="T1566.001-T1204.001-FileCreation" groupRelation="or">
      <FileCreate onmatch="include">
        <!-- Suspicious files in download locations -->
        <TargetFilename condition="contains">\Downloads\</TargetFilename>
        <TargetFilename condition="contains">\Temp\</TargetFilename>
        <TargetFilename condition="end with">.zip</TargetFilename>
        <TargetFilename condition="end with">.rar</TargetFilename>
        <TargetFilename condition="end with">.7z</TargetFilename>
        <TargetFilename condition="end with">.iso</TargetFilename>
        <TargetFilename condition="end with">.vbs</TargetFilename>
        <TargetFilename condition="end with">.js</TargetFilename>
        <TargetFilename condition="end with">.jar</TargetFilename>
        <TargetFilename condition="end with">.hta</TargetFilename>
      </FileCreate>
    </RuleGroup>

    <!-- Event ID 22: DNS Query - Malicious domains -->
    <RuleGroup name="T1204.001-DNSQueries" groupRelation="or">
      <DnsQuery onmatch="include">
        <!-- Suspicious TLDs and patterns -->
        <QueryName condition="end with">.tk</QueryName>
        <QueryName condition="end with">.ml</QueryName>
        <QueryName condition="end with">.ga</QueryName>
        <QueryName condition="end with">.cf</QueryName>
        <QueryName condition="contains">bit.ly</QueryName>
        <QueryName condition="contains">tinyurl</QueryName>
        <QueryName condition="contains">t.co</QueryName>
        <!-- Domains with suspicious patterns -->
        <QueryName condition="contains">-</QueryName>
        <QueryName condition="contains">update</QueryName>
        <QueryName condition="contains">secure</QueryName>
        <QueryName condition="contains">verify</QueryName>
      </DnsQuery>
    </RuleGroup>

    <!-- Event ID 13: Registry modifications for persistence -->
    <RuleGroup name="T1566.001-Persistence" groupRelation="or">
      <RegistryEvent onmatch="include">
        <!-- Monitor startup locations -->
        <TargetObject condition="contains">CurrentVersion\Run</TargetObject>
        <TargetObject condition="contains">CurrentVersion\RunOnce</TargetObject>
        <TargetObject condition="contains">Winlogon</TargetObject>
        <TargetObject condition="contains">Shell</TargetObject>
      </RegistryEvent>
    </RuleGroup>

  </EventFiltering>
</Sysmon>
```

**7.2 Apply Enhanced Configuration:**

```cmd
sysmon -c sysmonconfig-ttp.xml
```

**7.3 Verify Configuration:**

```cmd
sysmon -s
```

---

### 📊 Task 8: Advanced WMI Queries for TTP Detection (10 Minutes)

#### Steps:

**8.1 Create Enhanced WMI PowerShell Script:**

Create `ttp-monitor.ps1`:

```powershell
# Advanced WMI Monitoring Script for T1566.001 and T1204.001
# MITRE ATT&CK TTP Detection

Write-Host "=== MITRE ATT&CK TTP Monitoring Script ===" -ForegroundColor Green
Write-Host "Detecting T1566.001 (Spearphishing Attachment) and T1204.001 (Malicious Link)" -ForegroundColor Yellow

# Create monitoring directories
$MonitoringPath = "C:\TTP-Monitoring"
if (!(Test-Path $MonitoringPath)) {
    New-Item -ItemType Directory -Path $MonitoringPath -Force
}

# T1566.001: Monitor processes spawned from email clients
Write-Host "`n[T1566.001] Checking for suspicious processes from email clients..." -ForegroundColor Cyan
$EmailProcesses = Get-WmiObject Win32_Process | Where-Object {
    $_.ParentProcessId -ne $null
} | ForEach-Object {
    $ParentProcess = Get-WmiObject Win32_Process -Filter "ProcessId = $($_.ParentProcessId)" -ErrorAction SilentlyContinue
    if ($ParentProcess -and ($ParentProcess.Name -match "outlook|thunderbird|winmail")) {
        [PSCustomObject]@{
            ProcessName = $_.Name
            ProcessId = $_.ProcessId
            ParentProcess = $ParentProcess.Name
            CommandLine = $_.CommandLine
            CreationDate = $_.CreationDate
            ExecutablePath = $_.ExecutablePath
        }
    }
}

if ($EmailProcesses) {
    Write-Host "ALERT: Suspicious processes spawned from email clients detected!" -ForegroundColor Red
    $EmailProcesses | Format-Table -AutoSize
    $EmailProcesses | Export-Csv "$MonitoringPath\T1566.001-EmailSpawned.csv" -NoTypeInformation
} else {
    Write-Host "No suspicious email-spawned processes detected." -ForegroundColor Green
}

# T1566.001: Monitor Office applications spawning processes
Write-Host "`n[T1566.001] Checking Office applications spawning suspicious processes..." -ForegroundColor Cyan
$OfficeProcesses = Get-WmiObject Win32_Process | Where-Object {
    $_.ParentProcessId -ne $null
} | ForEach-Object {
    $ParentProcess = Get-WmiObject Win32_Process -Filter "ProcessId = $($_.ParentProcessId)" -ErrorAction SilentlyContinue
    if ($ParentProcess -and ($ParentProcess.Name -match "winword|excel|powerpnt|acrord")) {
        [PSCustomObject]@{
            ProcessName = $_.Name
            ProcessId = $_.ProcessId
            ParentProcess = $ParentProcess.Name
            CommandLine = $_.CommandLine
            CreationDate = $_.CreationDate
            ExecutablePath = $_.ExecutablePath
        }
    }
}

if ($OfficeProcesses) {
    Write-Host "ALERT: Suspicious processes spawned from Office applications!" -ForegroundColor Red
    $OfficeProcesses | Format-Table -AutoSize
    $OfficeProcesses | Export-Csv "$MonitoringPath\T1566.001-OfficeSpawned.csv" -NoTypeInformation
} else {
    Write-Host "No suspicious Office-spawned processes detected." -ForegroundColor Green
}

# T1204.001: Monitor browser processes and their network activity
Write-Host "`n[T1204.001] Checking browser processes..." -ForegroundColor Cyan
$BrowserProcesses = Get-WmiObject Win32_Process | Where-Object {
    $_.Name -match "chrome|firefox|msedge|iexplore"
} | Select-Object Name, ProcessId, CommandLine, CreationDate, ExecutablePath

if ($BrowserProcesses) {
    Write-Host "Active browser processes detected:" -ForegroundColor Yellow
    $BrowserProcesses | Format-Table -AutoSize
    $BrowserProcesses | Export-Csv "$MonitoringPath\T1204.001-BrowserProcesses.csv" -NoTypeInformation
}

# Monitor suspicious file downloads
Write-Host "`n[T1566.001/T1204.001] Checking for suspicious downloaded files..." -ForegroundColor Cyan
$SuspiciousFiles = Get-WmiObject CIM_DataFile | Where-Object {
    ($_.Name -like "*\Downloads\*" -or $_.Name -like "*\Temp\*") -and
    ($_.Extension -eq "exe" -or $_.Extension -eq "scr" -or $_.Extension -eq "bat" -or 
     $_.Extension -eq "cmd" -or $_.Extension -eq "vbs" -or $_.Extension -eq "js" -or
     $_.Extension -eq "jar" -or $_.Extension -eq "hta" -or $_.Extension -eq "zip")
} | Select-Object Name, CreationDate, LastModified, FileSize, Extension

if ($SuspiciousFiles) {
    Write-Host "ALERT: Suspicious files found in download/temp directories!" -ForegroundColor Red
    $SuspiciousFiles | Format-Table -AutoSize
    $SuspiciousFiles | Export-Csv "$MonitoringPath\SuspiciousFiles.csv" -NoTypeInformation
} else {
    Write-Host "No suspicious files detected in download/temp directories." -ForegroundColor Green
}

# Monitor for persistence mechanisms
Write-Host "`n[T1566.001] Checking for persistence mechanisms..." -ForegroundColor Cyan
$RegistryRuns = Get-WmiObject Win32_StartupCommand | Select-Object Name, Command, Location, User

if ($RegistryRuns) {
    Write-Host "Current startup entries:" -ForegroundColor Yellow
    $RegistryRuns | Format-Table -AutoSize
    $RegistryRuns | Export-Csv "$MonitoringPath\StartupEntries.csv" -NoTypeInformation
}

# Generate summary report
Write-Host "`n=== TTP Detection Summary ===" -ForegroundColor Green
Write-Host "Results saved to: $MonitoringPath" -ForegroundColor Yellow
Write-Host "- Email-spawned processes: $($EmailProcesses.Count)" -ForegroundColor White
Write-Host "- Office-spawned processes: $($OfficeProcesses.Count)" -ForegroundColor White
Write-Host "- Active browser processes: $($BrowserProcesses.Count)" -ForegroundColor White
Write-Host "- Suspicious files found: $($SuspiciousFiles.Count)" -ForegroundColor White
Write-Host "- Startup entries: $($RegistryRuns.Count)" -ForegroundColor White

# Create timestamp for this scan
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
"TTP Monitoring completed at: $Timestamp" | Out-File "$MonitoringPath\LastScan.txt"
```

**8.2 Execute the Enhanced Script:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\ttp-monitor.ps1
```

---

### 🔍 Task 9: Simulate and Detect TTP Activities (10 Minutes)

#### Steps:

**9.1 Simulate T1566.001 (Safe Simulation):**

Create a test scenario in PowerShell:

```powershell
# Safe simulation - Create test files mimicking attachment behavior
New-Item -ItemType Directory -Path "C:\TTP-Test" -Force
New-Item -ItemType File -Path "C:\TTP-Test\invoice.exe" -Force
New-Item -ItemType File -Path "C:\TTP-Test\document.scr" -Force

# Simulate registry persistence (test entry)
New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "TestTTP" -Value "C:\TTP-Test\invoice.exe" -Force
```

**9.2 Monitor Detection:**

Run the monitoring script again and observe detections:

```powershell
.\ttp-monitor.ps1
```

**9.3 Clean Up Test:**

```powershell
Remove-Item "C:\TTP-Test" -Recurse -Force
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "TestTTP" -ErrorAction SilentlyContinue
```

---

### 📋 Task 10: Analyze TTP-Specific Logs (5 Minutes)

#### Steps:

**10.1 Review Sysmon Logs for TTPs:**

In Event Viewer, filter Sysmon logs for:
- Event ID 1: Process creation from email clients
- Event ID 3: Network connections from browsers
- Event ID 11: File creation in suspicious locations
- Event ID 13: Registry modifications

**10.2 Create TTP Detection Dashboard:**

Document findings with MITRE ATT&CK mapping:

```
TTP Detection Report
===================
Date: [Current Date]

T1566.001 - Spearphishing Attachment:
- Processes spawned from email clients: [Count]
- Office applications spawning processes: [Count]
- Suspicious file downloads: [Count]

T1204.001 - Malicious Link:
- Browser network connections monitored: [Count]
- DNS queries to suspicious domains: [Count]
- Downloaded files from browsers: [Count]

Recommendations:
- [List specific improvements based on findings]
```

---

## Enhanced Key Takeaways

- **TTP-Focused Monitoring**: Aligning detection capabilities with specific MITRE ATT&CK techniques improves threat hunting effectiveness.
- **Behavioral Analysis**: Monitoring parent-child process relationships reveals attack patterns.
- **Multi-Layered Detection**: Combining Sysmon, WMI, and behavioral indicators provides comprehensive coverage.
- **Threat Intelligence Integration**: Using MITRE ATT&CK framework guides configuration priorities.
- **Continuous Improvement**: Regular testing and simulation validates detection capabilities.

---
