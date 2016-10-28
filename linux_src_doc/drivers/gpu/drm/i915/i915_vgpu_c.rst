.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_vgpu.c

.. _`i915_check_vgpu`:

i915_check_vgpu
===============

.. c:function:: void i915_check_vgpu(struct drm_device *dev)

    detect virtual GPU

    :param struct drm_device \*dev:
        drm device \*

.. _`i915_check_vgpu.description`:

Description
-----------

This function is called at the initialization stage, to detect whether
running on a vGPU.

.. _`intel_vgt_deballoon`:

intel_vgt_deballoon
===================

.. c:function:: void intel_vgt_deballoon( void)

    deballoon reserved graphics address trunks

    :param  void:
        no arguments

.. _`intel_vgt_deballoon.description`:

Description
-----------

This function is called to deallocate the ballooned-out graphic memory, when
driver is unloaded or when ballooning fails.

.. _`intel_vgt_balloon`:

intel_vgt_balloon
=================

.. c:function:: int intel_vgt_balloon(struct drm_device *dev)

    balloon out reserved graphics address trunks

    :param struct drm_device \*dev:
        drm device

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
vGPUs in different VMs.

vGPU1 view         Host view
0 ------> +-----------+     +-----------+
^       \|///////////\|     \|   vGPU3   \|
\|       \|///////////\|     +-----------+
\|       \|///////////\|     \|   vGPU2   \|
\|       +-----------+     +-----------+
mappable GM    \| available \| ==> \|   vGPU1   \|
\|       +-----------+     +-----------+
\|       \|///////////\|     \|           \|
v       \|///////////\|     \|   Host    \|
+=======+===========+     +===========+
^       \|///////////\|     \|   vGPU3   \|
\|       \|///////////\|     +-----------+
\|       \|///////////\|     \|   vGPU2   \|
\|       +-----------+     +-----------+
unmappable GM    \| available \| ==> \|   vGPU1   \|
\|       +-----------+     +-----------+
\|       \|///////////\|     \|           \|
\|       \|///////////\|     \|   Host    \|
v       \|///////////\|     \|           \|
total GM size ------> +-----------+     +-----------+

.. _`intel_vgt_balloon.return`:

Return
------

zero on success, non-zero if configuration invalid or ballooning failed

.. This file was automatic generated / don't edit.

