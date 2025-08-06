# Hands-On Lab: Using AlienVault OTX to Identify Cybersecurity Threats

## Objective:
Students will learn how to use the Open Threat Exchange (OTX) platform from AlienVault to identify cybersecurity threats and create Indicators of Compromise (IOCs).

---

## Materials Needed:
- Computer with internet access
- Access to https://otx.alienvault.com
- Lab worksheet (provided below)

---

## Lab Setup:

### Duration:
- Approximately 15 minutes

### Instructions:
This is an individual lab. Each student should complete the following tasks using https://otx.alienvault.com and document their answers in the Day 2 worksheet.

---

## Tasks:

### Task 1: Register and Explore the OTX Platform
Go to https://otx.alienvault.com and create a free account if you do not already have one.

**Questions:**
- What are the main components of the OTX dashboard?
- Name one advantage of using OTX for threat intelligence.

---

### Task 2: Search for a Known Threat Actor or Malware
Search for a known malware (e.g., Emotet or Cobalt Strike) or a threat actor (e.g., APT28). Review the pulse and indicators associated with it.

**Questions:**
- What threat did you search for?
- List three types of IOCs found (e.g., IP, URL, domain, hash).
- Was this pulse contributed by a private user or a security vendor?

---

### Task 3: Create a Custom IOC Pulse
Create your own pulse using a hypothetical scenario: Assume your organization has observed suspicious communication with the IP `203.0.113.50` and a file hash `e99a18c428cb38d5f260853678922e03`.

**Instructions:**
1. Click “Create Pulse” from the OTX dashboard.
2. Give it a name and description.
3. Add the IOC details: include at least one IP address and one file hash.
4. Choose appropriate tags (e.g., malware, IOC, suspicious).
5. Publish the pulse.

**Questions:**
- What did you name your pulse?
- What type of threat does this pulse represent?
- Why is it important to share IOCs with the community?

---

## Instructor Notes (2 Minutes):
After 13 minutes, provide the answer key and demonstrate how to navigate the OTX platform and contribute IOCs.