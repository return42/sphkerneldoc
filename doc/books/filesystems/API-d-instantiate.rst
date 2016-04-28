.. -*- coding: utf-8; mode: rst -*-

.. _API-d-instantiate:

=============
d_instantiate
=============

*man d_instantiate(9)*

*4.6.0-rc5*

fill in inode information for a dentry


Synopsis
========

.. c:function:: void d_instantiate( struct dentry * entry, struct inode * inode )

Arguments
=========

``entry``
    dentry to complete

``inode``
    inode to attach to this dentry


Description
===========

Fill in inode information in the entry.

This turns negative dentries into productive full members of society.

NOTE! This assumes that the inode count has been incremented (or
otherwise set) by the caller to indicate that it is now in use by the
dcache.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
