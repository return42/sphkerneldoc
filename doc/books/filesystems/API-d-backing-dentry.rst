.. -*- coding: utf-8; mode: rst -*-

.. _API-d-backing-dentry:

================
d_backing_dentry
================

*man d_backing_dentry(9)*

*4.6.0-rc5*

Get upper or lower dentry we should be using


Synopsis
========

.. c:function:: struct dentry * d_backing_dentry( struct dentry * upper )

Arguments
=========

``upper``
    The upper layer


Description
===========

This is the helper that should be used to get the dentry of the inode
that will be used if this dentry were opened as a file. It may be the
upper dentry or it may be a lower dentry pinned by the upper.

Normal filesystems should not use this to access their own dentries.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
