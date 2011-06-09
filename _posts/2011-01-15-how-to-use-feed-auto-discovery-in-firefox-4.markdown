--- 
wordpress_id: 1970
layout: post
title: How to use feed auto-discovery in Firefox 4
date: "2011-01-15T22:20:22-05:00"
tags: 
- rss
- firefox
- feeds
- entries
- mozilla
- autodiscovery
- bug578967
wordpress_slug: how-to-use-feed-auto-discovery-in-firefox-4
wordpress_url: http://decafbad.com/blog/?p=1970
---
**TL;DR**: <em>The feed button is not dead; it's just been sent to sing backup in Firefox 4 because it's not pulling its weight up front. This post discusses how you can still use feed auto-discovery, even restoring the icon to the toolbar with a few clicks and a drag.</em>

There's [a brouhaha](http://camendesign.com/rss_a_reply) about [Bug 578967](https://bugzilla.mozilla.org/show_bug.cgi?id=578967), wherein the feed auto-discover icon in [the Firefox 4 Beta](http://www.mozilla.com/en-US/firefox/beta/) has been hidden by default. Being a feed nerd, the author of a book on the stuff, *and* a Mozilla employee—I've got at least a few opinions.

This post is one of [several on this subject](http://decafbad.com/blog/tag/bug578967).

### Feeds are too ubiquitous to need an indicator

Feeds are so successful and ubiquitous that it's simpler to assume every site has one, rather than keeping an un-lit indicator around to tell you when one's missing. So, Firefox 4 has an option in the bookmark menu to subscribe to the current page:

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-002.png" alt="feed-sub-00.png" border="0" width="600" height="242" />

The only indicator of a missing feed is that the menu item greys out. Since feeds are everywhere, you should feel comfortable reaching for that subscription menu whenever you like. Of course, this assumes that subscribing to a page falls into the same thought process as bookmarking it—but I don't think that's an unreasonable notion.

On the other hand, if you didn't know that subscribing to a page was possible—or if you worry there might be people (ie. the potential readers of your feeds) who are in that position—this change may seem problematic. 

I don't think that's an unreasonable notion, either. But, I'll get back to that in a future post.

### The feed icon isn't dead, it's just hiding

Even with the new bookmark menu item, the feed subscription button is still available and ready to return to your toolbar in [the Firefox 4 Beta](http://www.mozilla.com/en-US/firefox/beta/).

First, right-click somewhere in the empty space of your Firefox 4 toolbar. Try somewhere after the tabs, or somewhere between the toolbar buttons. [This is how it works on Windows](http://blog.fligtar.com/2011/01/16/how-to-customize-firefox-4s-ui/), and this is what it looks like on my Mac:

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-toolbarmenu.png" alt="feed-sub-toolbarmenu.png" border="0" width="220" height="161" />

Click Customize, and you'll get a panel like this:

<p><img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-01.png" alt="feed-sub-01.png" border="0" width="500" height="" />

This lets you customize which buttons and controls appear on the toolbar. If you scroll down in the panel, you'll see a "**Subscribe**" button. Drag that from the panel to a position in the toolbar, and you'll get a result like this:

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-02.png" alt="feed-sub-02.png" border="0" width="500" height="" />

Click "**Done**", and your browser should end up like this:

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-03.png" alt="feed-sub-03.png" border="0" width="600" height="203" />

I took my browser screenshots with [Dave Winer's screenshot of the old Firefox feed icon](http://scripting.com/stories/2011/01/15/mozillaPleaseKeepTheRssIco.html) for comparison. The result is different, but not radically so. It even enables and darkens when you visit a site with a feed:

<img src="http://decafbad.com/blog/wp-content/uploads/2011/01/feed-sub-04.png" alt="feed-sub-04.png" border="0" width="600" height="271" />

The main difference is that Dave's screenshot is the default in Firefox 3.6, whereas mine is the result of the last few screenshots of toolbar customization in Firefox 4 beta 9. That customization is easy, if you know it's possible—but the worry is, as they say: out of sight, out of mind. 
