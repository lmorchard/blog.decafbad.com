--- 
wordpress_id: 1450
layout: post
title: An unnecessary Template Attribute Language
wordpress_url: http://decafbad.com/blog/?p=1450
---
A funny thing happened on the way to building [a delayed real-time feed display][lizardfeeder]:  I got temporarily obsessed with implementing [a template language in JavaScript][jqtal] that, as it turned out later, I didn't need.  About [the feed project itself][lizardfeeder], I hope to write more soon—but for now I want to get this extra template language thing out of my system and see if anyone else might have a use for it.

See, I had a notion it would be keen if I had access to the same template language on the client as on the server.  I needed to render a number of list items statically on the server with feed entries, then update that list with new entries on the client as they became available through JSON feed polling.  It'd be a pain in the butt to maintain two separate list item templates for client and server, so I reached for a shared template language.

Never mind that I'd just gotten done writing [a small book on Dojo][book], and was already aware of the existence of the [DojoX Django Template Language][djt].  This might've worked, since the server end of things was written in Python (though not with Django).  That the JavaScript side already used [jQuery][] wasn't *too* tall a hurdle.  Also, I'm sure there are a handful of other JavaScript/Python template language match-ups to be found.

But, let's be honest here:  I've always been a fan of Zope's [Template Attribute Language][tal] for their [Page Templates][pt], and have long wondered how hard it would be to implement.  The concept seems so much cleaner to me than most string-formatting template languages, and the workflow from mockup-to-template and back again has always been appealing to me when it works.  So, when my first few experimental steps in trying my hand at it actually started working, I couldn't stop coding.  

And now, [the thing][thing] is mostly done.  It has no tests, has features left undone, and probably yields plenty of bugs—but I finished it enough to use it practically, and that was long enough to convince me it wasn't the right tool for the job.  

Still, though, I can't help thinking it might be the right tool for *some* job.  That could be because I spent a lot of time on it, or that I'm unreasonably fond of [TAL][tal], but it still feels like a decent little plugin to have on hand.  Maybe someone reading this will have a similar conclusion.

Oh and by the way, plain [jQuery][] turned out to be a better tool for [the job in question][lizardfeeder].  This seems to nicely balance the duplicate effort between server and client, demanding only that I stick with semantically significant CSS class names in the server template—something I should be doing anyway:

            // Clone and populate a new entry.
            var new_item = $('#feed-items .entry:last')
                .clone()
                .attr('class', entry_classes.join(' ')) 
                .find('.group span')
                    .text(tags['group'])
                .end()
                .find('.title')
                    .find('.favicon')
                        .attr('src', favicon)
                    .end()
                    .find('.link')
                        .attr('href', entry.link)
                        .text(entry.title)
                    .end()
                .end()
                .find('.updated')
                    .find('.timeago')
                        .attr('title', entry.updated)
                        .text(entry_updated.strftime('%+'))
                        .timeago()
                    .end()
                    .find('.time')
                        .text(entry_updated.strftime('%I:%M %p'))
                    .end()
                .end()
                .find('.author')
                    .text(entry.author || 'n/a')
                .end()
                .prependTo('#feed-items')
                .hide();

Of course, *plain* is a relative term here.

[jquery]: http://jquery.com/
[tal]: http://wiki.zope.org/ZPT/TALSpecification14
[pt]: http://wiki.zope.org/ZPT/FrontPage
[book]: http://www.amazon.com/gp/product/0470452021?ie=UTF8&tag=0xdecafbad01-20&linkCode=as2&camp=1789&c%0D%0Areative=9325&creativeASIN=0470452021
[djt]: http://svn.dojotoolkit.org/src/dojox/trunk/dtl/README
[jqtal]: http://github.com/lmorchard/jquery-tal-template/tree/master
[lizardfeeder]: http://svn.mozilla.org/projects/lizardfeeder/trunk/
[thing]: http://github.com/lmorchard/jquery-tal-template/tree/master/jquery.taltemplate.js
