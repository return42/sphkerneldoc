.. -*- coding: utf-8; mode: rst -*-

========
drm_mm.c
========



.. _xref_drm_mm_reserve_node:

drm_mm_reserve_node
===================

.. c:function:: int drm_mm_reserve_node (struct drm_mm * mm, struct drm_mm_node * node)

    insert an pre-initialized node

    :param struct drm_mm * mm:
        drm_mm allocator to insert **node** into

    :param struct drm_mm_node * node:
        drm_mm_node to insert



Description
-----------

This functions inserts an already set-up drm_mm_node into the allocator,
meaning that start, size and color must be set by the caller. This is useful
to initialize the allocator with preallocated objects which must be set-up
before the range allocator can be set-up, e.g. when taking over a firmware
framebuffer.



Returns
-------

0 on success, -ENOSPC if there's no hole where **node** is.




.. _xref_drm_mm_insert_node_generic:

drm_mm_insert_node_generic
==========================

.. c:function:: int drm_mm_insert_node_generic (struct drm_mm * mm, struct drm_mm_node * node, u64 size, unsigned alignment, unsigned long color, enum drm_mm_search_flags sflags, enum drm_mm_allocator_flags aflags)

    search for space and insert @node

    :param struct drm_mm * mm:
        drm_mm to allocate from

    :param struct drm_mm_node * node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

    :param unsigned alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for this node

    :param enum drm_mm_search_flags sflags:
        flags to fine-tune the allocation search

    :param enum drm_mm_allocator_flags aflags:
        flags to fine-tune the allocation behavior



Description
-----------

The preallocated node must be cleared to 0.



Returns
-------

0 on success, -ENOSPC if there's no suitable hole.




.. _xref_drm_mm_insert_node_in_range_generic:

drm_mm_insert_node_in_range_generic
===================================

.. c:function:: int drm_mm_insert_node_in_range_generic (struct drm_mm * mm, struct drm_mm_node * node, u64 size, unsigned alignment, unsigned long color, u64 start, u64 end, enum drm_mm_search_flags sflags, enum drm_mm_allocator_flags aflags)

    ranged search for space and insert @node

    :param struct drm_mm * mm:
        drm_mm to allocate from

    :param struct drm_mm_node * node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

    :param unsigned alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for this node

    :param u64 start:
        start of the allowed range for this node

    :param u64 end:
        end of the allowed range for this node

    :param enum drm_mm_search_flags sflags:
        flags to fine-tune the allocation search

    :param enum drm_mm_allocator_flags aflags:
        flags to fine-tune the allocation behavior



Description
-----------

The preallocated node must be cleared to 0.



Returns
-------

0 on success, -ENOSPC if there's no suitable hole.




.. _xref_drm_mm_remove_node:

drm_mm_remove_node
==================

.. c:function:: void drm_mm_remove_node (struct drm_mm_node * node)

    Remove a memory node from the allocator.

    :param struct drm_mm_node * node:
        drm_mm_node to remove



Description
-----------

This just removes a node from its drm_mm allocator. The node does not need to
be cleared again before it can be re-inserted into this or any other drm_mm
allocator. It is a bug to call this function on a un-allocated node.




.. _xref_drm_mm_replace_node:

drm_mm_replace_node
===================

.. c:function:: void drm_mm_replace_node (struct drm_mm_node * old, struct drm_mm_node * new)

    move an allocation from @old to @new

    :param struct drm_mm_node * old:
        drm_mm_node to remove from the allocator

    :param struct drm_mm_node * new:
        drm_mm_node which should inherit **old**'s allocation



Description
-----------

This is useful for when drivers embed the drm_mm_node structure and hence
can't move allocations by reassigning pointers. It's a combination of remove
and insert with the guarantee that the allocation start will match.




.. _xref_drm_mm_init_scan:

drm_mm_init_scan
================

.. c:function:: void drm_mm_init_scan (struct drm_mm * mm, u64 size, unsigned alignment, unsigned long color)

    initialize lru scanning

    :param struct drm_mm * mm:
        drm_mm to scan

    :param u64 size:
        size of the allocation

    :param unsigned alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for the allocation



Description
-----------

This simply sets up the scanning routines with the parameters for the desired
hole. Note that there's no need to specify allocation flags, since they only
change the place a node is allocated from within a suitable hole.



Warning
-------

As long as the scan list is non-empty, no other operations than
adding/removing nodes to/from the scan list are allowed.




.. _xref_drm_mm_init_scan_with_range:

drm_mm_init_scan_with_range
===========================

.. c:function:: void drm_mm_init_scan_with_range (struct drm_mm * mm, u64 size, unsigned alignment, unsigned long color, u64 start, u64 end)

    initialize range-restricted lru scanning

    :param struct drm_mm * mm:
        drm_mm to scan

    :param u64 size:
        size of the allocation

    :param unsigned alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for the allocation

    :param u64 start:
        start of the allowed range for the allocation

    :param u64 end:
        end of the allowed range for the allocation



Description
-----------

This simply sets up the scanning routines with the parameters for the desired
hole. Note that there's no need to specify allocation flags, since they only
change the place a node is allocated from within a suitable hole.



Warning
-------

As long as the scan list is non-empty, no other operations than
adding/removing nodes to/from the scan list are allowed.




.. _xref_drm_mm_scan_add_block:

drm_mm_scan_add_block
=====================

.. c:function:: bool drm_mm_scan_add_block (struct drm_mm_node * node)

    add a node to the scan list

    :param struct drm_mm_node * node:
        drm_mm_node to add



Description
-----------

Add a node to the scan list that might be freed to make space for the desired
hole.



Returns
-------

True if a hole has been found, false otherwise.




.. _xref_drm_mm_scan_remove_block:

drm_mm_scan_remove_block
========================

.. c:function:: bool drm_mm_scan_remove_block (struct drm_mm_node * node)

    remove a node from the scan list

    :param struct drm_mm_node * node:
        drm_mm_node to remove



Description
-----------

Nodes _must_ be removed in the exact same order from the scan list as they
have been added, otherwise the internal state of the memory manager will be
corrupted.


When the scan list is empty, the selected memory nodes can be freed. An
immediately following drm_mm_search_free with !DRM_MM_SEARCH_BEST will then
return the just freed block (because its at the top of the free_stack list).



Returns
-------

True if this block should be evicted, false otherwise. Will always
return false when no hole has been found.




.. _xref_drm_mm_clean:

drm_mm_clean
============

.. c:function:: bool drm_mm_clean (struct drm_mm * mm)

    checks whether an allocator is clean

    :param struct drm_mm * mm:
        drm_mm allocator to check



Returns
-------

True if the allocator is completely free, false if there's still a node
allocated in it.




.. _xref_drm_mm_init:

drm_mm_init
===========

.. c:function:: void drm_mm_init (struct drm_mm * mm, u64 start, u64 size)

    initialize a drm-mm allocator

    :param struct drm_mm * mm:
        the drm_mm structure to initialize

    :param u64 start:
        start of the range managed by **mm**

    :param u64 size:
        end of the range managed by **mm**



Description
-----------

Note that **mm** must be cleared to 0 before calling this function.




.. _xref_drm_mm_takedown:

drm_mm_takedown
===============

.. c:function:: void drm_mm_takedown (struct drm_mm * mm)

    clean up a drm_mm allocator

    :param struct drm_mm * mm:
        drm_mm allocator to clean up



Description
-----------

Note that it is a bug to call this function on an allocator which is not
clean.




.. _xref_drm_mm_debug_table:

drm_mm_debug_table
==================

.. c:function:: void drm_mm_debug_table (struct drm_mm * mm, const char * prefix)

    dump allocator state to dmesg

    :param struct drm_mm * mm:
        drm_mm allocator to dump

    :param const char * prefix:
        prefix to use for dumping to dmesg




.. _xref_drm_mm_dump_table:

drm_mm_dump_table
=================

.. c:function:: int drm_mm_dump_table (struct seq_file * m, struct drm_mm * mm)

    dump allocator state to a seq_file

    :param struct seq_file * m:
        seq_file to dump to

    :param struct drm_mm * mm:
        drm_mm allocator to dump


