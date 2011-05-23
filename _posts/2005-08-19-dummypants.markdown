--- 
wordpress_id: 676
layout: post
title: Super-fast DummyPants Addressbarlet for del.icio.us
wordpress_url: http://www.decafbad.com/blog/?p=676
---
Okay, so lately I've switched to using "[addressbarlets][addr]" for my [del.icio.us][] posting needs.  In particular, I've been using the [Super-Fast variety][superfast].  I cannot stress how much better these are than clicking links in the bookmark toolbar.  My [del.icio.us][] posting has converged that much closer to command-line / QuickSilver perfection.  

But, I just noticed that in my [del.icio.us][] RSS feed, the title "**del.icio.us warning: non-utf8 string! (sorry)**" has been popping up--especially on [Hot Links][hl], which includes my links on a regular basis.  

Well, although I'm not really all that hip to unicode and non-ASCII characters, it appears that things like [SmartyPants][] and the [use of chevrons in page titles][story] are throwing the monkey wrench for me when the addressbarlet picks up the `document.title`.  So, I decided to do a little sloppy butchery in my bookmarklet code to wrestle these titles into something acceptable.

After you've had a chance to try out / comprehend [the original versions][superfast], take a look at this revised addressbarlet:

* <a href="javascript:u=%22CHANGEME%22;us=[['\u201C','%22'],['\u201D','%22'],['\u2019',%22'%22],['\u2018',%22'%22],['\u2026',%22...%22],['\u00BB','-']];function es(p){for(var i=0;i<us.length;i++){p=p.replace(us[i][0],us[i][1])};p=p.replace(/[\u0080-\uFFFF]/g,'');return encodeURIComponent(p);};q=location.href;e=%22%22+(window.getSelection?window.getSelection():document.getSelection?document.getSelection():document.selection.createRange().text);p=document.title;window.location.href=%22http://del.icio.us/%22+u+%22?jump=doclose&#38;tags=%22+es(%22%s%22)+%22&#38;url=%22+es(q)+%22&#38;description=%22+es(p)+%22&#38;extended=%22+es('%22'+e+'%22').replace(/ /g,%22+%22);">Post to del.icio.us and close</a>

In case, for some reason, that doesn't come through in this entry, here's the code which should appear in the HREF:

<textarea rows="10" cols="65" name="code" class="javascript">
    javascript:u=%22CHANGEME%22;us=[['\u201C','%22'],['\u201D','%22'],['\u2019',%22'%22],['\u2018',%22'%22],['\u2026',%22...%22],['\u00BB','-']];function es(p){for(var i=0;i<us .length;i++){p=p.replace(us[i][0],us[i][1])};p=p.replace(/[\u0080-\uFFFF]/g,'');return encodeURIComponent(p);};q=location.href;e=%22%22+(window.getSelection?window.getSelection():document.getSelection?document.getSelection():document.selection.createRange().text);p=document.title;window.location.href=%22http://del.icio.us/%22+u+%22?jump=doclose&#38;tags=%22+es(%22%s%22)+%22&#38;url=%22+es(q)+%22&#38;description=%22+es(p)+%22&#38;extended=%22+es('%22'+e+'%22').replace(/ /g,%22+%22);</textarea>
	
I'm sure I have a few nasty bugs lurking in there, but basically I'm trying to reverse [SmartyPants][]--DummyPants, if you will--and crudely hack out everything that's not the usual ASCII.

If you happen to be having this problem, let me know if this code works for you.

[story]: http://www.365tomorrows.com/08/19/deo%e2%80%99s-hole/
[smartypants]: http://daringfireball.net/projects/smartypants/
[hl]: http://dev.upian.com/hotlinks/
[superfast]: http://ejohn.org/blog/super-fast-delicious-bookmarklet/
[del.icio.us]: http://del.icio.us
[addr]: http://naeblis.cx/rtomayko/2004/08/09/DeliciousAddresslets
<!--more-->
shortname=dummypants</us></textarea>
