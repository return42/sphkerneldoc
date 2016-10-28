.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gfx.c

.. _`amdgpu_gfx_scratch_get`:

amdgpu_gfx_scratch_get
======================

.. c:function:: int amdgpu_gfx_scratch_get(struct amdgpu_device *adev, uint32_t *reg)

    Allocate a scratch register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t \*reg:
        scratch register mmio offset

.. _`amdgpu_gfx_scratch_get.description`:

Description
-----------

Allocate a CP scratch register for use by the driver (all asics).
Returns 0 on success or -EINVAL on failure.

.. _`amdgpu_gfx_scratch_free`:

amdgpu_gfx_scratch_free
=======================

.. c:function:: void amdgpu_gfx_scratch_free(struct amdgpu_device *adev, uint32_t reg)

    Free a scratch register

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t reg:
        scratch register mmio offset

.. _`amdgpu_gfx_scratch_free.description`:

Description
-----------

Free a CP scratch register allocated for use by the driver (all asics)

.. This file was automatic generated / don't edit.

