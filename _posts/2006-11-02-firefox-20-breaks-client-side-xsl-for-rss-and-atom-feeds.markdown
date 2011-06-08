--- 
wordpress_id: 1012
layout: post
title: Firefox 2.0 breaks client-side XSL for RSS and Atom feeds
wordpress_slug: firefox-20-breaks-client-side-xsl-for-rss-and-atom-feeds
wordpress_date: "2006-11-02T10:31:05-05:00"
wordpress_url: http://decafbad.com/blog/2006/11/02/firefox-20-breaks-client-side-xsl-for-rss-and-atom-feeds
---
This seems like a small thing, but it bothers me:  For RSS and Atom feeds, Firefox ignores client-side XSL transformations in favor of its own new enhanced rendering.  The only way to work around this issue is to stuff 512 bytes or more of XML comment text before the initial feed tag.  [It's been marked as a bug][bug] for some months now - but after reading the discussion therein, I don't have much hope of this being fixed.  The gist of the discussion appears to boil down to this: "Firefox knows best, consistency is good, and anyone using client-side XSL on feeds is really after what we're doing anyway.  Thus, WONTFIX."

This strikes me as a bit condescending, presumptuous, and quite broken.  I don't care if [it's what IE 7 does][ie7] - they're broken too.  This breaks [FeedBurner][fb]'s XSL presentation, which I like though admittedly don't use for my own stuff.  This breaks the feed-styling XSL I've done at jobs past, which rolled in customer-demanded metrics tracking and branding.  And I don't care whether or not the Firefox team considers these or other use cases valid - that's up to me to decide.

This "feature" makes a special case breaking client-side XSL for XML documents that happen to have an "&lt;rss" or "&lt;atom" in the first 512 bytes.  That sucks.  I'd rather the browser left it up to me as a site author whether to follow Firefox's idea of consistency, or whether to happily shoot myself in the foot with my own decisions.

[bug]: https://bugzilla.mozilla.org/show_bug.cgi?id=338621
[fb]: http://www.feedburner.com/fb/a/home
[ie7]: http://blogs.msdn.com/rssteam/articles/PublishersGuide.aspx
