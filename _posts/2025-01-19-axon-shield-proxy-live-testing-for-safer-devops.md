---
title: "Axon Shield Proxy - Live Testing for Safer DevOps"
date: 2025-01-19T05:00:00-04:00
categories:
- devops
- testing
- proxy
tags:
- proxy
- testing
- devops
- deployment
- safety
---
![Axon Shield Proxy](/assets/images/posts/proxy-testing/axon-shield-proxy.jpg)
*Take control of your service deployments*

Take control of your service deployments. Imagine being able to manage new system versions. Performing live testing down to single customer, while gaining insights into your system's operations. Let me introduce a revolutionary testing proxy service that empowers you to fully control changes to your applications and systems.

The Challenge of Modern Service Testing
---------------------------------------

Deploying new version of production services is critical for reliability. Well-defined processes and coordination among multiple teams are needed to roll back changes quickly in case of errors when deploying updates to web services. One of the major challenges is DNS management: common DNS platforms don't support dynamic resolution switching, and engineers are usually afraid to lower TTL values below 5 minutes due to server load and propagation reliability concerns. With this limitation, it's practically impossible to implement fast and granular traffic switching between service versions using traditional DNS-based approaches.  
  
These DNS constraints, coupled with the inability of traditional testing methods to fully emulate real-world conditions, form a huge roadblock in agile service deployment. This is where our intelligent test proxy comes in.

What Makes Axon Proxy Special?
------------------------------

Think of this proxy as a high-end traffic controller for your web services. By building DNS directly into the proxy itself, we eliminate one of the largest operational bottlenecks in production testing: the need for coordination between different teams. No more waiting for DNS changes to propagate or orchestrating efforts between network operations and development teams when issues arise. The testing team has the freedom to independently control the traffic flow and respond quickly to any problems, making production testing faster, safer, and more agile.

  
Unlike the traditional proxies that simply forward requests, this has a brain: it routes traffic intelligently across different versions of your service and then collects and analyzes data to ensure everything runs smoothly. When there are issues, you can act immediately without waiting for DNS propagation or worrying about multiple teams coordinating their efforts.

### Flexible Architecture for Maximum Performance

The system offers two distinct operational modes, letting you choose the optimal approach for your needs:

1.  Proxy Forwarding Mode: The proxy handles the routing of requests between old and new versions, providing detailed monitoring and control while adding minimal latency.

2.  Direct DNS Resolution Mode: For maximum performance, the proxy can operate purely as a smart DNS resolver, directing selected users straight to either version of the service, completely bypassing the proxy for the actual requests. This ensures zero added latency while maintaining testing control.

You can even mix these approaches, using direct DNS resolution for most traffic while keeping proxy forwarding for specific test cases that need detailed monitoring.

The system has two operating modes, reflecting your needs and balancing the impact on customers with availability of analytical data:

1.  Proxy Forwarding Mode: The proxy will take care of routing requests between the old and new versions, providing full monitoring and control while introducing a minimal amount of latency.

2.  Direct DNS Resolution Mode: for the highest level of performance, the proxy can also act as a simple DNS resolver that directs certain users directly to either version of the service, bypassing the proxy entirely for the actual requests. This ensures zero added latency while still maintaining control over testing.

You can combine both modes with DNS changes. You can do direct DNS resolution for most of the traffic while still keeping proxy forwarding for some test cases that need close monitoring.

### Smart Traffic Management

The proxy can split your traffic in several ways to support your approach to live testing:

*   it can send a percentage of requests to the new version;
*   route specific users or sessions to test new features;
*   mirror live traffic to your test environment without affecting real users;
*   switch individual requests on the fly based on custom rules;
*   limit exposure by counting DNS responses to ensure only a predefined number of users are directed to the new version; or
*   target specific network segments by analyzing live traffic patterns and routing selectively based on IP ranges.

You could, for instance, expose your new version to just 100 DNS requests from your most active IP ranges in order to have a controlled test group based on real usage patterns. The precision in control over DNS resolution lets you accurately set the number and which users will participate in the test but retains the possibility to immediately turn back if required.

  
Best of all? All this is done transparently to your users. They keep using your service as usual while you collect valuable insights on the performance of your new version.

### Beyond Basic Metrics

Whereas traditional monitoring usually focuses on basic metrics like response time and status codes, our proxy takes it a few steps further. It is watching for those subtle changes in behavior that may indicate problems. It also allows defining new criteria to evaluate in the future.

*   response patterns that break the ruleUnforeseen changes in header structures;
*   content discrepancies that might affect the user experience; and
*   performance differences depending on request type.

We're also looking at advanced AI-driven analytics. It gets really interesting when you either don't know what to look for or want to use a different approach in identifying any changes in the behavior of the new version. The proxy includes AI-based anomaly detection, capable of identifying problems that might go unnoticed by traditional monitoring. It learns what "normal" looks like for your service and alerts you when something doesn't quite fit the pattern.

Imagine releasing a new edition and immediately recognizing whether it:

*   responds differently to certain types of requests
*   introduces subtle performance regressions
*   changes API behavior in unexpected ways
*   impacts certain user groups differently

And provides you with the criteria used so you can add them to your set of tests so the same difference is always checked in the future.

Real-World Applications
-----------------------

Let's look at some practical scenarios where this proxy can significantly reduce the risk of incidents during new versions' deployments.

The below assumes that your devops process already includes a "staging" environment that basically replicates your production, including using production data. This seems to be a common approach for production applications.

### Gradual Feature Rollouts

The beauty of this system is that it allows you to have fine-grained control over exposure to features. You don't have to begin with wide rollouts; you can begin as small as you'd like. Want to test with a single customer? No problem at all. Want to move to 1% of your user base? Piece of cake. Feeling pretty confident and wanting to hit 10% or more? The proxy handles all of these cases equally well.

What is powerful, though, is that this works in both operational modes: be it with proxy forwarding to gain detailed insight into the behavior of your customers, or directly in DNS resolution for ultimate performance—either way, you maintain granular control over your rollout. Such level of precise testing was very difficult with the traditional method of DNS-based deployments.

### Performance Testing

By mirroring live traffic to your test environment, you can check how your new version handles real-world load patterns. The AI analysis helps to detect performance bottlenecks before users are affected.

### API Evolution

Use the proxy to update APIs so that new versions maintain compatibility while adding features. Content analysis capabilities, integrated into a CI/CD pipeline, should help catch such unexpected changes in response structures and would also reveal whether the new API fails for a certain combination of request payloads.

### Geographic Testing

Need to test the performance of your service in a particular region? The proxy will route traffic from specific geographic regions or IP ranges directly to your new version, allowing you to test performance and functionality in target markets before doing a full rollout. Especially useful for:

*   Testing CDN configurations
*   Validating regional compliance features
*   Assessing localization changes
*   Measuring regional performance variations

### Database Migration Validation

Use the proxy to migrate a new database or caching layer, by:

*   Compare response times between old and new database implementations.
*   Validate data consistency across systems
*   Test cache hit rates and performance
*   Safely rollback when inconsistencies are found
*   All the while keeping your production database as the source of truth.

### Third-Party Integration Testing

Integrating new third-party services can be very helpful. The proxy can help in the following ways:

*   Testing new payment processor integrations on live traffic, but this traffic is limited and constrained in volume.
*   Validating new analytics implementations
*   Comparative performance of various service providers

The Axon proxy can you you guarantee smooth, seamless transitions when switching between providers.

### Compliance and Security Testing

Security and/or compliance are more and more important for internet services. The Axon proxy is perfect for validating security changes and compliance features:

*   Test new WAF configurations - not all vendors provide managed WAF updates
*   Test for GDPR or other regulatory compliance features
*   Test the impact of new security headers or policies; and
*   Monitor for security-related regressions.

### Infrastructure Migration

Moving to a new cloud provider or updating your infrastructure? Use the proxy to:

*   Compare performance between cloud providers
*   Validate service mesh configurations
*   Test new load balancer setups
*   Assess impact of network architecture changes

Advantage Over Global CDN Testing
---------------------------------

While global CDNs are great for delivering content and can be used in conjunction with this proxy, they are a huge problem for agile test and deploy. What's the big deal? Log reconciliation time.

Because of their massive global infrastructure, CDNs usually take hours to aggregate and return complete traffic logs. That means the delay is very real for companies running applications from one or a few cloud regions—think specific AWS or GCP locations. When you're operating at this scale, waiting hours for log data to understand how your changes are performing isn't just inconvenient; it's a major barrier to agile development.

Our proxy solution offers instant visibility into traffic patterns and application behavior. It means having real-time insight into:

*   how your changes are performing,
*   detecting problems or anomalies instantly, and
*   the ability to quickly make data-driven decisions concerning rollouts.

Shorter iteration cycles mean you can test and push deployments faster. You still use the global CDNs for their content-delivery strengths but augment that with a proxy for testing and traffic management. This hybrid approach gives you the best of both worlds:

*   CDN for global content delivery and DDoS protection
*   proxy for agile testing and instant visibility
*   seamless integration between both systems
*   no compromise on deployment speed or monitoring capabilities

Minimizing User Impact
----------------------

One of the most elegant aspects of this proxy-based testing approach is its natural resilience to problems. If the user experiences any issues with the new version, their natural response—refreshing the browser—actually acts as an automatic fallback mechanism. Here's how it works:

1.  When a user presses refresh in their browser, it initiates a new DNS resolution

2.  The proxy, either knowing of previous problems or just through its request counting mechanism, can route this new request to the stable, old version.

3.  The user is transparently redirected to the working version, in many cases without even realizing there was a problem.

The benefit to this behavior is that it provides a natural user-friendly circuit-breaker, enabling minimal service disruption. But users do not have to clean their cache or contact support. Waiting for a fix is also eliminated; their intuitive action of reloading the page sets them back on operation easily.

This fallback works even better in direct DNS resolution mode, where users are routed directly to the stable version without any proxy in the middle. All protective properties are retained, yet the system runs with minimal infrastructure overhead.

Testing web services in production doesn't have to be risky. With the right tools and approaches, you can evolve your services confidently while maintaining reliability. This smart testing proxy provides the safety net needed to innovate without compromising stability.

Would you consider using such a proxy in your infrastructure? What features would you find most valuable?