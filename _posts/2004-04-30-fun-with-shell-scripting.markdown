--- 
wordpress_id: 517
layout: post
title: Fun with shell scripting
excerpt: I went a little nuts tonight with shell scripting.
wordpress_url: http://www.decafbad.com/blog/?p=517
---
I went a little nuts tonight with shell scripting.  It started off with a few innocent bits of [`cat`][cat] and [`grep`][grep] piped together.  But then I invited trouble [started using][parse_log] [`sed`][sed].  Pretty soon, I was bringing in [`cut`][cut] and [`sort`][sort] and [`uniq`][uniq].  I knew I was doomed when I made the whole mess [start emailing me][mail400report] with [`sendmail`][sendmail].  

Oh, but then I went completely off the deep end.  I looked up [RSS 3.0][rss30], since that's so much easier to generate on the fly.  I started producing that with a little help from [`echo`][echo] and [`awk`][awk].  From there, I whipped up [a quick v3.0 to v0.91 converter][rss300to091] so I could get something [my aggregator][dbagg2] could understand.

It was all a very iterative process down a slippery slope of geekiness, and the resulting scripts are nothing that I'd've designed as such from scratch.  But, one thing led to another, and now I've got a [nightly report emailed][mail400report] to me of pages that have gone 404 and 500, and an [RSS feed of referers][referrers_rss] to boot.

I'm sure it looks like completely braindead work, but it was fun!  

[echo]: http://www.rt.com/man/echo.1.html
[awk]: http://www.rt.com/man/awk.1.html
[sendmail]: http://www.rt.com/man/sendmail.8.html
[cat]: http://www.rt.com/man/cat.1.html
[grep]: http://www.rt.com/man/grep.1.html
[sed]: http://www.rt.com/man/sed.1.html
[cut]: http://www.rt.com/man/cut.1.html
[sort]: http://www.rt.com/man/sort.1.html
[uniq]: http://www.rt.com/man/uniq.1.html
[referrers_rss]: http://www.decafbad.com/cvs/*checkout*/www.decafbad.com/bin/gen_referer_feed.sh
[dbagg2]: http://www.decafbad.com/cvs/dbagg2/
[rss300to091]: http://www.decafbad.com/cvs/*checkout*/www.decafbad.com/bin/rss300to091.py
[parse_log]: http://www.decafbad.com/cvs/*checkout*/www.decafbad.com/bin/parse_access_log
[mail400report]: http://www.decafbad.com/cvs/*checkout*/www.decafbad.com/bin/mail_500_400_report.sh
[rss30]: http://www.aaronsw.com/2002/rss30
