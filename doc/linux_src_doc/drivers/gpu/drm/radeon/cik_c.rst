.. -*- coding: utf-8; mode: rst -*-

=====
cik.c
=====


.. _`cik_get_allowed_info_register`:

cik_get_allowed_info_register
=============================

.. c:function:: int cik_get_allowed_info_register (struct radeon_device *rdev, u32 reg, u32 *val)

    fetch the register for the info ioctl

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 reg:
        register offset in bytes

    :param u32 \*val:
        register value



.. _`cik_get_allowed_info_register.description`:

Description
-----------

Returns 0 for success or -EINVAL for an invalid register



.. _`cik_get_xclk`:

cik_get_xclk
============

.. c:function:: u32 cik_get_xclk (struct radeon_device *rdev)

    get the xclk

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_get_xclk.description`:

Description
-----------

Returns the reference clock used by the gfx engine
(CIK).



.. _`cik_mm_rdoorbell`:

cik_mm_rdoorbell
================

.. c:function:: u32 cik_mm_rdoorbell (struct radeon_device *rdev, u32 index)

    read a doorbell dword

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 index:
        doorbell index



.. _`cik_mm_rdoorbell.description`:

Description
-----------

Returns the value in the doorbell aperture at the
requested doorbell index (CIK).



.. _`cik_mm_wdoorbell`:

cik_mm_wdoorbell
================

.. c:function:: void cik_mm_wdoorbell (struct radeon_device *rdev, u32 index, u32 v)

    write a doorbell dword

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 index:
        doorbell index

    :param u32 v:
        value to write



.. _`cik_mm_wdoorbell.description`:

Description
-----------

Writes ``v`` to the doorbell aperture at the
requested doorbell index (CIK).



.. _`cik_srbm_select`:

cik_srbm_select
===============

.. c:function:: void cik_srbm_select (struct radeon_device *rdev, u32 me, u32 pipe, u32 queue, u32 vmid)

    select specific register instances

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 me:
        selected ME (micro engine)

    :param u32 pipe:
        pipe

    :param u32 queue:
        queue

    :param u32 vmid:
        VMID



.. _`cik_srbm_select.description`:

Description
-----------

Switches the currently active registers instances.  Some
registers are instanced per VMID, others are instanced per
me/pipe/queue combination.



.. _`ci_mc_load_microcode`:

ci_mc_load_microcode
====================

.. c:function:: int ci_mc_load_microcode (struct radeon_device *rdev)

    load MC ucode into the hw

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`ci_mc_load_microcode.description`:

Description
-----------

Load the GDDR MC ucode into the hw (CIK).
Returns 0 on success, error on failure.



.. _`cik_init_microcode`:

cik_init_microcode
==================

.. c:function:: int cik_init_microcode (struct radeon_device *rdev)

    load ucode images from disk

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.



.. _`cik_tiling_mode_table_init`:

cik_tiling_mode_table_init
==========================

.. c:function:: void cik_tiling_mode_table_init (struct radeon_device *rdev)

    init the hw tiling table

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_tiling_mode_table_init.description`:

Description
-----------

Starting with SI, the tiling setup is done globally in a
set of 32 tiling modes.  Rather than selecting each set of
parameters per surface as on older asics, we just select
which index in the tiling table we want to use, and the
surface uses those parameters (CIK).



.. _`cik_select_se_sh`:

cik_select_se_sh
================

.. c:function:: void cik_select_se_sh (struct radeon_device *rdev, u32 se_num, u32 sh_num)

    select which SE, SH to address

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 se_num:
        shader engine to address

    :param u32 sh_num:
        sh block to address



.. _`cik_select_se_sh.description`:

Description
-----------

Select which SE, SH combinations to address. Certain
registers are instanced per SE or SH.  0xffffffff means
broadcast to all SEs or SHs (CIK).



.. _`cik_create_bitmask`:

cik_create_bitmask
==================

.. c:function:: u32 cik_create_bitmask (u32 bit_width)

    create a bitmask

    :param u32 bit_width:
        length of the mask



.. _`cik_create_bitmask.description`:

Description
-----------

create a variable length bit mask (CIK).
Returns the bitmask.



.. _`cik_get_rb_disabled`:

cik_get_rb_disabled
===================

.. c:function:: u32 cik_get_rb_disabled (struct radeon_device *rdev, u32 max_rb_num_per_se, u32 sh_per_se)

    computes the mask of disabled RBs

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 max_rb_num_per_se:

        *undescribed*

    :param u32 sh_per_se:
        number of SH blocks per SE for the asic



.. _`cik_get_rb_disabled.description`:

Description
-----------

Calculates the bitmask of disabled RBs (CIK).
Returns the disabled RB bitmask.



.. _`cik_setup_rb`:

cik_setup_rb
============

.. c:function:: void cik_setup_rb (struct radeon_device *rdev, u32 se_num, u32 sh_per_se, u32 max_rb_num_per_se)

    setup the RBs on the asic

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 se_num:
        number of SEs (shader engines) for the asic

    :param u32 sh_per_se:
        number of SH blocks per SE for the asic

    :param u32 max_rb_num_per_se:

        *undescribed*



.. _`cik_setup_rb.description`:

Description
-----------

Configures per-SE/SH RB registers (CIK).



.. _`cik_gpu_init`:

cik_gpu_init
============

.. c:function:: void cik_gpu_init (struct radeon_device *rdev)

    setup the 3D engine

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_gpu_init.description`:

Description
-----------

Configures the 3D engine and tiling configuration
registers so that the 3D engine is usable.



.. _`cik_scratch_init`:

cik_scratch_init
================

.. c:function:: void cik_scratch_init (struct radeon_device *rdev)

    setup driver info for CP scratch regs

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_scratch_init.description`:

Description
-----------

Set up the number and offset of the CP scratch registers.



.. _`cik_scratch_init.note`:

NOTE
----

use of CP scratch registers is a legacy inferface and
is not used by default on newer asics (r6xx+).  On newer asics,
memory buffers are used for fences rather than scratch regs.



.. _`cik_ring_test`:

cik_ring_test
=============

.. c:function:: int cik_ring_test (struct radeon_device *rdev, struct radeon_ring *ring)

    basic gfx ring test

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information



.. _`cik_ring_test.description`:

Description
-----------

Allocate a scratch register and write to it using the gfx ring (CIK).
Provides a basic gfx ring test to verify that the ring is working.
Used by :c:func:`cik_cp_gfx_resume`;
Returns 0 on success, error on failure.



.. _`cik_hdp_flush_cp_ring_emit`:

cik_hdp_flush_cp_ring_emit
==========================

.. c:function:: void cik_hdp_flush_cp_ring_emit (struct radeon_device *rdev, int ridx)

    emit an hdp flush on the cp

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ridx:
        radeon ring index



.. _`cik_hdp_flush_cp_ring_emit.description`:

Description
-----------

Emits an hdp flush on the cp.



.. _`cik_fence_gfx_ring_emit`:

cik_fence_gfx_ring_emit
=======================

.. c:function:: void cik_fence_gfx_ring_emit (struct radeon_device *rdev, struct radeon_fence *fence)

    emit a fence on the gfx ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        radeon fence object



.. _`cik_fence_gfx_ring_emit.description`:

Description
-----------

Emits a fence sequnce number on the gfx ring and flushes
GPU caches.



.. _`cik_fence_compute_ring_emit`:

cik_fence_compute_ring_emit
===========================

.. c:function:: void cik_fence_compute_ring_emit (struct radeon_device *rdev, struct radeon_fence *fence)

    emit a fence on the compute ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        radeon fence object



.. _`cik_fence_compute_ring_emit.description`:

Description
-----------

Emits a fence sequnce number on the compute ring and flushes
GPU caches.



.. _`cik_semaphore_ring_emit`:

cik_semaphore_ring_emit
=======================

.. c:function:: bool cik_semaphore_ring_emit (struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit a semaphore on the CP ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon ring buffer object

    :param struct radeon_semaphore \*semaphore:
        radeon semaphore object

    :param bool emit_wait:
        Is this a sempahore wait?



.. _`cik_semaphore_ring_emit.description`:

Description
-----------

Emits a semaphore signal/wait packet to the CP ring and prevents the PFP
from running ahead of semaphore waits.



.. _`cik_copy_cpdma`:

cik_copy_cpdma
==============

.. c:function:: struct radeon_fence *cik_copy_cpdma (struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

    copy pages using the CP DMA engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param uint64_t src_offset:
        src GPU address

    :param uint64_t dst_offset:
        dst GPU address

    :param unsigned num_gpu_pages:
        number of GPU pages to xfer

    :param struct reservation_object \*resv:
        reservation object to sync to



.. _`cik_copy_cpdma.description`:

Description
-----------

Copy GPU paging using the CP DMA engine (CIK+).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.



.. _`cik_ring_ib_execute`:

cik_ring_ib_execute
===================

.. c:function:: void cik_ring_ib_execute (struct radeon_device *rdev, struct radeon_ib *ib)

    emit an IB (Indirect Buffer) on the gfx ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        radeon indirect buffer object



.. _`cik_ring_ib_execute.description`:

Description
-----------

Emits a DE (drawing engine) or CE (constant engine) IB
on the gfx ring.  IBs are usually generated by userspace
acceleration drivers and submitted to the kernel for
scheduling on the ring.  This function schedules the IB
on the gfx ring for execution by the GPU.



.. _`cik_ib_test`:

cik_ib_test
===========

.. c:function:: int cik_ib_test (struct radeon_device *rdev, struct radeon_ring *ring)

    basic gfx ring IB test

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information



.. _`cik_ib_test.description`:

Description
-----------

Allocate an IB and execute it on the gfx ring (CIK).
Provides a basic gfx ring test to verify that IBs are working.
Returns 0 on success, error on failure.



.. _`cik_cp_gfx_enable`:

cik_cp_gfx_enable
=================

.. c:function:: void cik_cp_gfx_enable (struct radeon_device *rdev, bool enable)

    enable/disable the gfx CP MEs

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param bool enable:
        enable or disable the MEs



.. _`cik_cp_gfx_enable.description`:

Description
-----------

Halts or unhalts the gfx MEs.



.. _`cik_cp_gfx_load_microcode`:

cik_cp_gfx_load_microcode
=========================

.. c:function:: int cik_cp_gfx_load_microcode (struct radeon_device *rdev)

    load the gfx CP ME ucode

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_gfx_load_microcode.description`:

Description
-----------

Loads the gfx PFP, ME, and CE ucode.
Returns 0 for success, -EINVAL if the ucode is not available.



.. _`cik_cp_gfx_start`:

cik_cp_gfx_start
================

.. c:function:: int cik_cp_gfx_start (struct radeon_device *rdev)

    start the gfx ring

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_gfx_start.description`:

Description
-----------

Enables the ring and loads the clear state context and other
packets required to init the ring.
Returns 0 for success, error for failure.



.. _`cik_cp_gfx_fini`:

cik_cp_gfx_fini
===============

.. c:function:: void cik_cp_gfx_fini (struct radeon_device *rdev)

    stop the gfx ring

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_gfx_fini.description`:

Description
-----------

Stop the gfx ring and tear down the driver ring
info.



.. _`cik_cp_gfx_resume`:

cik_cp_gfx_resume
=================

.. c:function:: int cik_cp_gfx_resume (struct radeon_device *rdev)

    setup the gfx ring buffer registers

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_gfx_resume.description`:

Description
-----------

Program the location and size of the gfx ring buffer
and test it to make sure it's working.
Returns 0 for success, error for failure.



.. _`cik_cp_compute_enable`:

cik_cp_compute_enable
=====================

.. c:function:: void cik_cp_compute_enable (struct radeon_device *rdev, bool enable)

    enable/disable the compute CP MEs

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param bool enable:
        enable or disable the MEs



.. _`cik_cp_compute_enable.description`:

Description
-----------

Halts or unhalts the compute MEs.



.. _`cik_cp_compute_load_microcode`:

cik_cp_compute_load_microcode
=============================

.. c:function:: int cik_cp_compute_load_microcode (struct radeon_device *rdev)

    load the compute CP ME ucode

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_compute_load_microcode.description`:

Description
-----------

Loads the compute MEC1:c:type:`struct 2 <2>` ucode.
Returns 0 for success, -EINVAL if the ucode is not available.



.. _`cik_cp_compute_start`:

cik_cp_compute_start
====================

.. c:function:: int cik_cp_compute_start (struct radeon_device *rdev)

    start the compute queues

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_compute_start.description`:

Description
-----------

Enable the compute queues.
Returns 0 for success, error for failure.



.. _`cik_cp_compute_fini`:

cik_cp_compute_fini
===================

.. c:function:: void cik_cp_compute_fini (struct radeon_device *rdev)

    stop the compute queues

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_compute_fini.description`:

Description
-----------

Stop the compute queues and tear down the driver queue
info.



.. _`cik_cp_compute_resume`:

cik_cp_compute_resume
=====================

.. c:function:: int cik_cp_compute_resume (struct radeon_device *rdev)

    setup the compute queue registers

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_cp_compute_resume.description`:

Description
-----------

Program the compute queues and test them to make sure they
are working.
Returns 0 for success, error for failure.



.. _`cik_gpu_check_soft_reset`:

cik_gpu_check_soft_reset
========================

.. c:function:: u32 cik_gpu_check_soft_reset (struct radeon_device *rdev)

    check which blocks are busy

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_gpu_check_soft_reset.description`:

Description
-----------

Check which blocks are busy and return the relevant reset
mask to be used by :c:func:`cik_gpu_soft_reset`.
Returns a mask of the blocks to be reset.



.. _`cik_gpu_soft_reset`:

cik_gpu_soft_reset
==================

.. c:function:: void cik_gpu_soft_reset (struct radeon_device *rdev, u32 reset_mask)

    soft reset GPU

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 reset_mask:
        mask of which blocks to reset



.. _`cik_gpu_soft_reset.description`:

Description
-----------

Soft reset the blocks specified in ``reset_mask``\ .



.. _`cik_asic_reset`:

cik_asic_reset
==============

.. c:function:: int cik_asic_reset (struct radeon_device *rdev)

    soft reset GPU

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_asic_reset.description`:

Description
-----------

Look up which blocks are hung and attempt
to reset them.
Returns 0 for success.



.. _`cik_gfx_is_lockup`:

cik_gfx_is_lockup
=================

.. c:function:: bool cik_gfx_is_lockup (struct radeon_device *rdev, struct radeon_ring *ring)

    check if the 3D engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information



.. _`cik_gfx_is_lockup.description`:

Description
-----------

Check if the 3D engine is locked up (CIK).
Returns true if the engine is locked, false if not.



.. _`cik_mc_program`:

cik_mc_program
==============

.. c:function:: void cik_mc_program (struct radeon_device *rdev)

    program the GPU memory controller

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_mc_program.description`:

Description
-----------

Set the location of vram, gart, and AGP in the GPU's
physical address space (CIK).



.. _`cik_mc_init`:

cik_mc_init
===========

.. c:function:: int cik_mc_init (struct radeon_device *rdev)

    initialize the memory controller driver params

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_mc_init.description`:

Description
-----------

Look up the amount of vram, vram width, and decide how to place
vram and gart within the GPU's physical address space (CIK).
Returns 0 for success.



.. _`cik_pcie_gart_tlb_flush`:

cik_pcie_gart_tlb_flush
=======================

.. c:function:: void cik_pcie_gart_tlb_flush (struct radeon_device *rdev)

    gart tlb flush callback

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_pcie_gart_tlb_flush.description`:

Description
-----------

Flush the TLB for the VMID 0 page table (CIK).



.. _`cik_pcie_gart_enable`:

cik_pcie_gart_enable
====================

.. c:function:: int cik_pcie_gart_enable (struct radeon_device *rdev)

    gart enable

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_pcie_gart_enable.description`:

Description
-----------

This sets up the TLBs, programs the page tables for VMID0,
sets up the hw for VMIDs 1-15 which are allocated on
demand, and sets up the global locations for the LDS, GDS,
and GPUVM for FSA64 clients (CIK).
Returns 0 for success, errors for failure.



.. _`cik_pcie_gart_disable`:

cik_pcie_gart_disable
=====================

.. c:function:: void cik_pcie_gart_disable (struct radeon_device *rdev)

    gart disable

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_pcie_gart_disable.description`:

Description
-----------

This disables all VM page table (CIK).



.. _`cik_pcie_gart_fini`:

cik_pcie_gart_fini
==================

.. c:function:: void cik_pcie_gart_fini (struct radeon_device *rdev)

    vm fini callback

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_pcie_gart_fini.description`:

Description
-----------

Tears down the driver GART/VM setup (CIK).



.. _`cik_ib_parse`:

cik_ib_parse
============

.. c:function:: int cik_ib_parse (struct radeon_device *rdev, struct radeon_ib *ib)

    vm ib_parse callback

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        indirect buffer pointer



.. _`cik_ib_parse.description`:

Description
-----------

CIK uses hw IB checking so this is a nop (CIK).



.. _`cik_vm_init`:

cik_vm_init
===========

.. c:function:: int cik_vm_init (struct radeon_device *rdev)

    cik vm init callback

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_vm_init.description`:

Description
-----------

Inits cik specific vm parameters (number of VMs, base of vram for
VMIDs 1-15) (CIK).
Returns 0 for success.



.. _`cik_vm_fini`:

cik_vm_fini
===========

.. c:function:: void cik_vm_fini (struct radeon_device *rdev)

    cik vm fini callback

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_vm_fini.description`:

Description
-----------

Tear down any asic specific VM setup (CIK).



.. _`cik_vm_decode_fault`:

cik_vm_decode_fault
===================

.. c:function:: void cik_vm_decode_fault (struct radeon_device *rdev, u32 status, u32 addr, u32 mc_client)

    print human readable fault info

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 status:
        VM_CONTEXT1_PROTECTION_FAULT_STATUS register value

    :param u32 addr:
        VM_CONTEXT1_PROTECTION_FAULT_ADDR register value

    :param u32 mc_client:

        *undescribed*



.. _`cik_vm_decode_fault.description`:

Description
-----------

Print human readable fault information (CIK).



.. _`cik_vm_flush`:

cik_vm_flush
============

.. c:function:: void cik_vm_flush (struct radeon_device *rdev, struct radeon_ring *ring, unsigned vm_id, uint64_t pd_addr)

    cik vm flush using the CP

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:

        *undescribed*

    :param unsigned vm_id:

        *undescribed*

    :param uint64_t pd_addr:

        *undescribed*



.. _`cik_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using the CP (CIK).



.. _`cik_rlc_stop`:

cik_rlc_stop
============

.. c:function:: void cik_rlc_stop (struct radeon_device *rdev)

    stop the RLC ME

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_rlc_stop.description`:

Description
-----------

Halt the RLC ME (MicroEngine) (CIK).



.. _`cik_rlc_start`:

cik_rlc_start
=============

.. c:function:: void cik_rlc_start (struct radeon_device *rdev)

    start the RLC ME

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_rlc_start.description`:

Description
-----------

Unhalt the RLC ME (MicroEngine) (CIK).



.. _`cik_rlc_resume`:

cik_rlc_resume
==============

.. c:function:: int cik_rlc_resume (struct radeon_device *rdev)

    setup the RLC hw

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_rlc_resume.description`:

Description
-----------

Initialize the RLC registers, load the ucode,
and start the RLC (CIK).
Returns 0 for success, -EINVAL if the ucode is not available.



.. _`cik_enable_interrupts`:

cik_enable_interrupts
=====================

.. c:function:: void cik_enable_interrupts (struct radeon_device *rdev)

    Enable the interrupt ring buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_enable_interrupts.description`:

Description
-----------

Enable the interrupt ring buffer (CIK).



.. _`cik_disable_interrupts`:

cik_disable_interrupts
======================

.. c:function:: void cik_disable_interrupts (struct radeon_device *rdev)

    Disable the interrupt ring buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_disable_interrupts.description`:

Description
-----------

Disable the interrupt ring buffer (CIK).



.. _`cik_disable_interrupt_state`:

cik_disable_interrupt_state
===========================

.. c:function:: void cik_disable_interrupt_state (struct radeon_device *rdev)

    Disable all interrupt sources

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_disable_interrupt_state.description`:

Description
-----------

Clear all interrupt enable bits used by the driver (CIK).



.. _`cik_irq_init`:

cik_irq_init
============

.. c:function:: int cik_irq_init (struct radeon_device *rdev)

    init and enable the interrupt ring

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_init.description`:

Description
-----------

Allocate a ring buffer for the interrupt controller,
enable the RLC, disable interrupts, enable the IH
ring buffer and enable it (CIK).
Called at device load and reume.
Returns 0 for success, errors for failure.



.. _`cik_irq_set`:

cik_irq_set
===========

.. c:function:: int cik_irq_set (struct radeon_device *rdev)

    enable/disable interrupt sources

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_set.description`:

Description
-----------

Enable interrupt sources on the GPU (vblanks, hpd,
etc.) (CIK).
Returns 0 for success, errors for failure.



.. _`cik_irq_ack`:

cik_irq_ack
===========

.. c:function:: void cik_irq_ack (struct radeon_device *rdev)

    ack interrupt sources

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_ack.description`:

Description
-----------

Ack interrupt sources on the GPU (vblanks, hpd,
etc.) (CIK).  Certain interrupts sources are sw
generated and do not require an explicit ack.



.. _`cik_irq_disable`:

cik_irq_disable
===============

.. c:function:: void cik_irq_disable (struct radeon_device *rdev)

    disable interrupts

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_disable.description`:

Description
-----------

Disable interrupts on the hw (CIK).



.. _`cik_irq_suspend`:

cik_irq_suspend
===============

.. c:function:: void cik_irq_suspend (struct radeon_device *rdev)

    disable interrupts for suspend

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_suspend.description`:

Description
-----------

Disable interrupts and stop the RLC (CIK).
Used for suspend.



.. _`cik_irq_fini`:

cik_irq_fini
============

.. c:function:: void cik_irq_fini (struct radeon_device *rdev)

    tear down interrupt support

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_fini.description`:

Description
-----------

Disable interrupts on the hw and free the IH ring
buffer (CIK).
Used for driver unload.



.. _`cik_get_ih_wptr`:

cik_get_ih_wptr
===============

.. c:function:: u32 cik_get_ih_wptr (struct radeon_device *rdev)

    get the IH ring buffer wptr

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_get_ih_wptr.description`:

Description
-----------

Get the IH ring buffer wptr from either the register
or the writeback memory buffer (CIK).  Also check for
ring buffer overflow and deal with it.
Used by :c:func:`cik_irq_process`.
Returns the value of the wptr.



.. _`cik_irq_process`:

cik_irq_process
===============

.. c:function:: int cik_irq_process (struct radeon_device *rdev)

    interrupt handler

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_irq_process.description`:

Description
-----------

Interrupt hander (CIK).  Walk the IH ring,
ack interrupts and schedule work to handle
interrupt events.
Returns irq process return code.



.. _`cik_startup`:

cik_startup
===========

.. c:function:: int cik_startup (struct radeon_device *rdev)

    program the asic to a functional state

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_startup.description`:

Description
-----------

Programs the asic to a functional state (CIK).
Called by :c:func:`cik_init` and :c:func:`cik_resume`.
Returns 0 for success, error for failure.



.. _`cik_resume`:

cik_resume
==========

.. c:function:: int cik_resume (struct radeon_device *rdev)

    resume the asic to a functional state

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_resume.description`:

Description
-----------

Programs the asic to a functional state (CIK).
Called at resume.
Returns 0 for success, error for failure.



.. _`cik_suspend`:

cik_suspend
===========

.. c:function:: int cik_suspend (struct radeon_device *rdev)

    suspend the asic

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_suspend.description`:

Description
-----------

Bring the chip into a state suitable for suspend (CIK).
Called at suspend.
Returns 0 for success.



.. _`cik_init`:

cik_init
========

.. c:function:: int cik_init (struct radeon_device *rdev)

    asic specific driver and hw init

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_init.description`:

Description
-----------

Setup asic specific driver variables and program the hw
to a functional state (CIK).
Called at driver startup.
Returns 0 for success, errors for failure.



.. _`cik_fini`:

cik_fini
========

.. c:function:: void cik_fini (struct radeon_device *rdev)

    asic specific driver and hw fini

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_fini.description`:

Description
-----------

Tear down the asic specific driver variables and program the hw
to an idle state (CIK).
Called at driver unload.



.. _`dce8_line_buffer_adjust`:

dce8_line_buffer_adjust
=======================

.. c:function:: u32 dce8_line_buffer_adjust (struct radeon_device *rdev, struct radeon_crtc *radeon_crtc, struct drm_display_mode *mode)

    Set up the line buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_crtc \*radeon_crtc:
        the selected display controller

    :param struct drm_display_mode \*mode:
        the current display mode on the selected display
        controller



.. _`dce8_line_buffer_adjust.description`:

Description
-----------

Setup up the line buffer allocation for
the selected display controller (CIK).
Returns the line buffer size in pixels.



.. _`cik_get_number_of_dram_channels`:

cik_get_number_of_dram_channels
===============================

.. c:function:: u32 cik_get_number_of_dram_channels (struct radeon_device *rdev)

    get the number of dram channels

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_get_number_of_dram_channels.description`:

Description
-----------

Look up the number of video ram channels (CIK).
Used for display watermark bandwidth calculations
Returns the number of dram channels



.. _`dce8_dram_bandwidth`:

dce8_dram_bandwidth
===================

.. c:function:: u32 dce8_dram_bandwidth (struct dce8_wm_params *wm)

    get the dram bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_dram_bandwidth.description`:

Description
-----------

Calculate the raw dram bandwidth (CIK).
Used for display watermark bandwidth calculations
Returns the dram bandwidth in MBytes/s



.. _`dce8_dram_bandwidth_for_display`:

dce8_dram_bandwidth_for_display
===============================

.. c:function:: u32 dce8_dram_bandwidth_for_display (struct dce8_wm_params *wm)

    get the dram bandwidth for display

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_dram_bandwidth_for_display.description`:

Description
-----------

Calculate the dram bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the dram bandwidth for display in MBytes/s



.. _`dce8_data_return_bandwidth`:

dce8_data_return_bandwidth
==========================

.. c:function:: u32 dce8_data_return_bandwidth (struct dce8_wm_params *wm)

    get the data return bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_data_return_bandwidth.description`:

Description
-----------

Calculate the data return bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the data return bandwidth in MBytes/s



.. _`dce8_dmif_request_bandwidth`:

dce8_dmif_request_bandwidth
===========================

.. c:function:: u32 dce8_dmif_request_bandwidth (struct dce8_wm_params *wm)

    get the dmif bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_dmif_request_bandwidth.description`:

Description
-----------

Calculate the dmif bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the dmif bandwidth in MBytes/s



.. _`dce8_available_bandwidth`:

dce8_available_bandwidth
========================

.. c:function:: u32 dce8_available_bandwidth (struct dce8_wm_params *wm)

    get the min available bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_available_bandwidth.description`:

Description
-----------

Calculate the min available bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the min available bandwidth in MBytes/s



.. _`dce8_average_bandwidth`:

dce8_average_bandwidth
======================

.. c:function:: u32 dce8_average_bandwidth (struct dce8_wm_params *wm)

    get the average available bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_average_bandwidth.description`:

Description
-----------

Calculate the average available bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the average available bandwidth in MBytes/s



.. _`dce8_latency_watermark`:

dce8_latency_watermark
======================

.. c:function:: u32 dce8_latency_watermark (struct dce8_wm_params *wm)

    get the latency watermark

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_latency_watermark.description`:

Description
-----------

Calculate the latency watermark (CIK).
Used for display watermark bandwidth calculations
Returns the latency watermark in ns



.. _`dce8_average_bandwidth_vs_dram_bandwidth_for_display`:

dce8_average_bandwidth_vs_dram_bandwidth_for_display
====================================================

.. c:function:: bool dce8_average_bandwidth_vs_dram_bandwidth_for_display (struct dce8_wm_params *wm)

    check average and available dram bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_average_bandwidth_vs_dram_bandwidth_for_display.description`:

Description
-----------

Check if the display average bandwidth fits in the display
dram bandwidth (CIK).
Used for display watermark bandwidth calculations
Returns true if the display fits, false if not.



.. _`dce8_average_bandwidth_vs_available_bandwidth`:

dce8_average_bandwidth_vs_available_bandwidth
=============================================

.. c:function:: bool dce8_average_bandwidth_vs_available_bandwidth (struct dce8_wm_params *wm)

    check average and available bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_average_bandwidth_vs_available_bandwidth.description`:

Description
-----------

Check if the display average bandwidth fits in the display
available bandwidth (CIK).
Used for display watermark bandwidth calculations
Returns true if the display fits, false if not.



.. _`dce8_check_latency_hiding`:

dce8_check_latency_hiding
=========================

.. c:function:: bool dce8_check_latency_hiding (struct dce8_wm_params *wm)

    check latency hiding

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce8_check_latency_hiding.description`:

Description
-----------

Check latency hiding (CIK).
Used for display watermark bandwidth calculations
Returns true if the display fits, false if not.



.. _`dce8_program_watermarks`:

dce8_program_watermarks
=======================

.. c:function:: void dce8_program_watermarks (struct radeon_device *rdev, struct radeon_crtc *radeon_crtc, u32 lb_size, u32 num_heads)

    program display watermarks

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_crtc \*radeon_crtc:
        the selected display controller

    :param u32 lb_size:
        line buffer size

    :param u32 num_heads:
        number of display controllers in use



.. _`dce8_program_watermarks.description`:

Description
-----------

Calculate and program the display watermarks for the
selected display controller (CIK).



.. _`dce8_bandwidth_update`:

dce8_bandwidth_update
=====================

.. c:function:: void dce8_bandwidth_update (struct radeon_device *rdev)

    program display watermarks

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`dce8_bandwidth_update.description`:

Description
-----------

Calculate and program the display watermarks and line
buffer allocation (CIK).



.. _`cik_get_gpu_clock_counter`:

cik_get_gpu_clock_counter
=========================

.. c:function:: uint64_t cik_get_gpu_clock_counter (struct radeon_device *rdev)

    return GPU clock counter snapshot

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`cik_get_gpu_clock_counter.description`:

Description
-----------

Fetches a GPU clock counter snapshot (SI).
Returns the 64 bit clock counter snapshot.

