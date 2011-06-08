--- 
wordpress_id: 1224
layout: post
title: using Twitterrific with identi.ca
tags: 
- asides
- twitter
- laconica
- twitterrific
- identica
wordpress_slug: using-twitterrific-with-identica
wordpress_date: "2008-07-18T17:56:18-04:00"
wordpress_url: http://decafbad.com/blog/?p=1224
---
Since [identi.ca](http://identi.ca) [has introduced support][idapi] for the [Twitter API][tapi], switching [Twitterrific][] over seems to be as easy as entering this command in a [Terminal][] window:

    defaults write com.iconfactory.Twitterrific baseUrl -string 'identi.ca/api'

The command to switch back is the following:

    defaults write com.iconfactory.Twitterrific baseUrl -string 'twitter.com'

You'll also need to restart [Twitterrific][] after each of these to see the change working.  

It took me awhile to figure this out, because I didn't realize that they'd hidden the details in plain sight.  You know, like, in the README file that comes with the Twitterrific download.  Sheesh.  Who reads those?

[idapi]: http://www.scripting.com/stories/2008/07/18/identicaImplementsTheTwitt.html
[tapi]: http://twitter.com/help/api
[twitterrific]: http://iconfactory.com/software/twitterrific
[terminal]: http://www.osxterminal.com/launch_terminal/
