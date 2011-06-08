--- 
wordpress_id: 1793
layout: post
title: HTML5 drag and drop in Firefox 3.5
tags: 
- webdev
- firefox
- js
- outliners
- outlining
- javascript
- dhtml
- eventdelegation
- entries
- mozilla
- draganddrop
wordpress_slug: html5-drag-and-drop
wordpress_date: "2009-07-15T21:26:40-04:00"
wordpress_url: http://decafbad.com/blog/?p=1793
---
<p><i>
Oh hey, look! It's another blog post—and this one
<a href="http://hacks.mozilla.org/2009/07/html5-drag-and-drop/">is cross-posted on hacks.mozilla.com</a>.
I won't say this is the start of a renewed blogging habit, but let's see what happens.
</i></p>

<style type="text/css">
dl { margin-left: 2em; }
dd { margin-left: 2em; margin-bottom: 0.25em; }
</style>
<div id="introduction">
    <p>
        Drag and drop is one of the most fundamental interactions
        afforded by graphical user interfaces.  In one gesture, it
        allows users to pair the selection of an object with the
        execution of an action, often including a second object in the
        operation.  It's a simple yet powerful UI concept used to
        support copying, list reordering, deletion (ala the Trash / Recycle Bin),
        and even the creation of link relationships.
    </p><p>
        Since it's so fundamental, offering drag and drop in web
        applications has been a no-brainer ever since browsers first
        offered mouse events in DHTML.  But, although
        <code>mousedown</code>, <code>mousemove</code>, and
        <code>mouseup</code> made it possible, the implementation has been
        limited to the bounds of the browser window.  Additionally,
        since these events refer only to the object being dragged,
        there's a challenge to find the subject of the drop when
        the interaction is completed.
    </p><p>

        Of course, that doesn't prevent most modern JavaScript
        frameworks from abstracting away most of the problems and
        throwing in some flourishes while they're at it.  But, wouldn't
        it be nice if browsers offered first-class support for drag and
        drop, and maybe even extended it beyond the window sandbox?
    </p><p>
        As it turns out, this very wish is answered by the HTML 5 specification 
        <a target="_new" href="http://www.whatwg.org/specs/web-apps/current-work/multipage/editing.html#dnd">section on new drag-and-drop events</a>, and 
        <a target="_new" href="https://developer.mozilla.org/En/DragDrop/Drag_and_Drop">Firefox 3.5 includes an implementation</a> of those events.
    </p><p>
        If you want to jump straight to the code, I've put together 
        <a target="_new" target="_new" target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html">some simple demos</a> 
        of the new events.  
    </p><p>

        I've even scratched an itch of my own and
        built <a target="_new" target="_new" target="_new" href="http://decafbad.com/2009/07/drag-and-drop/outline.html">the beginnings of an outline editor</a>,
        where every draggable element is also a drop target—of which
        there could be dozens to hundreds in a complex document, something
        that gave me some minor hair-tearing moments in the past
        while trying to make do with plain old mouse events.
    </p><p>
        And, all the above can be downloaded or cloned from 
        <a href="http://github.com/lmorchard/fx35-drag-and-drop">a GitHub repository</a>
        I've created especially for this article—which continues after the jump.
    </p>
</div>

<!--more-->

<div id="events">

    <h2>The New Drag and Drop Events</h2>
    <p>
        So, with no further ado, here are the new drag and drop events,
        in roughly the order you might expect to see them fired:
    </p>
    <dl>
        <dt><code>dragstart</code></dt>
        <dd>
            A drag has been initiated, with the dragged element as the
            event target.
        </dd>

        <dt><code>drag</code></dt>
        <dd>
            The mouse has moved, with the dragged element as the event target.
        </dd>
        <dt><code>dragenter</code></dt>
        <dd>
            The dragged element has been moved into a drop listener,
            with the drop listener element as the event target.
        </dd>
        <dt><code>dragover</code></dt>

        <dd>
            The dragged element has been moved over a drop listener,
            with the drop listener element as the event target.  Since
            the default behavior is to cancel drops, returning
            <code>false</code> or calling <code>preventDefault()</code> in
            the event handler indicates that a drop is allowed here.
        </dd>
        <dt><code>dragleave</code></dt>
        <dd>
            The dragged element has been moved out of a drop listener,
            with the drop listener element as the event target.
        </dd>

        <dt><code>drop</code></dt>
        <dd>
            The dragged element has been successfully dropped on a drop
            listener, with the drop listener element as the event
            target.
        </dd>
        <dt><code>dragend</code></dt>
        <dd>
            A drag has been ended, successfully or not, with the
            dragged element as the event target.
        </dd>
    </dl>

    <p>
        Like the mouse events of yore, listeners can be attached to
        elements using <code>addEventListener()</code> 
        directly or by way of your favorite JS library.  
    </p><p>
        Consider the following example using jQuery, 
        <a target="_new" target="_new" target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html#newschool">also available as a live demo</a>:
    </p>
    <pre lang="javascript" line="1">
<div id="newschool">
    <div class="dragme">Drag me!</div>
    <div class="drophere">Drop here!</div>
</div>

<script type="text/javascript">
    $(document).ready(function() {
        $('#newschool .dragme')
            .attr('draggable', 'true')
            .bind('dragstart', function(ev) {
                var dt = ev.originalEvent.dataTransfer;
                dt.setData("Text", "Dropped in zone!");
                return true;
            })
            .bind('dragend', function(ev) {
                return false;
            });
        $('#newschool .drophere')
            .bind('dragenter', function(ev) {
                $(ev.target).addClass('dragover');
                return false;
            })
            .bind('dragleave', function(ev) {
                $(ev.target).removeClass('dragover');
                return false;
            })
            .bind('dragover', function(ev) {
                return false;
            })
            .bind('drop', function(ev) {
                var dt = ev.originalEvent.dataTransfer;
                alert(dt.getData('Text'));
                return false;
            });
    });
</script>
    </pre>
    <p>
        Thanks to the new events and jQuery, this example is both short
        and simple—but it packs in a lot of functionality, as the rest
        of this article will explain.  
    </p><p>
        Before moving on, there are at least three things about the above
        code that are worth mentioning:
    </p>
    <ul>
        <li>

            <p>
                Drop targets are enabled by virtue of having
                listeners for drop events.  But, 
                <a target="_new" href="http://www.whatwg.org/specs/web-apps/current-work/multipage/editing.html#drag-and-drop-processing-model">per the HTML 5 spec</a>,
                draggable elements need an
                attribute of <code>draggable="true"</code>, set either in
                markup or in JavaScript.  
            </p>
            <p>
                Thus, <code>$('#newschool&nbsp;.dragme').attr('draggable', 'true')</code>.
            </p>

        </li>
        <li>
            <p>
                The original DOM event (as opposed to jQuery's event
                wrapper) offers a property called <code>dataTransfer</code>.
                Beyond just manipulating elements, the new drag and drop
                events accomodate the transmission of user-definable data
                during the course of the interaction.  
            </p>
        </li>
        <li>
            <p>

                Since these are first-class events, you can apply 
                <a target="_new" href="http://icant.co.uk/sandbox/eventdelegation/">the technique of Event Delegation</a>.
            </p><p>
                What's that?  Well, imagine you have a list of 1000
                list items—as part of a deeply-nested outline document,
                for instance.  Rather than needing to attach listeners
                or otherwise fiddle with all 1000 items, simply attach
                a listener to the parent node (eg. the
                <code><ul></code> element) and all events from
                the children will propagate up to the single parent listener.
                As a bonus, all new child elements added after page
                load will enjoy the same benefits.
            </p><p>
                <a target="_new" target="_new" target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html#delegated">Check out this demo</a>, 
                and 
                <a target="_new" target="_new" href="http://decafbad.com/2009/07/drag-and-drop/js/drag-delegated.js">the associated JS code</a> 
                to see more about these events and Event Delegation.
            </p>

        </li>
    </ul>
</div>

<div id="datatransfer">
    <h2>Using dataTransfer</h2>
    <p>
        As mentioned in the last section, the new drag and drop events
        let you send data along with a dragged element.  But, it's even
        better than that:  Your drop targets can receive data
        transferred by content objects dragged into the window from 
        other browser windows, and even <i>other applications</i>.
    </p><p>

        Since the example is a bit longer,  
        <a target="_new" target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html#data_transfer">check out the live demo</a>
        and 
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/js/drag-datatransfer.js">associated code</a>
        to get an idea of what's possible with <code>dataTransfer</code>.
    </p><p>
        In a nutshell, the stars of this show are the
        <code>setData()</code> and <code>getData()</code> methods of
        the <code>dataTransfer</code> property exposed by the Event object.
    </p>

    <p>
        The <code>setData()</code> method is typically called in the 
        <code>dragstart</code> listener, loading <code>dataTransfer</code>
        up with one or more strings of content with associated
        <a href="https://developer.mozilla.org/En/DragDrop/Recommended_Drag_Types#link">recommended content types</a>.
    </p>

    <p>
        For illustration, here's a quick snippet from the example code:
    </p>
    <pre lang="javascript" line="1">
var dt = ev.originalEvent.dataTransfer;    
dt.setData('text/plain', $('#logo').parent().text());
dt.setData('text/html', $('#logo').parent().html());
dt.setData('text/uri-list', $('#logo')[0].src);
    </pre>
    </p><p>
        On the other end, <code>getData()</code> allows you to query
        for content by type (eg. <code>text/html</code> followed by
        <code>text/plain</code>).  This, in turn, allows you to decide
        on acceptable content types at the time of the
        <code>drop</code> event or even during <code>dragover</code>

        to offer feedback for unacceptable types during the drag.
    </p><p>
        Here's another example from the receiving end of the example code:
    </p>
    <pre lang="javascript" line="1">
var dt = ev.originalEvent.dataTransfer;    
$('.content_url .content').text(dt.getData('text/uri-list'));
$('.content_text .content').text(dt.getData('text/plain'));
$('.content_html .content').html(dt.getData('text/html'));
    </pre>
    <p>
        Where <code>dataTransfer</code> really shines, though, is that
        it allows your drop targets to receive content from 
        sources outside your defined draggable elements and even from
        outside the browser altogether.  Firefox accepts such drags, 
        and attempts to populate <code>dataTransfer</code> with
        appropriate content types extracted from the external object.
    </p><p>

        Thus, you could select some text in a word processor window and
        drop it into one of your elements, and at least expect to find
        it available as <code>text/plain</code> content.  
    </p><p>
        You can also select content in 
        another browser window, and expect to see <code>text/html</code>
        appear in your events.  Check out the 
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/outline.html">outline editing demo</a>
        and see what happens when you try dragging various elements 
        (eg. images, tables, and lists) and highlighted content from
        other windows onto the items there.
    </p>

</div>

<div id="dragfeedback">
    <h2>Using Drag Feedback Images</h2>
    <p>
       An important aspect of the drag and drop interaction is a
       representation of the thing being dragged.  By default in
       Firefox, this is a "ghost" image of the dragged element itself.  But,
       the <code>dataTransfer</code> property of the original Event
       object exposes the method <code>setDragImage()</code> for use
       in customizing this representation.
    </p><p>

        There's
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html#feedback_image">a live demo</a> of this feature, as well as
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/js/drag-feedback-images.js">associated JS code</a> 
        available.  The gist, however, is sketched out in these code snippets:
    </p>
    <pre lang="javascript" line="1">
var dt = ev.originalEvent.dataTransfer;    

dt.setDragImage( $('#feedback_image h2')[0], 0, 0);

dt.setDragImage( $('#logo')[0], 32, 32); 

var canvas = document.createElement("canvas");
canvas.width = canvas.height = 50;

var ctx = canvas.getContext("2d");
ctx.lineWidth = 8;
ctx.moveTo(25,0);
ctx.lineTo(50, 50);
ctx.lineTo(0, 50);
ctx.lineTo(25, 0);
ctx.stroke();

dt.setDragImage(canvas, 25, 25);
    </pre>
    <p>
        You can supply a DOM node as the first parameter to 
        <code>setDragImage()</code>, which includes everything from
        text to images to <code>canvas</code> elements.  The
        second two parameters indicate at what left and top offset
        the mouse should appear in the image while dragging.
    </p><p>

        For example, since the <code>#logo</code> image is 64x64,
        the parameters in the second <code>setDragImage()</code>
        method places the mouse right in the center of the image.
        On the other hand, the first call positions the feedback
        image such that the mouse rests in the upper left corner.
    </p><p>
    </p>
</div>

<div id="dragfeedback">

    <h2>Using Drop Effects</h2>
    <p>
        As mentioned at the start of this article, the drag and drop
        interaction has been used to support actions such as copying,
        moving, and linking.  Accordingly, the HTML 5 specification 
        accomodates these operations in the form of the 
        <code>effectAllowed</code> and <code>dropEffect</code>
        properties exposed by the Event object.
    </p>
    <p>

        For a quick fix, check out the
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html#drag_effects">a live demo</a> 
        of this feature, as well as the
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/js/drag-effects.js">associated JS code</a>.
    </p><p>
        The basic idea is that the <code>dragstart</code> event
        listener can set a value for <code>effectAllowed</code> like so:
    </p>

    <pre lang="javascript" line="1">
var dt = ev.originalEvent.dataTransfer;
switch (ev.target.id) {
    case 'effectdrag0': dt.effectAllowed = 'copy'; break;
    case 'effectdrag1': dt.effectAllowed = 'move'; break;
    case 'effectdrag2': dt.effectAllowed = 'link'; break;
    case 'effectdrag3': dt.effectAllowed = 'all'; break;
    case 'effectdrag4': dt.effectAllowed = 'none'; break;
}
    </pre>
    <p>The choices available for this property include the following:</p>
    <dl> 
        <dt><code>none</code></dt><dd>no operation is permitted </dd>
        <dt><code>copy</code></dt><dd>copy only </dd>

        <dt><code>move</code></dt><dd>move only </dd>
        <dt><code>link</code></dt><dd>link only </dd>
        <dt><code>copyMove</code></dt><dd>copy or move only </dd>
        <dt><code>copyLink</code></dt><dd>copy or link only </dd>
        <dt><code>linkMove</code></dt><dd>link or move only </dd>

        <dt><code>all</code></dt><dd>copy, move, or link </dd>
    </dl>
    <p>
        On the other end, the <code>dragover</code> event listener 
        can set the value of the
        <code>dropEffect</code> property to indicate the expected effect
        invoked on a successful drop.  If the value does
        not match up with <code>effectAllowed</code>, the drop will
        be considered cancelled on completion.
    </p><p>

        In the 
        <a target="_new" href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html#drag_effects">a live demo</a>,
        you should be able to see that only elements with matching
        effects can be dropped into the appropriate drop zones.  This
        is accomplished with code like the following:
    </p>
    <pre lang="javascript" line="1">
var dt = ev.originalEvent.dataTransfer;
switch (ev.target.id) {
    case 'effectdrop0': dt.dropEffect = 'copy'; break;
    case 'effectdrop1': dt.dropEffect = 'move'; break;
    case 'effectdrop2': dt.dropEffect = 'link'; break;
    case 'effectdrop3': dt.dropEffect = 'all'; break;
    case 'effectdrop4': dt.dropEffect = 'none'; break;
}
    </pre>
    <p>
        Although the OS itself can provide some feedback, you 
        can also use these properties to update your own visible 
        feedback, both on the dragged element and on the drop zone
        itself.
    </p>

</div>

<div id="conclusion">
    <h2>Conclusion</h2>
    <p>
        The new first-class drag and drop events in HTML5 and Firefox
        make supporting this form of UI interaction simple, concise,
        and powerful in the browser.  But beyond the new simplicity of
        these events, the ability to transfer content between
        applications opens brand new avenues for web-based applications
        and collaboration with desktop software in general.
    </p><p>
    </p><p>
    </p>
</div>

