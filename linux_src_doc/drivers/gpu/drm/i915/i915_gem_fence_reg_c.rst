.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_fence_reg.c

.. _`i915_vma_put_fence`:

i915_vma_put_fence
==================

.. c:function:: int i915_vma_put_fence(struct i915_vma *vma)

    force-remove fence for a VMA

    :param struct i915_vma \*vma:
        vma to map linearly (not through a fence reg)

.. _`i915_vma_put_fence.description`:

Description
-----------

This function force-removes any fence from the given object, which is useful
if the kernel wants to do untiled GTT access.

.. _`i915_vma_put_fence.return`:

Return
------


0 on success, negative error code on failure.

.. _`i915_vma_get_fence`:

i915_vma_get_fence
==================

.. c:function:: int i915_vma_get_fence(struct i915_vma *vma)

    set up fencing for a vma

    :param struct i915_vma \*vma:
        vma to map through a fence reg

.. _`i915_vma_get_fence.description`:

Description
-----------

When mapping objects through the GTT, userspace wants to be able to write
to them without having to worry about swizzling if the object is tiled.
This function walks the fence regs looking for a free one for \ ``obj``\ ,
stealing one if it can't find any.

It then sets up the reg based on the object's properties: address, pitch
and tiling format.

For an untiled surface, this removes any existing fence.

.. _`i915_vma_get_fence.return`:

Return
------


0 on success, negative error code on failure.

.. _`i915_gem_restore_fences`:

i915_gem_restore_fences
=======================

.. c:function:: void i915_gem_restore_fences(struct drm_i915_private *dev_priv)

    restore fence state

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`i915_gem_restore_fences.description`:

Description
-----------

Restore the hw fence state to match the software tracking again, to be called
after a gpu reset and on resume. Note that on runtime suspend we only cancel
the fences, to be reacquired by the user later.

.. _`i915_gem_detect_bit_6_swizzle`:

i915_gem_detect_bit_6_swizzle
=============================

.. c:function:: void i915_gem_detect_bit_6_swizzle(struct drm_i915_private *dev_priv)

    detect bit 6 swizzling pattern

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`i915_gem_detect_bit_6_swizzle.description`:

Description
-----------

Detects bit 6 swizzling of address lookup between IGD access and CPU
access through main memory.

.. _`i915_gem_object_do_bit_17_swizzle`:

i915_gem_object_do_bit_17_swizzle
=================================

.. c:function:: void i915_gem_object_do_bit_17_swizzle(struct drm_i915_gem_object *obj, struct sg_table *pages)

    fixup bit 17 swizzling

    :param struct drm_i915_gem_object \*obj:
        i915 GEM buffer object

    :param struct sg_table \*pages:
        the scattergather list of physical pages

.. _`i915_gem_object_do_bit_17_swizzle.description`:

Description
-----------

This function fixes up the swizzling in case any page frame number for this
object has changed in bit 17 since that state has been saved with
\ :c:func:`i915_gem_object_save_bit_17_swizzle`\ .

This is called when pinning backing storage again, since the kernel is free
to move unpinned backing storage around (either by directly moving pages or
by swapping them out and back in again).

.. _`i915_gem_object_save_bit_17_swizzle`:

i915_gem_object_save_bit_17_swizzle
===================================

.. c:function:: void i915_gem_object_save_bit_17_swizzle(struct drm_i915_gem_object *obj, struct sg_table *pages)

    save bit 17 swizzling

    :param struct drm_i915_gem_object \*obj:
        i915 GEM buffer object

    :param struct sg_table \*pages:
        the scattergather list of physical pages

.. _`i915_gem_object_save_bit_17_swizzle.description`:

Description
-----------

This function saves the bit 17 of each page frame number so that swizzling
can be fixed up later on with \ :c:func:`i915_gem_object_do_bit_17_swizzle`\ . This must
be called before the backing storage can be unpinned.

.. This file was automatic generated / don't edit.

