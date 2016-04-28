.. -*- coding: utf-8; mode: rst -*-

.. _API-unlock-sock-fast:

================
unlock_sock_fast
================

*man unlock_sock_fast(9)*

*4.6.0-rc5*

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

fast unlock socket for user context. If slow mode is on, we call regular
``release_sock``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
