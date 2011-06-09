--- 
wordpress_id: 947
layout: post
title: iptables, port forwarding, and access from LAN-side
date: "2006-05-09T22:19:16-04:00"
tags: 
- asides
wordpress_slug: iptables-port-forwarding-and-access-from-lan-side
wordpress_url: http://decafbad.com/blog/2006/05/09/iptables-port-forwarding-and-access-from-lan-side
---
 <p>Nothing like firewall rules to make me feel like a moron.  I recently wiped and reinstalled <a href="http://openwrt.org/">OpenWRT</a> on my WRT54G router.  Before the wipe, I had firewall rules which forwarded port 80 to a web server on my home LAN behind the router.</p>
 <p>The nice part was that I could access that server both from outside and inside the LAN, using the external WAN IP.  I've got scraped RSS feeds and other HTTP accessible bits that I access from my laptop.  This laptop travels between work and coffee shop and home.  I like being able to subscribe to and point at these things by URLs that don't change.</p>
 <p>But now, after the wipe, I've got firewall rules which open the WAN port to the home LAN for access from outside - but not from inside.  I've lost the old rules, and the knowledge I had that let me build the rules has since paged out of my brain and been lost to the ether.</p>
 <p>I suppose I could try building a VPN to home again - or use some SSH port tunneling - but I'd really like to get this port forwarding working again.  Anyone know how this crud works?</p>
