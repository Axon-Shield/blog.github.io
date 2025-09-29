---
title: "Akamai Web Application Firewall - How It Works"
date: 2025-05-18T05:00:00-04:00
categories:
- cybersecurity
- web-security
- akamai
tags:
- waf
- firewall
- security
- ddos
- protection
---
![Akamai Waf](/assets/images/posts/akamai-waf/akamai-waf.jpg)
*Akamai Waf*

Akamai's Web Application Firewall (WAF) delivers enterprise-grade protection against evolving cyber threats through its innovative Adaptive Security Engine. Leveraging AI and ML algorithms, Akamai's solution continuously updates its ruleset to defend against zero-day exploits, DDoS attacks, SQL injections, and XSS vulnerabilities without impacting legitimate traffic. What sets Akamai apart is its logical organization of protection through attack groups—from Web Attack Tools to Cross-Site Scripting—enabling administrators to quickly customize security postures with just a few clicks. The global edge server network ensures minimal latency while maximizing security across your applications and APIs. Axon Shield enhances this protection by seamlessly integrating Akamai APIs into your cyber defense ecosystem, providing actionable intelligence for your SOC team and strengthening your overall security posture against the ever-changing threat landscape.

Introduction
------------

Web Application Firewalls (WAFs) have been a critical component of modern web security. It is playing a critical role in protecting the enterprise perimeter against harmful Internet traffic. As the primary function of WAFs is to carefully examine, clean, and terminate any HTTP/HTTPS connections that show signs of malicious software and targeted at web applications or enterprise Application Programming Interfaces (APIs), these systems can provide a single pane of glass showing you all attempts to attack protected assets - whether it's server takeovers denial of service (DoS) or unauthorize data queries.

Akamai Overview
---------------

This forward-looking approach for dealing with cyber risks is an indispensable part of defending against a wide range of cyber threats, including various threats like zero-day exploits, Distributed Denial of Service (DDoS) attacks, SQL injection, and Cross-Site Scripting (XSS) that are as yet to be discovered in the future. The Akamai WAF product is integrated with their core function of content delivery (CDN) but must be configured separately.

The core Akamai's WAF (also known as Kona Site Defender) can be further combined with API protection, Bot detection, or Client reputation modules. Not all of them are suitable for every enterprise - the use depends on your software design patterns and some are only effective for particular types of applications or endpoints of applications/web sites.

All these solutions benefit from Akamai's robust network of "edge servers" which is distributed across the globe. It comes with a myriad of strategically located servers worldwide and automatically optimizes traffic routing between users and servers. The network that has been designed in this way ensures minimal latency and maximum availability of content and security services.

Akamai WAF Updates
------------------

An essential component of the Akamai WAF design is the Adaptive Security Engine with automatic updates of WAF rules. This technology is powered by a set of AI (Artificial Intelligence) and ML (Machine Learning) algorithms, and intelligent threat assessment systems - all working for Akamai customers behind the scenes. It continuously identifies new cyber threats, which constantly emerge in their different patterns. From the customer point of view, the results of this learning are twofold. The first represents continuous updates of WAF ruleset that are applied automatically whilst ensuring no impact on genuine traffic. The second, a recent addition, are "rapid rules", which are responses to new attacks. These are shown separately and Akamai decides on the default mode of protection (alert, stop traffic, ignore) - customers can change the behaviour anytime.

Note: We have been having a number of discussions whether to apply Akamai on applications in public clouds with own WAF services. This feature of managed rules is unparalleled. It is absolutely necessary for any enterprise to be able to response to new threats quickly. It is customer responsibility to implement these rules in public clouds.

Akamai WAF divides its protection rules into Attack groups. The groups represent logical combinations of rules by Kona Rule Set (KRS), Akamai's proprietary library of continuously updated security rules that are tailored to fight a variety of known web application vulnerabilities.

These groups have been simply imagined as if rules were placed logically according to their aim and separated into the attack groups by Akamai. What it means for you? You can very quickly select attack groups irrelevant to a particular application and disable them with a simple mouse click.

The attack groups are easy to understand and represent unique attack vectors like Website Attack Tools, Web Protocol Attacks, SQL Injection Attacks, and Cross-Site Scripting Attacks.

Security policy management has been greatly simplified via the strategic use of attack groups. Therefore, administrators are able to grant, revoke, or change the specifics of entire categories of threats in just a few mouse clicks. The resulting efficiency not only incorporates all the operational activities but also brings about an improving and better situation for the security controls, there has been no such a direct application of controls related to the threat landscape of the web application or API as now is the case.

Akamai Security Configuration
-----------------------------

Akamai's categorization of web application attacks is indeed a well-thought-out system. The company goes into the details, groups the attacks together, and does it in a very systematic way. The broad categories that such an understanding could be divided into are as follows: Reputation Activity (the issue here is the origin of the traffic), App Protection (the attacks are basic security measures), Custom Rules (the rules that the user can make themselves to tackle certain specific security issues), Bot Activity (malicious traffic that is automated), and DoS Protection (the traffic management effective during DoS).

The basic configuration must cover:

1.  DoS protection
    
2.  WAF rules
    
3.  Custom Rules - highly recommended to create an alert "counter" rule that provides real time info about the overall traffic v "suspected malicious" traffic.
    

Let's focus on the WAF rules for now - KRS used to be a simple "kill or let through". The current implementation uses weighing. Each transgression that an HTTP/HTTPS request makes counts towards an aggregate scoring within an attack group. When that reaches a threshold, the request is marked as malicious and blocked (if the the attack group is set into enforcement mode, i.e., "block".

How does the scoring work? Akamai has succeeded in bolstering its WAF capabilities greatly over time with the advent of the Adaptive Security Engine (ASE), which is a top-drawer AI-based tool for attack detection that has the unique quality of learning as detection is on. The ASE benefits from the human reasoning aspect and the KRS, which are the brains of the operation and, consequently, they do the checking and assign the threats a score to precisely rate the situation with every single interaction.

The ASE checks the validity of incoming requests contextualizing their challenging nature and assigns a weight to each of the investigations of the score. Such an elaborated strategy at work forth the foundation set by the KRS rules and well-organized in attacking groups, ASE brings in the most critical feature of dynamic analysis and real-time adaptation. The WAF will hence be enabled to not only effectively find and stop both traditional and brand new attack routes but also to keep the posture of its defense intact and adaptive.

An In-depth Review of Specific Akamai WAF Attack Groups
-------------------------------------------------------

Akamai's Web Application Firewall offers a wide range of attack groups where each is carefully designed to address specific types of web application threats. Having knowledge of each group's purpose and domain is essential to properly setting up and handling Akamai's WAF for web applications and APIs security.

*   **Web Attack Tools (WAT)**: This attack group is highly specialized in the detection and removal of harmful traffic, which is planted by commonly known attack tools and bot scripts. Such tools are widely used by the attackers to find the vulnerabilities, to scan the target, and for the automated execution of the different web application attacks. The detection in this group is often based on the discovery of particular user-agent strings and request patterns that are correlated with these tools.}
    
*   **SQL Injection Attacks (SQL)**: This technology group is entirely responsible for locating and preventing illegal activities where a hacker tries to insert a malicious code into a web application database. A significant and widely spread threat, SQL injection is a hack that allows attackers to take control of the database. The content of the group consists of detection patterns for SQL keywords and syntax in the users supplied input.
    

*   **Web Protocol Attacks (PROTOCOL)**: The particular collection of the group is all about the detection and avoidance of the exploitation of vulnerabilities or the deviation from regular web protocols like HTTP. It concentrates on the conformity of protocol standards and therefore is capable of detecting and blocking the requests that are intentionally out-of-spec and thus dangerous. Detection can be made by means like irregular and omitted headers.
    
*   **Cross-Site Scripting Attacks (XSS)**: This group is aimed at stopping the intruders from inserting malevolent scripts into the web pages, which are later executed in the other users' browsers. It's done by analyzing a variety of XSS attacks and determining signs of a script being injected, like the presence of HTML script tags or JavaScript event handlers.
    
*   **Local File Inclusion Attacks (LFI):** This group of attacks are to find and prevent hackers from inserting local files into the web server using applications' file processing vulnerabilities. Identification often employs the method of tracing (e.g., ../) by the attacker in the input where user input is present.
    
*   **Remote File Inclusion Attacks (RFI)**: This particular group, belonging to the RFIs and sharing the same meaning as LFI, is against the hosting of files located on remote servers to the unsecured area of the web application, hence making the web server vulnerable to the attacker's whims. Detection might include the entry of a URL from an external source in user input.
    
*   **Command Injection Attacks (CMD)**: This group concentrates on the discovery and prevention of suspicious activities such as attempts to run unauthorized commands on the operating system of the web server. Identify the attack by regularly reviewing for operating system command separators and by examining any input that seems to be common system command or modify that input.
    
*   **Web Platform Attacks (PLATFORM)**: This group is mainly concerned with threats that particularly target the basic web platform or the technologies that are employed to build and manage the web application. Such attacks can be directed at the server or the application framework. The method of detection can be tracked by looking for the request patterns that are peculiar to known platform-specific attacks.
    
*   **Web Policy Violations (POLICY)**: This attack group's main purpose is to find and stop requests that are in conflict with certain safety policies which were set by the organization for their web application. The detection aspect is highly adaptable and it is based on the specified policies.
    
*   **Outbound Traffic (OUTBOUND)**: This group is responsible for keeping an eye on the traffic which is sent out by the web application and thus controlling, if needed. It is helpful in recognizing data exfiltration trial or contacting with command and control servers.
    

Other Security Engines
----------------------

Beyond the core WAF (Kona Rule Set), Akamai offers the following security engines, which are available as separate modules - you are usually charged extra for Bot Management and Client Reputation.

*   **Reputation Activity**: Using Akamai's threat intelligence data, this attack group scores the clients' IP addresses concerning their reputation, thus, blocking any traffic they are suspicious of, either alerting on traffic from sources with a bad history of being involved in malicious activities.
    
*   **Bot Activity (BOT)**: It is a particular group of attackers that focus mainly on recognizing and deleting abnormal traffic which is automated and, therefore, malicious (bots). Identification includes the analysis of request patterns and behavioral analysis processes.
    
*   **DoS Protection (DOS)**: The gang of attackers who execute this sort of attack is called DoS. In this case, the attack group's function is to secure and maintain a web application's and APIs' working by blocking the Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS) attacks. Detection will mostly require the ability of observing increased traffic at an unusual level or patterns which may suggest a DoS attack.
    
*   **App Protection**: This kind of attack group is usually referred to as a "broad" one because it encompasses a lot of protective strategies for web applications and APIs. Such measures are usually for those vulnerabilities and attack vectors that are not limited to just some special cases.
    

![Akamai Network](/assets/images/posts/akamai-waf/flow.jpg)


Managing and Configuring Akamai WAF
-----------------------------------

The Akamai web console (aka Control Center, aka Luna), is the single point of access for the security administrators to be able to enter into and make changes to every element of their WAF configuration, bearing in mind that the settings for attack groups are also part of that.

The security configuration is applied based on hostnames and if you need more granular approach, you can use URI paths. Setting up a new WAF Security Configuration and Policies within, starts by defining which hostnames will this apply to. Once you define the "target", you can quickly go through firewall settings. I highly recommend creating "network lists" - even if they are empty to start with - for firewall blocking and whitelisting. You also need to quickly go into DoS configuration and set all the default items into Alert. Now we can proceed to the more interesting part - WAF rules.

The Akamai WAF doesn't just permit you to decide the various actions on a per-group basis, changing this and that according to the individual type of threat, but it actually helps you to follow it through with the implementation of those actions. Choices are in action would include, but not be limited to, responses such as "Alert", if no blocking is done to let the request be logged; "Deny", to block the request; or "None" that leads to non-action being taken. Actions at the rule level give a finer control over the WAF's behavior.

You start a new configuration by simply setting all attack groups into Alert - ignore rules within, we get back to them once Akamai starts showing some data. You activate the configuration into the Production network and let it do its thing for a couple of weeks.

Once you have data about what the WAF identifies as malicious, you can start fine-tuning attack rules. When it comes to situations where you could not say if the traffic was legitimate and thus the WAF rules cause an unexpected reaction, with Akamai WAF you can set exceptions to specific rules or attack groups by using the web interface, for instance. If required, define exceptions to let through genuine traffic that triggers false positives. These exceptions can be varied depending on attributes such as IP address, the geographical location of the client, patterns in the payload, or the user's setting of parameters within the HTTP request.

What Axon Shield provides is effective use of Akamai APIs to integrate WAF into your cyber defence. Akamai offers a set of APIs for organizations that aim at automating security management, enabling not only to automate the process of securing applications and APIs on Akamai devices, but also the use of the console or other products of the same line of the company.

Akamai's customers are primarily interested in DoS protection and Akamai's default reports focus on this aspect of protection. However, you can, as Akamai customer, request additional reports that would detail WAF, Bot, and/or reputation threat landscape.

Monitoring and Analytics for Attack Groups
------------------------------------------

The Akamai Web Security Analytics platform is there to help security teams that are in charge of the WAF system to run the procedures of monitoring and analysis without hitches while at the same time monitoring the performance of attack groups. A variety of toolsets enables the tracking of attack traffic trends, the plotting of the attacks into different categories, and the estimation of the effect of security configurations.

There is a main security dashboard that shows aggregate data for the WAF protection. From that, you can go into web analytics, where you can go into detailed analysis of attacks to identify source, attack data (patterns) - which can show the tool attackers used (although you may need knowledge of tool sets available on the market).

This great visibility advantage will push and confirm the identification of trends and patterns that will bring forth an easy refining of WAF configurations. If needed, the very detailed information stored in WAF logs on the firing of rules may be used for an understanding of security situations and elimination of false alerts.

Onboarding to Akamai WAF
------------------------

A phased approach is the only safe and effective way to set up attack groups in Akamai WAF. The initial "Alert" mode is used to monitor the situation. The latter "Deny" (or Ignore) mode is then utilized for active blocking. A regular review of attack groups and updates based on the traffic patterns and the threat landscape changes is vital.

Attack group setting tuning is the method for minimizing both false positives and negatives; this can be achieved through the implementation of the necessary exceptions. A thorough testing in an environment other than production before making the changes public is highly advised. It is imperative to integrate the monitoring of attack group activity into the security operations of the organization, along with the establishment of alerts and SIEM integration for a proactive security posture.

A completely separate topic is integration of Akamai with ITSM. ITSM integration becomes important when cyber/infosec and application teams start using it actively as part of day-to-day operations. One approach we have worked on with a client was a definition of a "server category" as Akamai configurations can be conceptually viewed used as such. But this is for another post.

Once you tuned the protection, you can feed attack data into your cyber SOC team to take further actions, e.g., blacklisting particular IP addresses or even geographic regions on a temporary (or permanent) basis.

This co-ordination with you SOC is important during the initial phase when you want to be protected during the onboarding process where WAF only "alerts". This means you can see attacks but they are not blocked - they do ultimately hit your applications.

Conclusion
----------

Akamai Web Application Firewall, with the help of attack groups, is a powerful arsenal in defending web applications from online threats. The attack groups are created with the Kona Rule Set and further developed by the Adaptive Security Engine to provide web applications and APIs with a controlled and organized level of protection. The security professionals who delve into the purpose and the scope of each attack group and map them to applications' different layers take a big leap forward in terms of security. The management and configuration of these attack groups, using the provided tools and features of Akamai, are a must-have for the security of web applications. Besides, WAF policies need to be continuously tracked, analyzed, and improved based on the changes in the threat landscape to keep a security posture strong and avoid successful cyberattacks.

Want to learn how to integrate Akamai into your SOC without exceeding your SIEM bandwidth? Get in Touch.