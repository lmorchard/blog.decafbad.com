--- 
wordpress_id: 646
layout: post
title: Further quick thoughts on GreaseMonkey
wordpress_slug: further-greasemonkey
wordpress_date: "2005-06-08T16:47:56-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=646
---
Now for some quick GreaseMonkey spew, recorded without any effort to actually see what's up in the community or reading any FAQs:

* I want to separate script code into reusable modules.
* That said, am I an [Architecture Astronaut][astro] when I can't get more than 10 minutes into a quick project without already starting to digress into building a *reusable framework*?
* Is it wrong that I felt like I was working in Perl again when I wrote [that script][script]?
* That said, I wish JavaScript had either multi-line quotes ala Python or Perl heredoc syntax.
* Doing some twisty regex search-and-replace in Vi lets you do a lot of refactoring / recoding damage to source code in no time flat.
* Can I just say how nice it is to not worry about other browsers when coding?

I've also got a few ideas I'd like to record and pursue for future GreaseMonkey endeavors:

* Record the URL of all form submissions via XMLHTTPRequest to a remote server, with blog comment forms in mind.  Track changes on those URLs.  Notify me via Atom feed when new comments arrive in places where I posted comments.
* Clean up and abstract that magic form thing I did into a more general way to make all kinds of magic textarea forms.  (More microformats?  .sig files for LiveJournal responses?  /usr/bin/banner for annoying blog comments?)
* Revive [Third Voice][tvoice] in GreaseMonkey style.  Subscribe to arbitrary REST API'ed annotation servers, fetch & aggregate annotations for current URL via XMLHTTPRequest, build cute floating stickies with rude comments from friends.
* Auto-ROT13 en/decoder ring, because there's a need for that.
* Script which redirects all links to books on Amazon.com to point at my new book.  I will install this on all computers at CompUSA and the Apple Store.

I've suddenly realized that a lot of the things I wanted to do with [Agent Frank][afrank] are possible with GreaseMonkey.  Also, I wonder how long it'll be before I get sucked into further FireFox extension hacking.

[afrank]: http://www.decafbad.com/twiki/bin/view/Main/AgentFrank
[tvoice]: http://wired-vig.wired.com/news/business/0,1367,42803,00.html
[astro]: http://www.joelonsoftware.com/articles/fog0000000018.html
[script]: http://www.decafbad.com/2005/06/magic_hcalendar.user.js
<!--more-->
shortname=further_greasemonkey
