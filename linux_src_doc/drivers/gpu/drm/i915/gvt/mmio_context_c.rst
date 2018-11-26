.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/mmio_context.c

.. _`intel_gvt_switch_mmio`:

intel_gvt_switch_mmio
=====================

.. c:function:: void intel_gvt_switch_mmio(struct intel_vgpu *pre, struct intel_vgpu *next, int ring_id)

    switch mmio context of specific engine

    :param pre:
        the last vGPU that own the engine
    :type pre: struct intel_vgpu \*

    :param next:
        the vGPU to switch to
    :type next: struct intel_vgpu \*

    :param ring_id:
        specify the engine
    :type ring_id: int

.. _`intel_gvt_switch_mmio.description`:

Description
-----------

If pre is null indicates that host own the engine. If next is null
indicates that we are switching to host workload.

.. _`intel_gvt_init_engine_mmio_context`:

intel_gvt_init_engine_mmio_context
==================================

.. c:function:: void intel_gvt_init_engine_mmio_context(struct intel_gvt *gvt)

    Initiate the engine mmio list

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. This file was automatic generated / don't edit.

