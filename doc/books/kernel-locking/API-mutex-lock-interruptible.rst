.. -*- coding: utf-8; mode: rst -*-

.. _API-mutex-lock-interruptible:

========================
mutex_lock_interruptible
========================

*man mutex_lock_interruptible(9)*

*4.6.0-rc5*

acquire the mutex, interruptible


Synopsis
========

.. c:function:: int __sched mutex_lock_interruptible( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be acquired


Description
===========

Lock the mutex like ``mutex_lock``, and return 0 if the mutex has been
acquired or sleep until the mutex becomes available. If a signal arrives
while waiting for the lock then this function returns -EINTR.

This function is similar to (but not equivalent to)
``down_interruptible``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
