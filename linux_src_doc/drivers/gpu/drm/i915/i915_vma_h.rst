.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_vma.h

.. _`i915_vma_pin_iomap`:

i915_vma_pin_iomap
==================

.. c:function:: void __iomem *i915_vma_pin_iomap(struct i915_vma *vma)

    calls ioremap_wc to map the GGTT VMA via the aperture

    :param vma:
        VMA to iomap
    :type vma: struct i915_vma \*

.. _`i915_vma_pin_iomap.description`:

Description
-----------

The passed in VMA has to be pinned in the global GTT mappable region.
An extra pinning of the VMA is acquired for the return iomapping,
the caller must call i915_vma_unpin_iomap to relinquish the pinning
after the iomapping is no longer required.

Callers must hold the struct_mutex.

Returns a valid iomapped pointer or ERR_PTR.

.. _`i915_vma_unpin_iomap`:

i915_vma_unpin_iomap
====================

.. c:function:: void i915_vma_unpin_iomap(struct i915_vma *vma)

    unpins the mapping returned from i915_vma_iomap

    :param vma:
        VMA to unpin
    :type vma: struct i915_vma \*

.. _`i915_vma_unpin_iomap.description`:

Description
-----------

Unpins the previously iomapped VMA from \ :c:func:`i915_vma_pin_iomap`\ .

Callers must hold the struct_mutex. This function is only valid to be
called on a VMA previously iomapped by the caller with \ :c:func:`i915_vma_pin_iomap`\ .

.. _`i915_vma_pin_fence`:

i915_vma_pin_fence
==================

.. c:function:: int i915_vma_pin_fence(struct i915_vma *vma)

    pin fencing state

    :param vma:
        vma to pin fencing for
    :type vma: struct i915_vma \*

.. _`i915_vma_pin_fence.description`:

Description
-----------

This pins the fencing state (whether tiled or untiled) to make sure the
vma (and its object) is ready to be used as a scanout target. Fencing
status must be synchronize first by calling \ :c:func:`i915_vma_get_fence`\ :

The resulting fence pin reference must be released again with
\ :c:func:`i915_vma_unpin_fence`\ .

.. _`i915_vma_pin_fence.return`:

Return
------


True if the vma has a fence, false otherwise.

.. _`i915_vma_unpin_fence`:

i915_vma_unpin_fence
====================

.. c:function:: void i915_vma_unpin_fence(struct i915_vma *vma)

    unpin fencing state

    :param vma:
        vma to unpin fencing for
    :type vma: struct i915_vma \*

.. _`i915_vma_unpin_fence.description`:

Description
-----------

This releases the fence pin reference acquired through
i915_vma_pin_fence. It will handle both objects with and without an
attached fence correctly, callers do not need to distinguish this.

.. _`for_each_ggtt_vma`:

for_each_ggtt_vma
=================

.. c:function::  for_each_ggtt_vma( V,  OBJ)

    Iterate over the GGTT VMA belonging to an object.

    :param V:
        the #i915_vma iterator
    :type V: 

    :param OBJ:
        the #drm_i915_gem_object
    :type OBJ: 

.. _`for_each_ggtt_vma.description`:

Description
-----------

GGTT VMA are placed at the being of the object's vma_list, see
\ :c:func:`vma_create`\ , so we can stop our walk as soon as we see a ppgtt VMA,
or the list is empty ofc.

.. This file was automatic generated / don't edit.

