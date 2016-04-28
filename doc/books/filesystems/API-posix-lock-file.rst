.. -*- coding: utf-8; mode: rst -*-

.. _API-posix-lock-file:

===============
posix_lock_file
===============

*man posix_lock_file(9)*

*4.6.0-rc5*

Apply a POSIX-style lock to a file


Synopsis
========

.. c:function:: int posix_lock_file( struct file * filp, struct file_lock * fl, struct file_lock * conflock )

Arguments
=========

``filp``
    The file to apply the lock to

``fl``
    The lock to be applied

``conflock``
    Place to return a copy of the conflicting lock, if found.


Description
===========

Add a POSIX style lock to a file. We merge adjacent & overlapping locks
whenever possible. POSIX locks are sorted by owner task, then by
starting address

Note that if called with an FL_EXISTS argument, the caller may
determine whether or not a lock was successfully freed by testing the
return value for -ENOENT.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
