
.. _API-set-nlink:

=========
set_nlink
=========

*man set_nlink(9)*

*4.6.0-rc1*

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

This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink.
