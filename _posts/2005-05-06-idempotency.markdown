--- 
wordpress_id: 642
layout: post
title: "Idempotency: It's not just for APIs (or, the web is an API)"
wordpress_slug: idempotency
wordpress_date: "2005-05-06T19:51:54-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=642
---
<blockquote>Implementors should be aware that the software represents the user in  their interactions over the Internet, and should be careful to allow  the user to be aware of any actions they might take which may have an  unexpected significance to themselves or others.<br /><br />

In particular, the convention has been established that the GET and  HEAD methods SHOULD NOT have the significance of taking an action  other than retrieval. These methods ought to be considered "safe".  This allows user agents to represent other methods, such as POST, PUT  and DELETE, in a special way, so that the user is made aware of the  fact that a possibly unsafe action is being requested.<br /><br />

Naturally, it is not possible to ensure that the server does not  generate side-effects as a result of performing a GET request; in  fact, some dynamic resources consider that a feature. The important  distinction here is that the user did not request the side-effects,  so therefore cannot be held accountable for them.
</blockquote>
<div align="right"><small>Source: <cite><a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html">HTTP/1.1: Method Definitions</a></cite></small></div>

So, like... uh...  Did Google [build their accelerator][nsf1] [that way][nsf] just to provide a dramatic example of why [explanations of REST][c] [focus repeatedly][a] ([to the annoyance of some][d]) [on the fact that][b] *the HTTP GET method is specified as and should be implemented as **idempotent***?

Seriously.  Did they?  Well, at any rate, I guess they didn't read this PDF:

* [Assertion: Prefetching With GET is Not Good][ng].

But, eh, I hadn't read that PDF until a few minutes ago anyway.  Though, it is kind of funny that I found it as the first hit on Google for the terms "[rest get idempotent prefetch problem][terms]".  (Which, snarkily, is really the only reason I mention it.)

<blockquote>Yes, one could argue that only "badly designed" web applications that don't follow the rules of GET and POST will be affected, but I'm not sure this is an argument that Google (or anyone else who actually builds or uses web apps in the wild) would care to make in this situation.
</blockquote>
<div align="right"><small>Source: <cite><a href="http://radar.oreilly.com/archives/2005/05/google_web_acce_1.html">O'Reilly Radar: Google Web Accelerator considered overzealous</a></cite></small></div>

Er, oh yeah...  I guess I can't be too smug about GET and idempotency, now that I look at a few of the web apps with which I've been involved.  Yeah, that smarts.  

Although, I do have to say that most of the nonidempotent-(read: broken)-GET-driven things I've put together tend to be behind `href="javascript: do_foo()"` function call links which, while hated by some, would have protected you from this--at least until Google's prefetch learned JavaScript.

Bah, I say.  Maybe it's time to start actually, really paying attention to this?

[terms]: http://www.google.com/search?q=rest+get+idempotent+prefetch+problem
[d]: http://www.franklinmint.fm/blog/archives/000379.html
[c]: http://www.intertwingly.net/blog/784.html
[a]: http://www.xml.com/lpt/a/2004/08/11/rest.html
[b]: http://www-128.ibm.com/developerworks/webservices/library/ws-restvsoap/
[ng]: http://www.cs.bu.edu/techreports/2001-017-wcw01-proceedings/119_davison.pdf
[nsf1]: http://radar.oreilly.com/archives/2005/05/google_web_acce_1.html
[nsf]: http://37signals.com/svn/archives2/google_web_accelerator_hey_not_so_fast_an_alert_for_web_app_designers.php
<!--more-->
shortname=idempotency
