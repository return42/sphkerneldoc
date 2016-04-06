
.. _API-generic-permission:

==================
generic_permission
==================

*man generic_permission(9)*

*4.6.0-rc1*

check for access rights on a Posix-like filesystem


Synopsis
========

.. c:function:: int generic_permission( struct inode * inode, int mask )

Arguments
=========

``inode``
    inode to check access rights for

``mask``
    right to check for (``MAY_READ``, ``MAY_WRITE``, ``MAY_EXEC``, ...)


Description
===========

Used to check for read/write/execute permissions on a file. We use “fsuid” for this, letting us set arbitrary permissions for filesystem access without changing the “normal” uids
which are used for other things.

generic_permission is rcu-walk aware. It returns -ECHILD in case an rcu-walk request cannot be satisfied (eg. requires blocking or too much complexity). It would then be called
again in ref-walk mode.
