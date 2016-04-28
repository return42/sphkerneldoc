.. -*- coding: utf-8; mode: rst -*-

.. _API-lock-two-nondirectories:

=======================
lock_two_nondirectories
=======================

*man lock_two_nondirectories(9)*

*4.6.0-rc5*

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

Lock any non-NULL argument that is not a directory. Zero, one or two
objects may be locked by this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
