.. -*- coding: utf-8; mode: rst -*-

.. _API-lock-sock-fast:

==============
lock_sock_fast
==============

*man lock_sock_fast(9)*

*4.6.0-rc5*

fast version of lock_sock


Synopsis
========

.. c:function:: bool lock_sock_fast( struct sock * sk )

Arguments
=========

``sk``
    socket


Description
===========

This version should be used for very small section, where process wont
block return false if fast path is taken sk_lock.slock locked, owned =
0, BH disabled return true if slow path is taken sk_lock.slock
unlocked, owned = 1, BH enabled


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
