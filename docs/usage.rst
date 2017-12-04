.. _usage:

Usage
=====

Integrating `pinax-points` into your project is just a matter of using a couple of
template tags and wiring up a bit of javascript. 

Firstly, add load the template tags for `pinax-points`::

    {% load pinax_points_tags %}


Then, if you want to display an overall points for an object you can set
a context variable and display it::

    {% points_for_object user as points %}

    <div class="points">{{ points }}</div>

This displays overall points for the user.

You can specify any object here instead of user that you want to display points for.
For example if you want to display points for a post object::
    
    {% points_for_object post as points %}

    <div class="post-points">{{ points }}</div>
