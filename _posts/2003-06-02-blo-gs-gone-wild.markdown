--- 
wordpress_id: 424
layout: post
title: Blo.gs Pings Gone Wild
wordpress_slug: blo-gs-gone-wild
wordpress_date: "2003-06-02T16:10:33-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=424
---
<a href="http://shawnyeager.com/WebHome" target="_top">Shawn Yeager</a> just dropped me a line to let
me know that my blog has apparently been pinging <a href="http://www.blo.gs" target="_top">blo.gs</a> like crazy today, and
since he's set to recieve IM's on blog updates from <a href="http://www.blo.gs" target="_top">blo.gs</a>, he's been getting
flooded with IMs.
<br /><br />
First off, if this is happening to you:  Sorry out there!
<br /><br />
Second thing, this
might be interesting for anyone using a blosxom plugin to ping <a href="http://www.blo.gs" target="_top">blo.gs</a> or <a href="http://www.weblogs.com" target="_top">weblogs.com</a> like me.
Basically, I took the <a href="http://www.raelity.org/apps/blosxom/plugins/output/ping_weblogs_com.individual" target="_top">ping_weblogs_com</a>
plugin for blosxom, replaced the <a href="http://www.weblogs.com" target="_top">weblogs.com</a> request with one to <a href="http://www.blo.gs" target="_top">blo.gs</a>,
and searched for the pattern 'congratulations' instead of 'Thanks for the ping'
in the response.  Finding the pattern is assumed to mean the ping was successful.
A successful ping, then, causes the plugin to update the contents and timestamp
of the status file with the response.
<br /><br />
The status file is used by the plugin to determine whether or not a ping
should be sent.  This check is made everytime an item is viewed on my blog,
and if the plugin sees a blog item whose timestamp is newer than that of
the status file, a ping is sent.
<br /><br />
So!  Onto the punch-line: The appearance of the word 'congratulations' and
the successful registration of a ping are not the same thing.  Apparently,
<a href="http://www.blo.gs" target="_top">blo.gs</a> has been throwing up an error message in response to a ping, while
still registering a ping.  This error message does not contain the word
'congratulations', and so my plugin never updates the status file, and so
it happily tries pinging <a href="http://www.blo.gs" target="_top">blo.gs</a> again with the next blog view.
<br /><br />
Two lessons learned here:
<ol>
<li> When using a web service, whether a "real" service or a "scraped" service, be very sure to know and handle the difference between a valid response and an exception or error in the service itself.
</li>
<li> When using a web service, take care with your usage pattern.  That is, just how important is success?  Important enough to try again and again?  Or could you wait awhile, whether successful or not?  Or should you even try again?
</li>
</ol>
<br /><br />
My plugin doesn't know the real meaning of the response to a ping.  And further,
the fact that it's designed to try, try again in the case of apparent failure
is not the greatest choice for a usage pattern.
<br /><br />
So... longwinded post, but I think the realizations are valuable.
<!--more-->
shortname=blo_gs_gone_wild
