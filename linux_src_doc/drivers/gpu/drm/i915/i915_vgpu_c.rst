.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_vgpu.c

.. _`intel-gvt-g-guest-support`:

Intel GVT-g guest support
=========================

Intel GVT-g is a graphics virtualization technology which shares the
GPU among multiple virtual machines on a time-sharing basis. Each
virtual machine is presented a virtual GPU (vGPU), which has equivalent
features as the underlying physical GPU (pGPU), so i915 driver can run
seamlessly in a virtual machine. This file provides vGPU specific
optimizations when running in a virtual machine, to reduce the complexity
of vGPU emulation and to improve the overall performance.

A primary function introduced here is so-called "address space ballooning"
technique. Intel GVT-g partitions global graphics memory among multiple VMs,
so each VM can directly access a portion of the memory without hypervisor's
intervention, e.g. filling textures or queuing commands. However with the
partitioning an unmodified i915 driver would assume a smaller graphics
memory starting from address ZERO, then requires vGPU emulation module to
translate the graphics address between 'guest view' and 'host view', for
all registers and command opcodes which contain a graphics memory address.
To reduce the complexity, Intel GVT-g introduces "address space ballooning",
by telling the exact partitioning knowledge to each guest i915 driver, which
then reserves and prevents non-allocated portions from allocation. Thus vGPU
emulation module only needs to scan and validate graphics addresses without
complexity of address translation.

.. _`i915_check_vgpu`:

i915_check_vgpu
===============

.. c:function:: void i915_check_vgpu(struct drm_i915_private *dev_priv)

    detect virtual GPU

    :param dev_priv:
        i915 device private
    :type dev_priv: struct drm_i915_private \*

.. _`i915_check_vgpu.description`:

Description
-----------

This function is called at the initialization stage, to detect whether
running on a vGPU.

.. _`intel_vgt_deballoon`:

intel_vgt_deballoon
===================

.. c:function:: void intel_vgt_deballoon(struct drm_i915_private *dev_priv)

    deballoon reserved graphics address trunks

    :param dev_priv:
        i915 device private data
    :type dev_priv: struct drm_i915_private \*

.. _`intel_vgt_deballoon.description`:

Description
-----------

This function is called to deallocate the ballooned-out graphic memory, when
driver is unloaded or when ballooning fails.

.. _`intel_vgt_balloon`:

intel_vgt_balloon
=================

.. c:function:: int intel_vgt_balloon(struct drm_i915_private *dev_priv)

    balloon out reserved graphics address trunks

    :param dev_priv:
        i915 device private data
    :type dev_priv: struct drm_i915_private \*

.. _`intel_vgt_balloon.description`:

Description
-----------

This function is called at the initialization stage, to balloon out the
graphic address space allocated to other vGPUs, by marking these spaces as
reserved. The ballooning related knowledge(starting address and size of
the mappable/unmappable graphic memory) is described in the vgt_if structure
in a reserved mmio range.

To give an example, the drawing below depicts one typical scenario after
ballooning. Here the vGPU1 has 2 pieces of graphic address spaces ballooned
out each for the mappable and the non-mappable part. From the vGPU1 point of
view, the total size is the same as the physical one, with the start address
of its graphic space being zero. Yet there are some portions ballooned out(
the shadow part, which are marked as reserved by drm allocator). From the
host point of view, the graphic address space is partitioned by multiple
vGPUs in different VMs. ::

                        vGPU1 view         Host view
             0 ------> +-----------+     +-----------+
               ^       |###########|     |   vGPU3   |
               |       |###########|     +-----------+
               |       |###########|     |   vGPU2   |
               |       +-----------+     +-----------+
        mappable GM    | available | ==> |   vGPU1   |
               |       +-----------+     +-----------+
               |       |###########|     |           |
               v       |###########|     |   Host    |
               +=======+===========+     +===========+
               ^       |###########|     |   vGPU3   |
               |       |###########|     +-----------+
               |       |###########|     |   vGPU2   |
               |       +-----------+     +-----------+
      unmappable GM    | available | ==> |   vGPU1   |
               |       +-----------+     +-----------+
               |       |###########|     |           |
               |       |###########|     |   Host    |
               v       |###########|     |           |
 total GM size ------> +-----------+     +-----------+

.. _`intel_vgt_balloon.return`:

Return
------

zero on success, non-zero if configuration invalid or ballooning failed

.. This file was automatic generated / don't edit.

