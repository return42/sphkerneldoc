.. -*- coding: utf-8; mode: rst -*-

.. _API---inode-permission:

==================
__inode_permission
==================

*man __inode_permission(9)*

*4.6.0-rc5*

Check for access rights to a given inode


Synopsis
========

.. c:function:: int __inode_permission( struct inode * inode, int mask )

Arguments
=========

``inode``
    Inode to check permission on

``mask``
    Right to check for (``MAY_READ``, ``MAY_WRITE``, ``MAY_EXEC``)


Description
===========

Check for read/write/execute permissions on an inode.

When checking for MAY_APPEND, MAY_WRITE must also be set in ``mask``.

This does not check for a read-only file system. You probably want
``inode_permission``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
