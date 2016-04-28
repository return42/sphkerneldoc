.. -*- coding: utf-8; mode: rst -*-

.. _API-vfs-lock-file:

=============
vfs_lock_file
=============

*man vfs_lock_file(9)*

*4.6.0-rc5*

file byte range lock


Synopsis
========

.. c:function:: int vfs_lock_file( struct file * filp, unsigned int cmd, struct file_lock * fl, struct file_lock * conf )

Arguments
=========

``filp``
    The file to apply the lock to

``cmd``
    type of locking operation (F_SETLK, F_GETLK, etc.)

``fl``
    The lock to be applied

``conf``
    Place to return a copy of the conflicting lock, if found.


Description
===========

A caller that doesn't care about the conflicting lock may pass NULL as
the final argument.

If the filesystem defines a private ->``lock`` method, then ``conf``
will be left unchanged; so a caller that cares should initialize it to
some acceptable default.

To avoid blocking kernel daemons, such as lockd, that need to acquire
POSIX locks, the ->``lock`` interface may return asynchronously, before
the lock has been granted or denied by the underlying filesystem, if
(and only if) lm_grant is set. Callers expecting ->``lock`` to return
asynchronously will only use F_SETLK, not F_SETLKW; they will set
FL_SLEEP if (and only if) the request is for a blocking lock. When
->``lock`` does return asynchronously, it must return
FILE_LOCK_DEFERRED, and call ->``lm_grant`` when the lock request
completes. If the request is for non-blocking lock the file system
should return FILE_LOCK_DEFERRED then try to get the lock and call the
callback routine with the result. If the request timed out the callback
routine will return a nonzero return code and the file system should
release the lock. The file system is also responsible to keep a
corresponding posix lock when it grants a lock so the VFS can find out
which locks are locally held and do the correct lock cleanup when
required. The underlying filesystem must not drop the kernel lock or
call ->``lm_grant`` before returning to the caller with a
FILE_LOCK_DEFERRED return code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
