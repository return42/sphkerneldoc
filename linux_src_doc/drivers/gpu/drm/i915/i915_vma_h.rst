.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_vma.h

.. _`i915_vma_pin_iomap`:

i915_vma_pin_iomap
==================

.. c:function:: void __iomem *i915_vma_pin_iomap(struct i915_vma *vma)

    calls ioremap_wc to map the GGTT VMA via the aperture

    :param struct i915_vma \*vma:
        VMA to iomap

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

    :param struct i915_vma \*vma:
        VMA to unpin

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

    :param struct i915_vma \*vma:
        vma to pin fencing for

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

    :param struct i915_vma \*vma:
        vma to unpin fencing for

.. _`i915_vma_unpin_fence.description`:

Description
-----------

This releases the fence pin reference acquired through
i915_vma_pin_fence. It will handle both objects with and without an
attached fence correctly, callers do not need to distinguish this.

.. This file was automatic generated / don't edit.

