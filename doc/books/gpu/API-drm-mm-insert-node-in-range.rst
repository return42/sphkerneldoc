
.. _API-drm-mm-insert-node-in-range:

===========================
drm_mm_insert_node_in_range
===========================

*man drm_mm_insert_node_in_range(9)*

*4.6.0-rc1*

ranged search for space and insert ``node``


Synopsis
========

.. c:function:: int drm_mm_insert_node_in_range( struct drm_mm * mm, struct drm_mm_node * node, u64 size, unsigned alignment, u64 start, u64 end, enum drm_mm_search_flags flags )

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

``start``
    start of the allowed range for this node

``end``
    end of the allowed range for this node

``flags``
    flags to fine-tune the allocation


Description
===========

This is a simplified version of ``drm_mm_insert_node_in_range_generic`` with ``color`` set to 0.

The preallocated node must be cleared to 0.


Returns
=======

0 on success, -ENOSPC if there's no suitable hole.
