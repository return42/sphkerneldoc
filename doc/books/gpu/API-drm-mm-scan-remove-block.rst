.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-scan-remove-block:

========================
drm_mm_scan_remove_block
========================

*man drm_mm_scan_remove_block(9)*

*4.6.0-rc5*

remove a node from the scan list


Synopsis
========

.. c:function:: bool drm_mm_scan_remove_block( struct drm_mm_node * node )

Arguments
=========

``node``
    drm_mm_node to remove


Description
===========

Nodes _must_ be removed in the exact same order from the scan list as
they have been added, otherwise the internal state of the memory manager
will be corrupted.

When the scan list is empty, the selected memory nodes can be freed. An
immediately following drm_mm_search_free with !DRM_MM_SEARCH_BEST
will then return the just freed block (because its at the top of the
free_stack list).


Returns
=======

True if this block should be evicted, false otherwise. Will always
return false when no hole has been found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
