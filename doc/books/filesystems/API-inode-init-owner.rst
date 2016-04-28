.. -*- coding: utf-8; mode: rst -*-

.. _API-inode-init-owner:

================
inode_init_owner
================

*man inode_init_owner(9)*

*4.6.0-rc5*

Init uid,gid,mode for new inode according to posix standards


Synopsis
========

.. c:function:: void inode_init_owner( struct inode * inode, const struct inode * dir, umode_t mode )

Arguments
=========

``inode``
    New inode

``dir``
    Directory inode

``mode``
    mode of the new inode


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
