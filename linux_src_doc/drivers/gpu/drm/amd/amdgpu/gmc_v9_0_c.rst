.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gmc_v9_0.c

.. _`gmc_v9_0_gart_flush_gpu_tlb`:

gmc_v9_0_gart_flush_gpu_tlb
===========================

.. c:function:: void gmc_v9_0_gart_flush_gpu_tlb(struct amdgpu_device *adev, uint32_t vmid)

    gart tlb flush callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t vmid:
        vm instance to flush

.. _`gmc_v9_0_gart_flush_gpu_tlb.description`:

Description
-----------

Flush the TLB for the requested page table.

.. _`gmc_v9_0_gart_set_pte_pde`:

gmc_v9_0_gart_set_pte_pde
=========================

.. c:function:: int gmc_v9_0_gart_set_pte_pde(struct amdgpu_device *adev, void *cpu_pt_addr, uint32_t gpu_page_idx, uint64_t addr, uint64_t flags)

    update the page tables using MMIO

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param void \*cpu_pt_addr:
        cpu address of the page table

    :param uint32_t gpu_page_idx:
        entry in the page table to update

    :param uint64_t addr:
        dst addr to write into pte/pde

    :param uint64_t flags:
        access flags

.. _`gmc_v9_0_gart_set_pte_pde.description`:

Description
-----------

Update the page tables using the CPU.

.. _`gmc_v9_0_mc_init`:

gmc_v9_0_mc_init
================

.. c:function:: int gmc_v9_0_mc_init(struct amdgpu_device *adev)

    initialize the memory controller driver params

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v9_0_mc_init.description`:

Description
-----------

Look up the amount of vram, vram width, and decide how to place
vram and gart within the GPU's physical address space.
Returns 0 for success.

.. _`gmc_v9_0_vm_init`:

gmc_v9_0_vm_init
================

.. c:function:: int gmc_v9_0_vm_init(struct amdgpu_device *adev)

    vm init callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v9_0_vm_init.description`:

Description
-----------

Inits vega10 specific vm parameters (number of VMs, base of vram for
VMIDs 1-15) (vega10).
Returns 0 for success.

.. _`gmc_v9_0_vm_fini`:

gmc_v9_0_vm_fini
================

.. c:function:: void gmc_v9_0_vm_fini(struct amdgpu_device *adev)

    vm fini callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v9_0_vm_fini.description`:

Description
-----------

Tear down any asic specific VM setup.

.. _`gmc_v9_0_gart_fini`:

gmc_v9_0_gart_fini
==================

.. c:function:: void gmc_v9_0_gart_fini(struct amdgpu_device *adev)

    vm fini callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v9_0_gart_fini.description`:

Description
-----------

Tears down the driver GART/VM setup (CIK).

.. _`gmc_v9_0_gart_enable`:

gmc_v9_0_gart_enable
====================

.. c:function:: int gmc_v9_0_gart_enable(struct amdgpu_device *adev)

    gart enable

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v9_0_gart_disable`:

gmc_v9_0_gart_disable
=====================

.. c:function:: void gmc_v9_0_gart_disable(struct amdgpu_device *adev)

    gart disable

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v9_0_gart_disable.description`:

Description
-----------

This disables all VM page table.

.. This file was automatic generated / don't edit.

