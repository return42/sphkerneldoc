.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_mm.c

.. _`overview`:

Overview
========

drm_mm provides a simple range allocator. The drivers are free to use the
resource allocator from the linux core if it suits them, the upside of drm_mm
is that it's in the DRM core. Which means that it's easier to extend for
some of the crazier special purpose needs of gpus.

The main data struct is \ :c:type:`struct drm_mm <drm_mm>`\ , allocations are tracked in \ :c:type:`struct drm_mm_node <drm_mm_node>`\ .
Drivers are free to embed either of them into their own suitable
datastructures. drm_mm itself will not do any memory allocations of its own,
so if drivers choose not to embed nodes they need to still allocate them
themselves.

The range allocator also supports reservation of preallocated blocks. This is
useful for taking over initial mode setting configurations from the firmware,
where an object needs to be created which exactly matches the firmware's
scanout target. As long as the range is still free it can be inserted anytime
after the allocator is initialized, which helps with avoiding looped
dependencies in the driver load sequence.

drm_mm maintains a stack of most recently freed holes, which of all
simplistic datastructures seems to be a fairly decent approach to clustering
allocations and avoiding too much fragmentation. This means free space
searches are O(num_holes). Given that all the fancy features drm_mm supports
something better would be fairly complex and since gfx thrashing is a fairly
steep cliff not a real concern. Removing a node again is O(1).

drm_mm supports a few features: Alignment and range restrictions can be
supplied. Furthermore every \ :c:type:`struct drm_mm_node <drm_mm_node>`\  has a color value (which is just an
opaque unsigned long) which in conjunction with a driver callback can be used
to implement sophisticated placement restrictions. The i915 DRM driver uses
this to implement guard pages between incompatible caching domains in the
graphics TT.

Two behaviors are supported for searching and allocating: bottom-up and
top-down. The default is bottom-up. Top-down allocation can be used if the
memory area has different restrictions, or just to reduce fragmentation.

Finally iteration helpers to walk all nodes and all holes are provided as are
some basic allocator dumpers for debugging.

Note that this range allocator is not thread-safe, drivers need to protect
modifications with their own locking. The idea behind this is that for a full
memory manager additional data needs to be protected anyway, hence internal
locking would be fully redundant.

.. _`drm_mm_reserve_node`:

drm_mm_reserve_node
===================

.. c:function:: int drm_mm_reserve_node(struct drm_mm *mm, struct drm_mm_node *node)

    insert an pre-initialized node

    :param struct drm_mm \*mm:
        drm_mm allocator to insert \ ``node``\  into

    :param struct drm_mm_node \*node:
        drm_mm_node to insert

.. _`drm_mm_reserve_node.description`:

Description
-----------

This functions inserts an already set-up \ :c:type:`struct drm_mm_node <drm_mm_node>`\  into the allocator,
meaning that start, size and color must be set by the caller. All other
fields must be cleared to 0. This is useful to initialize the allocator with
preallocated objects which must be set-up before the range allocator can be
set-up, e.g. when taking over a firmware framebuffer.

.. _`drm_mm_reserve_node.return`:

Return
------

0 on success, -ENOSPC if there's no hole where \ ``node``\  is.

.. _`drm_mm_insert_node_in_range`:

drm_mm_insert_node_in_range
===========================

.. c:function:: int drm_mm_insert_node_in_range(struct drm_mm * const mm, struct drm_mm_node * const node, u64 size, u64 alignment, unsigned long color, u64 range_start, u64 range_end, enum drm_mm_insert_mode mode)

    ranged search for space and insert \ ``node``\ 

    :param struct drm_mm \* const mm:
        drm_mm to allocate from

    :param struct drm_mm_node \* const node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

    :param u64 alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for this node

    :param u64 range_start:
        start of the allowed range for this node

    :param u64 range_end:
        end of the allowed range for this node

    :param enum drm_mm_insert_mode mode:
        fine-tune the allocation search and placement

.. _`drm_mm_insert_node_in_range.description`:

Description
-----------

The preallocated \ ``node``\  must be cleared to 0.

.. _`drm_mm_insert_node_in_range.return`:

Return
------

0 on success, -ENOSPC if there's no suitable hole.

.. _`drm_mm_remove_node`:

drm_mm_remove_node
==================

.. c:function:: void drm_mm_remove_node(struct drm_mm_node *node)

    Remove a memory node from the allocator.

    :param struct drm_mm_node \*node:
        drm_mm_node to remove

.. _`drm_mm_remove_node.description`:

Description
-----------

This just removes a node from its drm_mm allocator. The node does not need to
be cleared again before it can be re-inserted into this or any other drm_mm
allocator. It is a bug to call this function on a unallocated node.

.. _`drm_mm_replace_node`:

drm_mm_replace_node
===================

.. c:function:: void drm_mm_replace_node(struct drm_mm_node *old, struct drm_mm_node *new)

    move an allocation from \ ``old``\  to \ ``new``\ 

    :param struct drm_mm_node \*old:
        drm_mm_node to remove from the allocator

    :param struct drm_mm_node \*new:
        drm_mm_node which should inherit \ ``old``\ 's allocation

.. _`drm_mm_replace_node.description`:

Description
-----------

This is useful for when drivers embed the drm_mm_node structure and hence
can't move allocations by reassigning pointers. It's a combination of remove
and insert with the guarantee that the allocation start will match.

.. _`lru-scan-roster`:

lru scan roster
===============

Very often GPUs need to have continuous allocations for a given object. When
evicting objects to make space for a new one it is therefore not most
efficient when we simply start to select all objects from the tail of an LRU
until there's a suitable hole: Especially for big objects or nodes that
otherwise have special allocation constraints there's a good chance we evict
lots of (smaller) objects unnecessarily.

The DRM range allocator supports this use-case through the scanning
interfaces. First a scan operation needs to be initialized with
\ :c:func:`drm_mm_scan_init`\  or \ :c:func:`drm_mm_scan_init_with_range`\ . The driver adds
objects to the roster, probably by walking an LRU list, but this can be
freely implemented. Eviction candiates are added using
\ :c:func:`drm_mm_scan_add_block`\  until a suitable hole is found or there are no
further evictable objects. Eviction roster metadata is tracked in \ :c:type:`struct drm_mm_scan <drm_mm_scan>`\ .

The driver must walk through all objects again in exactly the reverse
order to restore the allocator state. Note that while the allocator is used
in the scan mode no other operation is allowed.

Finally the driver evicts all objects selected (drm_mm_scan_remove_block()
reported true) in the scan, and any overlapping nodes after color adjustment
(drm_mm_scan_color_evict()). Adding and removing an object is O(1), and
since freeing a node is also O(1) the overall complexity is
O(scanned_objects). So like the free stack which needs to be walked before a
scan operation even begins this is linear in the number of objects. It
doesn't seem to hurt too badly.

.. _`drm_mm_scan_init_with_range`:

drm_mm_scan_init_with_range
===========================

.. c:function:: void drm_mm_scan_init_with_range(struct drm_mm_scan *scan, struct drm_mm *mm, u64 size, u64 alignment, unsigned long color, u64 start, u64 end, enum drm_mm_insert_mode mode)

    initialize range-restricted lru scanning

    :param struct drm_mm_scan \*scan:
        scan state

    :param struct drm_mm \*mm:
        drm_mm to scan

    :param u64 size:
        size of the allocation

    :param u64 alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for the allocation

    :param u64 start:
        start of the allowed range for the allocation

    :param u64 end:
        end of the allowed range for the allocation

    :param enum drm_mm_insert_mode mode:
        fine-tune the allocation search and placement

.. _`drm_mm_scan_init_with_range.description`:

Description
-----------

This simply sets up the scanning routines with the parameters for the desired
hole.

.. _`drm_mm_scan_init_with_range.warning`:

Warning
-------

As long as the scan list is non-empty, no other operations than
adding/removing nodes to/from the scan list are allowed.

.. _`drm_mm_scan_add_block`:

drm_mm_scan_add_block
=====================

.. c:function:: bool drm_mm_scan_add_block(struct drm_mm_scan *scan, struct drm_mm_node *node)

    add a node to the scan list

    :param struct drm_mm_scan \*scan:
        the active drm_mm scanner

    :param struct drm_mm_node \*node:
        drm_mm_node to add

.. _`drm_mm_scan_add_block.description`:

Description
-----------

Add a node to the scan list that might be freed to make space for the desired
hole.

.. _`drm_mm_scan_add_block.return`:

Return
------

True if a hole has been found, false otherwise.

.. _`drm_mm_scan_remove_block`:

drm_mm_scan_remove_block
========================

.. c:function:: bool drm_mm_scan_remove_block(struct drm_mm_scan *scan, struct drm_mm_node *node)

    remove a node from the scan list

    :param struct drm_mm_scan \*scan:
        the active drm_mm scanner

    :param struct drm_mm_node \*node:
        drm_mm_node to remove

.. _`drm_mm_scan_remove_block.description`:

Description
-----------

Nodes **must** be removed in exactly the reverse order from the scan list as
they have been added (e.g. using \ :c:func:`list_add`\  as they are added and then
\ :c:func:`list_for_each`\  over that eviction list to remove), otherwise the internal
state of the memory manager will be corrupted.

When the scan list is empty, the selected memory nodes can be freed. An
immediately following \ :c:func:`drm_mm_insert_node_in_range_generic`\  or one of the
simpler versions of that function with !DRM_MM_SEARCH_BEST will then return
the just freed block (because its at the top of the free_stack list).

.. _`drm_mm_scan_remove_block.return`:

Return
------

True if this block should be evicted, false otherwise. Will always
return false when no hole has been found.

.. _`drm_mm_scan_color_evict`:

drm_mm_scan_color_evict
=======================

.. c:function:: struct drm_mm_node *drm_mm_scan_color_evict(struct drm_mm_scan *scan)

    evict overlapping nodes on either side of hole

    :param struct drm_mm_scan \*scan:
        drm_mm scan with target hole

.. _`drm_mm_scan_color_evict.description`:

Description
-----------

After completing an eviction scan and removing the selected nodes, we may
need to remove a few more nodes from either side of the target hole if
mm.color_adjust is being used.

.. _`drm_mm_scan_color_evict.return`:

Return
------

A node to evict, or NULL if there are no overlapping nodes.

.. _`drm_mm_init`:

drm_mm_init
===========

.. c:function:: void drm_mm_init(struct drm_mm *mm, u64 start, u64 size)

    initialize a drm-mm allocator

    :param struct drm_mm \*mm:
        the drm_mm structure to initialize

    :param u64 start:
        start of the range managed by \ ``mm``\ 

    :param u64 size:
        end of the range managed by \ ``mm``\ 

.. _`drm_mm_init.description`:

Description
-----------

Note that \ ``mm``\  must be cleared to 0 before calling this function.

.. _`drm_mm_takedown`:

drm_mm_takedown
===============

.. c:function:: void drm_mm_takedown(struct drm_mm *mm)

    clean up a drm_mm allocator

    :param struct drm_mm \*mm:
        drm_mm allocator to clean up

.. _`drm_mm_takedown.description`:

Description
-----------

Note that it is a bug to call this function on an allocator which is not
clean.

.. _`drm_mm_print`:

drm_mm_print
============

.. c:function:: void drm_mm_print(const struct drm_mm *mm, struct drm_printer *p)

    print allocator state

    :param const struct drm_mm \*mm:
        drm_mm allocator to print

    :param struct drm_printer \*p:
        DRM printer to use

.. This file was automatic generated / don't edit.

