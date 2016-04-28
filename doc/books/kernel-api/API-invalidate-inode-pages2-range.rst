.. -*- coding: utf-8; mode: rst -*-

.. _API-invalidate-inode-pages2-range:

=============================
invalidate_inode_pages2_range
=============================

*man invalidate_inode_pages2_range(9)*

*4.6.0-rc5*

remove range of pages from an address_space


Synopsis
========

.. c:function:: int invalidate_inode_pages2_range( struct address_space * mapping, pgoff_t start, pgoff_t end )

Arguments
=========

``mapping``
    the address_space

``start``
    the page offset 'from' which to invalidate

``end``
    the page offset 'to' which to invalidate (inclusive)


Description
===========

Any pages which are found to be mapped into pagetables are unmapped
prior to invalidation.

Returns -EBUSY if any pages could not be invalidated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
