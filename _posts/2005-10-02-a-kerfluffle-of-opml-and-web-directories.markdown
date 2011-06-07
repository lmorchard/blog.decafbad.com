--- 
wordpress_id: 711
layout: post
title: A kerfluffle of OPML and web directories
wordpress_url: http://decafbad.com/blog/?p=711
---
So, I guess there was a bit of an extended kerfluffle over the weekend.  And as these things usually do, it started out from a very cool idea: You can build a web directory as an outline of links, with some nodes "farmed out" to outlines hosted elsewhere—all through the magic of [transclusion][trans].  

For example, say you want to host a directory of resources on web development.  But, you might like to let me maintain the section on web syndication feeds.  Well, I can toss you a URL to my outline of RSS and Atom links, and you can just pull it into a branch of your "superset" outline—kind of like an RSS subscription, really.  Whenever I change my outline, yours will automatically get updated with my work.

Now, imagine this going off into infinity in both directions:  Outlines including outlines including outlines.  Outlines included by outlines included by outlines.  It's a world-wide outline.

So, anyway, [TechCrunch's brainstorm][tech] lead to [Dave Winer's kudos][dwk] and [Scoble's OPML evangelism and an implementation challenge][scoble].    But, to this, [James Robertson responded by calling OPML a "really, really crappy format"][jr].

From this ensued a splattering of posts in various places chiming in on both sides:

  1. [OPML is a sucky and under-specified format, with implementations subject to approval by one guy][bw].
  2. OPML is a working format already in use by lots of code, [so offer something better or shut up][scob2].

Now, [Shelley Powers of Burningbird says][sh] that the "put up or shut up" attitude is wrong, that it's "bad technology".  And, though I do agree with her, the problem is that the usual suspects involved in these sorts of kerfluffles fall on two sides:

  1. We want to see good, well-specified agreements before we code something useful.
  1. We want working, useful code that we'll agree is good when we see it.

While group #1 is willing to talk/shout things out and reach consensus ahead of time, group #2 wants to forge ahead with machines in motion and reach consensus through popular implementation.  So, members of group #2 will *never* take group #1 seriously until they've "put up", because that's *their* process.

Personally, [I sympathize with the dirty ways of group #2][dirt].  But, I've become convinced that what group #1 does is best over the long term, as some of the early successes of group #2 may become tottering unbalanced stacks of plates later on.

So...  What to do?  Bah, I don't know.  But, against my better judgement, I feel like [I have an idea or two to "put up"][idea].  

In the meantime: Members of group #1, stop arguing with members of group #2—you're not speaking in quite the same languages, and you're not going to convert anyone.  Just nod & smile, walk away and come up with a better idea, come back and show why it's better.

(Oh yeah, and whatever happened to [OML replacing OPML][oml]?)

[idea]: http://decafbad.com/blog/2005/10/02/web-directories-with-xoxo-and-xsl
[oml]: http://decafbad.com/blog/2003/04/16/opml-vs-oml
[dirt]: http://decafbad.com/blog/2002/12/13/oooced
[sh]: http://weblog.burningbird.net/archives/2005/10/01/put-up-or-shut-up/
[bw]: http://brainwagon.org/archives/2005/09/30/1610/
[trans]: http://en.wikipedia.org/wiki/Transclusion
[scob2]: http://radio.weblogs.com/0001011/2005/09/30.html#a11296
[jr]: http://www.cincomsmalltalk.com/blog/blogView?showComments=true&entry=3305486922
[dwk]: http://archive.scripting.com/2005/09/29#When:7:36:29AM
[tech]: http://www.techcrunch.com/2005/09/29/opml-an-awesome-experiment/
[scoble]: http://radio.weblogs.com/0001011/2005/09/29.html#a11295
[xoxo]: http://microformats.org/wiki/xoxo
