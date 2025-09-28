# Blog Post Date Correction Checklist

## Posts Needing Date Corrections (21 posts)

### Instructions:
1. Visit each AxonShield URL
2. Right-click → Inspect Element → Find `<span class="blog-list-item-date">`
3. Extract the date
4. Convert to YYYY-MM-DD format
5. Update the Jekyll post's front matter

### Posts to Fix:

#### DNS & Network Posts
- [ ] **dns-at-the-edge-performance-security-and-strategic-advantage**
  - URL: https://axonshield.com/dns-at-the-edge-performance-security-and-strategic-advantage
  - Current: 2025-09-28 → Actual: ___________

- [ ] **dns-resiliency-and-first-step-to-transform-your-cyber-defense**
  - URL: https://axonshield.com/dns-resiliency-and-first-step-to-transform-your-cyber-defense
  - Current: 2025-09-28 → Actual: ___________

- [ ] **deep-dive-into-dns-the-internets-super-smart-address-book**
  - URL: https://axonshield.com/deep-dive-into-dns-the-internets-super-smart-address-book
  - Current: 2025-09-28 → Actual: ___________

- [ ] **take-control-of-your-network-why-dns-is-key-to-understanding-your-internet**
  - URL: https://axonshield.com/take-control-of-your-network-why-dns-is-key-to-understanding-your-internet
  - Current: 2025-09-28 → Actual: ___________

- [ ] **data-driven-strategy-dns-security-analysis**
  - URL: https://axonshield.com/data-driven-strategy-dns-security-analysis
  - Current: 2025-09-28 → Actual: ___________

- [ ] **from-hoststxt-to-modern-internet-infrastructure**
  - URL: https://axonshield.com/from-hoststxt-to-modern-internet-infrastructure
  - Current: 2025-09-28 → Actual: ___________

#### Security Strategy Posts
- [ ] **cyber-defense-strategy-aligning-security-with-business-objectives**
  - URL: https://axonshield.com/cyber-defense-strategy-aligning-security-with-business-objectives
  - Current: 2025-09-28 → Actual: ___________

- [ ] **building-cyber-service**
  - URL: https://axonshield.com/building-cyber-service
  - Current: 2025-09-28 → Actual: ___________

- [ ] **reclaim-control-over-your-cyber-defense-empowerment-over-fear**
  - URL: https://axonshield.com/reclaim-control-over-your-cyber-defense-empowerment-over-fear
  - Current: 2025-09-28 → Actual: ___________

- [ ] **we-forget-that-cyber-defense-is-hard-apologies**
  - URL: https://axonshield.com/we-forget-that-cyber-defense-is-hard-apologies
  - Current: 2025-09-28 → Actual: ___________

- [ ] **prevent-v-detect-it-is-all-about-effort-i-mean-ai**
  - URL: https://axonshield.com/prevent-v-detect-it-is-all-about-effort-i-mean-ai
  - Current: 2025-09-28 → Actual: ___________

#### Certificate Management Posts
- [ ] **how-we-designed-automated-certificate-lifecycle-management-20-years-of-iteration**
  - URL: https://axonshield.com/how-we-designed-automated-certificate-lifecycle-management-20-years-of-iteration
  - Current: 2025-09-28 → Actual: ___________

- [ ] **the-business-case-for-modern-certificate-lifecycle-management**
  - URL: https://axonshield.com/the-business-case-for-modern-certificate-lifecycle-management
  - Current: 2025-09-28 → Actual: ___________

#### WAF & Application Security Posts
- [ ] **the-science-of-digital-fingerprinting-for-waf-integration**
  - URL: https://axonshield.com/the-science-of-digital-fingerprinting-for-waf-integration
  - Current: 2025-09-28 → Actual: ___________

- [ ] **waf-for-microservices-and-serverless-mastering-accuracy-in-modern-architectures**
  - URL: https://axonshield.com/waf-for-microservices-and-serverless-mastering-accuracy-in-modern-architectures
  - Current: 2025-09-28 → Actual: ___________

- [ ] **cost-benefit-analysis-and-tco-of-waf-deployment-models**
  - URL: https://axonshield.com/cost-benefit-analysis-and-tco-of-waf-deployment-models
  - Current: 2025-09-28 → Actual: ___________

#### Company & Operations Posts
- [ ] **the-convergence-of-cyber-security-origins-of-axon-shield**
  - URL: https://axonshield.com/the-convergence-of-cyber-security-origins-of-axon-shield-from-technical-experts-to-efficient-delivery-of-cyber-security
  - Current: 2025-09-28 → Actual: ___________

- [ ] **bridging-the-cyber-talent-gap-with-axon-shield-support**
  - URL: https://axonshield.com/bridging-the-cyber-talent-gap-with-axon-shield-support
  - Current: 2025-09-28 → Actual: ___________

- [ ] **from-walled-garden-to-axon-fusion-zone**
  - URL: https://axonshield.com/from-walled-garden-to-axon-fusion-zone
  - Current: 2025-09-28 → Actual: ___________

- [ ] **migrating-from-hashicorp-vault**
  - URL: https://axonshield.com/migrating-from-hashicorp-vault
  - Current: 2025-09-28 → Actual: ___________

- [ ] **beyond-the-dashboard-why-your-soc-needs-a-human-centered-command-center**
  - URL: https://axonshield.com/beyond-the-dashboard-why-your-soc-needs-a-human-centered-command-center
  - Current: 2025-09-28 → Actual: ___________

## Posts to Double-Check (these may also be wrong)

- [ ] **email-security-explained-how-your-digital-mail-stays-safe**
  - URL: https://axonshield.com/email-security-explained-how-your-digital-mail-stays-safe
  - Current: 2025-05-18 → Should be: 2025-05-03? (needs verification)

- [ ] **akamai-web-application-firewall-how-it-works**
- [ ] **how-to-get-started-with-akamais-web-application-firewall**
- [ ] **waf-as-code-the-future-of-web-security-automation**
- [ ] **akamai-and-security-operations**
- [ ] **scale-up-and-time-your-dns-management-with-whisper-watch**
- [ ] **axon-shield-proxy-live-testing-for-safer-devops**

## How to Update Jekyll Posts

1. Open the `.md` file in `_posts/`
2. Find the front matter at the top:
```yaml
---
layout: post
title: "Post Title"
date: 2025-09-28  ← Change this line
---
```
3. Update the date field with correct date
4. Save the file
