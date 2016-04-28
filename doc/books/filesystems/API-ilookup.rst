.. -*- coding: utf-8; mode: rst -*-

.. _API-ilookup:

=======
ilookup
=======

*man ilookup(9)*

*4.6.0-rc5*

search for an inode in the inode cache


Synopsis
========

.. c:function:: struct inode * ilookup( struct super_block * sb, unsigned long ino )

Arguments
=========

``sb``
    super block of file system to search

``ino``
    inode number to search for


Description
===========

Search for the inode ``ino`` in the inode cache, and if the inode is in
the cache, the inode is returned with an incremented reference count.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
