---
title: DMARC for beginners (or, deflecting bounty begging)
meta_title: ""
description: ComfyCon AU 2022 Winter
date: 2022-09-04 00:00:00
categories: ["ComfyCon AU 2022 Winter"]
speakers: Andrew McDonnell

draft: false
---
Email still runs on SMTP, which must be close to one of the oldest application protocols still in common use. Security was not a high priority design factor. Which can make it easy to spoof. Fortunately this can be mitigated with a few tweaks of your email provider settings (some even set it already for you; others just have wizards that suggest you fix it!) However, effectively configuring these features, known as SPF, DKIM, and DMARC, can often be overlooked in the presence of higher priorities, and coupled with wonderful free online reporting tools anyone can click a few buttons then send you a copy/paste message claiming they are an "ethical hacker", and could you spare them a bounty please? I will walk through the experience of first receiving one of these emails, discuss the relevant security settings, and then outline one approach for dealing with the subsequent annoyance that arises, making sense of the resulting flood of XML reports from your email providers.

<iframe width="560" height="315" src="None" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>