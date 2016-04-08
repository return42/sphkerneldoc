
.. _API-unlock-sock-fast:

================
unlock_sock_fast
================

*man unlock_sock_fast(9)*

*4.6.0-rc1*

complement of lock_sock_fast


Synopsis
========

.. c:function:: void unlock_sock_fast( struct sock * sk, bool slow )

Arguments
=========

``sk``
    socket

``slow``
    slow mode


Description
===========

fast unlock socket for user context. If slow mode is on, we call regular ``release_sock``
