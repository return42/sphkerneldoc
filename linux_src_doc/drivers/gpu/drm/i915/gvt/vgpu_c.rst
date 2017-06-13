.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/vgpu.c

.. _`intel_gvt_init_vgpu_types`:

intel_gvt_init_vgpu_types
=========================

.. c:function:: int intel_gvt_init_vgpu_types(struct intel_gvt *gvt)

    initialize vGPU type list

    :param struct intel_gvt \*gvt:
        GVT device

.. _`intel_gvt_init_vgpu_types.description`:

Description
-----------

Initialize vGPU type list based on available resource.

.. _`intel_gvt_activate_vgpu`:

intel_gvt_activate_vgpu
=======================

.. c:function:: void intel_gvt_activate_vgpu(struct intel_vgpu *vgpu)

    activate a virtual GPU

    :param struct intel_vgpu \*vgpu:
        virtual GPU

.. _`intel_gvt_activate_vgpu.description`:

Description
-----------

This function is called when user wants to activate a virtual GPU.

.. _`intel_gvt_deactivate_vgpu`:

intel_gvt_deactivate_vgpu
=========================

.. c:function:: void intel_gvt_deactivate_vgpu(struct intel_vgpu *vgpu)

    deactivate a virtual GPU

    :param struct intel_vgpu \*vgpu:
        virtual GPU

.. _`intel_gvt_deactivate_vgpu.description`:

Description
-----------

This function is called when user wants to deactivate a virtual GPU.
All virtual GPU runtime information will be destroyed.

.. _`intel_gvt_destroy_vgpu`:

intel_gvt_destroy_vgpu
======================

.. c:function:: void intel_gvt_destroy_vgpu(struct intel_vgpu *vgpu)

    destroy a virtual GPU

    :param struct intel_vgpu \*vgpu:
        virtual GPU

.. _`intel_gvt_destroy_vgpu.description`:

Description
-----------

This function is called when user wants to destroy a virtual GPU.

.. _`intel_gvt_create_idle_vgpu`:

intel_gvt_create_idle_vgpu
==========================

.. c:function:: struct intel_vgpu *intel_gvt_create_idle_vgpu(struct intel_gvt *gvt)

    create an idle virtual GPU

    :param struct intel_gvt \*gvt:
        GVT device

.. _`intel_gvt_create_idle_vgpu.description`:

Description
-----------

This function is called when user wants to create an idle virtual GPU.

.. _`intel_gvt_create_idle_vgpu.return`:

Return
------

pointer to intel_vgpu, error pointer if failed.

.. _`intel_gvt_destroy_idle_vgpu`:

intel_gvt_destroy_idle_vgpu
===========================

.. c:function:: void intel_gvt_destroy_idle_vgpu(struct intel_vgpu *vgpu)

    destroy an idle virtual GPU

    :param struct intel_vgpu \*vgpu:
        virtual GPU

.. _`intel_gvt_destroy_idle_vgpu.description`:

Description
-----------

This function is called when user wants to destroy an idle virtual GPU.

.. _`intel_gvt_create_vgpu`:

intel_gvt_create_vgpu
=====================

.. c:function:: struct intel_vgpu *intel_gvt_create_vgpu(struct intel_gvt *gvt, struct intel_vgpu_type *type)

    create a virtual GPU

    :param struct intel_gvt \*gvt:
        GVT device

    :param struct intel_vgpu_type \*type:
        type of the vGPU to create

.. _`intel_gvt_create_vgpu.description`:

Description
-----------

This function is called when user wants to create a virtual GPU.

.. _`intel_gvt_create_vgpu.return`:

Return
------

pointer to intel_vgpu, error pointer if failed.

.. _`intel_gvt_reset_vgpu_locked`:

intel_gvt_reset_vgpu_locked
===========================

.. c:function:: void intel_gvt_reset_vgpu_locked(struct intel_vgpu *vgpu, bool dmlr, unsigned int engine_mask)

    reset a virtual GPU by DMLR or GT reset

    :param struct intel_vgpu \*vgpu:
        virtual GPU

    :param bool dmlr:
        vGPU Device Model Level Reset or GT Reset

    :param unsigned int engine_mask:
        engines to reset for GT reset

.. _`intel_gvt_reset_vgpu_locked.description`:

Description
-----------

This function is called when user wants to reset a virtual GPU through
device model reset or GT reset. The caller should hold the gvt lock.

vGPU Device Model Level Reset (DMLR) simulates the PCI level reset to reset
the whole vGPU to default state as when it is created. This vGPU function
is required both for functionary and security concerns.The ultimate goal
of vGPU FLR is that reuse a vGPU instance by virtual machines. When we
assign a vGPU to a virtual machine we must isse such reset first.

Full GT Reset and Per-Engine GT Reset are soft reset flow for GPU engines
(Render, Blitter, Video, Video Enhancement). It is defined by GPU Spec.
Unlike the FLR, GT reset only reset particular resource of a vGPU per
the reset request. Guest driver can issue a GT reset by programming the
virtual GDRST register to reset specific virtual GPU engine or all
engines.

The parameter dev_level is to identify if we will do DMLR or GT reset.
The parameter engine_mask is to specific the engines that need to be
resetted. If value ALL_ENGINES is given for engine_mask, it means
the caller requests a full GT reset that we will reset all virtual
GPU engines. For FLR, engine_mask is ignored.

.. _`intel_gvt_reset_vgpu`:

intel_gvt_reset_vgpu
====================

.. c:function:: void intel_gvt_reset_vgpu(struct intel_vgpu *vgpu)

    reset a virtual GPU (Function Level)

    :param struct intel_vgpu \*vgpu:
        virtual GPU

.. _`intel_gvt_reset_vgpu.description`:

Description
-----------

This function is called when user wants to reset a virtual GPU.

.. This file was automatic generated / don't edit.

