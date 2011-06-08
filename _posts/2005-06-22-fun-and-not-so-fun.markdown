--- 
wordpress_id: 655
layout: post
title: Fun and not-so-fun
wordpress_slug: fun-and-not-so-fun
wordpress_date: "2005-06-22T18:23:47-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=655
---
* Last night's fun trick?  Say hello to <a href="aim:goim?Screenname=decafbot&Message=help">decafbot</a>!  

  I turned an IRC [Infobot][ib] into an AIM chatbot via [Bitlbee][bb].  It may or may not be online depending on how stable the rig is and how tolerant AIM's flood/spam triggers are.

  I've always been a fan of `purl` on the `#perl` IRC channel, so maybe I can try turning this little infobot into something useful.  At any rate, it was a quick hack involving two installs via DarwinPorts and a few config file tweaks.  So, send an IM on the AIM network to <a href="aim:goim?Screenname=decafbot&Message=help">`decafbot`</a> and see what happens.

[ib]: http://infobot.sourceforge.net
[bb]: http://www.bitlbee.org/

* Today's not-so-fun trick?  (Well, the past 2 weeks' not-so-fun...)

  Imagine a crazy crapstorm web app project which features allowing visitors to upload pictures, presumably from their digital cameras.  Ignore for the moment any details of feasibility, scope, timing, or resource planning.

  Oh, and you're stuck working with classic ASP 3.0.  You have no access to write to the file system on the production web server, and you've been told not to stick big things in the database tables--like photos from digital cameras, for instance.  Also, did I mention that you can't register any new DLLs on the production servers?  At least, not without the consultation of a committee who only meets every quarter or so.  Oh, and did I mention this was due last week?

  So, you've got to *somehow* capture those images and the accompanying metadata and stash it all *somewhere*, despite being denied a filesystem or a database.  What to do, what to do?  Oh, I know: let's email all this crap off to an inbox somewhere that something (or someone (*sorry, intern*)) will be able to batch process!

  Great!  Except, well... er...  ASP 3.0 doesn't really particularly like processing forms with file uploads.  In fact, it doesn't support it at all.  Luckily, I was able to find some code [implementing file upload handling in pure VBScript][file], although I had to scrape it off the HTML page itself since the .zip file had gone missing.

  With that, then, you can actually accept the form submission.  Now, how to fire off an email with the image as an attachment?  The only email support we have available is [CDONTS.DLL][cdonts], and it appears to only offer some support for attachments which are available in the filesystem--and all we have here is a stream of bytes in memory.  

  So, armed with a pure-ASP implementation of [base64][] and a decent understanding of SMTP and RFCs, I forged ahead to piece together a MIME multipart email the hard way in VBScript.  Remember to line break your stream of base64-encoded binary at 75 columns, and you'll need to trick CDONTS to allow you to inject a `Content-Type: multipart/mixed` header into the mix, and you're off!

  Whew... and, believe it or not, it all works.  I almost wish I could share the source code, ignoring that it's implemented with an obsolete set of technologies and that it's certainly not the prettiest code in the world.

[base64]: http://www.freevbcode.com/ShowCode.asp?ID=5248
[file]: http://aspzone.com/articles/160.aspx
[cdonts]: http://www.mostlylucid.co.uk/archive/2003/10/15/589.aspx
