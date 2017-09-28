.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_mm.h

.. _`drm_mm_insert_mode`:

enum drm_mm_insert_mode
=======================

.. c:type:: enum drm_mm_insert_mode

    control search and allocation behaviour

.. _`drm_mm_insert_mode.definition`:

Definition
----------

.. code-block:: c

    enum drm_mm_insert_mode {
        DRM_MM_INSERT_BEST,
        DRM_MM_INSERT_LOW,
        DRM_MM_INSERT_HIGH,
        DRM_MM_INSERT_EVICT
    };

.. _`drm_mm_insert_mode.constants`:

Constants
---------

DRM_MM_INSERT_BEST

    Search for the smallest hole (within the search range) that fits
    the desired node.

    Allocates the node from the bottom of the found hole.

DRM_MM_INSERT_LOW

    Search for the lowest hole (address closest to 0, within the search
    range) that fits the desired node.

    Allocates the node from the bottom of the found hole.

DRM_MM_INSERT_HIGH

    Search for the highest hole (address closest to U64_MAX, within the
    search range) that fits the desired node.

    Allocates the node from the *top* of the found hole. The specified
    alignment for the node is applied to the base of the node
    (&drm_mm_node.start).

DRM_MM_INSERT_EVICT

    Search for the most recently evicted hole (within the search range)
    that fits the desired node. This is appropriate for use immediately
    after performing an eviction scan (see \ :c:func:`drm_mm_scan_init`\ ) and
    removing the selected nodes to form a hole.

    Allocates the node from the bottom of the found hole.

.. _`drm_mm_insert_mode.description`:

Description
-----------

The \ :c:type:`struct drm_mm <drm_mm>`\  range manager supports finding a suitable modes using
a number of search trees. These trees are oranised by size, by address and
in most recent eviction order. This allows the user to find either the
smallest hole to reuse, the lowest or highest address to reuse, or simply
reuse the most recent eviction that fits. When allocating the \ :c:type:`struct drm_mm_node <drm_mm_node>`\ 
from within the hole, the \ :c:type:`struct drm_mm_insert_mode <drm_mm_insert_mode>`\  also dictate whether to
allocate the lowest matching address or the highest.

.. _`drm_mm_node`:

struct drm_mm_node
==================

.. c:type:: struct drm_mm_node

    allocated block in the DRM allocator

.. _`drm_mm_node.definition`:

Definition
----------

.. code-block:: c

    struct drm_mm_node {
        unsigned long color;
        u64 start;
        u64 size;
    }

.. _`drm_mm_node.members`:

Members
-------

color
    Opaque driver-private tag.

start
    Start address of the allocated block.

size
    Size of the allocated block.

.. _`drm_mm_node.description`:

Description
-----------

This represents an allocated block in a \ :c:type:`struct drm_mm <drm_mm>`\  allocator. Except for
pre-reserved nodes inserted using \ :c:func:`drm_mm_reserve_node`\  the structure is
entirely opaque and should only be accessed through the provided funcions.
Since allocation of these nodes is entirely handled by the driver they can be
embedded.

.. _`drm_mm`:

struct drm_mm
=============

.. c:type:: struct drm_mm

    DRM allocator

.. _`drm_mm.definition`:

Definition
----------

.. code-block:: c

    struct drm_mm {
        void (*color_adjust)(const struct drm_mm_node *node,unsigned long color, u64 *start, u64 *end);
    }

.. _`drm_mm.members`:

Members
-------

color_adjust

    Optional driver callback to further apply restrictions on a hole. The
    node argument points at the node containing the hole from which the
    block would be allocated (see \ :c:func:`drm_mm_hole_follows`\  and friends). The
    other arguments are the size of the block to be allocated. The driver
    can adjust the start and end as needed to e.g. insert guard pages.

.. _`drm_mm.description`:

Description
-----------

DRM range allocator with a few special functions and features geared towards
managing GPU memory. Except for the \ ``color_adjust``\  callback the structure is
entirely opaque and should only be accessed through the provided functions
and macros. This structure can be embedded into larger driver structures.

.. _`drm_mm_scan`:

struct drm_mm_scan
==================

.. c:type:: struct drm_mm_scan

    DRM allocator eviction roaster data

.. _`drm_mm_scan.definition`:

Definition
----------

.. code-block:: c

    struct drm_mm_scan {
    }

.. _`drm_mm_scan.members`:

Members
-------

void
    no arguments

.. _`drm_mm_scan.description`:

Description
-----------

This structure tracks data needed for the eviction roaster set up using
\ :c:func:`drm_mm_scan_init`\ , and used with \ :c:func:`drm_mm_scan_add_block`\  and
\ :c:func:`drm_mm_scan_remove_block`\ . The structure is entirely opaque and should only
be accessed through the provided functions and macros. It is meant to be
allocated temporarily by the driver on the stack.

.. _`drm_mm_node_allocated`:

drm_mm_node_allocated
=====================

.. c:function:: bool drm_mm_node_allocated(const struct drm_mm_node *node)

    checks whether a node is allocated

    :param const struct drm_mm_node \*node:
        drm_mm_node to check

.. _`drm_mm_node_allocated.description`:

Description
-----------

Drivers are required to clear a node prior to using it with the
drm_mm range manager.

Drivers should use this helper for proper encapsulation of drm_mm
internals.

.. _`drm_mm_node_allocated.return`:

Return
------

True if the \ ``node``\  is allocated.

.. _`drm_mm_initialized`:

drm_mm_initialized
==================

.. c:function:: bool drm_mm_initialized(const struct drm_mm *mm)

    checks whether an allocator is initialized

    :param const struct drm_mm \*mm:
        drm_mm to check

.. _`drm_mm_initialized.description`:

Description
-----------

Drivers should clear the struct drm_mm prior to initialisation if they
want to use this function.

Drivers should use this helper for proper encapsulation of drm_mm
internals.

.. _`drm_mm_initialized.return`:

Return
------

True if the \ ``mm``\  is initialized.

.. _`drm_mm_hole_follows`:

drm_mm_hole_follows
===================

.. c:function:: bool drm_mm_hole_follows(const struct drm_mm_node *node)

    checks whether a hole follows this node

    :param const struct drm_mm_node \*node:
        drm_mm_node to check

.. _`drm_mm_hole_follows.description`:

Description
-----------

Holes are embedded into the drm_mm using the tail of a drm_mm_node.
If you wish to know whether a hole follows this particular node,
query this function. See also \ :c:func:`drm_mm_hole_node_start`\  and
\ :c:func:`drm_mm_hole_node_end`\ .

.. _`drm_mm_hole_follows.return`:

Return
------

True if a hole follows the \ ``node``\ .

.. _`drm_mm_hole_node_start`:

drm_mm_hole_node_start
======================

.. c:function:: u64 drm_mm_hole_node_start(const struct drm_mm_node *hole_node)

    computes the start of the hole following \ ``node``\ 

    :param const struct drm_mm_node \*hole_node:
        drm_mm_node which implicitly tracks the following hole

.. _`drm_mm_hole_node_start.description`:

Description
-----------

This is useful for driver-specific debug dumpers. Otherwise drivers should
not inspect holes themselves. Drivers must check first whether a hole indeed
follows by looking at \ :c:func:`drm_mm_hole_follows`\ 

.. _`drm_mm_hole_node_start.return`:

Return
------

Start of the subsequent hole.

.. _`drm_mm_hole_node_end`:

drm_mm_hole_node_end
====================

.. c:function:: u64 drm_mm_hole_node_end(const struct drm_mm_node *hole_node)

    computes the end of the hole following \ ``node``\ 

    :param const struct drm_mm_node \*hole_node:
        drm_mm_node which implicitly tracks the following hole

.. _`drm_mm_hole_node_end.description`:

Description
-----------

This is useful for driver-specific debug dumpers. Otherwise drivers should
not inspect holes themselves. Drivers must check first whether a hole indeed
follows by looking at \ :c:func:`drm_mm_hole_follows`\ .

.. _`drm_mm_hole_node_end.return`:

Return
------

End of the subsequent hole.

.. _`drm_mm_nodes`:

drm_mm_nodes
============

.. c:function::  drm_mm_nodes( mm)

    list of nodes under the drm_mm range manager

    :param  mm:
        the struct drm_mm range manger

.. _`drm_mm_nodes.description`:

Description
-----------

As the drm_mm range manager hides its node_list deep with its
structure, extracting it looks painful and repetitive. This is
not expected to be used outside of the \ :c:func:`drm_mm_for_each_node`\ 
macros and similar internal functions.

.. _`drm_mm_nodes.return`:

Return
------

The node list, may be empty.

.. _`drm_mm_for_each_node`:

drm_mm_for_each_node
====================

.. c:function::  drm_mm_for_each_node( entry,  mm)

    iterator to walk over all allocated nodes

    :param  entry:
        &struct drm_mm_node to assign to in each iteration step

    :param  mm:
        &drm_mm allocator to walk

.. _`drm_mm_for_each_node.description`:

Description
-----------

This iterator walks over all nodes in the range allocator. It is implemented
with \ :c:func:`list_for_each`\ , so not save against removal of elements.

.. _`drm_mm_for_each_node_safe`:

drm_mm_for_each_node_safe
=========================

.. c:function::  drm_mm_for_each_node_safe( entry,  next,  mm)

    iterator to walk over all allocated nodes

    :param  entry:
        &struct drm_mm_node to assign to in each iteration step

    :param  next:
        &struct drm_mm_node to store the next step

    :param  mm:
        &drm_mm allocator to walk

.. _`drm_mm_for_each_node_safe.description`:

Description
-----------

This iterator walks over all nodes in the range allocator. It is implemented
with \ :c:func:`list_for_each_safe`\ , so save against removal of elements.

.. _`drm_mm_for_each_hole`:

drm_mm_for_each_hole
====================

.. c:function::  drm_mm_for_each_hole( pos,  mm,  hole_start,  hole_end)

    iterator to walk over all holes

    :param  pos:
        &drm_mm_node used internally to track progress

    :param  mm:
        &drm_mm allocator to walk

    :param  hole_start:
        ulong variable to assign the hole start to on each iteration

    :param  hole_end:
        ulong variable to assign the hole end to on each iteration

.. _`drm_mm_for_each_hole.description`:

Description
-----------

This iterator walks over all holes in the range allocator. It is implemented
with \ :c:func:`list_for_each`\ , so not save against removal of elements. \ ``entry``\  is used
internally and will not reflect a real drm_mm_node for the very first hole.
Hence users of this iterator may not access it.

.. _`drm_mm_for_each_hole.implementation-note`:

Implementation Note
-------------------

We need to inline list_for_each_entry in order to be able to set hole_start
and hole_end on each iteration while keeping the macro sane.

.. _`drm_mm_insert_node_generic`:

drm_mm_insert_node_generic
==========================

.. c:function:: int drm_mm_insert_node_generic(struct drm_mm *mm, struct drm_mm_node *node, u64 size, u64 alignment, unsigned long color, enum drm_mm_insert_mode mode)

    search for space and insert \ ``node``\ 

    :param struct drm_mm \*mm:
        drm_mm to allocate from

    :param struct drm_mm_node \*node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

    :param u64 alignment:
        alignment of the allocation

    :param unsigned long color:
        opaque tag value to use for this node

    :param enum drm_mm_insert_mode mode:
        fine-tune the allocation search and placement

.. _`drm_mm_insert_node_generic.description`:

Description
-----------

This is a simplified version of \ :c:func:`drm_mm_insert_node_in_range_generic`\  with no
range restrictions applied.

The preallocated node must be cleared to 0.

.. _`drm_mm_insert_node_generic.return`:

Return
------

0 on success, -ENOSPC if there's no suitable hole.

.. _`drm_mm_insert_node`:

drm_mm_insert_node
==================

.. c:function:: int drm_mm_insert_node(struct drm_mm *mm, struct drm_mm_node *node, u64 size)

    search for space and insert \ ``node``\ 

    :param struct drm_mm \*mm:
        drm_mm to allocate from

    :param struct drm_mm_node \*node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

.. _`drm_mm_insert_node.description`:

Description
-----------

This is a simplified version of \ :c:func:`drm_mm_insert_node_generic`\  with \ ``color``\  set
to 0.

The preallocated node must be cleared to 0.

.. _`drm_mm_insert_node.return`:

Return
------

0 on success, -ENOSPC if there's no suitable hole.

.. _`drm_mm_clean`:

drm_mm_clean
============

.. c:function:: bool drm_mm_clean(const struct drm_mm *mm)

    checks whether an allocator is clean

    :param const struct drm_mm \*mm:
        drm_mm allocator to check

.. _`drm_mm_clean.return`:

Return
------

True if the allocator is completely free, false if there's still a node
allocated in it.

.. _`drm_mm_for_each_node_in_range`:

drm_mm_for_each_node_in_range
=============================

.. c:function::  drm_mm_for_each_node_in_range( node__,  mm__,  start__,  end__)

    iterator to walk over a range of allocated nodes

    :param  node__:
        drm_mm_node structure to assign to in each iteration step

    :param  mm__:
        drm_mm allocator to walk

    :param  start__:
        starting offset, the first node will overlap this

    :param  end__:
        ending offset, the last node will start before this (but may overlap)

.. _`drm_mm_for_each_node_in_range.description`:

Description
-----------

This iterator walks over all nodes in the range allocator that lie
between \ ``start``\  and \ ``end``\ . It is implemented similarly to \ :c:func:`list_for_each`\ ,
but using the internal interval tree to accelerate the search for the
starting node, and so not safe against removal of elements. It assumes
that \ ``end``\  is within (or is the upper limit of) the drm_mm allocator.
If [@start, \ ``end``\ ] are beyond the range of the drm_mm, the iterator may walk
over the special _unallocated_ \ :c:type:`drm_mm.head_node <drm_mm>`\ , and may even continue
indefinitely.

.. _`drm_mm_scan_init`:

drm_mm_scan_init
================

.. c:function:: void drm_mm_scan_init(struct drm_mm_scan *scan, struct drm_mm *mm, u64 size, u64 alignment, unsigned long color, enum drm_mm_insert_mode mode)

    initialize lru scanning

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

    :param enum drm_mm_insert_mode mode:
        fine-tune the allocation search and placement

.. _`drm_mm_scan_init.description`:

Description
-----------

This is a simplified version of \ :c:func:`drm_mm_scan_init_with_range`\  with no range
restrictions applied.

This simply sets up the scanning routines with the parameters for the desired
hole.

.. _`drm_mm_scan_init.warning`:

Warning
-------

As long as the scan list is non-empty, no other operations than
adding/removing nodes to/from the scan list are allowed.

.. This file was automatic generated / don't edit.

