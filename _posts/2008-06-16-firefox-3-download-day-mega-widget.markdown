--- 
wordpress_id: 1148
layout: post
title: Firefox 3 Download Day Mega Widget
date: "2008-06-16T11:55:04-04:00"
tags: 
- firefox
- entries
- mozilla
- downloadday
wordpress_slug: firefox-3-download-day-mega-widget
wordpress_url: http://decafbad.com/blog/?p=1148
---
**Update:** Oh, and rumor has it that this widget will switch to reporting on downloads, rather than pledges, once the main event has begun.

**Update 2:** It didn't *quite* go like clockwork, but this widget is now showing estimated downloads by countries, rather than pledges.

Thanks to the completion of [bug 435967][bug], I can offer this totally unofficial hack of a mega widget (better late than never):

<script type="text/javascript" src="http://decafbad.com/2008/download-day-top-ten.js"></script>

If you'd like, you can include this on your own site with a Copy-and-Paste of the following:

<textarea cols="80" rows="3"><script type="text/javascript" src="http://decafbad.com/2008/download-day-top-ten.js"></script></textarea>

This is a total 2-hour cut, paste, reformat, and slight rejigger of [Kent Brewster's work on Content Syndication with Case-Hardened JavaScript][kent].  Hopefully it works, because I'm [releasing early][early] before I've had a chance to check it out on anything besides the browsers in my lap.

[kent]: http://kentbrewster.com/case-hardened-javascript/
[bug]: https://bugzilla.mozilla.org/show_bug.cgi?id=436967
[early]: http://catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html
