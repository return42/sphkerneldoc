
.. _API-shrink-dcache-sb:

================
shrink_dcache_sb
================

*man shrink_dcache_sb(9)*

*4.6.0-rc1*

shrink dcache for a superblock


Synopsis
========

.. c:function:: void shrink_dcache_sb( struct super_block * sb )

Arguments
=========

``sb``
    superblock


Description
===========

Shrink the dcache for the specified super block. This is used to free the dcache before unmounting a file system.
