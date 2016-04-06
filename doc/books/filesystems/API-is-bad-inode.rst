
.. _API-is-bad-inode:

============
is_bad_inode
============

*man is_bad_inode(9)*

*4.6.0-rc1*

is an inode errored


Synopsis
========

.. c:function:: bool is_bad_inode( struct inode * inode )

Arguments
=========

``inode``
    inode to test


Description
===========

Returns true if the inode in question has been marked as bad.
