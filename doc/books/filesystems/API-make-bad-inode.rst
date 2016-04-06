
.. _API-make-bad-inode:

==============
make_bad_inode
==============

*man make_bad_inode(9)*

*4.6.0-rc1*

mark an inode bad due to an I/O error


Synopsis
========

.. c:function:: void make_bad_inode( struct inode * inode )

Arguments
=========

``inode``
    Inode to mark bad


Description
===========

When an inode cannot be read due to a media or remote network failure this function makes the inode “bad” and causes I/O operations on it to fail from this point on.
