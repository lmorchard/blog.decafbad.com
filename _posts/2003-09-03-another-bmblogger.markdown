--- 
wordpress_id: 474
layout: post
title: Another BookmarkBlogger in Python
date: "2003-09-03T10:59:31-04:00"
wordpress_slug: another-bmblogger
wordpress_url: http://www.decafbad.com/blog/?p=474
---
<br /><br />
I haven't been paying attention to my referrers as much lately,
but I probably should.  Because, when I do, I find things like
<a href="http://www.hollytree-house.co.uk/twiki/bin/view/Main/BmBlog" target="_top">another implementation</a>
of <a href="http://www.decafbad.com/twiki/bin/view/Main/BookmarkBlogger">BookmarkBlogger</a> in Python, this one by
<a href="http://www.hollytree-house.co.uk/dme/cgi-bin/blosxom.cgi/web" target="_top">David Edmondson</a>.
<br /><br />
His version has many fewer requirements, using only core Python
libraries as far as I can see.  One of these which I hadn't any idea
existed is
<a href="http://www.usatlas.bnl.gov/~fisyak/star/public/WWW/sources/Python-2.3a1/Lib/plat-mac/plistlib.py" target="_top">plistlib</a>,
"a tool to generate and parse <a href="http://www.decafbad.com/twiki/bin/view/Main/MacOSX">MacOSX</a> .plist files".  When I get
another few round tuits, I'll likely tear out all the XPath use
in my version and replace it with this.  Bummer.  And here I thought
I was all clever using the XPaths like that in Python :)
<!--more-->
shortname=another_bmblogger
