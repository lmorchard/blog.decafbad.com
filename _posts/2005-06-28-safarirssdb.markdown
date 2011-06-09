--- 
wordpress_id: 661
layout: post
title: Safari RSS databases in Mac OS X Tiger - or Monkeys and Ninjas and Pirates and Robots, oh my!
date: "2005-06-28T11:53:35-04:00"
wordpress_slug: safarirssdb
wordpress_url: http://www.decafbad.com/blog/?p=661
---
Hey, what do you know?  The database used by `Syndication.framework` on OS X is accessible with [SQLite 3][sl3], assumedly by virtue of [Core Data][cd].  Check out this barely presentable capture of what I just did in a shell window:

[sl3]: http://www.sqlite.org/version3.html
[cd]: http://developer.apple.com/macosx/coredata.html

<pre style="font-size: 0.75em; overflow: auto">
[11:34:49] deusx@Caffeina2:~/Library/Syndication$ sqlite3 Database3 
SQLite version 3.0.8
Enter ".help" for instructions
sqlite> .tables

Articles  Sources 

sqlite> .schema Articles

CREATE TABLE Articles (id INTEGER PRIMARY KEY,
source_id INTEGER,author TEXT,title TEXT,contentType INT(1),
contents TEXT,excerpt TEXT,GUID TEXT,permalink TEXT,iconURL TEXT,
categories TEXT,date DATETIME,dateReceived DATETIME,unread INT(1),
flagged INT(1),collapsed INT(1),noComments INT(1));
CREATE INDEX ArticleCurrents ON Articles (noComments);
CREATE INDEX ArticleDates ON Articles (date);
CREATE INDEX ArticleDatesRcvd ON Articles (dateReceived);
CREATE INDEX ArticleSources ON Articles (source_id);
CREATE INDEX ArticleUnreads ON Articles (unread);

sqlite> .schema Sources

CREATE TABLE Sources (id INTEGER PRIMARY KEY,URL TEXT,
subscribed INT(1),title TEXT,iconURL TEXT,date INT,lastCheck INT,
lastUpdate INT,slider INT(1),description TEXT,homePage TEXT,
timespan INT(1),sort INT(1),HTTPdate VARCHAR,feedHash VARCHAR(40),
FOAFURL TEXT,protocol VARCHAR,lastError VARCHAR,maxDays INT(2),
maxArticles INT(2),x_monkey TEXT,x_ninja TEXT,x_pirate TEXT,
x_robot TEXT);

sqlite> select * from Sources;

id|URL|subscribed|title|iconURL|date|lastCheck|lastUpdate|slider|description|homePage|timespan|sort|HTTPdate|feedHash|FOAFURL|protocol|lastError|maxDays|maxArticles|x_monkey|x_ninja|x_pirate|x_robot
1|http://www.apple.com/main/rss/hotnews/hotnews.rss|1|Apple Hot News||141617700|141648125|141648128|||http://www.apple.com/hotnews/|||Tue, 28 Jun 2005 02:15:00 GMT|150fdf111cd223367f5c0cb8d28c65ec2a4ec195||RSS|||||||
2|http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wpa/MRSS/newreleases/limit=25/rss.xml|1|iTunes 25 New Releases|/images/rss/badge.gif|141577349|141648124|141648126|||http://phobos.apple.com/WebObjects/MZStore.woa/wa/com.apple.jingle.app.store.DirectAction/viewNewReleases?pageType=newReleases&id=1|||Mon, 27 Jun 2005 18:02:29 GMT|8a2c02423581414b223f4533f0bf89211e1aa6c7||RSS|||||||

...

sqlite> select * from Articles;

id|source_id|author|title|contentType|contents|excerpt|GUID|permalink|iconURL|categories|date|dateReceived|unread|flagged|collapsed|noComments
2003|5||'Mactel' desktops may offer triple-threat OS|0||Also: GE, IBM and GM: the welfare kings|http://news.com.com/News.com+Extra/2001-9373_3-0.html?part=rss&tag=rsspr.5748612&subj=news|http://news.com.com/News.com+Extra/2001-9373_3-0.html?part=rss&tag=rsspr.5748612&subj=news|||140527020|140612922|1|||0
2004|5||Virtual property becomes a reality|0||Blog: With the recent sentencing of a Chinese man who murdered an acquaintance in a dispute over a virtual sword, talk of the growing...|http://news.com.com/2061-10786_3-5748748.html?part=rss&tag=5748748&subj=news|http://news.com.com/2061-10786_3-5748748.html?part=rss&tag=5748748&subj=news|||140579040|140612922|1|||0
</pre>

There's one piece up there that had me do a coffee spit-take, though:

`x_monkey TEXT,x_ninja TEXT,x_pirate TEXT,x_robot TEXT`

Seems like the Syndication Wars have progressed, and the various sides have enlisted all of these combatting factions.  [Monkey vs Robot][mvr], [Pirates vs Ninja][pvn]--I only wonder whether the Ninjas and Robots will ally against the Monkeys and Pirates?  It just seems natural.

[mvr]: http://www.swervepictures.com/monkey.htm
[pvn]: http://daily.stanford.edu/tempo?page=content&id=17374&repository=0001_article
<!--more-->
shortname=safarirssdb
