# LAB 16_05: Answer Key - Bandook Kill Chain Analysis

---
## Task 2: Kill Chain Mapping - Overview of answers

| Kill Chain Phase      | Observations |
|-----------------------|--------------|
| Reconnaissance        | Not explicitly captured, likely performed prior to this capture by attacker via vulnerability scanning or phishing. tcp.flags.syn == 1 and tcp.flags.ack == 0 |
| Weaponization         | A malicious Bandook payload is hosted on a compromised site, ready for download. dns.qry.name contains "filedn" http.request.uri contains ".exe" |
| Delivery              | Victim is redirected through several URLs and downloads the Bandook loader (via filedn[.]com). ip.addr == [known IP] or dns.qry.name contains "filedn" http.response.code == 302 http.host contains "filedn" or http.request.uri contains ".exe" frame contains ".exe"|
| Exploitation          | The victim executes the downloaded loader manually or through social engineering. ip.addr == 185.10.68.52 tcp.port == 6591 |
| Installation          | The loader installs persistence via registry key and saves a file to AppData (e.g., QF.exe). http.request.uri contains "QF.exe"  ip.addr == 185.10.68.52 && tcp.port == 6591|
| Command and Control   | Outbound traffic observed to 185.10.68.52:6591 and vrunabo[.]su, consistent with Bandook C2 behavior. ip.addr == 185.10.68.52 && tcp.port == 6591  and /or dns.qry.name contains "vrunabo" dns.qry.name contains "vrunabo"
or
ip.addr == [resolved IP] |
| Actions on Objectives | Potential exfiltration and privilege escalation via batch files and additional downloads. http.request.method == "POST" tcp.len > 1000|

---

## Detailed answer

To correlate packet numbers from a **PCAP file** to each **Cyber Kill Chain phase** involving a **Bandook infection**, you'll need to follow a structured analysis using a tool like **Wireshark**. Below are **step-by-step instructions** for identifying relevant packets for each phase of the Kill Chain based on the typical behaviors observed in the Bandook campaign described:

---

### Step 1: Load the PCAP File

* Open **Wireshark**.
* Load the given **PCAP file** (`File > Open`).

### Step 2: Set Time References (Optional)

* To keep track of events, right-click on a packet and choose **"Set/Unset Time Reference"** to mark key points.

---

## 🔗 Kill Chain Phases Breakdown

### 1. **Reconnaissance**

* **Not typically present in PCAP**, but:

  * You may try filtering for **port scanning** or **unusual inbound connections**:

    ```wireshark
    tcp.flags.syn == 1 and tcp.flags.ack == 0
    ```
  * Look for frequent connection attempts to multiple ports or hosts.
  * These are likely *not* in your capture, as you said, but it's worth checking early packets.

---

### 2. **Weaponization**

* This phase is **implied**, not directly visible in traffic.
* However, note any **HTTP GET requests** to unusual URLs hosting **PE executables** (e.g., `.exe`, `.dll`).
* Use filter:

  ```wireshark
  http.request.uri contains ".exe"
  ```

---

### 3. **Delivery**

* Identify **HTTP GET** or **302 Redirects** leading to:

  * `filedn[.]com`
  * Other suspicious redirector domains

#### Step-by-Step:

1. Use this filter to identify redirections:

   ```wireshark
   http.response.code == 302
   ```
2. Follow TCP streams or use:

   ```wireshark
   http.host contains "filedn" || http.request.uri contains ".exe"
   ```
3. Look at the **packet number** where the `.exe` file is actually downloaded.

---

### 4. **Exploitation**

* Look for when the **downloaded loader is executed**.
* This might not show directly unless:

  * There is an **outbound connection immediately after download**.
  * A new **process initiates C2 communication**.

#### Step-by-Step:

1. Note the **timestamp of the download complete**.
2. Look for **outbound connections** shortly after — use:

   ```wireshark
   tcp.port == 6591
   ```

   or

   ```wireshark
   ip.addr == 185.10.68.52
   ```
3. Correlate packet numbers with these.

---

### 5. **Installation**

* Persistence mechanisms like **registry changes** aren't visible in network traffic directly.
* But, saving a file (like `QF.exe`) might trigger:

  * DNS lookups
  * HTTP requests for additional payloads

#### Step-by-Step:

1. Look for HTTP traffic with filenames in URIs:

   ```wireshark
   http.request.uri contains "QF.exe"
   ```
2. Use `Follow TCP Stream` on suspicious connections to extract file names or content.
3. DNS queries for weird subdomains may also hint at this phase.

---

### 6. **Command and Control (C2)**

* Outbound connections to:

  * `185.10.68.52:6591`
  * `vrunabo[.]su`

#### Step-by-Step:

1. Use this display filter:

   ```wireshark
   ip.addr == 185.10.68.52 && tcp.port == 6591
   ```

   and/or

   ```wireshark
   dns.qry.name contains "vrunabo"
   ```
2. Record the packet number of:

   * Initial DNS query (if using domain)
   * First successful TCP handshake
   * Any unusual payload (e.g., encrypted blobs)

---

### 7. **Actions on Objectives**

* Look for:

  * Batch script downloads or executions
  * New connections to unfamiliar external hosts
  * Possible **data exfiltration** (e.g., POST requests with large payloads)

#### Step-by-Step:

1. Use this filter to find HTTP POST:

   ```wireshark
   http.request.method == "POST"
   ```
2. Look for large uploads or encoded payloads (e.g., base64 in HTTP body).
3. Analyze payload in suspicious POSTs using `Follow TCP Stream`.

---

## 📌 Tip: Export Packet Numbers

* Right-click on any packet and choose:

  * **"Mark Packet"** (then use `Ctrl+M`)
  * Export all marked packets via: `File > Export Specified Packets`

---
## No TCP Traffic???

Yes — **you can still map the kill chain phases even without HTTP traffic**, but you'll need to shift focus to **non-HTTP indicators** such as:

* **TCP/UDP flows**, especially to known malicious IPs/ports
* **DNS queries**, which often precede or replace HTTP(S) communication
* **TLS/SSL traffic** (even if encrypted, metadata is revealing)
* **File transfers over alternate protocols** (e.g., SMB, FTP, custom C2)

Here’s how you can adapt the approach:

---

## 🔗 Kill Chain Mapping Without HTTP Traffic

### 1. **Reconnaissance**

* Still likely missing unless internal scanning is visible.
* Look for scanning patterns:

  ```wireshark
  tcp.flags.syn == 1 and tcp.flags.ack == 0
  ```

  Then analyze:

  * High frequency of SYN packets
  * Multiple ports/hosts targeted

---

### 2. **Weaponization**

* Since you can't see the hosting site via HTTP, focus on **DNS**:

  * Was there a **DNS query for a domain hosting a known payload**?
  * Look for unusual or newly registered domains.

  ```wireshark
  dns.qry.name contains "filedn"
  ```
* The fact that DNS resolution occurs for such domains suggests prior knowledge/preparation = **weaponization phase context**.

---

### 3. **Delivery**

* You won’t see the actual download, but you **can detect the delivery vector** if:

  * A file is fetched via an alternate protocol (e.g., **FTP, SMB**)
  * Or if a **DNS query to the payload domain** is followed by traffic to a known IP

#### What to do:

* Search for connections to known file hosting IPs/domains:

  ```wireshark
  ip.addr == [known IP] or dns.qry.name contains "filedn"
  ```

* Look for TCP streams initiated **immediately after such DNS resolution**.

* Also try:

  ```wireshark
  frame contains ".exe"
  ```

  (in case of file name passing through other protocols)

---

### 4. **Exploitation**

* You won’t see execution, but **initial outbound C2 activity after a silent period** may suggest payload execution.

#### Look for:

* Sudden traffic to rare destination (e.g., `185.10.68.52:6591`)
* Start of a persistent TCP stream

```wireshark
tcp.port == 6591
```

* Use **"Statistics > Conversations > TCP"** and sort by **start time** to find when unusual connections begin.

---

### 5. **Installation**

* Monitor for:

  * **Repeated connections from the same source process** (suggesting persistence)
  * **Beaconing patterns** (e.g., a packet every 60s)

#### How to detect:

* Use:

  ```wireshark
  ip.addr == 185.10.68.52 && tcp.port == 6591
  ```
* Right-click a flow and do **"Follow TCP Stream"**
* If the same destination is contacted multiple times across time windows, this hints at installed malware with persistence.

---

### 6. **C2 (Command & Control)**

You *can* still see C2:

#### Look for:

* Connections to:

  * `185.10.68.52:6591`
  * `vrunabo[.]su` (resolve IP via DNS traffic)

* Use:

  ```wireshark
  dns.qry.name contains "vrunabo"
  or
  ip.addr == [resolved IP]
  ```

* If TLS is used:

  ```wireshark
  ssl.handshake.type == 1
  ```

  (Client Hello indicates a TLS connection; SNI field can reveal the domain)

---

### 7. **Actions on Objectives**

Even without HTTP, you can find exfiltration or lateral movement:

#### Look for:

* **Large data transfers to external IPs**

  ```wireshark
  tcp.len > 1000
  ```

* Unusual ports

  ```wireshark
  tcp.port > 1024 && ip.dst != internal subnet
  ```

* Use **"Statistics > Endpoints > IPv4"** and sort by **Bytes Sent** to find large uploads.

* **SMB traffic** (for spreading):

  ```wireshark
  smb2
  ```

---

## Summary of Adapted Filters (No HTTP)

| Phase                 | Suggested Wireshark Filters / Tools                                              |
| --------------------- | -------------------------------------------------------------------------------- |
| Reconnaissance        | `tcp.flags.syn == 1 && tcp.flags.ack == 0`                                       |
| Weaponization         | `dns.qry.name contains "filedn"`                                                 |
| Delivery              | `ip.addr == [payload IP]`, `tcp.port == 445 or 21` (SMB, FTP)                    |
| Exploitation          | Sudden C2 activity after DNS resolution                                          |
| Installation          | Repeated connections, beaconing behavior                                         |
| C2                    | `ip.addr == 185.10.68.52`, `tcp.port == 6591`, `dns.qry.name contains "vrunabo"` |
| Actions on Objectives | Large outbound transfers, `tcp.len > 1000`, `smb2`                               |

---

If you'd like, you can **share a small sanitized sample of the PCAP**, or provide a list of IPs/domains, and I can guide you more precisely on what to filter or export.


## Task 3: Example Detection Rule

- **Technique:** Command and Control - Unusual Destination Port  
- **Log Source:** Firewall logs / IDS  
- **Query:**
  ```sql
  dst_ip == "185.10.68.52" AND dst_port == 6591
  ```
- **Logic:** Identifies outbound communication to known Bandook C2 infrastructure.
- **Response:**
  - Generate critical alert
  - Block IP on perimeter firewall
  - Quarantine and analyze host

---

## Task 4: Sample Threat Summary

> On August 1, 2023, a Bandook RAT infection was observed in a sample PCAP where the payload was delivered via malicious redirections and a hosted executable. The malware established persistence and began C2 communications with known malicious IPs. Based on the Cyber Kill Chain, the delivery, installation, and C2 phases were clearly observable. Detection rules were created to monitor for suspicious ports and destinations.

---

## Reflection Example Answers

1. **Hardest Kill Chain Phase:** Reconnaissance, as it's not present in the PCAP.
2. **Proactive Defense Use:** Enables defenders to identify which stage was successful and reinforce controls at weak points.
3. **Non-technical Brief:** “A malicious tool known as Bandook was downloaded via a fake update. It contacted known attacker servers, which we blocked. We've added alerts for any future similar activity.”

---

