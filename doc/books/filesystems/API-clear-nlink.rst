
.. _API-clear-nlink:

===========
clear_nlink
===========

*man clear_nlink(9)*

*4.6.0-rc1*

directly zero an inode's link count


Synopsis
========

.. c:function:: void clear_nlink( struct inode * inode )

Arguments
=========

``inode``
    inode


Description
===========

This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink. See ``drop_nlink`` for why we care about i_nlink hitting zero.
