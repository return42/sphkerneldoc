.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_gtt.h

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

.. This file was automatic generated / don't edit.

