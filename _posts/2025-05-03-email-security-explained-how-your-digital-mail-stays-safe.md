---
title: "Email Security Explained: How Your Digital Mail Stays Safe"
date: 2025-05-03T05:00:00-04:00
categories:
- cybersecurity
- email-security
- protocols
tags:
- email
- security
- spf
- dkim
- dmarc
- tls
- dane
---
![Email Security with DNS](/assets/images/posts/email-security/email-security.jpg)
*Ever get curious about how an electronic mail passes through the internet*

Do you ever get curious about how an electronic mail passes through the internet? Be with me in discovering how the security of these tools keeps your digital messages unharmed!

### Fun Facts About Email Security!

*   **Billions Protected**: Email security systems have an incredible job to do - processing and protecting over 300 billion emails sent daily across the world!
    
*   **Ninja Protectors**: Just like real ninja, the security systems work silently in the background all day and night - you won't hear it, but they are keeping you safe from the bad guys 24/7!
    
*   **Speed Champions:** The security scans are extremely fast (ten to twenty milliseconds, which is faster than the blink of an eye!), so, your emails will reach your destination with little time lost.
    
*   **History Fact**: In the 1990s, the first email security systems were invented when people were already aware that one can easily change the email source. Before that, emails were mostly not protected at all while being sent!
    
*   **Secret Languages**: Email security is based on a science called "cryptography" - the same method to develop secret codes that were applied to send across secret messages during wars!
    

### Imagine Your Email is a Letter...

Imagine that an email is like a letter that one sends through the postal system. However, in contrast to regular mail, emails are much easier to be captured, viewed, or altered by ill-intentioned people who did not duly protect them. Here is where the heroes of the email security save the day!

### DMARC, SPF, and DKIM: The Email ID Checkers

### SPF (Sender Policy Framework)

Consider that your settlement marks the carriers who are allowed to deliver from the toy store and has a list of approved couriers on this special list. This is how SPF operates!

SPF serves as a reference list for the mail carrier to identify the domain (such as [gmail.com](https://gmail.com)). It is like saying, "Only the specified servers are allowed to send messages labeled from our domain." An email that purports to be from [google.com](https://google.com) will be a problem if not sent from the Google-approved server and suspiciously observed.

**Simple explanation:** SPF verifies if the email was sent by an authorized computer.

### DKIM (DomainKeys Identified Mail)

One can liken DKIM to a wax seal on a vintage letter.

When your school sends a permission slip, they may put the official school seal on it so your parents can know that it is genuine. In the same way, DKIM provides a digital signature to each email. This signature guarantees the email was not only sent by the owner but also the message was not altered in any way on its journey to you.

**Simple explanation:** DKIM affixes a special digital seal that certifies the sender and verifies the content was intact.

### DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC is the person who acts on behalf of the rules in the school.

DMARC is an extension of what is done by SPF and DKIM through the issuer's instruction to report to the email provider for failed email. Query from another person: "Can I post this block in first position?" Yes, you can move it. To what place though? No concern at all, you can move it to any position that fits. Besides, DMARC will gather information from the owner of the email domain about the emails that didn't pass through those checks

**Simply put:** DMARC authorizes what to do with dangerous emails and notifies the site admins of possible issues.

### StartTLS/TLS: The Secret Tunnel

TLS (Transport Layer Security) and StartTLS, its lower version, remind me of an email in your pocket.

When you send a note in class, you most likely send it underhand to avoid its exposure to others as it passes by multiple hands automatically. We can consider that if you could send the note to your friend through an invisible tube that links only the sender and the receiver, that would be the case with TLS. Basically, TLS is that magical tube.

Thus, not only does TLS build an insecure connection, but it also encrypts it. That is just what TLS and StartTLS do for email servers when the secure tunnel process has just been initiated. The unsafety of such a connection is the same as its being unencrypted. Email servers already have the technology to begin this process. This is what StartTLS is all about.

**Simple definition:** TLS represents a secure pathway to transmit your email in such a manner that nobody can look at your messages as the data is in transit.

### DANE (DNS-based Authentication of Named Entities): The Map Verifier

DANE works the same way as a reliable guide that leads you to the genuine email castle and away from fake ones.

Some of the unscrupulous guys can establish fake castles, pretending them to be the real ones. DANE makes use of the Domain Name System (DNS) - consider it as the internet's most reliable address book - to confirm that the secure connection for your email is from the rightful, legitimate, and actual server itself.

Going into more detail let me be clear how it operates:

*   **The Problem DANE Solves**: If DANE were not there someone could still be able to fool your computer despite the fact that your message will be secured by TLS (the tunnel between you two in our example). This is like a "man-in-the-middle" attack and the person doing it would be someone who would come to you as your friend and at the same time would read all your messages.
    
*   **Certificate Fingerprints**: DANE makes use of special data (called TLSA records) in the DNS resource. These are like the fingerprints of security certificates used by the servers. It's quite similar to the way your fingerprint is one and the only to you!
    
*   **Double-Checking**: Is the process of your email program talking to the server, and then DANE checking DNS for the fingerprint to match the certificate on the server. If they coincide, it is for real; if not, then something weird is really going on there!
    
*   **Extra Layer of Trust**: The normal TLS among other things relies on some people called Certificate Authorities to check on the identity of servers. DANE gives further protection and it doesn't depend on those people only - this is like having both your password and a fingerprint scanner.
    

**Simple explanation:** DANE certifies that your email connects to the real server and not a forger by preserving the server's unique "fingerprint" in the global address directory of the Internet.

### Bad Guys and Their Tricks: What Each Security Tool Protects Against

Just like different superheroes have different powers to fight various villains, each email security tool protects against specific types of bad guys and their sneaky tricks:

### What SPF Protects Against: Email Impersonators

**The Attack**: Email spoofing - when someone pretends an email is from your school, bank, or a friend by faking the "From" address.

**The Attackers**: Phishers who want to trick you into sharing passwords or personal information by pretending to be someone you trust.

**Real-World Example**: Someone sends emails that look like they're from "[amazon.com](http://amazon.com)" asking for your password, but they're actually sent from a hacker's computer.

### What DKIM Protects Against: Message Tamperers

**The Attack**: Message tampering - when someone intercepts your email and changes its contents before it reaches the destination. **The Attackers**: Hackers who want to change the content of messages, like changing "Don't send money" to "Please send money." **Real-World Example**: A hacker intercepts an email about where to meet for a birthday party and changes the location to somewhere else.

### What DMARC Protects Against: Sneaky Imposters

**The Attack**: Combined spoofing and deception techniques that try to bypass SPF and DKIM.

**The Attackers**: Sophisticated scammers who use advanced techniques to fake messages from trusted organizations.

**Real-World Example**: Scammers who figured out how to get around some security measures and send fake messages looking like they're from your bank, but DMARC catches them and tells your email provider to put these messages in the spam folder.

### What TLS/StartTLS Protects Against: Eavesdroppers

**The Attack**: Eavesdropping - when someone secretly listens to your email communications to steal information.

**The Attackers**: Snoopers on public Wi-Fi networks or hackers who can intercept internet traffic.

**Real-World Example**: Someone at a coffee shop using the same Wi-Fi tries to read emails being sent by customers, but TLS encryption makes the messages unreadable.

### What DANE Protects Against: Fake Destinations

**The Attack**: Man-in-the-middle attacks - when someone sets up a fake server between you and the real destination. **The Attackers**: Advanced hackers who can redirect internet traffic or compromise certificate authorities. **Real-World Example**: A hacker tricks your computer into connecting to their fake Gmail server instead of the real one. Your computer thinks it's secure because it has a certificate, but DANE would detect that it's not the real Gmail server.

![Email and DNS](/assets/images/posts/email-security/email_and_dns.png)


### Cool Email Security Trivia!

*   **Email Detective Work**: Some of the firms make use of email security techniques with regular computer software to read billions of emails and discover the trends that indicate new kinds of attacks. The software makes it faster, acting like digital detectives.
    
*   **Emoji Security**: Not to mention the fact that even the emoticons and special characters in our emails are being guarded by these machines! The intruders could replace 😊 with 😡 to change your message if the security were not there!
    
*   **Digital Disguises**: Email security systems are cognitive and can determine when someone is trying to duplicate your friends' writings on an advanced level. They use the writing style and common phrases to recognize the fraudsters.
    
*   **Self-Healing Systems**: Attacks on modern email security can actually turn out to be beneficial, as the system learns from them to become more robust - just like our organism gets stronger after the disease by the help of antibodies!
    

### How They All Work Together

These are a few of the tools that bond together to shield your email:

*   The SPF & DKIM combination serves as a check for the real sender of the email
    
*   DMARC in its turn warns about not secured mails that are looking suspicious
    
*   The message is wrapped in a tunnel and only the address and email can go through (TLS)
    
*   Furthermore, the path map is checked by DANE and therefore you are ensured that you drive to the correct location
    

It's kinda like having a letter with:

*   A well-known and trusted return address (SPF)
    
*   An official digital signature (DKIM)
    
*   Practical guidelines for handling suspect mail (DMARC)
    
*   The email is like a private and secure delivery truck (TLS)
    
*   A dependable and checked map to the right place (DANE)
    

### Why Should You Care?

Email security might sound boring, but it's super important! Without these tools, bad people could:

*   Pretend to be your school or friends
    
*   Read private messages
    
*   Send fake emails that look real
    
*   Steal passwords and personal information
    

Next time you send an email, remember all these invisible helpers working to keep your messages safe and private!