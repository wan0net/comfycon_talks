---
title: Scanning millions of domains and compromising the email supply chain of Australia's most respected institutions
meta_title: ""
description: ComfyCon AU 2022 Winter
date: 2022-09-04 00:00:00
categories: ["ComfyCon AU 2022 Winter"]
speakers: Sebastian Salla 

draft: false
---
Abstract: Curious to find out what happens when you perform OSINT at-scale? In this talk we'll discuss how the migration of email infrastructure from private to public cloud environments has significantly elevated the risks associated to IP takeover attacks. We'll then discuss how a seemingly innocuous scan of 1.8 Million Australian domains resulted in the email supply chain of 264 Australian organisations being compromised.
Detailed Presentation Outline:

Introduction Discuss what phishing is, how it has evolved and how an overlooked technique can be exploited to tip the table in favor of attackers. We'll talk about how email sender authentication is performed, how public cloud environments are ephemeral in nature and how trusted but unused IP addresses can be taken by threat actors with malicious intent.
Scanning millions of domains Discuss the methods used to collate a target list that includes millions of domains. Then deep dive into what's involved in extracting the full IP supply chain of an SPF record and the infrastructure necessary to scan millions of targets.
Trawling available AWS IPs Deep dive into IP takeover attacks on AWS' platform. Discuss what's involved in cycling through tens of thousands of IP addresses and how a persistent threat actor could continuously cycle through every available IP across all AWS regions – which encompasses tens of millions of IPs.
Sifting through the results Discuss the process for cross referencing scanned AWS IPs against a repository of known SPF IPs and how a limited scan I performed (i.e. focusing on Australian domains, only scanning AWS IPs and only scanning 0.1% of the AWS EC2 IP Address space) resulted in compromised email supply chains for some of Australia's most respected institutions (i.e. Australian Parliament House, University of Sydney, and 262 more organisations).
What's the impact? Discuss how each of the affected organisations and their downstream customers are significantly more susceptible to business email compromise and phishing-related attacks. Anyone with a credit card can sign-up for an AWS account, cycle through EC2 instances until they get a desirable IP, request AWS to remove any SMTP restrictions and begin sending SPF authenticated emails as though they are any of these organisations.
Wrapping up The outcome of this talk is to showcase how discovery and exploitation of this vulnerability can be automated and can yield high impact results – emphasizing that I've only scanned organisations in Australia, only covered 0.1% of potential AWS IP addresses and haven't looked at any other major cloud computing provider (e.g. Azure & Google Cloud), meaning there are likely thousands more vulnerable to this attack.

<iframe width="560" height="315" src="None" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>