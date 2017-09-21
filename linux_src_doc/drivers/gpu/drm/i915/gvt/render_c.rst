.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/render.c

.. _`intel_gvt_switch_mmio`:

intel_gvt_switch_mmio
=====================

.. c:function:: void intel_gvt_switch_mmio(struct intel_vgpu *pre, struct intel_vgpu *next, int ring_id)

    switch mmio context of specific engine

    :param struct intel_vgpu \*pre:
        the last vGPU that own the engine

    :param struct intel_vgpu \*next:
        the vGPU to switch to

    :param int ring_id:
        specify the engine

.. _`intel_gvt_switch_mmio.description`:

Description
-----------

If pre is null indicates that host own the engine. If next is null
indicates that we are switching to host workload.

.. This file was automatic generated / don't edit.

