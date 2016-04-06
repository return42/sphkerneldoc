
.. _API-flock-lock-inode-wait:

=====================
flock_lock_inode_wait
=====================

*man flock_lock_inode_wait(9)*

*4.6.0-rc1*

Apply a FLOCK-style lock to a file


Synopsis
========

.. c:function:: int flock_lock_inode_wait( struct inode * inode, struct file_lock * fl )

Arguments
=========

``inode``
    inode of the file to apply to

``fl``
    The lock to be applied


Description
===========

Apply a FLOCK style lock request to an inode.
