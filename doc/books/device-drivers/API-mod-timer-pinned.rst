
.. _API-mod-timer-pinned:

================
mod_timer_pinned
================

*man mod_timer_pinned(9)*

*4.6.0-rc1*

modify a timer's timeout


Synopsis
========

.. c:function:: int mod_timer_pinned( struct timer_list * timer, unsigned long expires )

Arguments
=========

``timer``
    the timer to be modified

``expires``
    new timeout in jiffies


Description
===========

``mod_timer_pinned`` is a way to update the expire field of an active timer (if the timer is inactive it will be activated) and to ensure that the timer is scheduled on the current
CPU.

Note that this does not prevent the timer from being migrated when the current CPU goes offline. If this is a problem for you, use CPU-hotplug notifiers to handle it correctly, for
example, cancelling the timer when the corresponding CPU goes offline.

mod_timer_pinned(timer, expires) is equivalent to:

del_timer(timer); timer->expires = expires; add_timer(timer);
