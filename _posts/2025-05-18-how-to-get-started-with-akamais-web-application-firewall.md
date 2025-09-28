---
layout: post
title: "How to Get Started with Akamai's Web Application Firewall"
date: 2025-05-18
categories: [cybersecurity, akamai, tutorial]
tags: [akamai, waf, setup, configuration, security]
image: /assets/images/posts/akamai-setup/akamai-waf-getting-started.jpg
author: AxonShield
original_url: https://axonshield.com/how-to-get-started-with-akamais-web-application-firewall
---

The very first days can be handled quite well by simply careful setting and regular checking. How do you put your personal touch in it? What rules would you set up just to soften your operation?

The most critical device you need for network safeguard nowadays is a Web Application Firewall (WAF), a sure way against security threats. We at Akamai and Cloudflare work closely with direct customers and therefore, we have practical experience with both.

## Understanding Akamai WAF

Web Application Firewall (WAF) is one of the ways that Akamai protects the network. It can be set to function in a "per hostname" mode and is primarily designed for ports 80 and 443. This differs from IP range-based DDoS protections that rely on port 80, 443 and the whole subnet of an ISP's network.

## Getting Started: Three Key Aspects

When adding a new website to Akamai, focus on the following three critical aspects:

### 1. HTTPS Certificate
The basis of WAF protection is the secure implementation of the proper certificate. This forms the foundation of your security architecture.

### 2. Go Live with DNS Updates

**Testing Phase:**
- Point your test laptop or VM to Akamai's staging network by editing the hosts file (or equivalent)
- Test your website and APIs thoroughly, or let your customers generate enough traffic
- Relax—issues are rare unless you have complex mTLS setups

**Production Deployment:**
- Update DNS records to point to Akamai
- Monitor traffic flow and application performance
- Validate all services are functioning correctly

### 3. Monitor and Fine-Tune

**Initial Monitoring (2-4 weeks):**
- Visit Akamai's Security Centre to review alerts
- Handle any false positives by adding exceptions to your WAF configuration
- Fine-tune rate limits for DDoS protection, controlling requests from single IP addresses

## The Finish Line

### Security Activation
- Switch your security configuration from "Alert" to "Block"
- From this point, Akamai's WAF will actively block XSS, SQLi, and other web attacks
- Akamai automatically updates WAF rules for emerging threats

### Ongoing Maintenance
- Monitor security alerts and adjust configurations as needed
- Renew your certificate annually
- Regular review of security policies and rules

## Real-World Success

We have managed to deploy Akamai for all internet services of a middle-tier UK bank in less than 12 months, which included:
- Establishment of an operating model
- Development of initial operating procedures
- Complete security policy implementation
- Staff training and knowledge transfer

## How Axon Shield Can Help

You can make the entire process efficient using Axon Shield's automation solution. We can help you:

- **Understand every step** of the deployment process
- **Write SOPs** that are appropriate for your organization
- **Teach your team** to set up WAF configurations without problems
- **Automate routine tasks** for ongoing management

🔒 The whole process of web security has become much easier for you!

*Original source: [How to Get Started with Akamai's Web Application Firewall](https://axonshield.com/how-to-get-started-with-akamais-web-application-firewall)*
