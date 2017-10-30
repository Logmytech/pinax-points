Below is some of the usage information of template tags extracted from https://github.com/pinax/pinax-points/blob/master/pinax/points/templatetags/pinax_points_tags.py


```
   Usage::
        {% top_objects "auth.User" as top_users limit 10 %}
    or::
        {% top_objects "auth.User" as top_users %}
    or::
        {% top_objects "auth.User" as top_users limit 10 timeframe 7 days %}
    All variations return a queryset of the model passed in with points annotated.
```

```
        Gets the current points for an object, usage:
        {% points_for_object user %}
    or
        {% points_for_object user as points %}
    or
        {% points_for_object user limit 7 days as points %}
        
 ```
 
 ```
    Usage::
        {% user_has_voted user obj as var %}
```
