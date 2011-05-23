--- 
wordpress_id: 1043
layout: post
title: Blog posting delegation and third-party auth
wordpress_url: http://decafbad.com/blog/2007/03/05/blog-posting-delegation-and-third-party-auth
---
Here's something I've been meaning to post about, brought back to mind from [Kim Cameron's post on "Wrong-headed impersonation"][kc]:  

I wish that blog posting interfaces (ie. [MetaWeblog API][ma] and [Atom Publishing Protocol][app]) offered a way to delegate blog posting to a 3rd party app (desktop or web) in such a way as to avoid providing one's login details (i.e. user name and password).  For instance, consider both [Flickr's][fa] and [Upcoming's][ua] 3rd party token-based authentication / authorization schemes.

In particular, I'm looking at things like del.icio.us' own Daily Blog Post and others.  These can be used to auto-post content to one's blog generated elsewhere - but at the price of sharing login details.  Granted, you can mostly trust these 3rd parties not to do anything nasty with your credentials, but it would be nice not to have to.

I figure that something RESTful like extending HTTP authentication (ala [Atom Authentication][aa]) with a token scheme could be interesting, and possibly fit nicely into [APP][app] itself.  It could probably be retrofit into the [MetaWeblog API][ma] by specifying a per-app user name and password.  I can imagine a WordPress admin plugin that issues approved authentication tokens to restrict the categories and other activities allowed by 3rd party apps.  

Just something I'm thinking about, as more services may or may not grow into delegated blog posting.

[aa]: http://www.xml.com/pub/a/2003/12/17/dive.html
[ma]: http://www.xmlrpc.com/metaWeblogApi
[app]: http://www.ietf.org/html.charters/atompub-charter.html
[fa]: http://www.flickr.com/services/api/auth.spec.html
[ua]: http://upcoming.org/services/api/token_auth.php
[kc]: http://www.identityblog.com/?p=701
