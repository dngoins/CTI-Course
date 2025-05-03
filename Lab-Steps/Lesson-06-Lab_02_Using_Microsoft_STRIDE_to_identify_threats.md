# Hands-On Lab: Using Microsoft STRIDE to Identify Threats

## Objective

In this lab, students will learn how to use the Microsoft STRIDE model to identify and classify potential threats to a system. STRIDE stands for Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.

---

## Prerequisites

Before starting this lab, students should have basic knowledge of:

- Threat modeling concepts
- Familiarity with Microsoft Threat Modeling Tool
- Understanding of the STRIDE framework and its components
- Basic understanding of system security threats

---

## Materials Needed

- Computer with internet access
- Microsoft Threat Modeling Tool (download from [Microsoft](https://aka.ms/threatmodelingtool))
- Sample application or system for analysis: Web-Mobile-Iot-Solution-Starter.tm7 (Threat Model file)
- Lab worksheet (provided below towards bottom of the document)

---

## Lab Setup

### Duration

60 minutes.

### Step 1: Introduction to STRIDE and Demo (10 minutes)

Instructor should provide a brief overview of the STRIDE acronym and demo the Microsoft Threat Modeling Tool. (Demo video $\approx$ 12min: [Here](https://www.youtube.com/watch?v=Wry2get_RRc))

- **Spoofing**: Impersonating something or someone else.
- **Tampering**: Modifying data or code.
- **Repudiation**: Denying an action or event.
- **Information Disclosure**: Exposing information to unauthorized entities.
- **Denial of Service**: Interrupting service availability.
- **Elevation of Privilege**: Gaining unauthorized access.

**Importance**: STRIDE helps in identifying and classifying threats, enabling proactive mitigation strategies to protect systems and applications.

   > **_NOTE:_** : For more information on STRIDE, refer to the [Microsoft STRIDE documentation ](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-stride) and quick [Youtube video](https://youtu.be/YCkDfjJP5YI?si=WHtknR5rIdvQdmkY)

---

### Step 2: Setting Up the Environment

1. **Download and Install Microsoft Threat Modeling Tool**
   - Go to [Microsoft Threat Modeling Tool](https://aka.ms/threatmodelingtool) and install it on your machine.

2. **Prepare the Sample Application**
   - Open the provided **Web-Mobile-Iot-Solution-Starter.tm7** file. The instructor will provide this file.
   - Familiarize yourself with the system architecture and components represented in the diagram.
   - Understand the data flows and interactions between components, such as:
     - Mobile App
     - Web App
     - IoT Devices
     - Databases (e.g., Cosmos, Fabric)
     - Web Server
   
---

### Step 3: Creating a Threat Model

1. **Modify the Web-Mobile-Iot-Solution-Starter**
   - Use the Lab Worksheet to document the components and their interactions only.
   - Threat Modeling can take some time, so focus on the components and their interactions of the Lab Worksheet only.
   - In real-world scenarios, you would typically start with a system diagram and then identify the components and their interactions and complete the whole network diagram.
   - 

2. **Define the Scope**
   - Identify the boundaries of the system. For example:
     - Local User Zones
     - IoT Device Zones
     - Machine Trust Boundaries
   - Draw the boundaries around the components.
   - Determine the assets, data flows, and components that exist within the defined scope.

3. **Review the System Diagram**
   - Use the tool to update the diagram of the system.
   - Ensure that all components, data flows, and interactions are represented accurately, including Mobile, Browser, and other components with Request and Response connections within the components of the Lab Worksheet.

---

### Step 4: Applying STRIDE to Identify Threats

1. **Analyze Each Component**
   - Select the Browser component in the diagram.
   - Go to View -> Analysis View.
   - Expand the Threat List and Threat Properties window.
   - Filter the Threat List on the "Interaction" column and use the "breq" prefix to focus on the connections from the Browser component.

2. **Review Threats**
   - For each potential threat, read through the description and associated mitigation strategies.
   - Mark the status as "Mitigated" for each identified threat.

---

### Step 5: Mitigating Identified Threats

1. **Propose Mitigations**
   - Find the **Spoofing** threat identified in the Browser component.
   - Use the STRIDE Category column to filter on **Spoofing**.
   - Propose mitigation strategies, such as implementing **multi-factor authentication**.

2. **Document Mitigation Strategies**
   - For each identified threat, record your proposed mitigations in the **Notes** section of the tool.

---

### Step 6: Reporting, Review, and Validating the Threat Model

1. **Generate a Report**
   - Navigate to the **Reports** menu and create a custom report.
   - Select the **Mitigated** state and include migrated threats.
   - Save the report as **Web-Mobile-Iot-Solution-Starter.htm**.

2. **Review and Validate**
   - Verify that 23 mitigations have been implemented.
   - Conduct a thorough review to ensure all threats are accurately identified and mitigated.

3. **Peer Review**
   - Have peers or instructors review the threat model for feedback.
   - Incorporate feedback and make any necessary adjustments.

---

## Lab Worksheet

### Component Analysis:

- **Component**: Browser (e.g., Login Page)
  - **Threat**: Spoofing
  - **Mitigation**: Implement multi-factor authentication.

- **Component**: Databases (e.g., Cosmos, Fabric)
  - **Threat**: Tampering
  - **Mitigation**: Use encryption and integrity checks.

- **Component**: Web Server
  - **Threat**: Denial of Service
  - **Mitigation**: Implement rate limiting and load balancing.

---

## Key Takeaways

- **STRIDE** is a comprehensive model for identifying and classifying security threats.
- Proactive measures like multi-factor authentication and encryption significantly reduce risk.
- Threat modeling is essential for identifying vulnerabilities and developing defense strategies.
- Collaboration and peer review improve the overall accuracy and completeness of threat mitigation plans.


## References
- [Microsoft STRIDE Documentation](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-stride)
- [Microsoft Threat Modeling Tool](https://aka.ms/threatmodelingtool)
- [YouTube Video on Threat Modelling with Microsoft Threat Modeling Tool](https://www.youtube.com/watch?v=lnvYlg4HOX4)

---

## Answer Key and Explanation

- **Login Page** (Spoofing):
  - Mitigation: Multi-factor authentication adds an extra layer of security, making it harder for attackers to impersonate users.
  
- **Database** (Tampering):
  - Mitigation: Encryption ensures data protection, and integrity checks detect unauthorized modifications.

- **Web Server** (Denial of Service):
  - Mitigation: Rate limiting controls the number of requests, and load balancing distributes the load to prevent server overload.
