.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gmc_v9_0.c

.. _`gmc_v9_0_flush_gpu_tlb`:

gmc_v9_0_flush_gpu_tlb
======================

.. c:function:: void gmc_v9_0_flush_gpu_tlb(struct amdgpu_device *adev, uint32_t vmid)

    gart tlb flush callback

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vmid:
        vm instance to flush
    :type vmid: uint32_t

.. _`gmc_v9_0_flush_gpu_tlb.description`:

Description
-----------

Flush the TLB for the requested page table.

.. _`gmc_v9_0_set_pte_pde`:

gmc_v9_0_set_pte_pde
====================

.. c:function:: int gmc_v9_0_set_pte_pde(struct amdgpu_device *adev, void *cpu_pt_addr, uint32_t gpu_page_idx, uint64_t addr, uint64_t flags)

    update the page tables using MMIO

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param cpu_pt_addr:
        cpu address of the page table
    :type cpu_pt_addr: void \*

    :param gpu_page_idx:
        entry in the page table to update
    :type gpu_page_idx: uint32_t

    :param addr:
        dst addr to write into pte/pde
    :type addr: uint64_t

    :param flags:
        access flags
    :type flags: uint64_t

.. _`gmc_v9_0_set_pte_pde.description`:

Description
-----------

Update the page tables using the CPU.

.. _`gmc_v9_0_mc_init`:

gmc_v9_0_mc_init
================

.. c:function:: int gmc_v9_0_mc_init(struct amdgpu_device *adev)

    initialize the memory controller driver params

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v9_0_mc_init.description`:

Description
-----------

Look up the amount of vram, vram width, and decide how to place
vram and gart within the GPU's physical address space.
Returns 0 for success.

.. _`gmc_v9_0_gart_enable`:

gmc_v9_0_gart_enable
====================

.. c:function:: int gmc_v9_0_gart_enable(struct amdgpu_device *adev)

    gart enable

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v9_0_gart_disable`:

gmc_v9_0_gart_disable
=====================

.. c:function:: void gmc_v9_0_gart_disable(struct amdgpu_device *adev)

    gart disable

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v9_0_gart_disable.description`:

Description
-----------

This disables all VM page table.

.. This file was automatic generated / don't edit.

