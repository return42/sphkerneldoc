
.. _API-inc-nlink:

=========
inc_nlink
=========

*man inc_nlink(9)*

*4.6.0-rc1*

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

This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink. Currently, it is only here for parity with ``dec_nlink``.
