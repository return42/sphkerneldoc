.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/aperture_gm.c

.. _`intel_vgpu_write_fence`:

intel_vgpu_write_fence
======================

.. c:function:: void intel_vgpu_write_fence(struct intel_vgpu *vgpu, u32 fence, u64 value)

    write fence registers owned by a vGPU

    :param vgpu:
        vGPU instance
    :type vgpu: struct intel_vgpu \*

    :param fence:
        vGPU fence register number
    :type fence: u32

    :param value:
        Fence register value to be written
    :type value: u64

.. _`intel_vgpu_write_fence.description`:

Description
-----------

This function is used to write fence registers owned by a vGPU. The vGPU
fence register number will be translated into HW fence register number.

.. _`intel_vgpu_free_resource`:

intel_vgpu_free_resource
========================

.. c:function:: void intel_vgpu_free_resource(struct intel_vgpu *vgpu)

    free HW resource owned by a vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_free_resource.description`:

Description
-----------

This function is used to free the HW resource owned by a vGPU.

.. _`intel_vgpu_reset_resource`:

intel_vgpu_reset_resource
=========================

.. c:function:: void intel_vgpu_reset_resource(struct intel_vgpu *vgpu)

    reset resource state owned by a vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_reset_resource.description`:

Description
-----------

This function is used to reset resource state owned by a vGPU.

.. _`intel_vgpu_alloc_resource`:

intel_vgpu_alloc_resource
=========================

.. c:function:: int intel_vgpu_alloc_resource(struct intel_vgpu *vgpu, struct intel_vgpu_creation_params *param)

    allocate HW resource for a vGPU

    :param vgpu:
        vGPU
    :type vgpu: struct intel_vgpu \*

    :param param:
        vGPU creation params
    :type param: struct intel_vgpu_creation_params \*

.. _`intel_vgpu_alloc_resource.description`:

Description
-----------

This function is used to allocate HW resource for a vGPU. User specifies
the resource configuration through the creation params.

.. _`intel_vgpu_alloc_resource.return`:

Return
------

zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

