
.. _API-drm-mm-insert-node-generic:

==========================
drm_mm_insert_node_generic
==========================

*man drm_mm_insert_node_generic(9)*

*4.6.0-rc1*

search for space and insert ``node``


Synopsis
========

.. c:function:: int drm_mm_insert_node_generic( struct drm_mm * mm, struct drm_mm_node * node, u64 size, unsigned alignment, unsigned long color, enum drm_mm_search_flags sflags, enum drm_mm_allocator_flags aflags )

Arguments
=========

``mm``
    drm_mm to allocate from

``node``
    preallocate node to insert

``size``
    size of the allocation

``alignment``
    alignment of the allocation

``color``
    opaque tag value to use for this node

``sflags``
    flags to fine-tune the allocation search

``aflags``
    flags to fine-tune the allocation behavior


Description
===========

The preallocated node must be cleared to 0.


Returns
=======

0 on success, -ENOSPC if there's no suitable hole.
