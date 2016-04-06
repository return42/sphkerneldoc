
.. _API-d-find-any-alias:

================
d_find_any_alias
================

*man d_find_any_alias(9)*

*4.6.0-rc1*

find any alias for a given inode


Synopsis
========

.. c:function:: struct dentry ⋆ d_find_any_alias( struct inode * inode )

Arguments
=========

``inode``
    inode to find an alias for


Description
===========

If any aliases exist for the given inode, take and return a reference for one of them. If no aliases exist, return ``NULL``.
