---
title: "Take Control of Your Network: Why DNS is Key to Understanding Your Internet"
date: 2025-02-15T05:00:00-04:00
categories:
- dns
- networking
- network-management
- control
tags:
- dns-control
- network-visibility
- internet-understanding
- network-security
---
![Dns Network Control](/assets/images/posts/network-control/dns-network-control.jpg)
*Why DNS is Key to Understand Your Networks*

Getting your DNS in order is the first step to taking control of your network perimeter. It will provide you with definitive information about your internet-facing services and websites. It also reveals all the third parties to whom you outsource your capabilities—from SEO and marketing to email, to hosting your applications.


**DNS - Strategy for Perimeter Security**
-----------------------------------------

With multiple clients, we have seen immense impact of creating and maintaining up-to-date inventory of DNS data. Whether a single registered domain name, or hundreds of domains managed by different teams across the IT operations. We knew that this information is important but the impact of its availability always surprises us.

Firstly, what we talk about - we talk about domains that some people still type into web browsers - like "[google.com](https://google.com)" or "[irs.gov](http://irs.gov)". DNS is a system that finds your company on the internet. The size of your "DNS" depends on who you are. If you're the US government, your DNS are all internet names ending with ".gov" - thousands of domains. As an internet company you will probably have one registered name "[mycompany.com](http://mycompany.com)" and if you acquired other businesses, you may manage tens of domains.

DNS (Domain Name System) management plays a critical role in network operations and security. Beyond translating human-friendly domain names to servers hosting your websites, DNS records can be a valuable source of intelligence for understanding network behavior, identifying security risks, and making strategic decisions to protect digital assets.

With multiple clients, we have implemented an ultimate DNS inventory, and we want to highlight some interesting aspects of our past achievements. Our process involves collecting data, understanding its value, and analyzing the results to trigger various infrastructure tasks and projects. The follow-up actions range from record removal to improvements in certificate management and its automation, as well as the implementation of protective measures such as Web Application Firewalls (WAF) and DDoS protection.

Collecting DNS Data
-------------------

The first step is to collect as much of your DNS data as possible. Even for companies with extensive DNS management, the data is usually managed by just one or a few teams. This is due to the available technologies and even when ignoring cyber-security, you realise the importance of centralising changes to your DNS.

We can collect data with a widely support "zone transfer" mechanism but we can also directly parse configuration data of DNS systems (Bind9, Akamai Edge DNS, AWS R53, GCP DNS, etc). Some of these mechanisms require changes to your network protection and this is one of the reasons why we implement our automation in cloud accounts you control - there is no vendor lock to Axon Shield.

At this point, let me quickly go through some of the information we can start reporting to you:

1.  **Service addresses (IP addresses)** - indicate the servers running your applications. We will connect these addresses to the owners of the relevant IP ranges. This gives you insight into your platforms and third parties that you trust to provide internet-facing services for you. How do we know you trust them? They will interact with your customers while appearing to be you, as their services will use your "[mycompany.com](http://mycompany.com)" domain.
    
2.  **Email setup** - we can immediately identify your email servers. Additionally, we offer comprehensive instructions on implementing email protection records. This will allow you to quickly view the domains you are using for email communication. After our review, we can recommend strategies to secure your email practices, ensuring that unauthorized communications do not falsely appear to originate from your organization.
    
3.  **DNS Resilience** - We can measure the accessibility of your DNS data and assess its robustness. As a primary target for denial-of-service attacks, DNS is particularly vulnerable. Businesses with a longstanding online presence often fall victim to contemporary assaults that can easily overwhelm any in-house infrastructure. The expense of such distributed attacks is minimal, making them accessible even to those with limited resources.
    
4.  **DNS attacks** - DNS is vulnerable to hijacking through a tactic known as "cache poisoning", where adversaries substitute legitimate data with fraudulent information by rerouting customer inquiries to harmful servers. We will not only update you on your current status but also assist in implementing necessary changes using a proven framework we have successfully employed for similar adjustments.
    
5.  **Improper issuance of certificates** - DNS allows you to control the origin of your certificates by limiting the certificate authorities you permit. This interaction signifies an area where DNS governance intersects with certificate administration. In a future article, we will elaborate on how certificates have evolved into what can be termed a "DNS-enhanced" technology.
    

Analyzing DNS Data
------------------

Once your DNS information is stored in a database, we can begin to analyze the data and construct a comprehensive overview of your internet landscape.

The first step involves establishing a refined DNS dataset. We verify each record to ensure its accuracy and functionality. This process confirms that DNS entries are correctly directing to resources while identifying outdated or redundant records.

Why does this matter? Your infrastructure changes over time as you discontinue relationships with third-party services, phase out older servers, and introduce new virtual machines. Commonly, we find DNS entries linked to non-existent servers—a better situation—or linked to servers owned by others, which poses a significant risk by creating potential vulnerabilities for impersonation.

The automated process, which starts working the moment you are onboarded, will:

*   **Verify Addresses**: Ensure that server addresses in your DNS accurately link to your servers and firewalls. Outdated IP addresses may signify neglected infrastructure that could be susceptible to security breaches.
    
*   **Consistency of DNS Aliases**: Validate that DNS alias records are correct and functional. Invalid or broken aliases can lead to service disruptions and expose vulnerabilities.
    
*   **Email Security**: Inadequate or erroneous email protection records enable unauthorized parties to send emails posing as you. DNS serves as a crucial source of information, allowing email servers worldwide to notify you about messages originating from your domains. Remarkably, the entire internet collects analytics regarding each email sent from your domain(s) and shares this data with you, provided your DNS is configured properly.
    

**DNS Analysis Done - Taking Action**
-------------------------------------

After evaluating the DNS records, it's essential to take decisive action. AXON Shield will equip you with vital information and assist in orchestrating necessary modifications. Here’s a concise overview of the most impactful steps to consider in the initial phase.

1.  **Deleting Obsolete Records**:
    
    *   **Identify Outdated Entries**: Records that are no longer useful can expose your network to security risks. Eliminating these records minimizes your vulnerability.
        
    *   **Automated Cleanup**: If your DNS inventory (and its size) justifies it, we can implement scripts that automatically remove records that meet certain criteria, such as those linking to IP addresses outside your organization. Effective change management is vital in this process.
        
2.  **Guarding Against Phishing Attacks**: Email attacks aimed at clients and collaborators are among the oldest tactics in cybercrime and continue to pose significant threats to your brand. Axon Shield employs a thorough procedure to first analyze your email usage and subsequently establish a whitelist of approved email sources.
    
3.  **Enhancing Security: Deploying WAF and DDoS Defense**: Start by reinforcing your DNS to withstand potential threats. Utilizing a reliable cloud provider ensures that any DNS assault can be absorbed, allowing your operations team to gather data for enhancing your threat model. This knowledge is crucial for optimizing resources in cybersecurity. Additional measures can include implementing WAF protection, which significantly decreases the likelihood of successful attacks on your web applications by blocking unauthorized access to APIs and customer data.
    

**Ongoing Operations - Homerun**
--------------------------------

Once an automated system is up and running with a regular collection of DNS data, we will offer ongoing monitoring and timely alerts.

You will have immediate access to dashboards available through the Axon Shield automation platform. However, we recognize that each customer has unique processes and inventory systems, so we facilitate the integration of data into those platforms. This approach is fundamental to our operational model and our commitment to customer support.

Our aim is to minimize the need for ad-hoc automation and configuration projects that demand specialized expertise. Once this foundation is established, you can concentrate on what truly matters—responding to incidents effectively and mitigating them, either through proactive measures or prompt incident management.

**Conclusion**
--------------

DNS data extends beyond merely linking domain names to servers; it plays a crucial role in an effective security framework. By gathering, resolving, and scrutinizing DNS records, you can make informed choices to eliminate obsolete records, strengthen your security defenses, and actively safeguard your applications through Web Application Firewalls (WAF) and DDoS mitigation solutions.

DNS management is an ongoing process. Continuous surveillance and strategic actions driven by data insights guarantee that your digital assets remain secure and perform at their best.
