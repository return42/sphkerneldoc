
.. _API-inode-inc-iversion:

==================
inode_inc_iversion
==================

*man inode_inc_iversion(9)*

*4.6.0-rc1*

increments i_version


Synopsis
========

.. c:function:: void inode_inc_iversion( struct inode * inode )

Arguments
=========

``inode``
    inode that need to be updated


Description
===========

Every time the inode is modified, the i_version field will be incremented. The filesystem has to be mounted with i_version flag
