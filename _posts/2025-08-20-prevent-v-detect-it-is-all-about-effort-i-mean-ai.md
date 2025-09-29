---
title: "Prevent v Detect: It is All About Effort
- I Mean AI"
date: 2025-08-20T05:00:00-04:00
categories:
- cybersecurity
- ai
- prevention
- detection
tags:
- prevention-vs-detection
- artificial-intelligence
- security-strategy
- automation
---
![Prevent Detect Ai](/assets/images/posts/prevent-detect/prevent-detect-ai.jpg)
*Detection v prevention - agility v prohibition*

My topic here is detection versus prevention in cybersecurity: should we assume most of our co-workers just want to get their jobs done, or should we make cybersecurity difficult? The use case is enterprise certificate management (aka certificate lifecycle management - CLM) and its automation.

Let’s say that you’re responsible for the technology side of a project building an enterprise certificate management system. The goal of such a project is to minimize downtimes due to expired certificates through automation. This is a significant problem to solve, and even a relatively small company will have many different ways it uses certificates, making a centralized system available for all of them quite challenging. Sooner or later, you will find that not everything can be automated. The point is to make it as painless as possible.

We have built this kind of automation many times, so the technology itself has been relatively easy ever since Let’s Encrypt “codified” the ACME protocol (RFC 8555). At some point, however, you may begin to receive pushback from users within the client organization. They might start complaining that the way you control onboarding is not secure enough.

Spanner in the Works
--------------------

This is the point when you, as the team delivering automation, can easily find yourself between a rock and a hard place. The challenge here is to combine the technology with the operational model to create a service that can be accepted across the entirety of the client’s company.

Let’s say you integrate (which is often the case) your automated certificate issuance with the company’s configuration management database (CMDB). What you can easily achieve is the automation of certificate issuance and the upload of all new certificates into the CMDB, allowing other teams to integrate that into their overall enterprise reporting.

You may also want to use the CMDB to create relationships between certificates, applications, and support teams. One way to do this is to capture all that information in service requests that are part of the onboarding process for the automation. If the automation can use the service request reference as part of the process, you suddenly gain a robust integration with enterprise operational workflows.

We usually try to reuse as many existing workflows as possible. If an application team needs to automate certificates, they create a request in the CMDB and then use the reference as part of the certificate client configuration. This reference essentially acts like a “username” that links certificates to the initial requests and, as such, to all the contextual information you may need.

Issues can begin to arise quickly if the service operations—i.e., the people overseeing certificate management—don’t keep an eye on what is happening. A part of any operational model should include procedures to deal with unauthorized certificates and incorrect sharing of API and client authentication keys. The technology provides enough information to support such processes, but it is not your team’s responsibility, and most likely, it will be an internal team that has to learn everything from scratch. Managing a service is a complex task.

**Operating an Automated Service**
----------------------------------

When you think about automation and running an automated service, the main focus of its operational model should be ensuring you know what to do when things go wrong. The challenge is that when such a service is introduced, not much tends to break initially. It’s easy for service owners to start thinking that they don’t need to put any effort into improving the service model.

However, two things will eventually happen. Firstly, things with a long lifecycle will trigger actions that may not have undergone as much testing. Secondly, as the service penetrates further across your company, users will start encountering difficulties that need to be addressed.

Here’s one example of what we experienced when more regulated clients wanted to start using the certificate automation.

![Prevent Detect Ai](/assets/images/posts/prevent-detect/prevent-detect-crowd.jpg)

The operational model was geared towards “low onboarding friction.” The technology had built-in hooks to support the resolution of unauthorized use, but these were not fully operationalized. The regulated clients feared onboarding, and their initial conversations with the service owner resulted in more confusion and irrational behavior. This can be explained by analogizing it to applying for a driving license. Their position was: we don’t want to obtain a driving license (automated certificates) because driving licenses can be used for identity fraud (someone else acquires certificates for our servers). Not using the service will not protect them from “identity fraud,” but the confusion was such that, at that point, the service had to implement excessive changes to calm things down.

Eventually, we identified three actions to improve the situation and regain the trust of users. Our aim was still to achieve as little friction as possible, but it had to become part of the changes.

1.  Prevent 1 - Increase interactions with new users to prevent the completely automated launch of new ACME software clients. This increases the effort required by the service users, but we were able to implement it as a self-service option.
    
2.  React 1 - Increase the ability to detect incorrect or improper behavior. No technological changes were required for this. Operationally, however, the team had to review their operating model and strengthen their oversight. New certificates were logged in a main inventory system, and their new tasks included daily reviews of issued certificates and the revocation of those violating agreed-upon terms and conditions (or cybersecurity standards). The team was able to implement this and start resolving situations within one business day.
    
3.  React 2 - The technology was already integrated into the client’s business intelligence dashboards, but events marked as security-related were not consistently followed up on. One such example was the “floating IP addresses” of registered clients. These events indicate that a registered software client changes the IP address from which it connects to the service. While this behavior is mostly non-malicious, it can also indicate that a client (API) key has been compromised.
    
4.  Prevent 2 - The final action was to increase friction for clients coming from “untrusted networks.” At this point, we had a better understanding of which IP ranges belong to the client and which were “external.” This understanding allowed us to configure and start enforcing existing technology controls. When new clients connected from external IP addresses, they would have to authorize their connection by responding to Slack or email prompts.
    

**Resolution**
--------------

Unsurprisingly, the technology changes from our side took priority. This isn’t surprising—conflicting interests often lead to choosing the path of least resistance first. Additionally, while the operational team was growing, new members were only learning the service features and gaining confidence in how to use them.

We could see that the governance model was not ideal, and we strongly encouraged the operational team to increase their engagement with users and create a “technology forum.” This forum would allow customer teams to raise their concerns, enabling the operations team to respond, suggest possible solutions, and listen to other users to understand the impact across the user base.

We have no way to instruct the client on how to build their operational model, but it was clear to everyone that communication towards users must be much stronger. Just as the technology remained fairly low-friction, enabling users to raise concerns should also be low-friction. Users need to be able to pose questions easily and receive prompt responses.

In one particular example, every new team using the service had to go through an onboarding process. The main point was to understand the use case and grasp what to do in case of breakages. This meant that establishing communication with users was quite straightforward, as there was a list of contact details. The difficult part was encouraging—mostly engineers—to overcome their timidity and start talking to other engineers. While this initial step can be challenging, it has a massively positive impact on how the service is perceived and trusted.

**Lessons Learned**
-------------------

As technology partners, we were not involved in initial conversations and missed opportunities to enhance the understanding of the technology controls. While this is something we cannot change for the future, our lesson was to improve documentation and enhance the operational teams’ understanding of the technology. The goal is for them to be able to answer questions correctly before concerns escalate to Level 3 support.

Returning to my initial question: detect vs. prevent. Should we increase friction and complicate the use of automation, or should we improve detection, assuming that 99% of users just want to get on with their jobs?

The latter is indeed the more difficult option—the actual service owner has to take on a lot of responsibility and “pain.” However, many manual tasks that represent that pain can be handled with AI agentic systems. What this means is that the technology can alleviate the burden on those operating automated services.

Axon Shield’s approach is to provide these AI-powered services as a combination of “self-hosted” deployments with centralized development of augmentation algorithms. This approach minimizes the security risks of data leaks, as the data never leaves the customers’ infrastructure, while allowing us to offer our cutting-edge expertise and deploy it through AI-powered services to customers as quickly as they desire.
