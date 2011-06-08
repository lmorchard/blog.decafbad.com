--- 
wordpress_id: 540
layout: post
title: More Cooks in the Feed Stew Kitchen
excerpt: I tell ya, this is an idea that's catching.  Feeds go into a searchable stew, come back out as new synthetic feeds.  What comes out looks like what goes in, and there's a well-defined spec behind it.  Sprinkle in the elegance of loosely coupled UNIX pipelines and filters, REST interfaces, and XML tech like XSLT for munging, and you've got the makings of the next generation of syndication and XML feeds.
tags: 
- syndication
- xml
wordpress_slug: more-cooks-in-the-feed-stew-kitchen
wordpress_date: "2004-08-23T23:14:40-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=540
---
<blockquote>
<p>
I've talked before about why I like Atom. It's because it's the fixed point around which all the rest can crystallise...</p>

</blockquote>
<div class="credit" align="right"><small>Source: <cite><a href=
"http://interconnected.org/home/2004/08/24/diego_dovals_atomflow">diego dovals atomflow (24 August 2004, Interconnected)</a></cite></small></div>

<blockquote>
<p>
One, that by using Atom as input format, you could simplify entry into this black-box system and use it, for example, on the receiving end of a UNIX pipe. Content on the source could be either straight Atom or come in some other form that would require transforming it into Atom, but that'd be easy to do, since transforming XML is pretty easy these days.
</p><p>
 Two, that by using Atom as the output format you'd have the same flexibility. To generate a feed if you wanted, or transform it into something else, say, a weblog.
</p>
</blockquote>
<div class="credit" align="right"><small>Source: <cite><a href=
"http://www.dynamicobjects.com/d2r/archives/002885.html">d2r: atomflow</a></cite></small></div>

So, first I discover [Urchin][urchin], and now I read [this][matt].  I tell ya, this is an idea that's catching.  Granted, Urchin's all about RSS, and [atomflow][atomflow] and [dbagg3][dbagg3] are all about Atom, but the spirit's the same:  

Feeds go into a searchable stew, come back out as new synthetic feeds.  What comes out looks like what goes in, and there's a well-defined spec behind it.  Sprinkle in the elegance of loosely coupled UNIX pipelines and filters, REST interfaces, and XML tech like XSLT for munging, and you've got the makings of the next generation of syndication and XML feeds.

I guess maybe I should start checking into this Java stuff again, since smart guys like [Diego][diego] and [Matt][matt] are making noises I like, over in that sandbox.  Well, at least I'll have things like [Jython][jython], [Beanshell][beanshell], and [Groovy][groovy] to toy with over there.  And it's not like I haven't [played with Java][agentfrank] before.

So who else has something like this brewing?

[agentfrank]: http://www.decafbad.com/cvs/AgentFrank/
[groovy]: http://groovy.codehaus.org/
[beanshell]: http://www.beanshell.org/
[jython]: http://www.jython.org/
[matt]: http://interconnected.org/home/
[diego]: http://www.dynamicobjects.com/d2r/
[dbagg3]: http://www.decafbad.com/cvs/dbagg3/
[atomflow]: http://www.dynamicobjects.com/d2r/archives/002885.html
[matt]: http://interconnected.org/home/2004/08/24/diego_dovals_atomflow
[urchin]: http://urchin.sourceforge.net/
