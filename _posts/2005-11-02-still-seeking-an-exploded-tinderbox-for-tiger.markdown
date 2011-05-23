--- 
wordpress_id: 763
layout: post
title: Still Seeking an Exploded Tinderbox for Tiger
wordpress_url: http://decafbad.com/blog/?p=763
---
This is a recurring thought: I still really, really want [an exploded Tinderbox on Tiger][exp].  It could *so* become an *Ã¼ber* Spotlight/Finder replacement.  I just don't seem to have time or ambition to write it.

I don't mention [Tinderbox][tb] very often, but I've got a few Tinderbox documents set as Login Items on my PowerBook.  So, this app has become ubiquitous on my machine for [idea capture, sorting, and exploration][id].  In fact, I used it to capture, shape, and structure everything I put into [Hacking RSS and Atom][book].

However, I haven't ever gotten far into some of the more advanced features like agents or export templates.  My most used HTML export templates simply boil an outline of notes down into [XOXO][xoxo], and that's about it.  I have had [further][tree] [ambitions][drag] for richer Tinderbox export / extension, but I haven't pursued them much lately.  

Really, my main reason for not delving into Tinderbox's advanced features is that learning and using them effectively would burrow me further into the app's own pocket universe of conventions and technology.

Since Tinderbox saves to XML, I *can* bridge to a larger information space via [XSLT and XPath based tools][tools].  But, all the conversion and roundtrip can get kludgey and awkwardâ€”and I lose the ease of [life inside text files][txt] augmented by grep, awk, sed, vim, perl, python, [QuickSilver][qs], and [Markdown][md].

This is the point where I think opportunities presented by Tiger and the advent of Spotlight can come into playâ€”especially with the availability of [SpotMeta][sm].  SpotMeta weds Spotlight with HFS Extended Attributes in order to enable the management of arbitrary user-specified metadata on files in addition to Spotlight Importer metadata.  

See, the main magic of Tinderboxâ€”at least to meâ€”is visualization and management of relationships between notions and microcontent.  At present, Tinderbox needs to swallow the universe to accomplish everything it wants to accomplish.  It needs to include word processor features and metadata handling and graphics and all.  

But, what if Tinderbox could surrender all of those functions up to TextEdit and MS Word and other desktop apps?  What if all of the "notes" in a Tinderbox document were just documents and files, and all of the relationships managed by Tinderbox (ie. spatial, links, aliased) were just encoded as extended attributes?

In this scenario, *the file system is the Tinderbox document*.  Don't want to use your whole hard drive?  Make a new disk image and compartmentalize things.  Tinderbox could become the world's most revolutionary Finder rethink ever invented.  And the thing is, I can see all of this being enabled by Spotlight and extended attributes.

<!-- tags: tinderbox tiger spotlight xoxo -->

[omnigraffle]: http://www.omnigroup.com/applications/omnigraffle/
[md]: http://daringfireball.net/projects/markdown/
[qs]: http://quicksilver.blacktree.com/
[txt]: http://www.43folders.com/2005/08/17/life-inside-one-big-text-file/
[tools]: http://www.maparent.ca/tinderbox/
[book]: http://www.amazon.com/exec/obidos/ASIN/0764597582/0xdecafbad01-20?creative=327641&amp;camp=14573&amp;link_code=as1
[id]: http://decafbad.com/blog/2005/08/11/quick-thoughts-for-a-thursday
[exp]: http://decafbad.com/blog/2005/05/01/tiger-and-tinderbox
[tb]: http://www.eastgate.com/Tinderbox
[sm]: http://www.fluffy.co.uk/spotmeta/
[tree]: http://decafbad.com/blog/2005/07/02/css-treemaps "Treemaps in CSS"
[drag]: http://decafbad.com/blog/2005/07/02/drag-the-boxes-stretch-the-lines "DHTML map views"
[xoxo]: http://developers.technorati.com/wiki/XOXO
