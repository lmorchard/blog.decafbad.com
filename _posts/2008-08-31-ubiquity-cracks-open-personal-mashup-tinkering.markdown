--- 
wordpress_id: 1286
layout: post
title: Ubiquity cracks open personal mashup tinkering
date: "2008-08-31T00:07:22-04:00"
tags: 
- webdev
- mashups
- javascript
- entries
- mozilla
- ubiquity
wordpress_slug: ubiquity-cracks-open-personal-mashup-tinkering
wordpress_url: http://decafbad.com/blog/?p=1286
---
When I was a wee hacker, I lived my digital life though a [Commodore 64][c64].  I played games on it, did homework, talked to people far away—you know, all the stuff they showed in the pictures on the box.  I also took things apart—both the machine itself and software running on it.  I grew up learning that my digital environment was ultimately understandable, [susceptible to tinkering][transactor], and open to being bent to my own purposes.

From the Commodore 64, I graduated eventually to terminals and text editors, opening portals mostly onto computers elsewhere via powerful UNIX command shells.  And, of course, over the past decade, this has largely given way to life in a browser.  

Yet, for a little while, particularly in the first few years of browsers, freedom to tinker seemed cramped.  JavaScript had yet to arrive, and was a little messy when it did.  There was no relatively easy addon development.  And, though the portals opened by a browser were richer than those provided by terminals, the paths of navigation defined by links controlled by site owners offered less freedom of movement than UNIX commands.  I could create my own pages, but I couldn't do much to others' pages.

But then, javascript: URLs came around, dots were connected, and [bookmarklets][] were born.  Suddenly, it was possible to customize *my* browsing environment with arbitrary JavaScript code having access to the current page—no matter *whose* page it was.  And, through the various tricks of the AJAX trade, bookmarklets have only gotten more capable throughout the years.

[Smart keyword shortcuts][shortcuts] came around a little later, allowing quick access to bookmarks via simple keywords typed into the location bar.  The smart part, though, came in the form of bookmarked URLs with placeholders and keywords given arguments to fill the placeholders—allowing not only quick access to bookmarked pages but also search engine forms bookmarked with late-bound fields.

Bookmarklets inherited the benefits of smart keyword shortcuts.  The same placeholder in http: URLs can be inserted into the code of a javascript: URL, thus parameterizing the JavaScript code and incidentally turning the location bar into a kind of primitive command line.  For example, one of my most heavily used "[addresslets](http://naeblis.cx/weblog/2004/08/09/DeliciousAddresslets)" is based on [John Resig's original "Super-Fast Delicious Bookmarklet"](http://ejohn.org/blog/super-fast-delicious-bookmarklet/).

Another leap in prying open the browser tinkering space came in the form of [Greasemonkey][]—an addon-powered environment created explicitly for the purpose of end-user scripting applied to others' pages.  [Greasemonkey][] user scripts can do more than bookmarklets, and with a much better development environment to boot.  And, though a user script can't do quite as much as a proper browser addon, they're much easier to hack on and distribute.

Now, consider one of [Mozilla Labs][labs]' [newest projects][ubiquity], named [Ubiquity][].  This rough and experimental addon for Firefox combines and improves upon everything I've described so far:

* [Ubiquity][] is a hackable command line environment, better than [bookmarklets][] and smart [keyword shortcuts][shortcuts];
* [Ubiquity][] enables persistent customization of others' pages, not unlike [Greasemonkey][]; 
* [Ubiquity][] facilitates live in-browser creation and web-based subscription to user commands and scripts;
* [Ubiquity][] gives access to browser chrome resources without a need for frequent restarts;

So far, most of the [commands][] I see popping up since the 0.1 release have not accomplished much more than [smart keyword shortcuts][shortcuts] in the location bar could.  But, it's early yet, and [Ubiquity][] is far from limited to these commands.

Once the basics have been well-explored, I expect to see more people taking a crack at the broader capabilities offered by [Ubiquity][].  [Bookmarklets][] and [Greasemonkey][] can't access browser chrome—but [Ubiquity][] can.  [Ubiquity][] also offers a user interface that's so much more promising than keyword shortcuts, including command previews and typed parameters with suggestions.

Ubiquity promises web-wide mashups directed by a conversational command interface.  All in all, the potential of this makes me feel like my digital environment—browser and web as a whole—is getting even more intimately, personally hackable.  

It'll be very interesting to see where this project goes.

[labs]: http://labs.mozilla.com/
[transactor]: http://cbm.csbruce.com/~csbruce/cbm/transactor/
[c64]: http://www.virtualsky.net/iadoremyc64/
[shortcuts]: http://www.mozilla.org/docs/end-user/keywords.html
[greasemonkey]: http://www.greasespot.net/
[bookmarklets]: http://en.wikipedia.org/wiki/Bookmarklet
[ubiquity]: http://labs.mozilla.com/2008/08/introducing-ubiquity/
[commands]: https://labs.toolness.com/ubiquity-herd/
