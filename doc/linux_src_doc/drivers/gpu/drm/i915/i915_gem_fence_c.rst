.. -*- coding: utf-8; mode: rst -*-

================
i915_gem_fence.c
================



.. _xref_i915_gem_object_put_fence:

i915_gem_object_put_fence
=========================

.. c:function:: int i915_gem_object_put_fence (struct drm_i915_gem_object * obj)

    force-remove fence for an object

    :param struct drm_i915_gem_object * obj:
        object to map through a fence reg



Description
-----------

This function force-removes any fence from the given object, which is useful
if the kernel wants to do untiled GTT access.



Returns
-------



0 on success, negative error code on failure.




.. _xref_i915_gem_object_get_fence:

i915_gem_object_get_fence
=========================

.. c:function:: int i915_gem_object_get_fence (struct drm_i915_gem_object * obj)

    set up fencing for an object

    :param struct drm_i915_gem_object * obj:
        object to map through a fence reg



Description
-----------

When mapping objects through the GTT, userspace wants to be able to write
to them without having to worry about swizzling if the object is tiled.
This function walks the fence regs looking for a free one for **obj**,
stealing one if it can't find any.


It then sets up the reg based on the object's properties: address, pitch
and tiling format.


For an untiled surface, this removes any existing fence.



Returns
-------



0 on success, negative error code on failure.




.. _xref_i915_gem_object_pin_fence:

i915_gem_object_pin_fence
=========================

.. c:function:: bool i915_gem_object_pin_fence (struct drm_i915_gem_object * obj)

    pin fencing state

    :param struct drm_i915_gem_object * obj:
        object to pin fencing for



Description
-----------

This pins the fencing state (whether tiled or untiled) to make sure the
object is ready to be used as a scanout target. Fencing status must be
synchronize first by calling :c:func:`i915_gem_object_get_fence`:


The resulting fence pin reference must be released again with
:c:func:`i915_gem_object_unpin_fence`.



Returns
-------



True if the object has a fence, false otherwise.




.. _xref_i915_gem_object_unpin_fence:

i915_gem_object_unpin_fence
===========================

.. c:function:: void i915_gem_object_unpin_fence (struct drm_i915_gem_object * obj)

    unpin fencing state

    :param struct drm_i915_gem_object * obj:
        object to unpin fencing for



Description
-----------

This releases the fence pin reference acquired through
i915_gem_object_pin_fence. It will handle both objects with and without an
attached fence correctly, callers do not need to distinguish this.




.. _xref_i915_gem_restore_fences:

i915_gem_restore_fences
=======================

.. c:function:: void i915_gem_restore_fences (struct drm_device * dev)

    restore fence state

    :param struct drm_device * dev:
        DRM device



Description
-----------

Restore the hw fence state to match the software tracking again, to be called
after a gpu reset and on resume.




.. _xref_i915_gem_detect_bit_6_swizzle:

i915_gem_detect_bit_6_swizzle
=============================

.. c:function:: void i915_gem_detect_bit_6_swizzle (struct drm_device * dev)

    detect bit 6 swizzling pattern

    :param struct drm_device * dev:
        DRM device



Description
-----------

Detects bit 6 swizzling of address lookup between IGD access and CPU
access through main memory.




.. _xref_i915_gem_object_do_bit_17_swizzle:

i915_gem_object_do_bit_17_swizzle
=================================

.. c:function:: void i915_gem_object_do_bit_17_swizzle (struct drm_i915_gem_object * obj)

    fixup bit 17 swizzling

    :param struct drm_i915_gem_object * obj:
        i915 GEM buffer object



Description
-----------

This function fixes up the swizzling in case any page frame number for this
object has changed in bit 17 since that state has been saved with
:c:func:`i915_gem_object_save_bit_17_swizzle`.


This is called when pinning backing storage again, since the kernel is free
to move unpinned backing storage around (either by directly moving pages or
by swapping them out and back in again).




.. _xref_i915_gem_object_save_bit_17_swizzle:

i915_gem_object_save_bit_17_swizzle
===================================

.. c:function:: void i915_gem_object_save_bit_17_swizzle (struct drm_i915_gem_object * obj)

    save bit 17 swizzling

    :param struct drm_i915_gem_object * obj:
        i915 GEM buffer object



Description
-----------

This function saves the bit 17 of each page frame number so that swizzling
can be fixed up later on with :c:func:`i915_gem_object_do_bit_17_swizzle`. This must
be called before the backing storage can be unpinned.


