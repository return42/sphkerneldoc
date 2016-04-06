
.. _API-inode-init-always:

=================
inode_init_always
=================

*man inode_init_always(9)*

*4.6.0-rc1*

perform inode structure intialisation


Synopsis
========

.. c:function:: int inode_init_always( struct super_block * sb, struct inode * inode )

Arguments
=========

``sb``
    superblock inode belongs to

``inode``
    inode to initialise


Description
===========

These are initializations that need to be done on every inode allocation as the fields are not initialised by slab allocation.
