# LAB 16_02: Elastic Stack (ELK) Hands-on Lab

## Objective

In this lab, students will learn how to set up and utilize the Elastic Stack (ELK – Elasticsearch, Logstash, Kibana) on a Linux environment for effective log analysis and visualization, essential skills for cybersecurity analysis and incident response.

---

## Prerequisites

Before beginning this lab, students should have:

- A Kali Linux machine or VM with at least 8 GB RAM.
- Administrative (root) access on the Linux machine.
- Reliable internet access to download required components.

---

## Scenario

As a cybersecurity analyst, your team has been tasked with implementing a centralized log analysis solution for continuous security monitoring. You will set up an ELK Stack to ingest, analyze, and visualize log data, enabling proactive identification and mitigation of threats within your organization's infrastructure.

---

## Lab Setup

### Materials Needed

- Kali Linux VM (minimum 8GB RAM)
- Internet access for downloading software
- Terminal access on Kali Linux
- Digital note-taking tools (e.g., OneNote, Evernote)

### Duration

45–60 minutes total

---

## Instructions

### 🕐 Task 1: Environment Preparation (10 Minutes)

**Steps:**

1.1 Start your Kali Linux VM with at least 8GB of RAM allocated.

1.2 Open a terminal window and prepare your environment for ELK installation.

---

### 📥 Task 2: Install ELK Stack Components (10 Minutes)

**Objective:** Set up Elasticsearch, Logstash, and Kibana on your Kali Linux machine.

**Steps:**

2.1 **Install Java (OpenJDK):**
```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

2.2 **Install Elasticsearch:**
```bash
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-9.0.0-amd64.deb
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-9.0.0-amd64.deb.sha512
shasum -a 512 -c elasticsearch-9.0.0-amd64.deb.sha512
sudo dpkg -i elasticsearch-9.0.0-amd64.deb

sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
```

2.3 **Install Logstash:**
```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg
sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-8.x.list
sudo apt-get update && sudo apt-get install logstash
sudo systemctl start logstash
sudo systemctl enable logstash
```

2.4 **Install Kibana:** [Instructions here](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package#deb-repo)
```bash
wget https://artifacts.elastic.co/downloads/kibana/kibana-7.10.2-amd64.deb
sudo dpkg -i kibana-7.10.2-amd64.deb
sudo systemctl start kibana
sudo systemctl enable kibana
```

---

### ⚙️ Task 3: Configure ELK Stack Components (10 Minutes)

**Objective:** Properly configure each ELK component for seamless integration.

**Steps:**

3.1 **Configure Elasticsearch:**
Edit configuration file:
```bash
sudo nano /etc/elasticsearch/elasticsearch.yml
```

Add the following configurations:
```yaml
cluster.name: my-elk-cluster
network.host: 0.0.0.0
```

3.2 **Configure Logstash:**
Create and edit Logstash configuration:
```bash
sudo nano /etc/logstash/conf.d/logstash.conf
```

Insert the following configurations:
```conf
input {
  file {
    path => "/var/log/syslog"
    start_position => "beginning"
  }
}

filter {
  grok {
    match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{DATA:program}: %{GREEDYDATA:logmessage}" }
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "syslog-%{+YYYY.MM.dd}"
  }
  stdout { codec => rubydebug }
}
```

3.3 **Configure Kibana:**
Edit Kibana configuration file:
```bash
sudo nano /etc/kibana/kibana.yml
```

Set configurations as follows:
```yaml
server.host: "localhost"
elasticsearch.hosts: ["http://localhost:9200"]
```

---

### 🔄 Task 4: Start Log Ingestion (5 Minutes)

**Objective:** Verify logs are being ingested properly.

**Steps:**

4.1 Restart Logstash to apply configurations:
```bash
sudo systemctl restart logstash
```

4.2 Check Logstash logs for ingestion confirmation:
```bash
sudo tail -f /var/log/logstash/logstash-plain.log
```

---

### 🔍 Task 5: Explore Logs with Kibana (10 Minutes)

**Objective:** Conduct preliminary analysis of logs through Kibana.

**Steps:**

5.1 Open a web browser and navigate to:
```
http://localhost:5601
```
(Kibana may take 3–5 minutes to load.)

5.2 Create and configure an Index Pattern in Kibana:
- Navigate to **Index Management > Index Templates**.
- Create an index template pattern: `syslog-*`.

5.3 (Optional) Enable Elasticsearch Filebeat:
- Follow the guided setup:
```
http://localhost:5601/app/home#/tutorial/elasticsearchLogs
```

5.4 Utilize Kibana's **Discover** tab to query logs and identify patterns or anomalies.

---

### 📊 Task 6: Data Visualization & Alerts (10 Minutes)

**Objective:** Create visualizations and configure alerts in Kibana.

**Steps:**

6.1 Go to the **Dashboard** tab and create a new dashboard with various visualizations (bar charts, pie charts, line graphs).

6.2 Navigate to **Alerting** to configure alerts based on identified log events or unusual activities.

- Set actions such as email notifications for triggered alerts.

---

### 📢 Task 7: Discussion and Lab Review (5 Minutes)

**Objective:** Reflect and discuss insights from the ELK setup.

**Steps:**

7.1 Share dashboards and key findings with peers or instructors.

7.2 Discuss how log visualization aids threat identification and proactive defense measures.

7.3 Instructor provides feedback and discusses best practices.

---

## Key Takeaways

- ELK Stack enables robust and centralized log management.
- Log visualization and analysis are crucial for threat detection.
- Effective cybersecurity involves proactive monitoring and response strategies.
- Structured tools and processes streamline incident analysis and remediation.

---

## Additional Resources

- [Elastic Documentation](https://www.elastic.co/guide/index.html)
- [ELK Stack Tutorial Videos](https://www.elastic.co/videos)

--- 

✅ **Lab Complete!** You now have a functional ELK Stack configured for cyber threat analysis and visualization.