.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gmc.h

.. _`amdgpu_gmc_vram_full_visible`:

amdgpu_gmc_vram_full_visible
============================

.. c:function:: bool amdgpu_gmc_vram_full_visible(struct amdgpu_gmc *gmc)

    Check if full VRAM is visible through the BAR

    :param gmc:
        *undescribed*
    :type gmc: struct amdgpu_gmc \*

.. _`amdgpu_gmc_vram_full_visible.return`:

Return
------

True if full VRAM is visible through the BAR

.. _`amdgpu_gmc_sign_extend`:

amdgpu_gmc_sign_extend
======================

.. c:function:: uint64_t amdgpu_gmc_sign_extend(uint64_t addr)

    sign extend the given gmc address

    :param addr:
        address to extend
    :type addr: uint64_t

.. This file was automatic generated / don't edit.

