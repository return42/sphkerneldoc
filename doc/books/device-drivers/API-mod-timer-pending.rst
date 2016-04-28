.. -*- coding: utf-8; mode: rst -*-

.. _API-mod-timer-pending:

=================
mod_timer_pending
=================

*man mod_timer_pending(9)*

*4.6.0-rc5*

modify a pending timer's timeout


Synopsis
========

.. c:function:: int mod_timer_pending( struct timer_list * timer, unsigned long expires )

Arguments
=========

``timer``
    the pending timer to be modified

``expires``
    new timeout in jiffies


Description
===========

``mod_timer_pending`` is the same for pending timers as ``mod_timer``,
but will not re-activate and modify already deleted timers.

It is useful for unserialized use of timers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
