.. -*- coding: utf-8; mode: rst -*-

.. _API-posix-unblock-lock:

==================
posix_unblock_lock
==================

*man posix_unblock_lock(9)*

*4.6.0-rc5*

stop waiting for a file lock


Synopsis
========

.. c:function:: int posix_unblock_lock( struct file_lock * waiter )

Arguments
=========

``waiter``
    the lock which was waiting


Description
===========

lockd needs to block waiting for locks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
