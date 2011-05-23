--- 
wordpress_id: 1130
layout: post
title: Week 3 at Mozilla
wordpress_url: http://decafbad.com/blog/?p=1130
---
So, it's getting to the end of my third week at Mozilla, and [I'm a part][part] of [the Planet now][planet]â€”hooray!  Having gotten a membership into that club, I feel like I should start making some noise about what I'm doing at work.  Having stayed mostly quiet about day job affairs thus far in my career, it's going to take a bit to get used to a place as open as Mozilla.

Being a noob, I haven't started anything earthshaking yet.  But, I have gotten a couple of starter bugs thrown my way:

* [Bug 395271][b2] - Use memcache to cache output pages for non logged in users 

    [SUMO][] is [support.mozilla.org][support], a humongous and mostly volunteer-driven support effort for Mozilla products.  I've never really been to the site before myself, so this bug is an iceberg-tip intro to the effort for me.  I'm wading chest deep into [TikiWiki][] and plonking memcached into the middle of it to try to make knowledge base wiki page views a lot less expensive.

    Oh, and the source I'm working on is [in subversion][sumosvn].  Weird.  Like, you could go look at it right now, and tell me [how bad][bad1] [my code][bad2] is.

[bad1]: http://viewvc.svn.mozilla.org/vc?view=rev&revision=13362
[bad2]: http://viewvc.svn.mozilla.org/vc?view=rev&revision=13504
[tikiwiki]: http://tikiwiki.org
[sumosvn]: https://svn.mozilla.org/projects/sumo/
[sumo]: http://wiki.mozilla.org/Sumo
[support]: http://support.mozilla.com/en-US/kb/Firefox+Support+Home+Page

* [Bug 419647][b1] - Add a sexy theme browser

    [AMO][] is [addons.mozilla.org][addons], another humongous effort to support distribution and developers of extensions for Firefox and more.  This is a site I've been to plenty of times, but never as an extension developer.  And so, here's another opportunity to start wading into the deep end.  For this particular bug, the goal is to work up a presentation of themes more easily scanned visually.

    Nothing checked into SVN for this one yet, so you'll have to withhold ridicule for a little bit yet.

I'm really working on squashing my nerd fanboy tendencies.  Because, I remember downloading the original Mozilla Open Source release, staying home from work to compile it on Windows with Visual Studio, and getting just one or two page views out of it before it fell over and caught on fire.  And of course, long before that, I remember using the original lizard in monochrome on a Sun workstation, freaking out over everything and looking up [Earth 2][e2] episode guides.

So, although I'm kinda subdued in general right nowâ€”subdued as in beat about the head and shouldersâ€”I've got a serious amount of breathlessness going on while trying hard to just kinda be nonchalant.  :)

[e2]: http://umsa7.ums.edu/~anniebw/earth2/
[amo]: http://wiki.mozilla.org/Update:Remora
[addons]: https://addons.mozilla.org/en-US/firefox/
[b1]: https://bugzilla.mozilla.org/show_bug.cgi?id=419647
[b2]: https://bugzilla.mozilla.org/show_bug.cgi?id=395271
[part]: http://blog.mozilla.com/planet/2008/05/19/planet-addition-class-of-5192008/
[planet]: http://planet.mozilla.org/
