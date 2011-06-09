--- 
wordpress_id: 1310
layout: post
title: Writing a Delicious command for Ubiquity
date: "2008-09-01T00:37:03-04:00"
tags: 
- delicious
- webdev
- javascript
- greasemonkey
- entries
- mozilla
- ubiquity
wordpress_slug: writing-a-delicious-command-for-ubiquity
wordpress_url: http://decafbad.com/blog/?p=1310
---
In my [last post][last], I got all fluffy about how cool [Ubiquity][] is but didn't share any code to prove the point.  As it happens, I have come up with at least one useful command that I'm starting to use habitually in posting bookmarks to Delicious.  You can [subscribe to my command][subs] or [check out the full source][source]—this post will serve as a dissection of the thing.  Since this will be fairly lengthy, follow along after the jump.

Oh, and it's been awhile since I posted something this in-depth around here, so feel free to let me know how this first draft works.  And, bug reports and patches are of course welcome.

[ubiquity]: http://labs.mozilla.com/2008/08/introducing-ubiquity/
[last]: http://decafbad.com/blog/2008/08/31/ubiquity-cracks-open-personal-mashup-tinkering "Ubiquity cracks open personal mashup tinkering"
[subs]: http://decafbad.com/UbiquityCommands/
[source]: http://decafbad.com/hg/UbiquityCommands/file/tip/delicious.ubiq.js

<!--more-->

To begin, consider the following code starting off the command source code:

<pre lang="javascript" line="1">
/**
 * share-on-delicious - an Ubiquity command for sharing bookmarks on
 * delicious.com
 *
 * l.m.orchard@pobox.com
 * http://decafbad.com/
 * Share and Enjoy!
 */
var uext = Application.extensions.get('ubiquity@labs.mozilla.com');

var cookie_mgr = Components.classes["@mozilla.org/cookiemanager;1"]
    .getService(Components.interfaces.nsICookieManager);
</pre>

The first thing to note here is that a short header comment introduces the command.  This isn't required, but it's a good idea.  It's also something you can't really do with bookmarklets.  On the other hand, Greasemonkey user scripts expect metadata about the script to be provided here, but Ubiquity doesn't use this convention.

Second, notice that the code accesses some chrome-level resources.  Again, this is something unavailable to bookmarklets and Greasemonkey user scripts.  Just take a look at the [FUEL library documentation][fuel] to get a quick sense of what's available using that simplified API, not to mention what's available using the lower-level browser APIs.

[fuel]: http://developer.mozilla.org/en/FUEL

Now, check out this next chunk of code, which begins the construction of an Ubiquity command:

<pre lang="javascript" line="13">
CmdUtils.CreateCommand({
    
    name:        
        'share-on-delicious',
    icon:
        'http://delicious.com/favicon.ico',
    description: 
        'Share the current page as a bookmark on delicious.com',
    help:        
        'Select text on the page to use as notes, or enter your own ' + 
        'text after the command word.  You can also assign tags to the '+ 
        'bookmark with the "tagged" modifier, and alter the bookmark ' + 
        'default page title with the "entitled" modifier.  Note that ' + 
        'you must also already be logged in at delicious.com to use ' +
        'this command.',

    homepage:   
        'http://decafbad.com',
    author: { 
        name: 'Leslie Michael Orchard', 
        email: 'l.m.orchard@pobox.com' 
    },
    license:
        'MPL/GPL/LGPL',
</pre>

Whereas Greasemonkey scripts support metadata in the header comment, the Ubiquity command script API works a little differently.  

The [`CmdUtils` module][cmdutils] provided by Ubiquity offers a `CreateCommand` function, which expects an object as a parameter.  The object literal whose construction is begun in the code above serves as a self-contained package for the command, bearing metadata describing the command as well as containing all the code necessary to implement it.

So, in the above code block, you can see the machine-readable description of the command—including a command name, display icon, home page URL, author information, and license.  The command name (`share-on-delicious`) will be used by the Ubiquity command parser, but the rest of the description will also be used in the list of commands available to the user, invoked by the `command-list` command, like so:

<img src="/2008/ubiq-share-on-delicious-list.jpg" style="border: 1px solid #333; margin: 0.25em; padding: 0.25em" />

[cmdutils]: http://hg.toolness.com/ubiquity-firefox/file/tip/ubiquity/chrome/content/cmdutils.js

Moving along, this next chunk of code introduces the first functional bits of the command:

<pre lang="javascript" line="37">
    takes: { notes: noun_arb_text },
    modifiers: { 
        tagged:  noun_arb_text,
        entitled: noun_arb_text
    },
</pre>

Like smart keyword shortcut bookmarks, Ubiquity commands accept user-supplied input.  But, what's unique to Ubiquity is that it employs a parser whose goal is to support something approximating natural language.  At present, this results in commands that support a single primary argument—declared above with the `takes` property—and any number of additional keyword modifiers—declared above by the `modifiers` property.

For the command under construction here, this establishes a pattern something like the following:

    share-on-delicious {notes} [tagged {tags} entitled {title}]

Content for the `{notes}` argument can either be typed directly by hand, or it can be supplied by text highlighted on the page.  To use highlighted text, you can either issue the command alone, or use the word `this` for the `{notes}` argument before including further modifiers.

The modifiers `tagged` and `entitled` are optional, and can be used in any order.  Each of these keywords signifies the start of a different argument—which unfortunately can collide with the literal data supplied for notes, which will hopefully be a rare occurrence.

All of this adds up command invocations including the following:

    share-on-delicious
    share-on-delicious I really like this page tagged nifty amusing
    share-on-delicious this entitled This bookmark has no tags
    sh this tagged osx software apple entitled This is good OS X software

That last example is important—since I have no other commands starting with "`sh`", I can abbreviate the full command.  Ubiquity only requires enough of a command name to disambiguate it within your collection of commands.

Another thing to note is the use of the constant value `noun_arb_text`, which declares that these arguments should expect any arbitrary text as input.  

This facility is not exploited for the present command, but Ubiquity defines [noun types][noun].  These include concepts such as plain text, dates, address book contacts, browser tabs, bookmark tags, and more.  You can define your own noun types, as well as implement suggestion schemes that help guide the user toward constructing useful input values in the command interface.  You can [read more about this][noun_tut] in the official author tutorial.

[noun]: http://hg.toolness.com/ubiquity-firefox/file/tip/ubiquity/chrome/content/nlparser/en/nountypes.js
[noun_tut]: https://wiki.mozilla.org/Labs/Ubiquity/Ubiquity_0.1_Author_Tutorial#Introduction_to_Noun_Types

Next up is a quick bit of command-specific configuration:

<pre lang="javascript" line="42">
    /**
     * Command configuration settings.
     */
    _config: {
        // Base URL for the delicious v1 API
        api_base:      'https://api.del.icio.us',

        // Domain and name of the delicious login session cookie.
        cookie_domain: '.delicious.com',
        cookie_name:   '_user'
    },
</pre>

Since this command will be posting to Delicious via the V1 API, it's handy to declare the base URL for the API in an easily changed spot.  That way, you could change this value later on to point the command at another implementation of the API.

Additionally, this command will employ a little-known authentication trick supported by the Delicious API that accepts the user's login cookie set by the Delicious website—this "cookie god" auth is used by the official Delicious addon for Firefox.  It's handy for piggybacking on the website login and removing the need to ask the user for their username and password again and possibly storing it in an insecure manner.

In fact, this next chunk of code defines a utility method to rummage through the cookie jar:

<pre lang="javascript" line="53">
    /**
     * Dig up the Delicious login session cookie.
     */
    _getUserCookie: function() {
        var iter = cookie_mgr.enumerator;
        while (iter.hasMoreElements()) {
            var cookie = iter.getNext();
            if( cookie instanceof Components.interfaces.nsICookie && 
                cookie.host.indexOf(this._config.cookie_domain) != -1 && 
                cookie.name == this._config.cookie_name) {
                return decodeURIComponent(cookie.value);
            }
        }
    },
</pre>

The method defined above, `._getUserCookie()`, uses the browser's cookie manager and the values defined in the previous configuration section to find the login session cookie set for Delicious.  Take note that this is far beyond the allowed capabilities of bookmarklets and Greasemoney user scripts—this is digging straight into the browser itself, skipping past the usual content-space security restrictions.  

In other words: In Ubiquity, *the gun is loaded* and you should be careful.  

Moving along, consider this next utility method:

<pre lang="javascript" line="67">
    /**
     * Given input data and modifiers, attempt to assemble data necessary to
     * post a bookmark.
     */
    _extractBookmarkData: function(input_obj, mods) {
        return {
            _user:
                this._getUserCookie(),
            url:
                context.focusedWindow.location,
            description:
                mods.entitled.text || context.focusedWindow.document.title,
            extended: 
                input_obj.text,
            tags:
                mods.tagged.text
        };
    },
</pre>

Named `._extractBookmarkData()`, this utility method accepts the results of Ubiquity's parser interpreting the primary argument and modifier arguments supplied by the user.  Using these data structures, it attempts to build a structure representing the fields of a Delicious bookmark.

The `_user` field is used for authentication via the site login cookie.  The `url` is set from the location bar of the current page.  The `description`, or title, field of the bookmark is taken from either the `entitled` modifier or the title of the current page.  The `tags`, if any, come from the `tagged` modifier.  And, finally, the `extended` notes for the bookmark are taken from the primary input argument of the command.

As you'll see shortly, this utility method will be used in both the preview and the execution of the command.

Next, there's one more utility method to cover:

<pre lang="javascript" line="85">
    /**
     * Given an object, build a URL query string
     */
    _buildQueryString: function(data) {
        var qs = [];
        for (k in data) if (data[k]) 
            qs.push( encodeURIComponent(k) + '=' + 
                encodeURIComponent(data[k]) );
        return qs.join('&');
    },
</pre>

In anticipation of using the Delicious V1 API, the `._buildQueryString()` method accepts an object and constructs a URL query string from the encoded properties of the object.  This will be paired with the `._extractBookmarkData()` method to supply data for API calls.

Moving along, it's time to start digging into the meat of this Ubiquity command:

<pre lang="javascript" line="95">
    /**
     * Present a preview of the bookmark under construction during the course
     * of composing the command.
     */
    preview: function(pblock, input_obj, mods) {

        var bm          = this._extractBookmarkData(input_obj, mods);
        var user_cookie = this._getUserCookie();
        var user_name   = (user_cookie) ? user_cookie.split(' ')[0] : '';

        var ns = { user_name: user_name, bm: bm };
        var tmpl;
</pre>

With this code, the implementation of command method `.preview()` has begun.  This method is used by Ubiquity to generate a live preview of the command.  Called with a DOM node (`pblock`) and partially completed command input (`input_obj` and `mods`), this method is expected to build a representation of the command's results in the DOM node.  As the user types, this method will be called over and over again, ideally offering feedback as the user composes a command.

Continuing on, consider this next chunk of code checking the validity of command input:

<pre lang="javascript" line="107">
        if (!user_name) {

            // If there's no user name, there's no login, so this command won't work. 
            tmpl = [ 
                '<p style="color: #d44">No active user found - log in at ', 
                '<img src="http://delicious.com/favicon.ico"> ',
                '<b><a style="color: #3774D0" href="http://delicious.com">delicious.com</a></b> ', 
                'to use this command.</p>'
            ].join('');

        } else if (!bm.description) {

            // If there's no title, then this is an error too.
            tmpl = [ 
                '<p style="color: #d44">A title is required for bookmarks on ', 
                '<img src="http://delicious.com/favicon.ico"> ',
                '<b><a style="color: #3774D0" href="http://delicious.com">delicious.com</a></b> ', 
                '</p>'
            ].join('');
</pre>

This chunk of code first checks for a user name, which can be extracted from a valid Delicious login cookie, if one was found.  If not found, the command will fail—so the preview built here will instruct the user to login at Delicious before going further.

The second precondition for using the command is that the bookmark has been given a title.  By default, this is the title of the current page—but, some pages don't offer titles.  So, an error needs to be flagged if the user hasn't manually supplied a title in this case.

Finally, notice in both of these error cases, a string of HTML is composed in the variable `tmpl`.  This will be used at the end of the method to populate the DOM node passed in as `pblock`.

Now, assuming that all the command's prerequisites have been met, it's time to try constructing a proper preview for the results of this command: 

<pre lang="javascript" line="126">
        } else {

            // Attempt to construct a vaguely delicious-esque preview of a bookmark.
            tmpl = [ 
                '<style type="text/css">',
                    '.preview a { color: #3774D0 }',
                    '.del-bookmark { font: 12px arial; color: #ddd; background: #eee; line-height: 1.25em }',
                    '.del-bookmark a.title { color: #1259C7 }',
                    '.del-bookmark .full-url { color: #396C9B; font-size: 12px; display: block; padding: 0.25em 0 }',
                    '.del-bookmark .notes { color: #4D4D4D }',
                    '.del-bookmark .tags { color: #787878; padding-top: 0.25em; text-align: right }',
                '</style>',
                '<div class="preview">',
                    '<p>Share a bookmark at <img src="http://delicious.com/favicon.ico"> ',
                        '<b><a href="http://delicious.com/${user_name}">delicious.com/${user_name}</a></b>:</p>',
                    '<div class="del-bookmark">',
                        '<div style="padding: 1em;">',
                        '<a class="title" href="${bm.url}">${bm.description}</a>',
                        '<a class="full-url" href="${bm.url}">${bm.url}</a>',
                        bm.extended ? 
                            '<div class="notes">${bm.extended}</div>' : '',
                        bm.tags ?
                            '<div class="tags"><span>tags:</span> ${bm.tags}</div>' : '',
                    '</div>',
                '</div>'
            ].join("\n");

        }

        pblock.innerHTML = CmdUtils.renderTemplate(tmpl, ns);
    },
</pre>

Building on the notion that previews are built in a DOM node, the code above uses both CSS and HTML to assemble a quick-and-dirty facsimile of a Delicious bookmark—which will be rendered like this:

<img src="/2008/ubiq-share-on-delicious-preview.jpg" style="border: 1px solid #333; margin: 0.25em; padding: 0.25em" />

Also note that Ubiquity provides a template engine for use in generating content—namely the [JavaScript Templates][jst] engine from the [TrimPath][] project.  This engine may eventually be replaced with another, but the notion is that Ubiquity will provide tools to more easily generate previews and more.

The conclusion of the `.preview()` method uses the template engine with a call to `CmdUtils.renderTemplate()` to inject content into the preview element by way of the `.innerHTML` property.

[jst]: http://code.google.com/p/trimpath/wiki/JavaScriptTemplates
[trimpath]: http://code.google.com/p/trimpath/wiki/TrimPath

Now that the preview is out of the way, it's time to get down to implementing the execution of the command:

<pre lang="javascript" line="157">    
    /**
     * Attempt to use the delicious v1 API to post a bookmark using the 
     * command input
     */
    execute: function(input_obj, mods) {
        var bm          = this._extractBookmarkData(input_obj, mods);
        var user_cookie = this._getUserCookie();
        var user_name   = (user_cookie) ? user_cookie.split(' ')[0] : '';

        if (!user_name) {
            // If there's no user name, there's no login, so this command won't work. 
            displayMessage('No active user found - log in at delicious.com ' +
                'to use this command.');
            return false;
        }

        if (!bm.description) {
            // If there's no title, somehow, then this is an error too.
            displayMessage("A title is required for bookmarks at delicious.com");
            return false;
        }
</pre>

Mirroring the `.preview()` method, the `.execute()` method first checks for validity of the arguments given by the user.  A missing user name or title result in a notification that the command has failed.

But, if the arguments are all valid, it's time to actually issue a request to the Delicious V1 API:

<pre lang="javascript" line="178">
        var path = '/v1/posts/add';
        var url  = this._config.api_base + path;

        var req = Components.classes["@mozilla.org/xmlextras/xmlhttprequest;1"].
            createInstance();

        req.open('POST', url, true);

        req.onload = function(ev) { 
            displayMessage('Bookmark "' + bm.description + '" ' + 
                'shared at delicious.com/' + user_name);
        }

        req.onerror = function(ev) { 
            displayMessage('ERROR: Bookmark "' + bm.description + '" ' + 
                ' NOT shared on delicious.com/' + user_name);
        }
</pre>

Using the base URL for the Delicious API declared earlier in the configuration section, the `.execute()` method constructs an API URL for the `/v1/posts/add` method.  Then, it creates an instance of `XMLHttpRequest` from the browser to be used in sending the API request.  Event handlers are registered with the object to present notifications to the user indicating whether or not the API request was successful.

At long last, it's time to wrap up this method and make the API request:

<pre lang="javascript" line="195">
        req.setRequestHeader('Authorization', 'Basic Y29va2llOmNvb2tpZQ=='); // btoa('cookie:cookie')

        var mediator = Components.classes["@mozilla.org/appshell/window-mediator;1"].
            getService(Components.interfaces.nsIWindowMediator);
        var win = mediator.getMostRecentWindow(null);
        var user_agent = win.navigator.userAgent + ";Ubiquity-share-on-delicious";

        req.setRequestHeader("User-Agent", user_agent);      

        req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        req.send(this._buildQueryString(bm));
    },

    EOF:null // I hate trailing commas
});
</pre>

The login cookie authentication supported by the Delicious V1 API is triggered by supplying a user name / password pair of `cookie`, which is done by setting the `Authorization` request header.  The login cookie is then expected to be passed in as the POST variable `_user`, which is done in the `._extractBookmarkData()` utility method.

Another bit here that shows more access of browser resources is the construction of a unique User-Agent header for this API call based on the browser's own User-Agent string, something that's suggested in the guidelines for using the Delicious API.

Finally, the `.execute()` method—and the command itself—is wrapped up with by sending off the bookmark data encoded as POST form variables with the `._buildQueryString()` utility method.

And, that's it—a command-driven Delicious browser extension in a little over 200 lines of code.  There's still more to be done to really make this thing full-featured, but I think this shows off the basic features of Ubiquity.  I'm hoping to dig in deeper and explore further, taking a look at running Greasemonkey-style code at [browser startup and page load][load], as well as playing with some more browser chrome features.  

[load]: https://wiki.mozilla.org/Labs/Ubiquity/Ubiquity_0.1_Author_Tutorial#Running_on_page_load_and_startup
