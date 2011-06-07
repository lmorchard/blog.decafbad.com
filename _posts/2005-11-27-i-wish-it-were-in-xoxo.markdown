--- 
wordpress_id: 781
layout: post
title: I wish it were in XOXO
wordpress_url: http://decafbad.com/blog/?p=781
---
<blockquote cite="http://blogs.msdn.com/alexbarn/archive/2005/11/24/496636.aspx">Note: hey, mum & dad - you can check out my Christmas OPML wishlist in your browser right now (in case you're tuning in ;-)</blockquote>
<small style="text-align:right; display:block">Source: <a href="http://blogs.msdn.com/alexbarn/archive/2005/11/24/496636.aspx">Alex Barnett blog : Wow, an OPML browser and wishlist</a></small>

Okay, so I'm trying to catch up on the latest round of renewed buzz for OPML.  In my reading, I just caught the above-quoted post about a wishlist expressed as OPML.  

This is what I read:  He [links to the wishlist][wish] in HTML form, by way of a conversion service on a site called [Opmlmanager][opml].  You can also download & install the [.NET framework][net], if you'd like to run [a desktop OPML browser][brow].  Sounds like a nice stack of technology, [neat like digital watches][neat].

So, this is my question: Why not just keep it all in XHTML lists—that is to say, [XOXO][].  The HTML output of that [Opmlmanager][opml] conversion is just *barely* not valid XOXO, but with a few tweaks it'd be fine—complete with fancy DHTML expand/collapse functionality *and* maybe even some [outline transclusion][ot] hints.

With XOXO, there's no need for a conversion service, and you can use a standard web browser without downloading any frameworks.  I'd say these are nicer criteria for sharing things on the web.

As for authoring tools?  At the moment, I can't think of a specific outliner that produces XOXO directly.  But, any general HTML editor would help, and there are dozens of tools with list editing baked in.  (ie. WordPress, TypePad)  And if you have a sane OPML file, you can try using [a little bit of XSLT][xsl] to convert it to XOXO.

<strike>Finally, what really strikes me as weird about Alex Barnett's post is that I can't find a link to any raw OPML anywhere on the page.  In fact, I can't find any OPML on the [converted wishlist page][wish], either.  All I'm seeing are links and HTML from where I'm sitting—where's the OPML magic?</strike>

**Update:** Alex has provided the [link to the OPML][alex].  Thanks for the pointer!  I think what I was trying to get at with the above is that sharing the HTML on the web is more natural than sharing the OPML.  But I think I've run out of XOXO steam for today :)

[alex]: http://www.opmlmanager.com/opml/alexbarnett.opml
[ot]: http://decafbad.com/blog/2005/10/02/web-directories-with-xoxo-and-xsl
[net]: http://www.microsoft.com/downloads/details.aspx?FamilyID=0856eacb-4362-4b0d-8edd-aab15c5e04f5&amp;DisplayLang=en
[opml]: http://www.opmlmanager.com/
[wish]: http://www.opmlmanager.com/outliner/alexbarnett
[xoxo]: http://www.microformats.org/wiki/xoxo
[brow]: http://www.opmlmanager.com/opmlbrowser/
[neat]: http://www.decafbad.com/twiki/bin/view/Main/NeatLikeDigitalWatches
[xsl]: http://decafbad.com/trac/browser/trunk/GopherNext/opml-to-xoxo.xsl
