--- 
wordpress_id: 524
layout: post
title: Use Atom for a Universal Blog Transfer Protocol
excerpt: You could use some mashup of RSS and XML-RPC for a Universal Blog Transfer Protocol, but I&#8217;d suggest using Atom. It&#8217;s a data model and an API, where the data model represents blog content quite well and the API complements it for the purposes of shuffling things around. With a mix of XML-RPC and RSS, I could only imagine lots of fiddling going on to transliterate between RSS and metaWeblog API structs or whatnot.
wordpress_url: http://www.decafbad.com/blog/?p=524
---
> One of the options in Tinderbox is to download your most recent posts from your current MT/Radio/Blogger blog into a Tinderbox document, which in turn could be easily turned into a Tinderbox weblog.

> Could XML-RPC and RSS some kind of universal blog transfer protocol to move sites from one blogging tool to another? It seems to me that RSS should/could have most of the information needed to translate one file format to another.

<div class="credit" align="right"><small>Source:<cite><a href=
"http://www.ahawkins.org/mt/archives/000641.html">Universal Blog Transfer Protocol</a></cite></small></div>

Hmm - I was going to drop a note in comments on the above entry, but I see that they're disabled.  So...  I'm off to post a trackback from my own blog!

You could use some mashup of RSS and XML-RPC for this, but I'd suggest using Atom.  It's a data model *and* an API, where the data model represents blog content quite well and the API complements it for the purposes of shuffling things around.  With a mix of XML-RPC and RSS, I could only imagine [lots of fiddling][meta_fiddling] going on to transliterate between RSS and [metaWeblog API structs][metaweblog] or whatnot.

Practically speaking, it seems to me that it'd be [pretty trivial][atom_tut] to build a little conduit between [Atom Enabled][atomenabled] blogs.  Make a request to blog #1 for entries, then turn around and take the data returned by that request and post directly to blog #2.  I imagine there'd be just a *tad* more to do than that, such as splitting up the list of entries and posting each individually.  But since it's all Atom for input and output, there's not much massaging of the data that needs to go on along the way. 

If I get a few round tuits, maybe I'll take a stab at whipping up a sort of Atom-to-Atom-Copy command as an example.  

(And, as an aside, I'd love it if [Tinderbox][tinderbox] supported the Atom API--especially since I'm [hearing noises][joe_wiki] toward [wikis supporting the Atom API][jsp_atom]!)

[tinderbox]: http://www.eastgate.com/Tinderbox/ "Great app for catching and developing ideas"
[atom_tut]: http://www.atomenabled.org/developers/tutorials/api-quick-guide.php "All the pieces are here in an Atom API tutorial"
[metaweblog]: http://www.xmlrpc.com/metaWeblogApi "The metaWeblog API specification"
[meta_fiddling]: http://www.xml.com/pub/a/2003/10/15/dive.html "Mark Pilgrim's overview of the Atom API.  In particular, check out the section about the metaWeblog API's relationship to RSS 2.0"
[atomenabled]: http://www.atomenabled.org/
[joe_wiki]: http://www.xml.com/pub/a/2004/04/14/atomwiki.html "Joe Gregorio explores Atom-Powered Wiki"
[jsp_atom]: http://www.ecyrd.com/ButtUgly/Wiki.jsp?page=Main_blogentry_160504_2 "Wherein the author of JSPWiki entertains the notion of an Atom API"
