--- 
wordpress_id: 483
layout: post
title: Dynamic feed polling times for news aggregators
wordpress_slug: dynamic-feed-scan-times
wordpress_date: "2003-09-25T22:45:29-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=483
---
<p>Today, <a href=http://www.decafbad.com/cvs/dbagg/">my aggregator</a> got
the following SQL worked into its <a href="http://www.decafbad.com/cvs/dbagg/lib/dbagg/scan.py?rev=HEAD&content-type=text/vnd.viewcvs-markup">feed poll scheduling machinery</a>:</p>

<pre>SELECT id as source,
       'update_period' as name,
       max(1, 1/max((1.0/24.0),
                    sum(update_count)/(7*24))) AS value 
FROM sources 
LEFT JOIN (
    SELECT source AS count_id,
                round(iso8601_to_epoch(created)/(60*60)) AS hour, 
                count(id) AS update_count 
    FROM items 
    WHERE created>epoch_to_iso8601(now()-(7*(24*60*60))) 
    GROUP BY hour
) ON id=count_id
GROUP BY source
ORDER BY value</pre>

<p>
It's likely that this is really nasty, but I have only a street-level
working knowledge of SQL.  Also, a few of the date functions are
specific to how I've <a href="http://pysqlite.sourceforge.net/documentation/pysqlite/node10.html#SECTION004231000000000000000">extended sqlite in Python</a>.  It works though, and
what it does is this:
</p>

<p>
For each feed to which I'm subscribed, work out
an average time between updates for the past week, with a maximum
period of 24 hours and a minimum of 1 hour.
</p>

<p>
My aggregator does this daily, and uses the results to determine how
frequently to schedule scans.  In this way, it automatically backs off
on checking feeds which update infrequently, and ramps up its polling
of more active feeds.  This shortens my feed downloading and scanning
time, and is kinder in general to everyone on my subscription list.
</p>

<p>
Next, among other things, I have to look into making sure that the
HTTP client parts of this beast pass all the
<a href="http://diveintomark.org/tests/client/http/">aggregator client
HTTP tests</a> that <a href="http://diveintomark.org/">Mark
Pilgrim</a> put together.
</p>

<p>
<b>Update</b>: Well, it seemed like a good idea, anyway.  But, on
further examination, it has flaws.  The most notable is that it
assumes a polling frequency of once per hour.  This works right up
until I start changing the polling frequency with the results of the
calculation.  I haven't poked at it yet, but maybe if I take this
into account, it'll be more accurate.
</p>

<p>
On the other hand, I've also been thinking about a much simpler
approach to ramping polling frequency up and down:  Start out at
a poll every hour.  If, after a poll, no new items are found,
double the time until the next poll.  If new items were found,
halve the time until the next poll.</p>

<p>
Provide lower and upper limits to this, say between 1 hour and 1
week.  Also, consider the ramp up and ramp down factor as a variable
setting too.  Instead of a factor of 2, maybe try 1.5 or even 1.25 for
a more gradual change.  To go even further, I wonder if it would be
valuable to dynamically alter this factor itself, to try to get the
polling time zeroed in on a realistic polling time.
</p>

<p>
Okay.  There the simpler approach leaves simplicity.  I'm sure there's
some decently elegant math that could be pulled in here.  :)
</p>
<!--more-->
shortname=dynamic_feed_scan_times
