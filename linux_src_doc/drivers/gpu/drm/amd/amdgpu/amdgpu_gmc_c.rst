.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gmc.c

.. _`amdgpu_gmc_get_pde_for_bo`:

amdgpu_gmc_get_pde_for_bo
=========================

.. c:function:: void amdgpu_gmc_get_pde_for_bo(struct amdgpu_bo *bo, int level, uint64_t *addr, uint64_t *flags)

    get the PDE for a BO

    :param bo:
        the BO to get the PDE for
    :type bo: struct amdgpu_bo \*

    :param level:
        the level in the PD hirarchy
    :type level: int

    :param addr:
        resulting addr
    :type addr: uint64_t \*

    :param flags:
        resulting flags
    :type flags: uint64_t \*

.. _`amdgpu_gmc_get_pde_for_bo.description`:

Description
-----------

Get the address and flags to be used for a PDE (Page Directory Entry).

.. _`amdgpu_gmc_pd_addr`:

amdgpu_gmc_pd_addr
==================

.. c:function:: uint64_t amdgpu_gmc_pd_addr(struct amdgpu_bo *bo)

    return the address of the root directory

    :param bo:
        *undescribed*
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_gmc_agp_addr`:

amdgpu_gmc_agp_addr
===================

.. c:function:: uint64_t amdgpu_gmc_agp_addr(struct ttm_buffer_object *bo)

    return the address in the AGP address space

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

.. _`amdgpu_gmc_agp_addr.description`:

Description
-----------

Tries to figure out how to access the BO through the AGP aperture. Returns
AMDGPU_BO_INVALID_OFFSET if that is not possible.

.. _`amdgpu_gmc_vram_location`:

amdgpu_gmc_vram_location
========================

.. c:function:: void amdgpu_gmc_vram_location(struct amdgpu_device *adev, struct amdgpu_gmc *mc, u64 base)

    try to find VRAM location

    :param adev:
        amdgpu device structure holding all necessary informations
    :type adev: struct amdgpu_device \*

    :param mc:
        memory controller structure holding memory informations
    :type mc: struct amdgpu_gmc \*

    :param base:
        base address at which to put VRAM
    :type base: u64

.. _`amdgpu_gmc_vram_location.description`:

Description
-----------

Function will try to place VRAM at base address provided
as parameter.

.. _`amdgpu_gmc_gart_location`:

amdgpu_gmc_gart_location
========================

.. c:function:: void amdgpu_gmc_gart_location(struct amdgpu_device *adev, struct amdgpu_gmc *mc)

    try to find GART location

    :param adev:
        amdgpu device structure holding all necessary informations
    :type adev: struct amdgpu_device \*

    :param mc:
        memory controller structure holding memory informations
    :type mc: struct amdgpu_gmc \*

.. _`amdgpu_gmc_gart_location.description`:

Description
-----------

Function will place try to place GART before or after VRAM.

If GART size is bigger than space left then we ajust GART size.
Thus function will never fails.

.. _`amdgpu_gmc_agp_location`:

amdgpu_gmc_agp_location
=======================

.. c:function:: void amdgpu_gmc_agp_location(struct amdgpu_device *adev, struct amdgpu_gmc *mc)

    try to find AGP location

    :param adev:
        amdgpu device structure holding all necessary informations
    :type adev: struct amdgpu_device \*

    :param mc:
        memory controller structure holding memory informations
    :type mc: struct amdgpu_gmc \*

.. _`amdgpu_gmc_agp_location.description`:

Description
-----------

Function will place try to find a place for the AGP BAR in the MC address
space.

AGP BAR will be assigned the largest available hole in the address space.
Should be called after VRAM and GART locations are setup.

.. This file was automatic generated / don't edit.

