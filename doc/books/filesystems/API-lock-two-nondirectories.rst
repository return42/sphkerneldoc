
.. _API-lock-two-nondirectories:

=======================
lock_two_nondirectories
=======================

*man lock_two_nondirectories(9)*

*4.6.0-rc1*

take two i_mutexes on non-directory objects


Synopsis
========

.. c:function:: void lock_two_nondirectories( struct inode * inode1, struct inode * inode2 )

Arguments
=========

``inode1``
    first inode to lock

``inode2``
    second inode to lock


Description
===========

Lock any non-NULL argument that is not a directory. Zero, one or two objects may be locked by this function.
