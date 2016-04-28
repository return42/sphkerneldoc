.. -*- coding: utf-8; mode: rst -*-

.. _API-iunique:

=======
iunique
=======

*man iunique(9)*

*4.6.0-rc5*

get a unique inode number


Synopsis
========

.. c:function:: ino_t iunique( struct super_block * sb, ino_t max_reserved )

Arguments
=========

``sb``
    superblock

``max_reserved``
    highest reserved inode number


Description
===========

Obtain an inode number that is unique on the system for a given
superblock. This is used by file systems that have no natural permanent
inode numbering system. An inode number is returned that is higher than
the reserved limit but unique.


BUGS
====

With a large number of inodes live on the file system this function
currently becomes quite slow.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
