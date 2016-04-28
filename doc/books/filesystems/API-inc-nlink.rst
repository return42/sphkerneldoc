.. -*- coding: utf-8; mode: rst -*-

.. _API-inc-nlink:

=========
inc_nlink
=========

*man inc_nlink(9)*

*4.6.0-rc5*

directly increment an inode's link count


Synopsis
========

.. c:function:: void inc_nlink( struct inode * inode )

Arguments
=========

``inode``
    inode


Description
===========

This is a low-level filesystem helper to replace any direct filesystem
manipulation of i_nlink. Currently, it is only here for parity with
``dec_nlink``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
