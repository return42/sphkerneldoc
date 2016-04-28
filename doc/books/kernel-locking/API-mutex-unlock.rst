.. -*- coding: utf-8; mode: rst -*-

.. _API-mutex-unlock:

============
mutex_unlock
============

*man mutex_unlock(9)*

*4.6.0-rc5*

release the mutex


Synopsis
========

.. c:function:: void __sched mutex_unlock( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be released


Description
===========

Unlock a mutex that has been locked by this task previously.

This function must not be used in interrupt context. Unlocking of a not
locked mutex is not allowed.

This function is similar to (but not equivalent to) ``up``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
