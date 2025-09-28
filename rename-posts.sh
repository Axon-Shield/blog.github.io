#!/bin/bash

# Script to rename blog posts with logical publication dates
# Based on content type and existing date patterns

echo "🔄 Renaming blog posts with logical publication dates..."
echo "=================================================="

# Function to update both filename and front matter date
update_post() {
    local old_name="$1"
    local new_date="$2"
    local reason="$3"
    
    echo "📝 $old_name"
    echo "   → $new_date ($reason)"
    
    ./update-date.sh "$old_name" "$new_date"
    echo ""
}

# 2024 Posts - Foundational and Infrastructure Content
echo "🏗️  FOUNDATIONAL CONTENT (2024)"
echo "--------------------------------"

update_post "from-hoststxt-to-modern-internet-infrastructure" "2024-03-15" "Historical perspective - early in year"
update_post "deep-dive-into-dns-the-internets-super-smart-address-book" "2024-04-10" "DNS fundamentals"
update_post "data-driven-strategy-dns-security-analysis" "2024-05-20" "DNS security analysis"
update_post "cyber-defense-strategy-aligning-security-with-business-objectives" "2024-06-12" "Strategic foundation"
update_post "building-cyber-service" "2024-07-08" "Service building concepts"
update_post "from-walled-garden-to-axon-fusion-zone" "2024-08-14" "Architecture evolution"
update_post "dns-resiliency-and-first-step-to-transform-your-cyber-defense" "2024-09-18" "DNS resilience"
update_post "the-convergence-of-cyber-security-origins-of-axon-shield" "2024-10-22" "Company origin story"

# Late 2024 - Advanced Topics
echo "🚀 ADVANCED TOPICS (Late 2024)"
echo "-------------------------------"

update_post "bridging-the-cyber-talent-gap-with-axon-shield-support" "2024-11-25" "After DNS network control"
update_post "how-we-designed-automated-certificate-lifecycle-management-20-years-of-iteration" "2024-12-05" "Before Vault migration"

# 2025 Posts - Modern and Cutting-Edge Content  
echo "⚡ MODERN CONTENT (2025)"
echo "------------------------"

update_post "the-business-case-for-modern-certificate-lifecycle-management" "2025-01-30" "After Proxy launch"
update_post "take-control-of-your-network-why-dns-is-key-to-understanding-your-internet" "2025-02-15" "Network control concepts"
update_post "dns-at-the-edge-performance-security-and-strategic-advantage" "2025-03-10" "Advanced DNS"
update_post "beyond-the-dashboard-why-your-soc-needs-a-human-centered-command-center" "2025-03-25" "SOC operations"
update_post "reclaim-control-over-your-cyber-defense-empowerment-over-fear" "2025-04-05" "Before Akamai operations"

# Mid 2025 - Specialized WAF Content
echo "🛡️  WAF SPECIALIZATION (Mid 2025)"
echo "-----------------------------------"

update_post "the-science-of-digital-fingerprinting-for-waf-integration" "2025-05-28" "After WAF-as-Code"
update_post "waf-for-microservices-and-serverless-mastering-accuracy-in-modern-architectures" "2025-06-12" "Advanced WAF"
update_post "cost-benefit-analysis-and-tco-of-waf-deployment-models" "2025-07-08" "WAF business case"

# Recent 2025 - Latest Thinking
echo "🧠 LATEST THINKING (Recent 2025)"
echo "---------------------------------"

update_post "prevent-v-detect-it-is-all-about-effort-i-mean-ai" "2025-08-20" "AI/ML perspectives"
update_post "we-forget-that-cyber-defense-is-hard-apologies" "2025-09-10" "Industry reflection"

echo "✅ All posts renamed with logical publication dates!"
echo "📊 Timeline spans: March 2024 → September 2025"
