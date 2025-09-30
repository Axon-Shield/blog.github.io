---
title: "DNS Resiliency and First Step to Transform Your Cyber Defense"
date: 2024-11-23T05:00:00-04:00
categories:
- dns
- cybersecurity
- resilience
- transformation
tags:
- dns-resilience
- cyber-defense
- infrastructure
- security-transformation
---
![Dns Defense Transformation](/assets/images/posts/dns-resilience/dns-defense-transformation.jpg)
*Dns Defense Transformation - first we fortified their DNS*

After facing multiple DNS attacks that disrupted its operations, the customer recognized that the situation was no longer tenable. Once we became involved, we fortified their DNS infrastructure against future attacks in a couple of weeks. We could also start transforming their cyber defense with new data.

The Problem
-----------

The customer had a moderate internet presence of 100 registered domains. Our first finding indicated that 30 of them were active. This was as a result of a passive analysis that checked the validity of name servers, the contents of SOA records and whether random DNS queries returned results.

We found that there were 2 DNS servers or simple Linux servers behind a firewall that could not block DDoS DNS attacks. At this point, we didn’t look for a single culprit. We realized that the company had a fairly long history and that there was no single party fault. It is a situation that has been compounded by the sudden increase in attacks over the last 10 years which have made the DNS infrastructure susceptible to fairly cheap targeted attacks.

We frequently observe small, frequent, and brief attacks that last between one to two minutes and are carried out from one domain to another. The principal goal seems to be the assessment of the DNS's reliability together with other specific website or web service attacks.

In military terms, it is like deploying reconnaissance teams ahead to gather information about the terrain. Increasingly, internet attacks are like guerrilla warfare. It is feasible to believe that those who can be hired to attack various targets on the web wish to know as much as possible about the current weaknesses and problems in the digital world.

DDoS Resiliency
---------------

There are three main options for your resiliency for DoS (denial of service) attacks against your DNS system:

1.  On-net scrubbing (i.e., always on): You can create your own scrubbing system within your infrastructure or you can purchase it from a cloud provider. We tend to steer clear of the on-premises solution because very few have sufficient network bandwidth.
    
2.  Off-net scrubbing (usually off): You need to build a scrubbing service just like in option 1; the main differences are:
    
    1.  Zero false positives in "normal"state but higher false positives when scrubbing is enabled..
        
    2.  Your infrastructure needs to hold up alone during attacks which typically last between 5 to 15 minutes since scrubbing systems need time to activate.
        
3.  Implement a DNS system that is scalable with the traffic without any limit; it will manage whatever volume of traffic is directed at it. I.e., the system is so powerful that "scrubbing" is not required.
    

What many people forget when considering on-premises options is that it’s not only about your DNS system, but also about all the routers and firewalls that are between your DNS and the internet. Additionally, it is also important to consider the capacity of your internal network. It is expensive to have enough bandwidth connecting your on-premises services to withstand even moderate DoS attacks.

If you are the target of a 1 Tbps DDoS attack, the chances are that your network cables will become saturated; genuine traffic is affected by the fact that it simply cannot get through physically. Routers and firewalls can only handle a certain number of UDP requests, and they can manage significantly fewer TCP connections and even fewer SSL connections.

If you need a robust and dependable DNS system, we always recommend using one of the cloud providers. You can obtain this kind of service as part of a bundle of services from public clouds (AWS, GCP, Azure, etc.), CDN/WAF services (e.g., Cloudflare, Akamai, etc.), or you can choose a DNS specialist.

Let’s focus on this option.

How To Revamp Your DNS for The Future
-------------------------------------

Once you are clear about your DNS options—and if you’re in a hurry, just go with a public cloud option. It’s quick, pricing is fairly transparent, and you probably already use one or more public clouds anyway. This means that you don’t have to go through the procurement hoops and can jump directly to the technical implementation.

![ ](/assets/images/posts/dns-resilience/columns.jpg)


What we almost always hear is that there is no desire to change the way DNS is managed. This is okay, as DNS can be easily split into two parts: 1. where/how the DNS content is managed, and 2. where DNS requests are served. It’s three levels of how to deal with DDoS attacks.

Set up the new DNS system of your choice as a secondary DNS system. This means that you will still control the DNS contents from your current DNS, but you will add a new DNS system to assist in serving DNS requests. In other words, if your old DNS comes under attack, clients will query the new DNS, which limits the impact of DoS attacks.

Diversify your secondary DNS. In fact, customers are not fully confident that DNS providers can offer 100% uptime and do not wish to be tied to a single third-party service. This can be achieved by setting up an additional secondary DNS system. Split your primary DNS. The first two steps enhance the resilience by providing systems where your clients and customers can direct their DNS queries, however the third step actually stops DoS attacks that aim to knock off or hijack your DNS system by stopping all external DNS queries.

### Set Up Secondary DNS

These days, this can be done very quickly and really depends on how much you can push your:

1.  Network team to alter firewall and traffic routing rules.
    
2.  DNS registration team to update “DNS glue,” i.e., nameservers at your DNS registrar.
    

  
We often come across network teams that try to follow a “pattern” that may require more work than strictly necessary. What we mean is that there are two aspects of communication between primary and secondary DNS:

1.  Secondary DNS checks and downloads changes in your primary DNS.
    
2.  Primary DNS can send notifications when changes occur.
    

  
The second step can prove complicated if your network has strong protections, such as a DMZ zone and segmentation. However, it is not strictly necessary to have this in place. The difference in not having it in place is relatively small from an operational point of view. Instead of the secondary DNS updating its copy “upon change,” it may take a couple of minutes to discover the change itself using a standard DNS request.

Another aspect of setting up secondary DNS is the security of “zone transfers,” that is, how to ensure that only the authorized DNS systems can retrieve your entire DNS data with a single request. There are two mechanisms available:

1.  Limit access to your primary DNS by whitelisting only the relevant IP addresses.
    
2.  Set up a shared signing key.
    

  
Interestingly, even some well-known brands of DNS and firewalls cannot perform both functions simultaneously.

In general, our recommendation is to prioritize simplicity. Using IP address whitelisting is effective, and its advantage is that you can block a DoS attack using zone transfer requests.

Once you have completed the secondary DNS setup and verified that changes are reflected and the contents of the secondary DNS are correct, you can add NS records to your DNS data. An NS record is a pointer to a name server, which directs DNS requests related to your company.

At this stage, you will begin sharing the DNS traffic load between your primary DNS and the secondary DNS. You may start to see traffic data in the secondary DNS. In some cases, this is the first time customers get a real sense of which parts of their DNS are utilized, as reporting in cloud-based DNS systems is presented in easy-to-understand and easy-to-access formats.

The next step, which should be completed as soon as the secondary DNS is confirmed as operational, is to update the nameserver records at the registrar (DNS glue).

### Isolating your Primary DNS

Once you are satisfied with the performance of the new secondary DNS system, you can start considering the isolation of your primary DNS. This can be accomplished in two steps:

1.  Remove name servers and DNS glue from your primary DNS.
    
2.  Disable DNS traffic to your primary DNS on your firewalls.
    

  
This is a significant step for customers. Until now, the secondary DNS has served to assist during attacks, while they could still rely on their own primary DNS. By shutting down traffic to the primary DNS, they lose the feeling of “having and controlling a box I can touch in my data center.”

Some may proceed through this gate without hesitation, while others may require more reassurance and might opt for an additional secondary DNS to ensure there is no dependency on a single third party.

You should execute the two steps with some gap so that your infrastructure teams can measure the effects of each step. Whether it is the DNS latency performance from the client’s perspective or the volumetric change on your primary DNS systems as you remove NS records.

Clean Up
--------

You achieved your primary objective. Your DNS is resilient; if there’s a DDoS attack, you either can’t see it at all or you simply observe how it unfolds, as there is no impact on your customers or on your IT infrastructure at all.

One of the benefits is that you now have much better visibility of your DNS data and the traffic associated with it. Let’s put this visibility to work. If your company has been in business for more than a couple of years, then it is likely that your DNS contains many records that are no longer needed or in use.

There may be entire registered zones that you “keep on your books,” but they are neither in use nor is there any traffic on them. In the example we started this article with, we identified 30 zones in use. Once we gained visibility into the traffic data, we realized that there are only 5 DNS zones with actual traffic data. This means you can remove a lot of content from your DNS, which simplifies operations, affects the cost of any infrastructure changes, and removes threats based on unmaintained DNS records. One of the significant effects of being able to operate with this primary data is that you reduce your dependency on ASM products, you can see the problem directly, rather than depending on network scanning by ASM tools. The second significant effect is that you can directly feed your DNS data to your ASM product and enable it to cover 100% of your attack surface.
