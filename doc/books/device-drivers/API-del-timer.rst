.. -*- coding: utf-8; mode: rst -*-

.. _API-del-timer:

=========
del_timer
=========

*man del_timer(9)*

*4.6.0-rc5*

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

``del_timer`` deactivates a timer - this works on both active and
inactive timers.

The function returns whether it has deactivated a pending timer or not.
(ie. ``del_timer`` of an inactive timer returns 0, ``del_timer`` of an
active timer returns 1.)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
