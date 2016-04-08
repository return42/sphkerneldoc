
.. _API-lock-sock-fast:

==============
lock_sock_fast
==============

*man lock_sock_fast(9)*

*4.6.0-rc1*

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

This version should be used for very small section, where process wont block return false if fast path is taken sk_lock.slock locked, owned = 0, BH disabled return true if slow
path is taken sk_lock.slock unlocked, owned = 1, BH enabled
