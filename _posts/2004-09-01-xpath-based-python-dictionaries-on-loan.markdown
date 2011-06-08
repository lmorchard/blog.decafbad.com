--- 
wordpress_id: 544
layout: post
title: XPath based Python dictionaries, on loan
excerpt: But, while I'm in the process of wheel reinvention, how about I borrow Kimbro's idea?  I just threw together a quick class called XPathDict, based on libxml2.
tags: 
- hacks
- xml
wordpress_slug: xpath-based-python-dictionaries-on-loan
wordpress_date: "2004-09-01T06:47:41-04:00"
wordpress_url: http://www.decafbad.com/blog/?p=544
---
So [Kimbro Staken][kimbro] posted this nifty idea to build [XPath based Python dictionaries][xpathdict] to access XML data as a part of his incredibly nifty [Syncato][syncato] microcontent management system.  Eventually, I've really got to break down and get that thing built and running on my server and my laptop-- it really seems like I'm reinventing so many wheels by not basing [`dbagg3`][dbagg3] on it.

But, while I'm in the process of wheel reinvention, how about I borrow Kimbro's idea?  I just threw together [a quick class called XPathDict][myxdict], based on [libxml2][libxml2].  It works a little something like this:

    feed_xd = XPathDict(file="sample-atom.xml")
    for entry_node in feed_xd.nodes("//atom:entry"):
        entry = XPathDict(doc=entry_node.doc, node=entry_node)
        print "Title: " % entry['atom:title']
        if 'atom:author' in entry:
            print "Author: " % entry['atom:author/atom:name']

    xml = """
       <dbagg3:user xmlns="http://purl.org/atom/ns#" 
                xmlns:dbagg3="http://decafbad.com/2004/07/dbagg3/">
            <name>deusx</name>
            <email>deus_x@pobox.com</email>
            <url>http://www.decafbad.com/</url>
            <dbagg3:prefs>
                <dbagg3:pref name="foo">bar</dbagg3:pref>
            </dbagg3:prefs>
       </dbagg3:author>
    """

    map = (
        ('userName',  'a:name'),
        ('userEmail', 'a:email'),
        ('fooPref',   "dbagg3:prefs/dbagg3:pref[@name='foo']")
    )

    xd = XPathDict(xml=xml)
    xd.cd("/dbagg3:user")
    print xd.extract(map)

    #    {'userName'  : 'deusx', 
    #     'userEmail' : 'deus_x@pobox.com', 
    #     'fooPref'   : 'bar'}

There isn't any spectacular code behind all this, and the idea *was* Kimbro's, but it's working.  It's also incredibly convenient, especially with the little XML-to-dict extraction map method I whipped up.  This would take a bit more work to pry it out of its current context, such as turning the hardcoded namespaces into an option, among other things.  But, [here's the code][myxdict] for you to peruse.

(I got hooked early on subverting in-built language constructs from perl's `tie` facilities, and C++'s operator overloading.  Now I'm loving Python's [special class methods][methods].  Someday, maybe, I'll actually get down to doing some work in LISP and wrap my head around some *real* language subversion.)

Anyway, while this is neither quite [Native XML Scripting][nativexml] nor XML as [a native language construct][nativeconstruct], it's getting there.

[methods]: http://diveintopython.org/object_oriented_framework/special_class_methods2.html
[nativeconstruct]: http://www.xmldatabases.org/WK/blog/663?t=item
[nativexml]: http://dev2dev.bea.com/products/wlworkshop/articles/JSchneider_XML.jsp
[libxml2]: http://www.xmlsoft.org/
[myxdict]: http://www.decafbad.com/cvs/*checkout*/dbagg3/lib/dbagg3/xmlutils.py
[dbagg3]: http://www.decafbad.com/cvs/dbagg3/
[syncato]: http://www.syncato.org/
[kimbro]: http://www.xmldatabases.org/WK/blog
[xpathdict]: http://www.xmldatabases.org/WK/blog/1964_XPath_based_Python_Dictionaries.item
