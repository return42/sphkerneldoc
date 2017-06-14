.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_fence_reg.c

.. _`fence-register-handling`:

fence register handling
=======================

Important to avoid confusions: "fences" in the i915 driver are not execution
fences used to track command completion but hardware detiler objects which
wrap a given range of the global GTT. Each platform has only a fairly limited
set of these objects.

Fences are used to detile GTT memory mappings. They're also connected to the
hardware frontbuffer render tracking and hence interact with frontbuffer
compression. Furthermore on older platforms fences are required for tiled
objects used by the display engine. They can also be used by the render
engine - they're required for blitter commands and are optional for render
commands. But on gen4+ both display (with the exception of fbc) and rendering
have their own tiling state bits and don't need fences.

Also note that fences only support X and Y tiling and hence can't be used for
the fancier new tiling formats like W, Ys and Yf.

Finally note that because fences are such a restricted resource they're
dynamically associated with objects. Furthermore fence state is committed to
the hardware lazily to avoid unnecessary stalls on gen2/3. Therefore code must
explicitly call \ :c:func:`i915_gem_object_get_fence`\  to synchronize fencing status
for cpu access. Also note that some code wants an unfenced view, for those
cases the fence can be removed forcefully with \ :c:func:`i915_gem_object_put_fence`\ .

Internally these functions will synchronize with userspace access by removing
CPU ptes into GTT mmaps (not the GTT ptes themselves) as needed.

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

.. _`i915_gem_revoke_fences`:

i915_gem_revoke_fences
======================

.. c:function:: void i915_gem_revoke_fences(struct drm_i915_private *dev_priv)

    revoke fence state

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`i915_gem_revoke_fences.description`:

Description
-----------

Removes all GTT mmappings via the fence registers. This forces any user
of the fence to reacquire that fence before continuing with their access.
One use is during GPU reset where the fence register is lost and we need to
revoke concurrent userspace access via GTT mmaps until the hardware has been
reset and the fence registers have been restored.

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

.. _`tiling-swizzling-details`:

tiling swizzling details
========================

The idea behind tiling is to increase cache hit rates by rearranging
pixel data so that a group of pixel accesses are in the same cacheline.
Performance improvement from doing this on the back/depth buffer are on
the order of 30%.

Intel architectures make this somewhat more complicated, though, by
adjustments made to addressing of data when the memory is in interleaved
mode (matched pairs of DIMMS) to improve memory bandwidth.
For interleaved memory, the CPU sends every sequential 64 bytes
to an alternate memory channel so it can get the bandwidth from both.

The GPU also rearranges its accesses for increased bandwidth to interleaved
memory, and it matches what the CPU does for non-tiled.  However, when tiled
it does it a little differently, since one walks addresses not just in the
X direction but also Y.  So, along with alternating channels when bit
6 of the address flips, it also alternates when other bits flip --  Bits 9
(every 512 bytes, an X tile scanline) and 10 (every two X tile scanlines)
are common to both the 915 and 965-class hardware.

The CPU also sometimes XORs in higher bits as well, to improve
bandwidth doing strided access like we do so frequently in graphics.  This
is called "Channel XOR Randomization" in the MCH documentation.  The result
is that the CPU is XORing in either bit 11 or bit 17 to bit 6 of its address
decode.

All of this bit 6 XORing has an effect on our memory management,
as we need to make sure that the 3d driver can correctly address object
contents.

If we don't have interleaved memory, all tiling is safe and no swizzling is
required.

When bit 17 is XORed in, we simply refuse to tile at all.  Bit
17 is not just a page offset, so as we page an object out and back in,
individual pages in it will have different bit 17 addresses, resulting in
each 64 bytes being swapped with its neighbor!

Otherwise, if interleaved, we have to tell the 3d driver what the address
swizzling it needs to do is, since it's writing with the CPU to the pages
(bit 6 and potentially bit 11 XORed in), and the GPU is reading from the
pages (bit 6, 9, and 10 XORed in), resulting in a cumulative bit swizzling
required by the CPU of XORing in bit 6, 9, 10, and potentially 11, in order
to match what the GPU expects.

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

