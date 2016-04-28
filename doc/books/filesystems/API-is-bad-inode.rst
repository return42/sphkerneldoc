.. -*- coding: utf-8; mode: rst -*-

.. _API-is-bad-inode:

============
is_bad_inode
============

*man is_bad_inode(9)*

*4.6.0-rc5*

is an inode errored


Synopsis
========

.. c:function:: bool is_bad_inode( struct inode * inode )

Arguments
=========

``inode``
    inode to test


Description
===========

Returns true if the inode in question has been marked as bad.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
