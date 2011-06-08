--- 
wordpress_id: 1231
layout: post
title: delicious 2.0 legacy bookmarklet fix
tags: 
- asides
- delicious
- bookmarklets
- greasemonkey
- delicious2
wordpress_slug: delicious-20-legacy-bookmarklet-fix
wordpress_date: "2008-08-02T18:34:28-04:00"
wordpress_url: http://decafbad.com/blog/?p=1231
---
As you've probably seen by now, [Delicious 2.0 has launched][del2].  It's an all new design and the whole thing has been rewritten from the ground up.  Most of the gripes I've seem like general dislike of change—which actually attests to the gargantuan effort put forth to reimplement the original from scratch in a whole new language and architecture.

That said, I found [at least one little bug][tw1] that stops my usual bookmarklet flow.  And, what's really annoying is that, it's probably a bug in code I wrote at one point.  As it turns out, the original URL parameters for the bookmark posting form don't seem to be accepted anymore, so legacy bookmarklets may be broken.  I swore I tested that, since I've got some personal investment in it.

But, although I can't contribute code to the project anymore, I've at least still got [Greasemonkey][gm].  And, through [this quick & dirty user script][legacyfix], I'm back to using my legacy bookmarking bookmarklets.  In case you're interested, [here's my favorite Firefox keyword shortcut bookmarklet][bm]—just select some text, type the keyword in the URL bar with some tags, and hit return.

[gm]: http://www.greasespot.net/
[tw1]: http://twitter.com/lmorchard/statuses/875002291
[tw2]: http://twitter.com/lmorchard/statuses/875004144
[del2]: http://blog.delicious.com/blog/2008/07/oh-happy-day.html
[legacyfix]: http://decafbad.com/2008/deliciouscom_legacy_book.user.js
[bm]: javascript:u=%22USERNAME%22;q=location.href;e%20=%20%22%22%20+%20(window.getSelection%20?%20window.getSelection()%20:%20document.getSelection%20?%20document.getSelection()%20%20:%20document.selection.createRange().text);p=document.title;window.location.href=%22http://del.icio.us/%22+u+%22?jump=doclose&noui&tags=%22+encodeURIComponent(%22%s%22)+%22&url=%22+encodeURIComponent(q)+%22&description=%22+encodeURIComponent(p)+%20%20%22&extended=%22%20+%20encodeURIComponent('%22'+e+'%22').replace(/%20/g,%20%22+%22);
