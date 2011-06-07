--- 
wordpress_id: 805
layout: post
title: FeedBurner feeds give heartburn to PHP XML parsers?
wordpress_url: http://decafbad.com/blog/?p=805
---
**Final Update**: *Actually, it turns out that feeding raw, uncompressed gzip streams to PHP XML parsers causes heartburn.  Go figure.  [I guess that teaches me to poke the lazyweb with a stick.][poke]*

[poke]: http://decafbad.com/blog/2005/12/19/sometimes-the-lazyweb-delivers-with-a-deluge

I'm trying to chase this bug down, but is it just me or do FeedBurner feeds give trouble to PHP XML parsers? (*No, it's just me.*)  These three scripts <strike>break</strike> *do not break*:

* FeedBurner feed - <http://feeds.feedburner.com/AVc>
* JSON via Magpie parsing — <http://decafbad.com/2005/12/FeedMagick/www-bin/as-json.php?in=http%3A%2F%2Ffeeds.feedburner.com%2FAVc>
* Passthough with SAX parsing — <http://decafbad.com/2005/12/FeedMagick/www-bin/passthru-sax.php?in=http%3A%2F%2Ffeeds.feedburner.com%2FAVc>
* Passthough with DOM parsing — <http://decafbad.com/2005/12/FeedMagick/www-bin/passthru-dom.php?in=http%3A%2F%2Ffeeds.feedburner.com%2FAVc>

I'm willing to blame my own ineptitude, except that the error in MagpieRSS parsing happens in the bowels of that beast, right where the XML parsing happens... and that's not *my* code.

*Update*:  Actually, I think it's a different problem, but just one that FeedBurner feeds all happen to trigger.  Maybe something to do with the initial tag separated from the XML declaration by some whitespace?

*Update:* By the by, I don't *really* think MagpieRSS is a beast.  Although, I do feel like I'm in the belly of one when I'm wandering through PHP code in general.  And the "not my code" bit is mostly me trying to figure out what's breaking where and why—since Magpie works in other cases except where I'm abusing it.  More like *head-scratching* italics, not *finger-pointing* italics.  Seems like my code's breaking it, but it's not breaking *in my code*.
