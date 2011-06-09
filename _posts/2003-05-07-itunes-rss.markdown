--- 
wordpress_id: 414
layout: post
title: iTunes Music Store RSS Feeds
date: "2003-05-07T17:21:10-04:00"
wordpress_slug: itunes-rss
wordpress_url: http://www.decafbad.com/blog/?p=414
---
Yeah, I know I <a href="http://www.decafbad.com/blog/geek/itunes_does_drm.html" target="_top">gave the iTMS a 'bah'</a>
last week in response to discovering DRM under the hood.  But I've softened in
my opinion since then.  And bought a few more songs that I haven't heard in years.
And burned an Audio CD.  And wasn't <strong>too</strong> inconvenienced.  
<br /><br />
My girlfriend and I almost
bought iPods last night, and though we resisted the temptation this time, I expect that
we'll end up with them before long.  And when that happens, I imagine we'll try sharing
tracks, and that doesn't seem to be too inconvenient either.  And then, there's the
fact that the iTMS seems to have a pretty nifty set of underpinnings that look like
fun to play with.
<br /><br />
So now, like anything I'm interested in on the interweb, I want to swallow it up with my aggregator.
<br /><br />
Thus, I attempt a new project:  <a href="http://www.decafbad.com/twiki/bin/view/Main/ItunesMusicStoreToRss">ItunesMusicStoreToRss</a>
<br /><br />
Progress so far, but I've hit a stumbling block.  Anyone want to help?
<br /><br />
<strong>Update:</strong> A little bit of cut &amp; paste from the wiki page:
<br /><br />
If you spy on iTunes while browsing to a "Just Added" section of a genre, you'll find that a URL like the following is accessed: 
<br /><br />
<a href="http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wa/com.apple.jingle.app.store.DirectAction/viewPlayListsPage?fcId=145690&amp;pageType=justAdded&amp;id=21" target="_top">(it's a long URL)</a>
<br /><br />
The response to that URL is some very interesting XML that looks like a GUI language.  Buried in the GUI recipe, however, is what I want flowing into my aggregator.  So, I dust off my XSL skills and have a go at mangling this content into <a href="http://www.decafbad.com/twiki/bin/view/Main/RSS">RSS</a>.  I seem to have been successful.  A test run appears to validate, and is accepted in my aggregator. 
<br /><br />
The problem, though, lies in the aforementioned URL.  Everything seems pretty clear and straightforward, and I can change genre's by supplying discovered ID's to the id parameter.  However, the  "fcid=145690" parameter  is an unknown to me.  It seems to change, though I haven't yet investigated its derivation or how often it changes.  I was working on things yesterday, and the value was one thing, this morning it was another. If the number is not valid, unexpected results happen, sometimes resulting in HTML output describing an application exception.  So, until the fcid mystery is solved, I've yet to automate this transformation. 
<br /><br />
Any ideas out there on the lazyweb?  Visit the wiki page (<a href="http://www.decafbad.com/twiki/bin/view/Main/ItunesMusicStoreToRss">ItunesMusicStoreToRss</a>) and feel free to poke fun at my XSL skills.
<!--more-->
shortname=itunes_rss
