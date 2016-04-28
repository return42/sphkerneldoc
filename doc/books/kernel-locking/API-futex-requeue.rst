.. -*- coding: utf-8; mode: rst -*-

.. _API-futex-requeue:

=============
futex_requeue
=============

*man futex_requeue(9)*

*4.6.0-rc5*

Requeue waiters from uaddr1 to uaddr2


Synopsis
========

.. c:function:: int futex_requeue( u32 __user * uaddr1, unsigned int flags, u32 __user * uaddr2, int nr_wake, int nr_requeue, u32 * cmpval, int requeue_pi )

Arguments
=========

``uaddr1``
    source futex user address

``flags``
    futex flags (FLAGS_SHARED, etc.)

``uaddr2``
    target futex user address

``nr_wake``
    number of waiters to wake (must be 1 for requeue_pi)

``nr_requeue``
    number of waiters to requeue (0-INT_MAX)

``cmpval``
    ``uaddr1`` expected value (or ``NULL``)

``requeue_pi``
    if we are attempting to requeue from a non-pi futex to a pi futex
    (pi to pi requeue is not supported)


Description
===========

Requeue waiters on uaddr1 to uaddr2. In the requeue_pi case, try to
acquire uaddr2 atomically on behalf of the top waiter.


Return
======

>=0 - on success, the number of tasks requeued or woken; <0 - on error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
