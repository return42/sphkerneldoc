.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gmc_v8_0.c

.. _`gmc_v8_0_mc_wait_for_idle`:

gmc_v8_0_mc_wait_for_idle
=========================

.. c:function:: int gmc_v8_0_mc_wait_for_idle(struct amdgpu_device *adev)

    wait for MC idle callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_mc_wait_for_idle.description`:

Description
-----------

Wait for the MC (memory controller) to be idle.
(evergreen+).
Returns 0 if the MC is idle, -1 if not.

.. _`gmc_v8_0_init_microcode`:

gmc_v8_0_init_microcode
=======================

.. c:function:: int gmc_v8_0_init_microcode(struct amdgpu_device *adev)

    load ucode images from disk

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.

.. _`gmc_v8_0_mc_load_microcode`:

gmc_v8_0_mc_load_microcode
==========================

.. c:function:: int gmc_v8_0_mc_load_microcode(struct amdgpu_device *adev)

    load MC ucode into the hw

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_mc_load_microcode.description`:

Description
-----------

Load the GDDR MC ucode into the hw (CIK).
Returns 0 on success, error on failure.

.. _`gmc_v8_0_mc_program`:

gmc_v8_0_mc_program
===================

.. c:function:: void gmc_v8_0_mc_program(struct amdgpu_device *adev)

    program the GPU memory controller

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

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

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_mc_init.description`:

Description
-----------

Look up the amount of vram, vram width, and decide how to place
vram and gart within the GPU's physical address space (CIK).
Returns 0 for success.

.. _`gmc_v8_0_gart_flush_gpu_tlb`:

gmc_v8_0_gart_flush_gpu_tlb
===========================

.. c:function:: void gmc_v8_0_gart_flush_gpu_tlb(struct amdgpu_device *adev, uint32_t vmid)

    gart tlb flush callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t vmid:
        vm instance to flush

.. _`gmc_v8_0_gart_flush_gpu_tlb.description`:

Description
-----------

Flush the TLB for the requested page table (CIK).

.. _`gmc_v8_0_gart_set_pte_pde`:

gmc_v8_0_gart_set_pte_pde
=========================

.. c:function:: int gmc_v8_0_gart_set_pte_pde(struct amdgpu_device *adev, void *cpu_pt_addr, uint32_t gpu_page_idx, uint64_t addr, uint32_t flags)

    update the page tables using MMIO

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param void \*cpu_pt_addr:
        cpu address of the page table

    :param uint32_t gpu_page_idx:
        entry in the page table to update

    :param uint64_t addr:
        dst addr to write into pte/pde

    :param uint32_t flags:
        access flags

.. _`gmc_v8_0_gart_set_pte_pde.description`:

Description
-----------

Update the page tables using the CPU.

.. _`gmc_v8_0_set_fault_enable_default`:

gmc_v8_0_set_fault_enable_default
=================================

.. c:function:: void gmc_v8_0_set_fault_enable_default(struct amdgpu_device *adev, bool value)

    update VM fault handling

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param bool value:
        true redirects VM faults to the default page

.. _`gmc_v8_0_gart_enable`:

gmc_v8_0_gart_enable
====================

.. c:function:: int gmc_v8_0_gart_enable(struct amdgpu_device *adev)

    gart enable

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

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

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_gart_disable.description`:

Description
-----------

This disables all VM page table (CIK).

.. _`gmc_v8_0_gart_fini`:

gmc_v8_0_gart_fini
==================

.. c:function:: void gmc_v8_0_gart_fini(struct amdgpu_device *adev)

    vm fini callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_gart_fini.description`:

Description
-----------

Tears down the driver GART/VM setup (CIK).

.. _`gmc_v8_0_vm_init`:

gmc_v8_0_vm_init
================

.. c:function:: int gmc_v8_0_vm_init(struct amdgpu_device *adev)

    cik vm init callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_vm_init.description`:

Description
-----------

Inits cik specific vm parameters (number of VMs, base of vram for
VMIDs 1-15) (CIK).
Returns 0 for success.

.. _`gmc_v8_0_vm_fini`:

gmc_v8_0_vm_fini
================

.. c:function:: void gmc_v8_0_vm_fini(struct amdgpu_device *adev)

    cik vm fini callback

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`gmc_v8_0_vm_fini.description`:

Description
-----------

Tear down any asic specific VM setup (CIK).

.. _`gmc_v8_0_vm_decode_fault`:

gmc_v8_0_vm_decode_fault
========================

.. c:function:: void gmc_v8_0_vm_decode_fault(struct amdgpu_device *adev, u32 status, u32 addr, u32 mc_client)

    print human readable fault info

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 status:
        VM_CONTEXT1_PROTECTION_FAULT_STATUS register value

    :param u32 addr:
        VM_CONTEXT1_PROTECTION_FAULT_ADDR register value

    :param u32 mc_client:
        *undescribed*

.. _`gmc_v8_0_vm_decode_fault.description`:

Description
-----------

Print human readable fault information (CIK).

.. This file was automatic generated / don't edit.

