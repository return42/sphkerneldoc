.. -*- coding: utf-8; mode: rst -*-

.. _API-mod-timer:

=========
mod_timer
=========

*man mod_timer(9)*

*4.6.0-rc5*

modify a timer's timeout


Synopsis
========

.. c:function:: int mod_timer( struct timer_list * timer, unsigned long expires )

Arguments
=========

``timer``
    the timer to be modified

``expires``
    new timeout in jiffies


Description
===========

``mod_timer`` is a more efficient way to update the expire field of an
active timer (if the timer is inactive it will be activated)

mod_timer(timer, expires) is equivalent to:

del_timer(timer); timer->expires = expires; add_timer(timer);

Note that if there are multiple unserialized concurrent users of the
same timer, then ``mod_timer`` is the only safe way to modify the
timeout, since ``add_timer`` cannot modify an already running timer.

The function returns whether it has modified a pending timer or not.
(ie. ``mod_timer`` of an inactive timer returns 0, ``mod_timer`` of an
active timer returns 1.)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
