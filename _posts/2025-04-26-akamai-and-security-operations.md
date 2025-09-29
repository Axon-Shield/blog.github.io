---
title: "Akamai and Security Operations"
date: 2025-04-26T05:00:00-04:00
categories:
- cybersecurity
- operations
- akamai
tags:
- security-operations
- akamai
- enterprise
- deployment
---
![Akamai Security Operations](/assets/images/posts/akamai-operations/akamai-security-operations.jpg)
*Let's talk about operating Akamai WAF - the right way*

This blog post details experiences implementing Akamai security services across two large organizations, transforming limited initial deployments into comprehensive security solutions.

We have been using Akamai extensively to provide perimeter security protection and resilience against denial-of-service (DoS) attacks, as well as application-level attacks with its web application firewall (WAF) capabilities. Here are the things we found difficult without additional tooling.

### **What We Used Akamai For**

We have been driving - i.e., defining a change plan, implementing it, and handing operations over to internal teams - in two large companies. In both cases, the use of Akamai was limited, although in different ways. The first company used it for DOS protection for their main website only. The second company used it to speed up content delivery (as a CDN) with the security functions not really being used.

In both cases, we managed to do deliver majority of changes without really being noticed much. But in both cases, at the end of about 12 months' of effort, we delivered for the clients:

\- Massively increased use of Akamai - in one case we expanded the protection from 6 internet services to the entire internet perimeter with just a couple of exceptions.

*   \- Tuned and enforced DOS and WAF protection.
    
*   \- Defined an operational service wrapper.
    
*   \- Strengthened DNS - improved uptime and put in place DDoS resiliency.
    
*   \- Implemented security HTTP headers ensuring high scores in security benchmarks - from B to A+
    

Surprisingly, it was not the end of it; we have also actively worked with application teams and utilized CDN capabilities to mitigate issues in applications. Functionally, we addressed the mitigation of new HTTP/2 clients that would crash the application, TLS issues, and general HTTP header “pre-processing.” We even built a custom protection against bots, whitelisting only those bots that the company supported for SEO and marketing.

While the core Akamai platform is good and their professional services respond quickly when there is a problem, there were things we found difficult.

### **Collecting Logs**

There were two main issues we had to resolve to get Akamai security data into companies’ SIEM and log collection platforms (Splunk, Cribl, Vector, etc.).

Technical: Akamai has its own authentication mechanism, which is not officially supported and requires a “glue” layer that would pull the data and then forward it in a standard way to the target platform.

Operational: While the technical problem can be solved quickly (at least in the short term), the amount of data produced by Akamai security engines can quickly exhaust your bandwidth and storage limits. How to solve this issue depends on how you want to use Akamai for your cyber defense. In my opinion, the question is whether you have a large enough team so that some members can be trained to use Akamai analytics. Alternatively, you are likely to use your SIEM to collect Akamai data just like any other data and analyze it within your SIEM.

If Akamai is a large enough platform in terms of importance, you will need to invest more effort in cleaning up security feeds so that the volume of alerts is proportionate. We were quite amazed at how much more detail we could see when we tuned the DoS and WAF protection. We were able to identify not only DoS attacks but also all application-level attacks (from XSS to file injection) that were hidden within DoS, and we could drill down into the details of the likely attackers’ tools. This also allows you to make the most of the integrated attack protection that automatically blocks attacks.

The second approach is to move the core of your defense to a centralized SIEM and respond with IP address blocking—whether in the Akamai platform or in your infrastructure behind Akamai, such as public cloud services or firewall filtering.

Ultimately, the first approach is better, but it requires “sweat and toil” to implement. The second approach necessitates additional tooling. While it may be a worse option in the long term, it provides more flexibility and a longer runway to minimize impact.

![ ](/assets/images/posts/akamai-operations/akamai2.jpg)


### **Carrier-Grade NAT and DoS protection**

CGNAT may sound pretty geeky, but it has been impacting me since I switched my home internet to Starlink. CGNAT means that a large number of users share the same IP address, resulting in traffic per IP address being a multiple of what each user would normally produce.

It is almost impossible to register or log in to Facebook using Starlink. Some online newspapers will block you, and you will also encounter many more captchas. The same problem can be observed in users accessing the same web service from behind a company’s egress proxy.

In terms of Akamai, the usual way to implement DoS protection is to set rate limits per IP address. If it is for a website, it will be based on the typical traffic produced by a web browser.

There are several ways to get around this problem, but they are not easy nor generally suggested by Akamai support; the default is to significantly reduce the strength of Akamai’s DoS protection.

### **Operational Response - Alarms**

Alarms are another feature of Akamai’s security service, but they are hardly ever used correctly, and it is difficult to define their role.

One of the most challenging aspects we have been facing is efficient operational response, whether it involves changing legitimate traffic patterns or actual attacks against protected websites and APIs. There are two primary aspects to consider, with DoS being the more complex of the two.

As mentioned above, what you set in Akamai’s DoS protection is a rate limit for the number of requests per IP address. For instance, when a user accesses a website, their browser sends requests for the main page, images, style sheets, etc. You configure Akamai to define a threshold above which all requests will be blocked. You can further enforce a penalty box, which temporarily blocks the IP address completely for about five minutes.

This method is effective for conventional applications. However, not all applications behave the same way, and web browsers can change their behaviors over time, or your website may increase the number of resources per page. Consequently, legitimate users may engage in automated content scraping instead of using standard web browsers. While some of these automated systems may not be entirely legitimate, the challenge lies in determining whether a particular client is genuine or if it is a malicious entity attempting to crawl the website and harvest content for an attack, such as creating a clone of your site.

Akamai offers functionality to set alerts that notify you via email when specific patterns are detected. This feature operates independently of the actual protection measures, and it is essentially an aggregation mechanism.

There are 2 main problems:

1.  Time to respond - it takes long to "scramble" - most attacks are over in less than 5 minutes.
    
2.  Long-term changes (evoluation) of security patterns - the alarm is ON/OFF thing, doesn't tell you how close you're to the threshold.
    

When an alert occurs, you receive an email that allows you to log in, assess the situation, and update the protection settings. This process could take about 50 minutes during office hours, resulting in a potential impact duration of close to an hour if the threat is genuine. Additionally, if the changes are related to a new browser version that affects how requests are processed, the impact could be more pronounced.

Akamai can help you not only with security measures but also with addressing internal issues within your applications. This has significantly influenced our decision to expand Akamai’s use beyond merely protecting our main website to encompass all our internet-facing applications and APIs.

As for DDoS attacks, they follow a similar principle: changes can stem from both internal alterations and external factors. Issues can arise during testing, which might overlook certain scenarios, leading to false alerts or notifications through the WAF service in Akamai, thereby hindering service.

### **Prolexic Integration into SIEM**

Prolexic is an Akamai service that implements L3/L4 DoS protection via Akamai’s scrubbing centers. You essentially redefine the inbound traffic to go through Akamai’s scrubbing before it reaches your services. (Outbound traffic is not impacted.)

It is impossible to push this data into your SIEM without external tooling. While it is primarily a managed service, what you want to be able to see is the bandwidth used on your on-premises services. This fiber bandwidth (and your firewall capacity) represents the ultimate limit for what you can serve from your physical servers (and sometimes from the public cloud).

It is very useful to see the traffic profiles provided by Prolexic for your bandwidth planning. However, there is no built-in mechanism.

### **Bottomline**

The Akamai platform can be absolutely used as a self-contained system to manage the security of your network perimeter. However, you must build your operational model around the platform and its features.

If you want to build your Security Operations Center (SOC) around a Security Information and Event Management (SIEM) system, and to put it bluntly, base your defense on blocking IP addresses, Autonomous System Numbers (ASNs), and geographic regions, you will need some tools for integration with your SIEM to avoid unwanted surprises when you receive your next invoice for your SIEM service.

Adding some external managed tools definitely allows you to adapt Akamai to your cyber defense if you do not want to build it around a particular third-party platform.