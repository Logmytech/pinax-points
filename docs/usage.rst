. _usage:

Usage
=====

Integrating `pinax-points` into your project is just a matter of using a couple of
template tags and wiring up a bit of javascript. The rating form is intended
to function via AJAX and as such returns JSON.

Firstly, add load the template tags for `pinax-ratings`::

    {% load pinax_points_tags %}


Then, if you want to display an overall points for an object you can set
a context variable and display it::

    {% points_for_object user as points %}

    <div class="points">{{ points }}</div>

This displayes overall points for the user.
