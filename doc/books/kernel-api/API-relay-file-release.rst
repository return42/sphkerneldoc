.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-release:

==================
relay_file_release
==================

*man relay_file_release(9)*

*4.6.0-rc5*

release file op for relay files


Synopsis
========

.. c:function:: int relay_file_release( struct inode * inode, struct file * filp )

Arguments
=========

``inode``
    the inode

``filp``
    the file


Description
===========

Decrements the channel refcount, as the filesystem is no longer using
it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
