
.. _API-locks-lock-inode-wait:

=====================
locks_lock_inode_wait
=====================

*man locks_lock_inode_wait(9)*

*4.6.0-rc1*

Apply a lock to an inode


Synopsis
========

.. c:function:: int locks_lock_inode_wait( struct inode * inode, struct file_lock * fl )

Arguments
=========

``inode``
    inode of the file to apply to

``fl``
    The lock to be applied


Description
===========

Apply a POSIX or FLOCK style lock request to an inode.
