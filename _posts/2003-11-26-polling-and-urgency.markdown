--- 
wordpress_id: 511
layout: post
title: Varied feed polling times versus item urgency in aggregators
date: "2003-11-26T11:02:01-05:00"
wordpress_slug: polling-and-urgency
wordpress_url: http://www.decafbad.com/blog/?p=511
---
<blockquote cite="http://www.teledyn.com/mt/archives/001496.html">The problem with varying the polling interval is that the need varies. It's ok not to poll my little opensource website within 24 hours, but what about the announcements to the civil defence website or local municipal environment alerts, or the nuclear power plant news feed?
</blockquote>
<div class="credit" align="right"><small>Source:<cite><a href="http://www.teledyn.com/mt/archives/001496.html">Comments on The End of RSS </a></cite></small></div>

<p>
Definitely a good point there.  For most of the feeds in my daily habit, what I use is an AIMD variation on my polling frequency per feed based on occurrence of new items.  For feeds with low-frequency but high-urgency items, a different algorithm should come into play.
</p>

<p>
On the other hand...  should incoming alerts with that much urgency really be conveyed via an architecture driven by polling?  Here's an excellent case for tying instant messaging systems and pub/sub into the works.
</p>
<!--more-->
shortname=polling_and_urgency
