.. -*- coding: utf-8; mode: rst -*-

.. _API-invalidate-inode-pages2:

=======================
invalidate_inode_pages2
=======================

*man invalidate_inode_pages2(9)*

*4.6.0-rc5*

remove all pages from an address_space


Synopsis
========

.. c:function:: int invalidate_inode_pages2( struct address_space * mapping )

Arguments
=========

``mapping``
    the address_space


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
