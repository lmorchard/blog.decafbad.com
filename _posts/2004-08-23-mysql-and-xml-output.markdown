--- 
wordpress_id: 538
layout: post
title: mysql and XML output
excerpt: So...  How many of you have ever used mysql -X?
wordpress_url: http://www.decafbad.com/blog/?p=538
---
So...  How many of you have ever used `mysql -X`?

I just discovered it today, while screwing around with dumping database queries into Atom.  While I'm not entirely sure it's what I need to use, this is pretty nifty:

    $ mysql -Xp -udbagg3 dbagg3 -e '
    > select id, title, modified 
    > from feed
    > order by modified 
    > limit 4' 
    Enter password:
 
    <?xml version="1.0"?>

    <resultset statement="select id, title, modified 
            from feed order by modified limit 4">
      <row>
        <id>527</id>
        <title>Channel Dean</title>
        <modified>2004-03-04 15:56:54</modified>
      </row>

      <row>
        <id>31</id>
        <title>chocolate and vodka</title>
        <modified>2004-07-21 21:30:08</modified>
      </row>

      <row>
        <id>183</id>
        <title>floating atoll</title>
        <modified>2004-07-31 14:09:27</modified>
      </row>
 
      <row>
        <id>24</id>
        <title>What's Your Brand Mantra?</title>
        <modified>2004-08-02 03:15:03</modified>
      </row>
    </resultset>    

Now, while I don't think that using this for `dbagg3` is all that great an idea, it's something I need to remember for future shell and XSLT hacks...
