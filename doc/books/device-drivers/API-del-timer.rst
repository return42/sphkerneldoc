
.. _API-del-timer:

=========
del_timer
=========

*man del_timer(9)*

*4.6.0-rc1*

deactive a timer.


Synopsis
========

.. c:function:: int del_timer( struct timer_list * timer )

Arguments
=========

``timer``
    the timer to be deactivated


Description
===========

``del_timer`` deactivates a timer - this works on both active and inactive timers.

The function returns whether it has deactivated a pending timer or not. (ie. ``del_timer`` of an inactive timer returns 0, ``del_timer`` of an active timer returns 1.)
