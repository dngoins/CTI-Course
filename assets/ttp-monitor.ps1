# Advanced WMI Monitoring Script for T1566.001 and T1204.001
# MITRE ATT&CK TTP Detection Script
# Created for enhanced threat hunting and detection

Write-Host "=== MITRE ATT&CK TTP Monitoring Script ===" -ForegroundColor Green
Write-Host "Detecting T1566.001 (Spearphishing Attachment) and T1204.001 (Malicious Link)" -ForegroundColor Yellow
Write-Host "Script Version: 1.0" -ForegroundColor Gray

# Create monitoring directories
$MonitoringPath = "C:\TTP-Monitoring"
if (!(Test-Path $MonitoringPath)) {
    New-Item -ItemType Directory -Path $MonitoringPath -Force
    Write-Host "Created monitoring directory: $MonitoringPath" -ForegroundColor Green
}

# Initialize counters
$EmailProcessCount = 0
$OfficeProcessCount = 0
$BrowserProcessCount = 0
$SuspiciousFileCount = 0
$StartupEntryCount = 0

# T1566.001: Monitor processes spawned from email clients
Write-Host "`n[T1566.001] Checking for suspicious processes from email clients..." -ForegroundColor Cyan
try {
    $EmailProcesses = Get-WmiObject Win32_Process | Where-Object {
        $_.ParentProcessId -ne $null
    } | ForEach-Object {
        $ParentProcess = Get-WmiObject Win32_Process -Filter "ProcessId = $($_.ParentProcessId)" -ErrorAction SilentlyContinue
        if ($ParentProcess -and ($ParentProcess.Name -match "outlook|thunderbird|winmail")) {
            $EmailProcessCount++
            [PSCustomObject]@{
                ProcessName = $_.Name
                ProcessId = $_.ProcessId
                ParentProcess = $ParentProcess.Name
                CommandLine = $_.CommandLine
                CreationDate = $_.CreationDate
                ExecutablePath = $_.ExecutablePath
                TTP = "T1566.001"
                Severity = "HIGH"
            }
        }
    }

    if ($EmailProcesses) {
        Write-Host "ALERT: $EmailProcessCount suspicious process(es) spawned from email clients detected!" -ForegroundColor Red
        $EmailProcesses | Format-Table -AutoSize
        $EmailProcesses | Export-Csv "$MonitoringPath\T1566.001-EmailSpawned.csv" -NoTypeInformation
    } else {
        Write-Host "No suspicious email-spawned processes detected." -ForegroundColor Green
    }
} catch {
    Write-Host "Error monitoring email processes: $($_.Exception.Message)" -ForegroundColor Red
}

# T1566.001: Monitor Office applications spawning processes
Write-Host "`n[T1566.001] Checking Office applications spawning suspicious processes..." -ForegroundColor Cyan
try {
    $OfficeProcesses = Get-WmiObject Win32_Process | Where-Object {
        $_.ParentProcessId -ne $null
    } | ForEach-Object {
        $ParentProcess = Get-WmiObject Win32_Process -Filter "ProcessId = $($_.ParentProcessId)" -ErrorAction SilentlyContinue
        if ($ParentProcess -and ($ParentProcess.Name -match "winword|excel|powerpnt|acrord")) {
            $OfficeProcessCount++
            [PSCustomObject]@{
                ProcessName = $_.Name
                ProcessId = $_.ProcessId
                ParentProcess = $ParentProcess.Name
                CommandLine = $_.CommandLine
                CreationDate = $_.CreationDate
                ExecutablePath = $_.ExecutablePath
                TTP = "T1566.001"
                Severity = "MEDIUM"
            }
        }
    }

    if ($OfficeProcesses) {
        Write-Host "ALERT: $OfficeProcessCount suspicious process(es) spawned from Office applications!" -ForegroundColor Red
        $OfficeProcesses | Format-Table -AutoSize
        $OfficeProcesses | Export-Csv "$MonitoringPath\T1566.001-OfficeSpawned.csv" -NoTypeInformation
    } else {
        Write-Host "No suspicious Office-spawned processes detected." -ForegroundColor Green
    }
} catch {
    Write-Host "Error monitoring Office processes: $($_.Exception.Message)" -ForegroundColor Red
}

# T1204.001: Monitor browser processes and their network activity
Write-Host "`n[T1204.001] Checking browser processes..." -ForegroundColor Cyan
try {
    $BrowserProcesses = Get-WmiObject Win32_Process | Where-Object {
        $_.Name -match "chrome|firefox|msedge|iexplore"
    } | Select-Object Name, ProcessId, CommandLine, CreationDate, ExecutablePath,
        @{Name="TTP";Expression={"T1204.001"}},
        @{Name="Severity";Expression={"LOW"}}

    $BrowserProcessCount = $BrowserProcesses.Count

    if ($BrowserProcesses) {
        Write-Host "$BrowserProcessCount active browser process(es) detected:" -ForegroundColor Yellow
        $BrowserProcesses | Format-Table -AutoSize
        $BrowserProcesses | Export-Csv "$MonitoringPath\T1204.001-BrowserProcesses.csv" -NoTypeInformation
    } else {
        Write-Host "No browser processes currently running." -ForegroundColor Green
    }
} catch {
    Write-Host "Error monitoring browser processes: $($_.Exception.Message)" -ForegroundColor Red
}

# Monitor suspicious file downloads
Write-Host "`n[T1566.001/T1204.001] Checking for suspicious downloaded files..." -ForegroundColor Cyan
try {
    $SuspiciousExtensions = @("exe", "scr", "bat", "cmd", "vbs", "js", "jar", "hta", "zip", "rar", "7z", "iso")
    $SuspiciousFiles = @()
    
    foreach ($ext in $SuspiciousExtensions) {
        $Files = Get-WmiObject CIM_DataFile | Where-Object {
            ($_.Name -like "*\Downloads\*" -or $_.Name -like "*\Temp\*") -and
            $_.Extension -eq $ext
        } | Select-Object Name, CreationDate, LastModified, FileSize, Extension,
            @{Name="TTP";Expression={"T1566.001/T1204.001"}},
            @{Name="Severity";Expression={"MEDIUM"}}
        
        if ($Files) {
            $SuspiciousFiles += $Files
        }
    }

    $SuspiciousFileCount = $SuspiciousFiles.Count

    if ($SuspiciousFiles) {
        Write-Host "ALERT: $SuspiciousFileCount suspicious file(s) found in download/temp directories!" -ForegroundColor Red
        $SuspiciousFiles | Format-Table -AutoSize
        $SuspiciousFiles | Export-Csv "$MonitoringPath\SuspiciousFiles.csv" -NoTypeInformation
    } else {
        Write-Host "No suspicious files detected in download/temp directories." -ForegroundColor Green
    }
} catch {
    Write-Host "Error checking suspicious files: $($_.Exception.Message)" -ForegroundColor Red
}

# Monitor for persistence mechanisms
Write-Host "`n[T1566.001] Checking for persistence mechanisms..." -ForegroundColor Cyan
try {
    $RegistryRuns = Get-WmiObject Win32_StartupCommand | Select-Object Name, Command, Location, User,
        @{Name="TTP";Expression={"T1566.001"}},
        @{Name="Severity";Expression={"MEDIUM"}}

    $StartupEntryCount = $RegistryRuns.Count

    if ($RegistryRuns) {
        Write-Host "$StartupEntryCount startup entry/entries found:" -ForegroundColor Yellow
        $RegistryRuns | Format-Table -AutoSize
        $RegistryRuns | Export-Csv "$MonitoringPath\StartupEntries.csv" -NoTypeInformation
    } else {
        Write-Host "No startup entries detected." -ForegroundColor Green
    }
} catch {
    Write-Host "Error checking startup entries: $($_.Exception.Message)" -ForegroundColor Red
}

# Check for suspicious network connections (requires netstat)
Write-Host "`n[T1204.001] Checking for active network connections..." -ForegroundColor Cyan
try {
    $NetworkConnections = netstat -ano | Select-String "ESTABLISHED" | ForEach-Object {
        $parts = $_.ToString().Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
        if ($parts.Count -ge 5) {
            $ProcessId = $parts[4]
            $Process = Get-WmiObject Win32_Process -Filter "ProcessId = $ProcessId" -ErrorAction SilentlyContinue
            if ($Process -and ($Process.Name -match "chrome|firefox|msedge|iexplore")) {
                [PSCustomObject]@{
                    Protocol = $parts[0]
                    LocalAddress = $parts[1]
                    ForeignAddress = $parts[2]
                    State = $parts[3]
                    ProcessId = $ProcessId
                    ProcessName = $Process.Name
                    TTP = "T1204.001"
                    Severity = "LOW"
                }
            }
        }
    }

    if ($NetworkConnections) {
        Write-Host "Browser network connections detected:" -ForegroundColor Yellow
        $NetworkConnections | Format-Table -AutoSize
        $NetworkConnections | Export-Csv "$MonitoringPath\T1204.001-NetworkConnections.csv" -NoTypeInformation
    }
} catch {
    Write-Host "Error checking network connections: $($_.Exception.Message)" -ForegroundColor Red
}

# Generate comprehensive summary report
Write-Host "`n=== TTP Detection Summary Report ===" -ForegroundColor Green
Write-Host "Scan completed at: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor White
Write-Host "Results saved to: $MonitoringPath" -ForegroundColor Yellow
Write-Host ""
Write-Host "MITRE ATT&CK T1566.001 (Spearphishing Attachment):" -ForegroundColor Cyan
Write-Host "  - Email-spawned processes: $EmailProcessCount" -ForegroundColor White
Write-Host "  - Office-spawned processes: $OfficeProcessCount" -ForegroundColor White
Write-Host "  - Startup entries: $StartupEntryCount" -ForegroundColor White
Write-Host ""
Write-Host "MITRE ATT&CK T1204.001 (Malicious Link):" -ForegroundColor Cyan
Write-Host "  - Active browser processes: $BrowserProcessCount" -ForegroundColor White
Write-Host "  - Network connections monitored: Yes" -ForegroundColor White
Write-Host ""
Write-Host "General Indicators:" -ForegroundColor Cyan
Write-Host "  - Suspicious files found: $SuspiciousFileCount" -ForegroundColor White

# Risk assessment
$TotalAlerts = $EmailProcessCount + $OfficeProcessCount + $SuspiciousFileCount
if ($TotalAlerts -eq 0) {
    Write-Host "`nRisk Level: LOW - No immediate threats detected" -ForegroundColor Green
} elseif ($TotalAlerts -le 3) {
    Write-Host "`nRisk Level: MEDIUM - Some suspicious activity detected" -ForegroundColor Yellow
} else {
    Write-Host "`nRisk Level: HIGH - Multiple suspicious indicators detected!" -ForegroundColor Red
}

# Create timestamp for this scan
$ScanSummary = @"
TTP Monitoring Scan Summary
===========================
Scan Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
Script Version: 1.0

T1566.001 Detection Results:
- Email-spawned processes: $EmailProcessCount
- Office-spawned processes: $OfficeProcessCount
- Startup entries: $StartupEntryCount

T1204.001 Detection Results:
- Active browser processes: $BrowserProcessCount
- Suspicious files: $SuspiciousFileCount

Total Alerts: $TotalAlerts
Risk Level: $(if ($TotalAlerts -eq 0) {"LOW"} elseif ($TotalAlerts -le 3) {"MEDIUM"} else {"HIGH"})

Recommendations:
- Review any flagged processes for legitimacy
- Investigate suspicious files in download directories
- Monitor startup entries for unauthorized additions
- Consider implementing additional email security controls
- Enable advanced browser security features

Next Steps:
1. Review Sysmon logs for correlated events
2. Analyze any flagged files with antivirus/sandbox
3. Update threat intelligence feeds
4. Review user training on phishing awareness
"@

$ScanSummary | Out-File "$MonitoringPath\ScanSummary-$(Get-Date -Format 'yyyyMMdd-HHmmss').txt"
Write-Host "`nDetailed scan summary saved to: $MonitoringPath\ScanSummary-$(Get-Date -Format 'yyyyMMdd-HHmmss').txt" -ForegroundColor Green
