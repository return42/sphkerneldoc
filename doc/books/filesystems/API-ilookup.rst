
.. _API-ilookup:

=======
ilookup
=======

*man ilookup(9)*

*4.6.0-rc1*

search for an inode in the inode cache


Synopsis
========

.. c:function:: struct inode ⋆ ilookup( struct super_block * sb, unsigned long ino )

Arguments
=========

``sb``
    super block of file system to search

``ino``
    inode number to search for


Description
===========

Search for the inode ``ino`` in the inode cache, and if the inode is in the cache, the inode is returned with an incremented reference count.
