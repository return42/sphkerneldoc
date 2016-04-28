.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-vma-offset-exact-lookup-locked:

==================================
drm_vma_offset_exact_lookup_locked
==================================

*man drm_vma_offset_exact_lookup_locked(9)*

*4.6.0-rc5*

Look up node by exact address


Synopsis
========

.. c:function:: struct drm_vma_offset_node * drm_vma_offset_exact_lookup_locked( struct drm_vma_offset_manager * mgr, unsigned long start, unsigned long pages )

Arguments
=========

``mgr``
    Manager object

``start``
    Start address (page-based, not byte-based)

``pages``
    Size of object (page-based)


Description
===========

Same as ``drm_vma_offset_lookup_locked`` but does not allow any offset
into the node. It only returns the exact object with the given start
address.


RETURNS
=======

Node at exact start address ``start``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
