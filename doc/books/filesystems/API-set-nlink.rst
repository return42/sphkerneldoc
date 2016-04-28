.. -*- coding: utf-8; mode: rst -*-

.. _API-set-nlink:

=========
set_nlink
=========

*man set_nlink(9)*

*4.6.0-rc5*

directly set an inode's link count


Synopsis
========

.. c:function:: void set_nlink( struct inode * inode, unsigned int nlink )

Arguments
=========

``inode``
    inode

``nlink``
    new nlink (should be non-zero)


Description
===========

This is a low-level filesystem helper to replace any direct filesystem
manipulation of i_nlink.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
