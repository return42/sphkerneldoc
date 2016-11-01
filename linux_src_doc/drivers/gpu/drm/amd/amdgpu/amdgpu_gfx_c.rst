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

.. _`amdgpu_gfx_parse_disable_cu`:

amdgpu_gfx_parse_disable_cu
===========================

.. c:function:: void amdgpu_gfx_parse_disable_cu(unsigned *mask, unsigned max_se, unsigned max_sh)

    Parse the disable_cu module parameter

    :param unsigned \*mask:
        array in which the per-shader array disable masks will be stored

    :param unsigned max_se:
        number of SEs

    :param unsigned max_sh:
        number of SHs

.. _`amdgpu_gfx_parse_disable_cu.description`:

Description
-----------

The bitmask of CUs to be disabled in the shader array determined by se and
sh is stored in mask[se \* max_sh + sh].

.. This file was automatic generated / don't edit.

