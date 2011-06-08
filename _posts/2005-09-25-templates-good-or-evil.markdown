--- 
wordpress_id: 689
layout: post
title: "Templates:  Good or Evil?"
tags: 
- webdev
- rss
- syndication
- webservices
- atom
- xml
wordpress_slug: templates-good-or-evil
wordpress_date: "2005-09-25T21:12:46-04:00"
wordpress_url: http://decafbad.com/blog/?p=689
---
<blockquote cite="http://lachy.id.au/log/2005/04/xhtml-future#comment-271">This cry and whine that draconian handling will break your page and make your users suffer for you if you have a single error is just another legacy of HTML we’ve gotten used to: our toolchains tend to be of the “glue strings together” (aka templates) variety. ... There should never be any part of your publishing toolchain just gluing strings together. Ever.</blockquote><span style="float:right; font-size: 0.75em; width:75%">Source: <a href="http://lachy.id.au/log/2005/04/xhtml-future#comment-271">Aristotle Pagaltzis in a comment on "The Future: HTML or XHTML"</a></span><br style="clear:both" /><blockquote cite="http://lesscode.org/2005/09/24/web-services-infrastructure-kid/">There’s no rule that says templates must only be used to generate HTML. Indeed, many of the RSS and Atom feeds in the wild are generated from some form of template. They are never automatically-generated-behind-the-scenes using language bindings and are very rarely generated using some kind of DOM/SAX API.</blockquote><span style="float:right; font-size: 0.75em; width:75%">Source: <a href="http://lesscode.org/2005/09/24/web-services-infrastructure-kid/">Web Services Infrastructure: Kid Templating  </a></span><br style="clear:both" />

I've been meaning to write about this for some time now, though I've never had my thoughts together to any degree to mount a decent case for either side.  Problem is, I haven't gotten much closer now, but I figured I'd at least post a few thoughts and conjure up a vague sketch of the issue.

You see, I think it all goes back to [thoughts about which I posted almost three years ago][lazy].  On the one hand, producing something like XML using "proper" DOM invocations and handwavings seems like the "correct" thing to do.  Yet, on the other hand, using a templating system lets me get down to business much more quickly and with much more clarity and succinct code.  

Yeah, templates provide a range of flexibility sufficient to aim the barrel at your own toes, while an API like the XML DOM keeps everything on the rails--but sometimes you know where you're going and don't need the rails to get you there.  Furthermore, isn't it possible to make a template system that Does The Right Thing?

Anyway, it's rather apparent that I'm solidly in favor of templates:  After all, a book of mine just hit the shelves which is just rife with template-based generation of RSS and Atom feeds.  

My only issue, really, is that I feel vaguely guilty about it.

[lazy]: http://decafbad.com/blog/2002/12/13/oooced
