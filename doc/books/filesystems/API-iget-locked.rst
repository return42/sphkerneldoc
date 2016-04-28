.. -*- coding: utf-8; mode: rst -*-

.. _API-iget-locked:

===========
iget_locked
===========

*man iget_locked(9)*

*4.6.0-rc5*

obtain an inode from a mounted file system


Synopsis
========

.. c:function:: struct inode * iget_locked( struct super_block * sb, unsigned long ino )

Arguments
=========

``sb``
    super block of file system

``ino``
    inode number to get


Description
===========

Search for the inode specified by ``ino`` in the inode cache and if
present return it with an increased reference count. This is for file
systems where the inode number is sufficient for unique identification
of an inode.

If the inode is not in cache, allocate a new inode and return it locked,
hashed, and with the I_NEW flag set. The file system gets to fill it in
before unlocking it via ``unlock_new_inode``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
