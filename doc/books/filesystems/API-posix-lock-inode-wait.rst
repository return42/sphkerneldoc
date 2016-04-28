.. -*- coding: utf-8; mode: rst -*-

.. _API-posix-lock-inode-wait:

=====================
posix_lock_inode_wait
=====================

*man posix_lock_inode_wait(9)*

*4.6.0-rc5*

Apply a POSIX-style lock to a file


Synopsis
========

.. c:function:: int posix_lock_inode_wait( struct inode * inode, struct file_lock * fl )

Arguments
=========

``inode``
    inode of file to which lock request should be applied

``fl``
    The lock to be applied


Description
===========

Apply a POSIX style lock request to an inode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
