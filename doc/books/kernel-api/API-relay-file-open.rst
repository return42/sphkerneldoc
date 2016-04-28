.. -*- coding: utf-8; mode: rst -*-

.. _API-relay-file-open:

===============
relay_file_open
===============

*man relay_file_open(9)*

*4.6.0-rc5*

open file op for relay files


Synopsis
========

.. c:function:: int relay_file_open( struct inode * inode, struct file * filp )

Arguments
=========

``inode``
    the inode

``filp``
    the file


Description
===========

Increments the channel buffer refcount.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
