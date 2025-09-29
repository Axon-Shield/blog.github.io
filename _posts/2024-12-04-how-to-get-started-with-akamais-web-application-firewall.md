---
title: "How to Get Started with Akamai's Web Application Firewall"
date: 2024-12-04T05:00:00-04:00
categories:
- cybersecurity
- akamai
- tutorial
tags:
- akamai
- waf
- setup
- configuration
- security
---
![Akamai Waf Getting Started](/assets/images/posts/akamai-setup/akamai-waf-getting-started.jpg)
*Let me walk you through the process of configuring Akamai’s WAF*

Your internet presence must be secure. Akamai's Web Application Firewall (WAF) is one of the finest ways to achieve this security. Perhaps it is the difficulty of the initial installation that you are worried about. Do you wonder how to make it suit your individual needs? Which methods guarantee that the onboard of new members is free of any negative effects on the procedures? In this post, we’ll walk you through the process of configuring Akamai’s WAF—from setting up your HTTPS certificate to creating a Property and fine-tuning security settings. Whether you're a seasoned IT professional or new to web application security, this guide will help you get your Akamai WAF up and running with ease. Let’s dive in and secure your digital assets step by step!

Ready to Fortify Your Network Perimeter? Here's How to Start with Akamai's WAF
------------------------------------------------------------------------------

Obtaining a Web Application Firewall (WAF), Akamai provides this with a powerful tool to improve one of the most secure parts of your web application. The very first days can be handled quite well by simply careful setting and regular checking. How do you put your personal touch in it? What rules would you set up just to soften your operation?

The most critical device you need for network safeguard nowadays is a Web Application Firewall (WAF), a sure way against security threats. We at Akamai and Cloudflare work closely with direct customers and therefore, we have practical experience with both. If I’m out of time, may I ask if you’ve conquered the first challenge--successfully executed the contract?

Web Application Firewall (WAF) is one of the ways that Akamai protects the network, it can also be set to function it based on a “per hostname” mode and it is mostly for ports 80 and 443. It is different from the IP range-based DDoS protections relying on port 80, 443 and the whole subnet of an ISP’s own network. When adding a new website to Akamai, focus on the following three aspects:

1.  **HTTPS Certificate** – The basis of WAF protection is the secure implementation of the proper certificate.

2.  **Property Creation** – Pretend you're the property owner of your digital site within Akamai's setup but you are only the one constructing the site virtually.

3.  **Security Configuration** – Build the specifics of the protection to secure your website that is distinguished among other sites.

After following them, you will surely be safe in your digital area. Are you willing to take on this challenge?

### Simplified Steps to Configure Akamai’s WAF and Secure Your Web Application

To safeguard your web application through Akamai's WAF, you should take the following key measures. Here’s a clear and practical guide to help you get started:

#### **Step 1: Secure Your HTTPS Certificate**

*   Select the domain names that you require.

*   Download a **CSR file** and set up your certificate.

*   Submit the certificate to Akamai, which stores the private key in one place of the platform where the key is needed.

**Pro Tip**: If your certificate isn’t ready yet, you can move forward with other setup tasks. The certificate will automatically attach to your configuration once it’s uploaded.

#### **Step 2: Build Your “Property”**

*   **What's a Property**? This represents the content delivery configuration for your site.

*   Start with Akamai's t**emplated Property** and customize it:
    *   Delete unnecessary elements.
    *   For minimal impact during onboarding, remove all caching and monitoring.
    *   Focus on directing traffic to your application that generates responses.

*   Establish an **edge hostname**, which is the significant portion of your DNS update that will connect your traffic to Akamai.

#### **Step 3: Create the Security Configuration**

*   Akamai gives you a **default security template** for you to initiate with.

*   Add the necessary **hostnames and paths** (set paths to /\* to capture all traffic).

*   For initial testing, leave all protections in **"Alert" mode** and deploy the configuration.

### **Testing & Final Adjustments**

1.  **Test on Akamai Staging**
    *   Point your test laptop or VM to Akamai's staging network by editing the hosts file (or equivalent).
    *   Test your website and APIs thoroughly..

2.  **Go Live with DNS Updates**
    *   Point your test laptop or VM to Akamai's staging network by editing the hosts file (or equivalent).
    *   Test your website and APIs thoroughly, or let your customers generate enough traffic.
    *   Relax—issues are rare unless you have complex mTLS setups.

3.  **Monitor and Fine-Tune**
    *   After 2–4 weeks, visit **Akamai's Security Centre** to review alerts.
    *   Handle any **false positives** by adding exceptions to your WAF configuration.
    *   Fine-tune **rate limits** for DDoS protection, controlling requests from single IP addresses.

###   
**The Finish Line**

*   Switch your security configuration from "**Alert**" to "**Block**." From this point, Akamai's WAF will actively block XSS, SQLi, and other web attacks.

*   Akamai automatically updates WAF rules for emerging threats. All you need to do is renew your certificate annually.

### **What We Can Do**

We have managed to deploy Akamai for all internet services of a middle-tier UK bank in less than 12 months, which included establishment of an operating model and an initial set of operating procedures.

You can make the entire process efficient using **Axon Shield's automation solution**. We can help you understand every step, write SOPs that are appropriate, and teach your team to set up WAF configurations without problems.

🔒 The whole process of web security has become much easier for you!
