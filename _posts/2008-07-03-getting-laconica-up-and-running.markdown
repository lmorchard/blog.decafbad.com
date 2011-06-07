--- 
wordpress_id: 1167
layout: post
title: Getting Laconica up and running
wordpress_url: http://decafbad.com/blog/?p=1167
---
*Update, 30 Sep 2008*: 

**You don't want to follow the directions on this page—instead, leave this page and read this:**  

[http://laconi.ca/darcs/README](http://laconi.ca/darcs/README)

At one point, very early on in Laconica-time, this blog post offered useful information on getting Laconica up and running.  But since then, my time has taken me away from playing with Laconica and thus this guide has fallen far behind.  Hopefully soon I'll get back around to Laconica hacking, but not today.

I'm leaving the original text of this post here for posterity, but this is *no longer current* and following this guide will *do more harm than good* in confusing you about Laconica installation!

**Again, to learn about getting Laconica up and running, leave this page and read this**:

[http://laconi.ca/darcs/README](http://laconi.ca/darcs/README)

---

The latest mini-sensations to arrive through my firehoses are [identi.ca](http://identi.ca), a Twitter-clone / microblogging site, and the Open Source software [Laconica][], which powers the aforementioned site.

Having started and neglected two Twitter cloning attempts of my own, [Cuckoo](http://decafbad.com/svn/trunk/Cuckoo) and [OpenInterocitor](http://decafbad.com/svn/trunk/OpenInterocitor), seeing someone else carry the torch with any modicum of momentum is attractive to me.  So, I spent a little bit last night getting the code running on my own servers, and managed to do it twice:

* [decafbad.com/laconica](http://decafbad.com/laconica)
* [lmorchard.com/laconica](http://lmorchard.com/laconica)

See, the interesting thing promised by [Laconica][]—and something I wanted in my own clones—is the ability to federate instances of the software.  That is, users on one [Laconica][]-based site should be able to subscribe to the updates from users on another site, by way of the [OpenMicroblogging specification][openmu].  Although federation isn't a silver bullet to a web-scale Twitter clone, I do think it's one of the most important bootstrap steps—but that's another blog post entirely.

Thus, since I'd like to see *you* run a Laconica site (or something like it) for mine to talk to, I figured I'd document how I got the thing running.  My server is running Ubuntu Gutsy, so your mileage may vary.  This is a long one, so check out the how-to after the jump...

[lighttpd]: http://www.lighttpd.net/
[openmu]: http://openmicroblogging.org/
[Twitter]: http://twitter.com
[laconica]: http://laconi.ca
[source]: http://laconi.ca/Main/Source
<!--more-->

## Get the Laconica code

I got my copy of the code by using [`darcs`](http://darcs.net/), as described on [the Laconica source page][source], like so:

    sudo apt-get install darcs
    darcs get --partial http://laconi.ca/darcs/

But, if you can't or don't want to use `darcs` right now, you can [grab a Laconica tarball](http://laconi.ca/laconica-0.4.1.tar.gz) to get started.

## Get modules and third-party prerequisites

I had already installed PHP and Apache, along with lighttpd, on my server.  But, I found I needed a few more things.  So, here's a slew of packages you may or may not already have:

    sudo apt-get install libapache2-mod-php5 php5-cgi php5-cli php-pear php5-gd php5-mysql

Next, now that you've got PHP and PEAR, you can install some of the PEAR-based prerequisites:

    sudo pear channel-update pear.php.net
    sudo pear install channel://pear.php.net/Validate-0.8.1
    sudo pear install DB_DataObject
    sudo pear install Mail
    sudo pear install Net_SMTP

After this, there are a few libraries that need to be downloaded by hand.  For this, I created an `extlib/` directory to keep them in, separate from Laconica's own `lib/` which will be subject to updates to the software itself:

    mkdir extlib xfers
    cd xfers
    curl -O http://openidenabled.com/files/php-openid/packages/php-openid-2.1.1.zip    
    curl -O http://michelf.com/docs/projets/php-markdown-1.0.1m.zip
    curl -O http://oauth.googlecode.com/svn/code/php/OAuth.php
    curl -O http://xmpphp.googlecode.com/files/xmpphp-0.1beta-r21.tar.gz
    unzip php-markdown-1.0.1m.zip
    cp 'PHP Markdown 1.0.1m/markdown.php' ../extlib/
    unzip php-openid-2.1.1.zip
    cp -r php-openid-2.1.1/Auth ../extlib/
    cp OAuth.php ../extlib/
    tar -zxf xmpphp-0.1beta-r21.tar.gz
    cp xmpphp/*.php ../extlib/
    cd ..
    rm -rf xfers

## Set up MySQL tables

I'll assume you already have MySQL installed.  To set up a database for Laconica, I did the following:

    mysql -uroot -p -e 'create database laconica';
    mysql -uroot -p -e "grant all privileges on laconica.* to laconica@localhost identified by 'PASSWORD'";
    mysql -uroot -p laconica < db/laconica.sql

## Configure Laconica

So far, I've found at least two config files that need tweaking—namely `config.php` and `dataobject.ini`.

The first thing I did to `config.php` was to add the following at around line 6 to account for my `extlib/` directory:


    #If you have downloaded libraries in random little places, you
    #can add the paths here
    define('INSTALLDIR', dirname(__FILE__));
    set_include_path(get_include_path() . PATH_SEPARATOR . INSTALLDIR . '/extlib');

The rest of the settings in `config.php` are somewhat self-explanatory.  These are the ones I changed for my installation:

    $config['site']['name'] = 'cafeonica';
    $config['site']['server'] = 'decafbad.com';
    $config['site']['path'] = 'laconica';
    $config['site']['fancy'] = true;
    $config['site']['theme'] = 'stoica';
    $config['site']['email'] = 'l.m.orchard@pobox.com';
    $config['site']['broughtby'] = '0xDECAFBAD';
    $config['site']['broughtbyurl'] = 'http://decafbad.com/';
    $config['db']['database'] = 'mysql://laconica:PASSWORD@localhost/laconica';
    $config['db']['ini_laconica'] = $config['db']['schema_location'].'/stoica.ini';

After this, I tweaked the first few settings of `dataobject.ini` to the following: 

    database = mysql://laconica:PASSWORD@localhost/laconica 
    schema_location = /www/decafbad.com/docs/laconica/classes 
    class_location = /www/decafbad.com/docs/laconica/classes 
    require_prefix = /www/decafbad.com/docs/laconica/classes/ 

Be sure to substitute your own web server paths and passwords in all the above.  And finally, in order to allow the upload of avatar images, you'll need to tweak the permissions on the `avatar/` directory, like so:

    sudo chown -R www-data avatar
    sudo chmod -R ug+rw avatar/

## Configure Web Server

There isn't really much to configure if you're using Apache.  There's a file `htaccess.sample` that needs to be copied to `.htaccess`—this will put in place all the `mod_rewrite` rules necessary to support "fancy" URLs.

On the other hand, if you're okay with uglier URLs with query parameters and whatnot, leave `.htaccess` alone and use `$config['site']['fancy'] = false` in your `config.php`.  

For comparison, here are examples of non-fancy and fancy profile URLs:

* http://decafbad.com/laconica/index.php?action=showstream&nickname=lmorchard
* http://decafbad.com/laconica/lmorchard

One catch to the non-fancy and fancy thing, though—if you start off with non-fancy URLs and later switch to fancy, all of the profiles registered before that switch will appear with non-fancy URLs in the timeline.  This is because the `profile` table stores the original URLs at registration in the `profileurl` column.  You could change these if you like, but there be dragons.

### Configure Lighttpd for "fancy" URLs (optional)

If you're like me, though, you're using something other than Apache for your main web server.  Personally, I just got up and running with [lighttpd][] not too long ago.  Alas, that means the `.htaccess` rewrite rules won't work directly.  

Admittedly, I am a novice to configuring [lighttpd][], so the following rules I added to my config could probably use some help:

    url.rewrite-final += (
        "^/laconica/index.php(.*)$" => "$0",

        "^/laconica/$" => "/laconica/index.php?action=public",
        "^/laconica/rss$" => "/laconica/index.php?action=publicrss",
        "^/laconica/xrds$" => "/laconica/index.php?action=publicxrds",

        "^/laconica/doc/about$" => "/laconica/index.php?action=doc&title=about",
        "^/laconica/doc/contact$" => "/laconica/index.php?action=doc&title=contact",
        "^/laconica/doc/faq$" => "/laconica/index.php?action=doc&title=faq",
        "^/laconica/doc/help$" => "/laconica/index.php?action=doc&title=help",
        "^/laconica/doc/im$" => "/laconica/index.php?action=doc&title=im",
        "^/laconica/doc/openid$" => "/laconica/index.php?action=doc&title=openid",
        "^/laconica/doc/openmublog$" => "/laconica/index.php?action=doc&title=openmublog",
        "^/laconica/doc/privacy$" => "/laconica/index.php?action=doc&title=privacy",
        "^/laconica/doc/source$" => "/laconica/index.php?action=doc&title=source",

        "^/laconica/main/login$" => "/laconica/index.php?action=login",
        "^/laconica/main/logout$" => "/laconica/index.php?action=logout",
        "^/laconica/main/register$" => "/laconica/index.php?action=register",
        "^/laconica/main/openid(?:\?(.*)|$)$" => "/laconica/index.php?action=openidlogin&$1",
        "^/laconica/main/remote(?:\?(.*)|$)$" => "/laconica/index.php?action=remotesubscribe&$1",

        "^/laconica/main/subscribe$" => "/laconica/index.php?action=subscribe",
        "^/laconica/main/unsubscribe$" => "/laconica/index.php?action=unsubscribe",
        "^/laconica/main/confirmaddress$" => "/laconica/index.php?action=confirmaddress",
        "^/laconica/main/confirmaddress/(.*)$" => "/laconica/index.php?action=confirmaddress&code=$1",
        "^/laconica/main/recoverpassword$" => "/laconica/index.php?action=recoverpassword",
        "^/laconica/main/recoverpassword/(.*)$" => "/laconica/index.php?action=recoverpassword&code=$1",

        "^/laconica/settings/avatar$" => "/laconica/index.php?action=avatar",
        "^/laconica/settings/password$" => "/laconica/index.php?action=password",
        "^/laconica/settings/profile$" => "/laconica/index.php?action=profilesettings",
        "^/laconica/settings/openid$" => "/laconica/index.php?action=openidsettings",
        "^/laconica/settings/im$" => "/laconica/index.php?action=imsettings",

        "^/laconica/notice/new$" => "/laconica/index.php?action=newnotice",
        "^/laconica/notice/(\d+)$" => "/laconica/index.php?action=shownotice&notice=$1",

        "^/laconica/user/(\d+)$" => "/laconica/index.php?action=userbyid&id=$1",

        "^/laconica/(\w+)/subscriptions$" => "/laconica/index.php?action=subscriptions&nickname=$1",
        "^/laconica/(\w+)/subscribers$" => "/laconica/index.php?action=subscribers&nickname=$1",
        "^/laconica/(\w+)/xrds$" => "/laconica/index.php?action=xrds&nickname=$1",
        "^/laconica/(\w+)/rss$" => "/laconica/index.php?action=userrss&nickname=$1",
        "^/laconica/(\w+)/all$" => "/laconica/index.php?action=all&nickname=$1",
        "^/laconica/(\w+)/all/rss$" => "/laconica/index.php?action=allrss&nickname=$1",
        "^/laconica/(\w+)/foaf$" => "/laconica/index.php?action=foaf&nickname=$1",

        "^/laconica/(\w+)$" => "/laconica/index.php?action=showstream&nickname=$1"
    )

## That's it (for now)

And that's all I've got for you for now.  At this point, it looks like my two Laconica installs are mostly working.  I've not yet played with the XMPP bot, nor have I been able to see the [OpenMicroblogging][openmu] stuff working with remore subscriptions.  However, I have been able to log in via OpenID, so that's something.
