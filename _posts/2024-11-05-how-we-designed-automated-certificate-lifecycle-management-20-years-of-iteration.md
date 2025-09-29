---
title: "How We Designed Automated Certificate Lifecycle Management: 20 Years of Iteration"
date: 2024-11-05T05:00:00-04:00
categories:
- cybersecurity
- certificates
- automation
- PKI
tags:
- certificates
- automation
- lifecycle-management
- ssl-tls
- evolution
---
![Certificate Automation Evolution](/assets/images/posts/certificate-evolution/certificate-automation-evolution.jpg)
*Our journey to automated certificate management*

We started with peer-to-peer certificates. Then we thought a centralized authority would be cool, so we designed PKI. More recently, we started talking about certificate lifecycle management. Axon believes that even this definition is too narrow for long-term success. When I say long-term, this horizon is shortening from over 10 years to 1-2 years as rules for certificate validity are being tightened by web browsers. This post shows the current state of our PKI evolution.

### **Technology**

We have built certificate management several times from scratch for different clients. Eventually, we have expanded the technology functions to include features we had not really thought would be possible when we started over 20 years ago.

Our latest implementation is automated automated PKI (public key infrastructure), or certificate lifecycle management, which includes a variety of items. A controlled release and automated updates of endpoint agents (or integration scripts) that allow servers and applications to obtain certificates. The actual issuance of certificates, the downloading of trusted CA certificates (aka, trust stores), and also validation - such as CRL (certificate revocation lists), OCSP (online certificate status protocol - a real-time protocol with caching) validation.

All of this runs as a serverless service using AWS Lambda functions, which is code running on a managed platform. It is deployed automatically with CI/CD pipelines, requiring zero need for human access to the AWS account where this deployment is running. The certification authorities (CAs) can be external - whether it is your own internal CA or hosted private CAs by one of the certificate providers (GlobalSign, Digicert, Sectigo, Entrust, etc.), or Amazon's own AWS Private CA or a public CA to automate management of public certificates.

### **Automating Certificates in Enterprise Environment**

One question you are likely going to get once you deploy the solution, and pretty quick, is what is the criticality of it in the context of your company. Any mature enterprise will want to know the answer from the cybersecurity perspective and also as part of its vendor onboarding. You are providing a service, which you say is really important for you. How critical is it to your business and does it satisfy your check list for the criticality level you state? Our technology design ensures components with different criticality can be operated independently.

Our experience is modular design and operations is the correct approach. As such, we split functional parts into independent components with separate levels of criticality.

### **Divide and Conquer - Critical Components**

Splitting the automated PKI into components will not only facilitate enterprise onboarding but also have a long-term positive effect on operational costs or the cost of ownership. The highest criticality component is OCSP, which is often combined with CRL, so you can consider these two together and refer to them as certificate validation services. Depending on your agility and risk awareness, you may require OCSP validation, which provides real-time validation for all uses of certificates. Therefore, you won’t need this to be separate.

On the other hand, the issuance of certificates can be classified as simple “business support.” If it undergoes maintenance or goes down for a day or even a week, it will not impact your business systems. The only consequence would be a delayed renewal of certificates, which would likely still fall within your predefined acceptable parameters. The configuration of certificate renewals always allows several days for “standard renewal” for manual runbooks. Moreover, if you design the certificate lifecycle management thoughtfully, you can achieve a robust level of resiliency. For example, you can renew certificates every month with a validity of 3-12 months. This approach lowers the risk of long-term key compromise, increases the run rate of the PKI and integrations, allowing you to detect any issues quickly, reduces costs, improves integration testing, and lowers the risk of failed certificate renewals for your business.

In summary, this means you maintain your business resiliency against failures in certificate management while aggressively limiting the time for key exposure and exploitation. The latter is due to the fact that every new certificate generates a new key, rendering the old key useless. For instance, if you obtain a certificate for a year and someone steals the related private key in the second month, the attacker will have more than ten months to exploit it for whatever purpose they intended to use to attack your organization. However, if you renew that certificate every month, then when I steal it two weeks in, I only have two weeks to find a way to exploit it.

### **Certificate Validation = Intelligence Source**

Centralizing validation services via DNS, i.e., having all validation requests served by your automated PKI, provides a valuable intelligence service, and you can build powerful analytics on top of the traffic data. The way we designed our technology includes the use of a single DNS domain for all client-facing services. This allows us to efficiently manage the CI/CD-based software lifecycle while also analyzing information about the certificate clients. It is especially powerful with the OCSP service, as validation requests contain an identifier for the certificate that a client needs to validate. The traffic data will provide a map of your network, showing what relies on a particular server with a certificate issued by our service. CRL-based validation is not as granular, but you can perform some powerful operational tuning that would split issuing into a number of CAs based on the type of client. This kind of intelligence is not common, as few companies have reached the level of maturity required to implement it. If you only need to cover “infrastructure for certificates,” additional functionality incurs an extra cost. However, this is not the case with Axon Shield, where you receive this as part of the software package, available from day one.

![High-level Design](/assets/images/posts/certificate-evolution/design.png)

### **Shortening Certificate Lifecycle**

By shortening certificate validity, you not only reduce related cybersecurity risks but also enhance your operational maturity and lower the risks of downtime for new applications. Certificate-related issues are identified much earlier within the application project, i.e., while the project team is still available to address those issues quickly.

### **Certificate Client Management = Business Support**

The second part of our PKI publishes files that you need to support PKI clients. This includes client agents, trust stores, documentation, and so on. It is advisable to keep these functions separate from the main PKI. From a change management perspective, you can update these quickly without impacting anything else, even if their criticality level is the same as that of the actual certificate issuance. The separation is quite straightforward from a technology standpoint, as file publishing is implemented with separate file storage (S3 buckets) and Lambda functions.

### **Certificate Issuance Module**

Certificate issuance is primarily classified as a business support function, where the recovery time can be in hours or even days. In contrast, OCSP may be critical or mission-critical, with recovery time measured in minutes, especially if you are in a regulated industry or working with sensitive applications.

### **Internal Structure of Axon Shield PKI**

Splitting the entire certificate management into modules is not difficult, and the core of this is accomplished via separate CI/CD pipelines that can be run independently. If you run a “Client publishing” pipeline, it will only affect components related to that specific set of functions. You can even delegate the management of this CI/CD to a separate team—this team will be closely aligned with DevOps and will work on tuning client configurations to support your developers.

Then you have the issuance of certificates, which will be available for your—most likely—PKI/cyber ops/infosec team. The intelligence data can be pushed into separate dashboards for your cyber defense team, which is responsible for identifying cybersecurity incidents. The PKI team may still be interested in “client download data” to identify PKI users and report on the utilization of certificate management across your enterprise. The certificate issuance/renewal data provides generic reporting for managers regarding how well and how much the system is being used. The certificate validation data is for cyber defense teams, so they can focus on specific attack vectors and will also help you map out and send clients on service with certificates. Ultimately, this can provide you with a map of who is connecting to which server, allowing you to create a comprehensive map of your network—an entirely independent data set from your generic traffic monitoring.

What’s the bottom line here? You can achieve fully-fledged certificate management almost instantly. Your team’s focus can then shift to reporting, compliance, and operational monitoring—all aspects of a cyber-mature organization.