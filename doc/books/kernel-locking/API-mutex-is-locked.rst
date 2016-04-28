.. -*- coding: utf-8; mode: rst -*-

.. _API-mutex-is-locked:

===============
mutex_is_locked
===============

*man mutex_is_locked(9)*

*4.6.0-rc5*

is the mutex locked


Synopsis
========

.. c:function:: int mutex_is_locked( struct mutex * lock )

Arguments
=========

``lock``
    the mutex to be queried


Description
===========

Returns 1 if the mutex is locked, 0 if unlocked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
