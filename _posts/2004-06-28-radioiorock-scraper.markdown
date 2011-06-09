--- 
wordpress_id: 531
layout: post
title: A mini-scraper for the playlist at radioio Rock
excerpt: Lately, my iTunes has been playing radioio Rock almost exclusively lately, but one thing that peeves me is that I don't seem to see the current song while the stream's playing.  Instead, the radioio site offers a pop-up window that displays the last few songs in the playlist.  However, I'm usually somewhere off in another window or a shell and don't really feel like popping over to a browser and navigating to the playlist just to see what this song is.  So, I wrote myself a little mini-scraper script...
date: "2004-06-28T19:17:36-04:00"
tags: 
- hacks
wordpress_slug: radioiorock-scraper
wordpress_url: http://www.decafbad.com/blog/?p=531
---
Lately, my iTunes has been playing [radioio Rock][rock] almost exclusively lately, but one thing that peeves me is that I don't seem to see the current song while the stream's playing.  Instead, the [radioio][radioio] site offers a pop-up window that displays the last few songs in the playlist.  However, I'm usually somewhere off in another window or a shell and don't really feel like popping over to a browser and navigating to the playlist just to see what this song is.

So, I wrote myself a little mini-scraper script:

    #!/bin/sh
    
    curl -s 'http://player.radioio.com/player.php?b=614&#38;stream=radioioRock' | \
        tidy -asxml --wrap 300 -q -f /dev/null | \
        xml sel -t -m "//*[@class='leadrock']" -v '.' -n \
            -o '    [http://www.radioio.com' -v '../@href' -o ']' -n 

The output looks something like this:

    [06/29 11:01:08] deusx@Caffeina2:~ % radioio
    
    Vast - I Need To Say Goodbye
        [http://www.radioio.com...]
    Cure - The End Of The World
        [http://www.radioio.com...]
    Seachange - Avs Co 10
        [http://www.radioio.com...]
    Pixies - Bam Thwok
        [http://www.radioio.com...]
    Death Cab For Cutie - The New Year
        [http://www.radioio.com...]
    Lovethugs - Drawing The Curtains
        [http://www.radioio.com...]

Oh yeah, and to run this script, you will need these tools:

* [curl][curl]
* [HTML Tidy][tidy] 
* [XMLStarlet][xmlstarlet]

Personally, I like the included URLs (which I edited here for length) since they launch a search for CDs by the artist.  However, you can cut the output down to just the artist/title by removing the final line of the script and the backslash at the end of the line before.

If you like a different [radioio][radioio] station, say [radioio Eclectic][eclectic], you can change `stream=radioioRock` to `stream=radioioEclectic` in the URL above and change `class='leadrock'` to `class='leadeclectic'`.  I could have parameterized these, but I'm lazy, and that was the whole point!

ShareAndEnjoy!

[curl]: http://curl.haxx.se/
[tidy]: http://tidy.sourceforge.net/
[xmlstarlet]: http://xmlstar.sourceforge.net/
[rock]: http://www.radioio.com/radioiorock.php?stream=radioioRock
[radioio]: http://www.radioio.com/
[eclectic]: http://www.radioio.com/radioioeclectic.php?stream=radioioEclectic
<!--more-->
shortname=radioiorock_scraper
