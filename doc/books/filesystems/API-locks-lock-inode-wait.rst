.. -*- coding: utf-8; mode: rst -*-

.. _API-locks-lock-inode-wait:

=====================
locks_lock_inode_wait
=====================

*man locks_lock_inode_wait(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
