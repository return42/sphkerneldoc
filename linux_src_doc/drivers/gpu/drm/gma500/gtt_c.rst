.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/gtt.c

.. _`psb_gtt_mask_pte`:

psb_gtt_mask_pte
================

.. c:function:: uint32_t psb_gtt_mask_pte(uint32_t pfn, int type)

    generate GTT pte entry

    :param pfn:
        page number to encode
    :type pfn: uint32_t

    :param type:
        type of memory in the GTT
    :type type: int

.. _`psb_gtt_mask_pte.description`:

Description
-----------

Set the GTT entry for the appropriate memory type.

.. _`psb_gtt_entry`:

psb_gtt_entry
=============

.. c:function:: u32 __iomem *psb_gtt_entry(struct drm_device *dev, struct gtt_range *r)

    find the GTT entries for a gtt_range

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param r:
        our GTT range
    :type r: struct gtt_range \*

.. _`psb_gtt_entry.description`:

Description
-----------

Given a gtt_range object return the GTT offset of the page table
entries for this gtt_range

.. _`psb_gtt_insert`:

psb_gtt_insert
==============

.. c:function:: int psb_gtt_insert(struct drm_device *dev, struct gtt_range *r, int resume)

    put an object into the GTT

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param r:
        our GTT range
    :type r: struct gtt_range \*

    :param resume:
        on resume
    :type resume: int

.. _`psb_gtt_insert.description`:

Description
-----------

Take our preallocated GTT range and insert the GEM object into
the GTT. This is protected via the gtt mutex which the caller
must hold.

.. _`psb_gtt_remove`:

psb_gtt_remove
==============

.. c:function:: void psb_gtt_remove(struct drm_device *dev, struct gtt_range *r)

    remove an object from the GTT

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param r:
        our GTT range
    :type r: struct gtt_range \*

.. _`psb_gtt_remove.description`:

Description
-----------

Remove a preallocated GTT range from the GTT. Overwrite all the
page table entries with the dummy page. This is protected via the gtt
mutex which the caller must hold.

.. _`psb_gtt_roll`:

psb_gtt_roll
============

.. c:function:: void psb_gtt_roll(struct drm_device *dev, struct gtt_range *r, int roll)

    set scrolling position

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param r:
        the gtt mapping we are using
    :type r: struct gtt_range \*

    :param roll:
        roll offset
    :type roll: int

.. _`psb_gtt_roll.description`:

Description
-----------

Roll an existing pinned mapping by moving the pages through the GTT.
This allows us to implement hardware scrolling on the consoles without
a 2D engine

.. _`psb_gtt_attach_pages`:

psb_gtt_attach_pages
====================

.. c:function:: int psb_gtt_attach_pages(struct gtt_range *gt)

    attach and pin GEM pages

    :param gt:
        the gtt range
    :type gt: struct gtt_range \*

.. _`psb_gtt_attach_pages.description`:

Description
-----------

Pin and build an in kernel list of the pages that back our GEM object.
While we hold this the pages cannot be swapped out. This is protected
via the gtt mutex which the caller must hold.

.. _`psb_gtt_detach_pages`:

psb_gtt_detach_pages
====================

.. c:function:: void psb_gtt_detach_pages(struct gtt_range *gt)

    attach and pin GEM pages

    :param gt:
        the gtt range
    :type gt: struct gtt_range \*

.. _`psb_gtt_detach_pages.description`:

Description
-----------

Undo the effect of psb_gtt_attach_pages. At this point the pages
must have been removed from the GTT as they could now be paged out
and move bus address. This is protected via the gtt mutex which the
caller must hold.

.. _`psb_gtt_pin`:

psb_gtt_pin
===========

.. c:function:: int psb_gtt_pin(struct gtt_range *gt)

    pin pages into the GTT

    :param gt:
        range to pin
    :type gt: struct gtt_range \*

.. _`psb_gtt_pin.description`:

Description
-----------

Pin a set of pages into the GTT. The pins are refcounted so that
multiple pins need multiple unpins to undo.

Non GEM backed objects treat this as a no-op as they are always GTT
backed objects.

.. _`psb_gtt_unpin`:

psb_gtt_unpin
=============

.. c:function:: void psb_gtt_unpin(struct gtt_range *gt)

    Drop a GTT pin requirement

    :param gt:
        range to pin
    :type gt: struct gtt_range \*

.. _`psb_gtt_unpin.description`:

Description
-----------

Undoes the effect of psb_gtt_pin. On the last drop the GEM object
will be removed from the GTT which will also drop the page references
and allow the VM to clean up or page stuff.

Non GEM backed objects treat this as a no-op as they are always GTT
backed objects.

.. _`psb_gtt_alloc_range`:

psb_gtt_alloc_range
===================

.. c:function:: struct gtt_range *psb_gtt_alloc_range(struct drm_device *dev, int len, const char *name, int backed, u32 align)

    allocate GTT address space

    :param dev:
        Our DRM device
    :type dev: struct drm_device \*

    :param len:
        length (bytes) of address space required
    :type len: int

    :param name:
        resource name
    :type name: const char \*

    :param backed:
        resource should be backed by stolen pages
    :type backed: int

    :param align:
        requested alignment
    :type align: u32

.. _`psb_gtt_alloc_range.description`:

Description
-----------

Ask the kernel core to find us a suitable range of addresses
to use for a GTT mapping.

Returns a gtt_range structure describing the object, or NULL on
error. On successful return the resource is both allocated and marked
as in use.

.. _`psb_gtt_free_range`:

psb_gtt_free_range
==================

.. c:function:: void psb_gtt_free_range(struct drm_device *dev, struct gtt_range *gt)

    release GTT address space

    :param dev:
        our DRM device
    :type dev: struct drm_device \*

    :param gt:
        a mapping created with psb_gtt_alloc_range
    :type gt: struct gtt_range \*

.. _`psb_gtt_free_range.description`:

Description
-----------

Release a resource that was allocated with psb_gtt_alloc_range. If the
object has been pinned by mmap users we clean this up here currently.

.. This file was automatic generated / don't edit.

