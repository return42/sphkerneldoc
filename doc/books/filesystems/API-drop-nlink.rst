
.. _API-drop-nlink:

==========
drop_nlink
==========

*man drop_nlink(9)*

*4.6.0-rc1*

directly drop an inode's link count


Synopsis
========

.. c:function:: void drop_nlink( struct inode * inode )

Arguments
=========

``inode``
    inode


Description
===========

This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink. In cases where we are attempting to track writes to the filesystem, a decrement to
zero means an imminent write when the file is truncated and actually unlinked on the filesystem.
