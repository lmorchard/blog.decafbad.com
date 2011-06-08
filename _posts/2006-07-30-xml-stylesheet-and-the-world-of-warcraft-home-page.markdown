--- 
wordpress_id: 960
layout: post
title: xml-stylesheet and the World of Warcraft home page
wordpress_slug: xml-stylesheet-and-the-world-of-warcraft-home-page
wordpress_date: "2006-07-30T14:59:38-04:00"
wordpress_url: http://decafbad.com/blog/2006/07/30/xml-stylesheet-and-the-world-of-warcraft-home-page
---
<p>The day before we left Michigan, my best friend and Best Man presented me with a copy of World of Warcraft.  He and his girlfriend have been playing the game for quite some time now, and it's how they keep in touch with a few family members - and now, it looks like it'll be a way that they can keep in touch with me.  I can only hope that I don't get <em>too </em>sucked into the game.  :)</p>
<p>All of that aside, though, I just noticed something as I was making an initial pass at registering for a WoW account:  At the moment, <a href="http://www.worldofwarcraft.com/index.xml">the World of Warcraft front page</a> is broken.</p>
<p>It'll probably be fixed by the time you see it, but since my first impulse upon seeing an error is to "View Source", I noticed something further:  Their front page is XML, with an XSL processing instruction at the top.  I'm not sure if this is the way it has been for some time now, but I have to admit I never expected to see this trick used on a production website.  Turns out the page is broken because the XML document is unexpectedly truncated in a run of JS code, and so Firefox throws up the old "XML Parsing Error" page.</p>
<p>Now, the reason I never expected to see it on a production site is because I didn't think enough browsers supported the <code>xml-stylesheet</code> processing instruction.  And then, of course, there's the issue of serving up parsing errors from your front page when strict parsers refuse to humor your sudden tag soup.</p>
<p>But, I do have to say that I've harbored a wish to use <code>xml-stylesheet</code> on real sites for quite some time now.  A lot of the things done with a server-side content management system could be pushed off to the client - things like headers and footers and sidebar assembly and includes.  And it just feels nice to make the client do some of the work for you, taking some weight off the poor abused servers.</p>
<p>On the other hand, I sure do wish that the WoW front page wasn't broken right now.
</p>
