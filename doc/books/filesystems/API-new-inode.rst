.. -*- coding: utf-8; mode: rst -*-

.. _API-new-inode:

=========
new_inode
=========

*man new_inode(9)*

*4.6.0-rc5*

obtain an inode


Synopsis
========

.. c:function:: struct inode * new_inode( struct super_block * sb )

Arguments
=========

``sb``
    superblock


Description
===========

Allocates a new inode for given superblock. The default gfp_mask for
allocations related to inode->i_mapping is GFP_HIGHUSER_MOVABLE. If
HIGHMEM pages are unsuitable or it is known that pages allocated for the
page cache are not reclaimable or migratable, ``mapping_set_gfp_mask``
must be called with suitable flags on the newly created inode's mapping


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
