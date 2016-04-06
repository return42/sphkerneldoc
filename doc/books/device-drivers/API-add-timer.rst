
.. _API-add-timer:

=========
add_timer
=========

*man add_timer(9)*

*4.6.0-rc1*

start a timer


Synopsis
========

.. c:function:: void add_timer( struct timer_list * timer )

Arguments
=========

``timer``
    the timer to be added


Description
===========

The kernel will do a ->function(->data) callback from the timer interrupt at the ->expires point in the future. The current time is 'jiffies'.

The timer's ->expires, ->function (and if the handler uses it, ->data) fields must be set prior calling this function.

Timers with an ->expires field in the past will be executed in the next timer tick.
