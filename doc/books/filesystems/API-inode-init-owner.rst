
.. _API-inode-init-owner:

================
inode_init_owner
================

*man inode_init_owner(9)*

*4.6.0-rc1*

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
