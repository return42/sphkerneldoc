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

.. _`intel_gvt_reset_vgpu`:

intel_gvt_reset_vgpu
====================

.. c:function:: void intel_gvt_reset_vgpu(struct intel_vgpu *vgpu)

    reset a virtual GPU

    :param struct intel_vgpu \*vgpu:
        virtual GPU

.. _`intel_gvt_reset_vgpu.description`:

Description
-----------

This function is called when user wants to reset a virtual GPU.

.. This file was automatic generated / don't edit.

