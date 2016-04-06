
.. _API-d-backing-dentry:

================
d_backing_dentry
================

*man d_backing_dentry(9)*

*4.6.0-rc1*

Get upper or lower dentry we should be using


Synopsis
========

.. c:function:: struct dentry ⋆ d_backing_dentry( struct dentry * upper )

Arguments
=========

``upper``
    The upper layer


Description
===========

This is the helper that should be used to get the dentry of the inode that will be used if this dentry were opened as a file. It may be the upper dentry or it may be a lower dentry
pinned by the upper.

Normal filesystems should not use this to access their own dentries.
