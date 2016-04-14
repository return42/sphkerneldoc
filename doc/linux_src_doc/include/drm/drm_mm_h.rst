.. -*- coding: utf-8; mode: rst -*-

========
drm_mm.h
========

.. _`drm_mm_node_allocated`:

drm_mm_node_allocated
=====================

.. c:function:: bool drm_mm_node_allocated (struct drm_mm_node *node)

    checks whether a node is allocated

    :param struct drm_mm_node \*node:
        drm_mm_node to check


.. _`drm_mm_node_allocated.description`:

Description
-----------

Drivers should use this helpers for proper encapusulation of drm_mm
internals.

Returns:
True if the ``node`` is allocated.


.. _`drm_mm_initialized`:

drm_mm_initialized
==================

.. c:function:: bool drm_mm_initialized (struct drm_mm *mm)

    checks whether an allocator is initialized

    :param struct drm_mm \*mm:
        drm_mm to check


.. _`drm_mm_initialized.description`:

Description
-----------

Drivers should use this helpers for proper encapusulation of drm_mm
internals.

Returns:
True if the ``mm`` is initialized.


.. _`drm_mm_hole_node_start`:

drm_mm_hole_node_start
======================

.. c:function:: u64 drm_mm_hole_node_start (struct drm_mm_node *hole_node)

    computes the start of the hole following @node

    :param struct drm_mm_node \*hole_node:
        drm_mm_node which implicitly tracks the following hole


.. _`drm_mm_hole_node_start.description`:

Description
-----------

This is useful for driver-sepific debug dumpers. Otherwise drivers should not
inspect holes themselves. Drivers must check first whether a hole indeed
follows by looking at node->hole_follows.

Returns:
Start of the subsequent hole.


.. _`drm_mm_hole_node_end`:

drm_mm_hole_node_end
====================

.. c:function:: u64 drm_mm_hole_node_end (struct drm_mm_node *hole_node)

    computes the end of the hole following @node

    :param struct drm_mm_node \*hole_node:
        drm_mm_node which implicitly tracks the following hole


.. _`drm_mm_hole_node_end.description`:

Description
-----------

This is useful for driver-sepific debug dumpers. Otherwise drivers should not
inspect holes themselves. Drivers must check first whether a hole indeed
follows by looking at node->hole_follows.

Returns:
End of the subsequent hole.


.. _`drm_mm_for_each_node`:

drm_mm_for_each_node
====================

.. c:function:: drm_mm_for_each_node ( entry,  mm)

    iterator to walk over all allocated nodes

    :param entry:
        drm_mm_node structure to assign to in each iteration step

    :param mm:
        drm_mm allocator to walk


.. _`drm_mm_for_each_node.description`:

Description
-----------

This iterator walks over all nodes in the range allocator. It is implemented
with list_for_each, so not save against removal of elements.


.. _`drm_mm_for_each_hole`:

drm_mm_for_each_hole
====================

.. c:function:: drm_mm_for_each_hole ( entry,  mm,  hole_start,  hole_end)

    iterator to walk over all holes

    :param entry:
        drm_mm_node used internally to track progress

    :param mm:
        drm_mm allocator to walk

    :param hole_start:
        ulong variable to assign the hole start to on each iteration

    :param hole_end:
        ulong variable to assign the hole end to on each iteration


.. _`drm_mm_for_each_hole.description`:

Description
-----------

This iterator walks over all holes in the range allocator. It is implemented
with list_for_each, so not save against removal of elements. ``entry`` is used
internally and will not reflect a real drm_mm_node for the very first hole.
Hence users of this iterator may not access it.

Implementation Note:
We need to inline list_for_each_entry in order to be able to set hole_start
and hole_end on each iteration while keeping the macro sane.

The __drm_mm_for_each_hole version is similar, but with added support for
going backwards.


.. _`drm_mm_insert_node`:

drm_mm_insert_node
==================

.. c:function:: int drm_mm_insert_node (struct drm_mm *mm, struct drm_mm_node *node, u64 size, unsigned alignment, enum drm_mm_search_flags flags)

    search for space and insert @node

    :param struct drm_mm \*mm:
        drm_mm to allocate from

    :param struct drm_mm_node \*node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

    :param unsigned alignment:
        alignment of the allocation

    :param enum drm_mm_search_flags flags:
        flags to fine-tune the allocation


.. _`drm_mm_insert_node.description`:

Description
-----------

This is a simplified version of :c:func:`drm_mm_insert_node_generic` with ``color`` set
to 0.

The preallocated node must be cleared to 0.

Returns:
0 on success, -ENOSPC if there's no suitable hole.


.. _`drm_mm_insert_node_in_range`:

drm_mm_insert_node_in_range
===========================

.. c:function:: int drm_mm_insert_node_in_range (struct drm_mm *mm, struct drm_mm_node *node, u64 size, unsigned alignment, u64 start, u64 end, enum drm_mm_search_flags flags)

    ranged search for space and insert @node

    :param struct drm_mm \*mm:
        drm_mm to allocate from

    :param struct drm_mm_node \*node:
        preallocate node to insert

    :param u64 size:
        size of the allocation

    :param unsigned alignment:
        alignment of the allocation

    :param u64 start:
        start of the allowed range for this node

    :param u64 end:
        end of the allowed range for this node

    :param enum drm_mm_search_flags flags:
        flags to fine-tune the allocation


.. _`drm_mm_insert_node_in_range.description`:

Description
-----------

This is a simplified version of :c:func:`drm_mm_insert_node_in_range_generic` with
``color`` set to 0.

The preallocated node must be cleared to 0.

Returns:
0 on success, -ENOSPC if there's no suitable hole.

