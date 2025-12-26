---
title: "The $15M Problem Hiding in Your Certificate Management System"
date: 2025-11-02T05:00:00-04:00
categories:
  - Certificate Management
  - Infrastructure Intelligence
  - Enterprise Strategy
  - Case Studies
tags:
  - PKI
  - Automation
  - DNS Management
  - ServiceNow
  - Cloud Migration
  - Financial Services
  - Telecommunications
  - Security
  - Operational Excellence
summary: "Three organizations, three completely different approaches to PKI, one universal truth. When starting, no one really understood the infrastructure and which critical systems use certificates and which do not. Over several years, enterprise certificate management was rebuilt for three major organizations: global telecom provider managing 15,000 certificates, international financial institution with 8,000 certificates across regulated environments, and healthcare organization with 3,500 certificates serving millions of patients. Each faced similar challenges despite different industries: explosive certificate growth, invisible infrastructure dependencies, hidden costs, compliance challenges, and scalability limits. The transformation followed similar patterns: discovery phase revealing actual certificate inventory, process documentation exposing inefficiencies, stakeholder engagement understanding team workflows, phased automation, and continuous improvement. Common lessons across implementations include underestimated complexity, distributed ownership, hidden dependencies, cultural resistance, and need for executive sponsorship. Measurable outcomes proved transformative: 85-95% reduction in routine management effort, zero unplanned certificate-related outages, audit-ready compliance in minutes, infrastructure visibility enabling other initiatives, and freed engineering capacity. The universal truth: whether managing 3,500 or 15,000 certificates, manual approaches break at scale. Organizations face a choice—automate proactively when they have time to do it right, or automate reactively after major incident forces their hand. Proactive automation costs less, provides competitive advantage, and avoids revenue impact and reputation damage. The $15M problem exists in organizations managing more than 500 certificates—hidden across distributed teams, invisible to traditional accounting, growing with infrastructure scale. The question isn't whether organizations can afford automation; it's whether they can afford to continue without it."
---

![The $15M Problem in Certificate Management](/assets/images/posts/15m-problem-certificate/new-intelligence.png)
*Three organizations, three different failures, one universal truth: automation reveals what manual processes hide.*

Three organizations, three completely different approaches to PKI, one universal truth. When I started, no one really understood the infrastructure and which critical systems use certificates and which do not.

Over the past several years, I've rebuilt enterprise certificate management for three major organizations. Combined, these companies were not even understanding the scale of the problem and what outage may hit them in a day, week, or month. The same was true about understanding the real cost of certificate management or projects expanding some difficult use-cases.

The fascinating part? Each organization failed in a completely different way.

## The Financial Institution: When "Weeks" Becomes Your Unit of Measurement

A major UK financial company (let's call them Nexus) had a problem that every developer understood but no executive could see: getting a digital certificate took weeks.

Not hours. Not days. Weeks.

Think about what this means. A developer needs to deploy a new microservice. A service owner integrates a third party service to provide a new customer service. A manager requires  They submit a certificate request through the proper channels. Then they wait. The security team reviews. IT ops gets involved. Approvals are required. Eventually—maybe two weeks later—they get their certificate.

So what did smart developers do? They hoarded certificates. They reused them across services. They found workarounds. They built insecure architectures because the secure path was operationally impossible.

The hidden cost: Every delayed certificate was a delayed feature, a delayed migration, a delayed revenue opportunity. Multiply that across hundreds of development teams, and you're looking at millions in lost productivity that finance couldn't see because it manifested as "slow delivery."

### What We Built

We didn't optimize the old process. We eliminated it.

New architecture:

- Offline root CA for maximum security
- Cloud-based self-service platform
- Automated issuance in seconds, not weeks
- Full integration with existing systems

The results in 6 months:

- Certificate issuance went from weeks to instant
- Tripled capacity at the same cost (economies of scale kicked in)
- Cloud migration accelerated—no longer bottlenecked
- Teams started using certificates properly because friction disappeared

**The lesson:** When security is painful, people avoid it. When security is automatic, it becomes the default.

## The Telecom Provider: The ServiceNow Death March

A major telecommunications provider had a different problem. They'd tried to solve certificate management by routing everything through ServiceNow.

On paper, this looked organized: Submit ticket → Approval workflow → Certificate issued → Close ticket.

In reality, no-one knew how to request a certificate as there were different types of service requests. Most of those were not monitored. Teams would submit requests. Tickets would sit in queues.

The result - application teams would use their creativity and provision certificates internally or from whatever source was quickest.

The automation paradox: They'd automated the ticketing but not the actual certificate lifecycle. This created an illusion of control while making the real problem worse.

### What We Built

Serverless, event-driven certificate renewal integrated directly with ServiceNow—but not as a ticketing system. As an inventory system.

Key architecture:

- Secure root CA infrastructure with HSM backing
- Client-specific encryption keys for multi-tenant security
- Automated renewal with risk-aware policies
- ServiceNow as the CMDB, not the workflow engine

The results in 7 months:

- Unified management of internal and public certificates
- Human error minimized—renewals became automatic
- Full compliance visibility for auditors
- ServiceNow became the source of truth, not the bottleneck

**The lesson:** Integration isn't about routing work through tools. It's about connecting tools to eliminate work.

## The Internet Enterprise: The DNS Shadow Infrastructure

The third case was different. An enterprise technology company thought they had their infrastructure documented. They didn't.

Their datacenter DNS and cloud DNS were managed separately. No unified view. No central inventory. When we started what was supposed to be a "simple DNS review," we discovered a shadow infrastructure that executives didn't know existed.

Hundreds of domain zones. Thousands of records. Nobody knew who owned what or whether it was still needed.

The security implication: Stale DNS records are attack vectors. Misconfigured zones are data exfiltration risks. But you can't fix what you can't see.

### What We Built

We turned a one-time audit into an automated intelligence platform.

Architecture:

- Unified data collection across all DNS systems
- Real-time monitoring and change notifications
- Executive dashboards showing exposure and risk
- Registrar-agnostic—worked across their entire portfolio

The results in 8 months:

- 100% visibility across datacenter and cloud
- Automated detection of misconfigurations and stale records
- Real-time alerts on DNS changes
- Executive leadership could finally make informed decisions

**The lesson:** Infrastructure intelligence is a continuous process, not a point-in-time audit.

## The Pattern: Automation Reveals What Manual Processes Hide

My experience with rebuilding infrastructure intelligence at these three major organizations (and many others) has taught me the following lessons:

**Your infrastructure knows more than your documentation.** The actual system operations become visible through certificates and DNS records and service dependencies which show the actual system behavior instead of what "managers believe".

**Friction creates security debt.** Teams will create alternative solutions bypassing all security controls - to get things done. Security operates as the standard practice when automated systems are in place.

**Integration complexity is the real challenge.** The technology platform choice becomes less important than the quality of its integration with your current CMDB and ticketing and monitoring and change management systems.

**Cost lives in recovered capacity.** The three organizations operated without dedicated funding for certificate management. The hidden expenses became visible through delayed project delivery and system failures and engineers spent 15-20% of their time on operational tasks instead of working on new developments.

**Scale changes everything.** Manual processes function properly when the system contains fewer than, let's say, 100 certificates. The system fails to operate properly when it handles more than 1,000 certificates. Organizations with 10,000 certificates must implement automation because it represents their survival requirement.

## What This Means for You

If you're a CTO, CISO, or infrastructure leader at a scaling organization, ask yourself:

- How long does it take to get a certificate - from the moment it's required till the moment of implementation?
- Do you know how many certificates you have and who owns them?
- Do you know where they all are and which applications depend on each?
- What happens when one expires, who needs to be involved for its replacement?
- What percentage of your engineers' time is spent on operational toil vs. innovation? Don't count just "time spent on the job" but also context switching and time lost by re-focusing.

If you don't like the answers, you're not alone. Every organization I've worked with thought they had this figured out—until we looked closely.

The difference between the organizations that transformed and the ones still struggling? They stopped trying to optimize broken processes and started building intelligence platforms.

Certificate automation isn't a cost-cutting project. DNS automation isn't a compliance checkbox. These are opportunities to understand how your infrastructure actually works—and use that intelligence to accelerate everything else.
