--- 
wordpress_id: 509
layout: post
title: Publishing Quick Links in blosxom with del.icio.us via xmlstarlet
date: "2003-11-21T09:47:10-05:00"
wordpress_slug: delicious-quicklinks
wordpress_url: http://www.decafbad.com/blog/?p=509
---
<p>
In case anyone is interested in using <a href="http://del.icio.us/">del.icio.us</a> with <a href="http://www.blosxom.com">blosxom</a> in place of my own <a href="http://www.decafbad.com/twiki/bin/view/Main/BookmarkBlogger">BookmarkBlogger</a>, get yourself a copy of <a href="http://xmlstar.sourceforge.net/">xmlstarlet</a> and check out this shell script:
</p>
<textarea rows="14" cols="70">
#!/bin/bash

DATE=${1-`date +%Y-%m-%d`}
BLOG="/Users/deusx/desktop/decafbad-entries/links"
FN="${BLOG}/"`echo ${DATE} | sed -e 'y/0123456789-/oabcdefghij/'`".txt"

curl -s -u deusx:HAHAHA 'http://del.icio.us/api/posts/get?dt='${DATE} |\
	tidy -xml -asxml -q -f /dev/null |\
	xml sel -t -o "Quick Links" -n \
			-e 'ul'  -m '//post' \
			-e 'li'  -e 'a' -a 'href' -v '@href' \
			-b -v 'text()' -n  > ${FN}

touch -d "${DATE} 23:59" ${FN}
</textarea>

<p>
You could do this with XSLT, but hacking with a REST-ish & XML producing web service entirely in a shell script seemed oddly appealing to me that week.  Extending this sort of thing to blogging systems other than blosxom is left as an exercise to the reader.
</p>
<p>
<b>Update:</b> Hmm, looks like one of the blosxom plugins I'm using hates the variables in my code above.  So I stuck curly braces in, which seem to get through okay.
</p>
<!--more-->
shortname=delicious_quicklinks
