.. -*- coding: utf-8; mode: rst -*-

.. _API-init-timer-key:

==============
init_timer_key
==============

*man init_timer_key(9)*

*4.6.0-rc5*

initialize a timer


Synopsis
========

.. c:function:: void init_timer_key( struct timer_list * timer, unsigned int flags, const char * name, struct lock_class_key * key )

Arguments
=========

``timer``
    the timer to be initialized

``flags``
    timer flags

``name``
    name of the timer

``key``
    lockdep class key of the fake lock used for tracking timer sync lock
    dependencies


Description
===========

``init_timer_key`` must be done to a timer prior calling *any* of the
other timer functions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
