--- 
wordpress_id: 413
layout: post
title: Getting a Strange "Component Manager" Message Under OS X?
wordpress_url: http://www.decafbad.com/blog/?p=413
---
Posting this just in case anyone needs it.  I've been getting the
following strange message lately in logs and consoles under OS X:
<blockquote><pre>## Component Manager: attempting to find symbols in a component alias of type (regR/carP/x!bt)</pre></blockquote>
<br /><br />
As it turns out, I had just installed Toast.  A quick Google search
leads me to <a href="http://www.mail-archive.com/cocoa-dev@lists.apple.com/msg09330.html" target="_top">blame Toast and remove a QuickTime component supporting Video CD</a>.
That's pretty obscure.  Hmph.  So much for never again worrying about strange drivers and
cryptic error messages under OS X.  :)
<!--more-->
shortname=strange_component_error
