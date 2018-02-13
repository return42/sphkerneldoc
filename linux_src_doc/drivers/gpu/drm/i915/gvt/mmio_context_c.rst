.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/mmio_context.c

.. _`trvattl3ptrdw`:

TRVATTL3PTRDW
=============

.. c:function::  TRVATTL3PTRDW( i)

    Ref: https://01.org/linuxgraphics/documentation/hardware-specification-prms

    :param  i:
        *undescribed*

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

.. _`intel_gvt_init_engine_mmio_context`:

intel_gvt_init_engine_mmio_context
==================================

.. c:function:: void intel_gvt_init_engine_mmio_context(struct intel_gvt *gvt)

    Initiate the engine mmio list

    :param struct intel_gvt \*gvt:
        GVT device

.. This file was automatic generated / don't edit.

