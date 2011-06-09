--- 
wordpress_id: 1039
layout: post
title: Thoughts on Pipes on the Web - Part II
date: "2007-02-15T03:49:56-05:00"
tags: 
- webdev
- rss
- mashups
- atom
- yahoo
- feedmagick
wordpress_slug: thoughts-on-pipes-on-the-web-part-ii
wordpress_url: http://decafbad.com/blog/2007/02/15/thoughts-on-pipes-on-the-web-part-ii
---
In [the last post][part1], I expressed concern for my own well-being over a lack of head-over-heels love for [Yahoo! Pipes][pipes].  On the surface, I think it's because it's not a freshly discovered concept for me, and also probably because I'm tired and a bit hacked out right now.  But, I think there's a bit more to it.

First of all, I'm not impressed by GUI builders for most things.  Don't get me wrong:  That [Pipes][] GUI is pretty sweet and quite an impressive implementation — but as a rule, such things don't quite get my geek on.  So, there's that.

Another thing is that I've done something *kinda* like [Yahoo! Pipes][pipes], called [FeedMagick][] — only, it doesn't have a GUI and I mostly abandoned it after releasing the code and having used it for a project at my old job.  It's one of those [serial enthusiasms][se] that I've figured I'd circle back to eventually.  I still think it's a pretty cool idea.  

All kudos to the [Yahoo! Pipes][pipes] team though: Unlike me, they've actually got a living and breathing project — which trumps a paged-to-disk [serial enthusiasm][se] most days.

So what else is really curbing my enthusiasm?  Well, [Yahoo! Pipes][pipes] looks like a pretty self-contained pipes engine — data goes in one end, [frobnication][] happens in the middle, data comes out the other side.

But, what I like about the notion of [the URL-line][urlline] is that you can take one URL and *supply it as a parameter to another URL* — making [messy pipelined URLs][pipelined] while building a crazy web-wide distributed execution environment powered by HTTP and REST.  This is the kernel of the notion that I think really excites me about pipe on the web — I just haven't had a chance to do much with it lately.

Depending on the perspective, true pipes on the web — that is, URLs fetching URLs — look to me like [functional programming][fp] ala [Lisp][].  Consider an idempotent GET request as a pure function call with no side-effects.  Then, consider a GET request that accepts a URL as a parameter — it's a nested function call: the outer GET must make an inner GET to fetch the parameter-supplied URL.  Give the inner URL another URL as a parameter, and you've got yet another nested function call.  

But, if you like, ignore the theoretical [benefits of functional programming][fp] — flip the nested function calls inside out and you've got a pipe.  And, since you're using HTTP GET, you can get all the benefits of HTTP — like caching of execution results and a web full of distributed processing nodes, among other things.  

I haven't explored [Yahoo! Pipes][pipes] deeply enough yet, so maybe I'm missing the features that pipe authors can used to call on other distributed pipe elements out on the web at large.  But, I think that's what ultimately gets me psyched about pipes the web and hasn't yet for [Yahoo! Pipes][pipes].

And, of course, I think I'm just a little hacked out and tired of whizbang new stuff right now.  :)

[fp]: http://www.defmacro.org/ramblings/fp.html
[lisp]: http://en.wikipedia.org/wiki/Lisp_programming_language
[pipelined]: http://www.decafbad.com/blog/2002/04/18/oooaod
[urlline]: http://207.22.26.166/bytecols/2001-08-15.html
[frobnication]: http://www.catb.org/~esr/jargon/html/F/frobnicate.html
[se]: http://decafbad.com/blog/2006/05/26/confessions-of-a-serial-enthusiast
[feedmagick]: http://decafbad.com/trac/wiki/FeedMagick
[pipes]: http://pipes.yahoo.com/
[part1]: http://decafbad.com/blog/2007/02/15/thoughts-on-pipes-on-the-web
