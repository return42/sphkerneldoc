.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gmc_v8_0.c

.. _`gmc_v8_0_init_microcode`:

gmc_v8_0_init_microcode
=======================

.. c:function:: int gmc_v8_0_init_microcode(struct amdgpu_device *adev)

    load ucode images from disk

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v8_0_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.

.. _`gmc_v8_0_tonga_mc_load_microcode`:

gmc_v8_0_tonga_mc_load_microcode
================================

.. c:function:: int gmc_v8_0_tonga_mc_load_microcode(struct amdgpu_device *adev)

    load tonga MC ucode into the hw

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v8_0_tonga_mc_load_microcode.description`:

Description
-----------

Load the GDDR MC ucode into the hw (CIK).
Returns 0 on success, error on failure.

.. _`gmc_v8_0_mc_program`:

gmc_v8_0_mc_program
===================

.. c:function:: void gmc_v8_0_mc_program(struct amdgpu_device *adev)

    program the GPU memory controller

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v8_0_mc_program.description`:

Description
-----------

Set the location of vram, gart, and AGP in the GPU's
physical address space (CIK).

.. _`gmc_v8_0_mc_init`:

gmc_v8_0_mc_init
================

.. c:function:: int gmc_v8_0_mc_init(struct amdgpu_device *adev)

    initialize the memory controller driver params

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v8_0_mc_init.description`:

Description
-----------

Look up the amount of vram, vram width, and decide how to place
vram and gart within the GPU's physical address space (CIK).
Returns 0 for success.

.. _`gmc_v8_0_flush_gpu_tlb`:

gmc_v8_0_flush_gpu_tlb
======================

.. c:function:: void gmc_v8_0_flush_gpu_tlb(struct amdgpu_device *adev, uint32_t vmid)

    gart tlb flush callback

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vmid:
        vm instance to flush
    :type vmid: uint32_t

.. _`gmc_v8_0_flush_gpu_tlb.description`:

Description
-----------

Flush the TLB for the requested page table (CIK).

.. _`gmc_v8_0_set_pte_pde`:

gmc_v8_0_set_pte_pde
====================

.. c:function:: int gmc_v8_0_set_pte_pde(struct amdgpu_device *adev, void *cpu_pt_addr, uint32_t gpu_page_idx, uint64_t addr, uint64_t flags)

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

.. _`gmc_v8_0_set_pte_pde.description`:

Description
-----------

Update the page tables using the CPU.

.. _`gmc_v8_0_set_fault_enable_default`:

gmc_v8_0_set_fault_enable_default
=================================

.. c:function:: void gmc_v8_0_set_fault_enable_default(struct amdgpu_device *adev, bool value)

    update VM fault handling

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param value:
        true redirects VM faults to the default page
    :type value: bool

.. _`gmc_v8_0_set_prt`:

gmc_v8_0_set_prt
================

.. c:function:: void gmc_v8_0_set_prt(struct amdgpu_device *adev, bool enable)

    set PRT VM fault

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param enable:
        enable/disable VM fault handling for PRT
    :type enable: bool

.. _`gmc_v8_0_gart_enable`:

gmc_v8_0_gart_enable
====================

.. c:function:: int gmc_v8_0_gart_enable(struct amdgpu_device *adev)

    gart enable

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v8_0_gart_enable.description`:

Description
-----------

This sets up the TLBs, programs the page tables for VMID0,
sets up the hw for VMIDs 1-15 which are allocated on
demand, and sets up the global locations for the LDS, GDS,
and GPUVM for FSA64 clients (CIK).
Returns 0 for success, errors for failure.

.. _`gmc_v8_0_gart_disable`:

gmc_v8_0_gart_disable
=====================

.. c:function:: void gmc_v8_0_gart_disable(struct amdgpu_device *adev)

    gart disable

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gmc_v8_0_gart_disable.description`:

Description
-----------

This disables all VM page table (CIK).

.. _`gmc_v8_0_vm_decode_fault`:

gmc_v8_0_vm_decode_fault
========================

.. c:function:: void gmc_v8_0_vm_decode_fault(struct amdgpu_device *adev, u32 status, u32 addr, u32 mc_client, unsigned pasid)

    print human readable fault info

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param status:
        VM_CONTEXT1_PROTECTION_FAULT_STATUS register value
    :type status: u32

    :param addr:
        VM_CONTEXT1_PROTECTION_FAULT_ADDR register value
    :type addr: u32

    :param mc_client:
        *undescribed*
    :type mc_client: u32

    :param pasid:
        *undescribed*
    :type pasid: unsigned

.. _`gmc_v8_0_vm_decode_fault.description`:

Description
-----------

Print human readable fault information (CIK).

.. This file was automatic generated / don't edit.

