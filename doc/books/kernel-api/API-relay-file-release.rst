
.. _API-relay-file-release:

==================
relay_file_release
==================

*man relay_file_release(9)*

*4.6.0-rc1*

release file op for relay files


Synopsis
========

.. c:function:: int relay_file_release( struct inode * inode, struct file * filp )

Arguments
=========

``inode``
    the inode

``filp``
    the file


Description
===========

Decrements the channel refcount, as the filesystem is no longer using it.
