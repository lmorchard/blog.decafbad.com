--- 
wordpress_id: 629
layout: post
title: Atom Format Versioning After Last Call?
date: "2005-04-27T10:40:17-04:00"
wordpress_slug: atom-format-versioning-after-last-call
wordpress_url: http://www.decafbad.com/blog/?p=629
---
<blockquote>An interesting sidebar is that the new Atom format doesn't have a version attribute and I understand it will sit in the same namespace. I tried a few rss clients with the new format and many crashed.</blockquote>
<div align="right"><small>Source: <cite><a href="http://www.burningdoor.com/eric/archives/001148.html">Randy Charles Morin, in comments on "Format Wars, Episode 3"</a></cite></small></div>

I've been pretty much tuned out of the development of Atom, due to a complete lack of time and an assumption that it'll all make sense once it's all been hashed out.  My ears have perked up with [the "last call" noises][lastcall] coming from that direction, so I'm getting the sense that I should start paying attention again.  (And I might need to think about updating [my book][book]!)  

From what little I've seen in my glimpses at drafts issued since this standards process started, there have of course been changes--some small tweaks like changing the &lt;feed>-level &lt;tagline/> to &lt;subtitle/>, and some subtle tweaks in the content model.  I've yet to see anyone chronicle or report on these changes, but I assume that's because it's such a moving target not yet worth tracking.  That, or I've just missed something.
  
But, changes these are, and incompatibilities they make.  So, the above comment concerns me--I don't want to read [another article about mythical compatibility][incom], this time about Atom.  [I figured versioning by namespaces was a good thing,][nsver] versus some arbitrary "version" attribute on the root element of a feed--but in any case, versioning is a must.  Unfortunately due to my tune-out, I have no idea whether the above assertion is true, a misunderstanding, or where to find the context surrounding the issue.  

Rather than jump onto the mailing list or something and ask what's likely a well-hashed issue, I'll restrain my ignorance to my own blog, then, while I continue googling and idly browsing through list archives as time permits.  But, just in case someone knows all about this and feels like tossing me a bone, I'm posting this entry.

**Update #1:** The following bit I'd missed on first glance in the latest Atom draft makes me think that this may not end up being a problem (anyone feel free to correct me):

> This specification uses XML Namespaces [W3C.REC-xml-names-19990114] to uniquely identify XML element names. It uses the following namespace prefix for the indicated namespace URI;

> "atom": http://purl.org/atom/ns#draft-ietf-atompub-format-08

> [rfc.comment.1: This paragraph to be removed by the RFC Editor. The  namespace here is a temporary one and will be changed when the  IESG approves this document as a standard. At that time, the  namespace will be drawn from W3C URI space. The choice of that  namespace will be coordinated between the IETF and W3C through  their respective liaisons.]

[incom]: http://diveintomark.org/archives/2004/02/04/incompatible-rss
[nsver]: http://www.decafbad.com/blog/2003/07/12/echo_unique_namespaces
[lastcall]: http://www.tbray.org/ongoing/When/200x/2005/04/20/Atom-Format-Last-Call
[book]: http://www.decafbad.com/blog/2005/04/25/hacking_rss_and_atom_is_a_real_book
