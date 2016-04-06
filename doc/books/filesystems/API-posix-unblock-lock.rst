
.. _API-posix-unblock-lock:

==================
posix_unblock_lock
==================

*man posix_unblock_lock(9)*

*4.6.0-rc1*

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
