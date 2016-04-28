.. -*- coding: utf-8; mode: rst -*-

.. _API-eventfd-signal:

==============
eventfd_signal
==============

*man eventfd_signal(9)*

*4.6.0-rc5*

Adds ``n`` to the eventfd counter.


Synopsis
========

.. c:function:: __u64 eventfd_signal( struct eventfd_ctx * ctx, __u64 n )

Arguments
=========

``ctx``
    [in] Pointer to the eventfd context.

``n``
    [in] Value of the counter to be added to the eventfd internal
    counter. The value cannot be negative.


Description
===========

This function is supposed to be called by the kernel in paths that do
not allow sleeping. In this function we allow the counter to reach the
ULLONG_MAX value, and we signal this as overflow condition by returning
a POLLERR to poll(2).

Returns the amount by which the counter was incremented. This will be
less than ``n`` if the counter has overflowed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
