.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gfx_v7_0.c

.. _`gfx_v7_0_init_microcode`:

gfx_v7_0_init_microcode
=======================

.. c:function:: int gfx_v7_0_init_microcode(struct amdgpu_device *adev)

    load ucode images from disk

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.

.. _`gfx_v7_0_tiling_mode_table_init`:

gfx_v7_0_tiling_mode_table_init
===============================

.. c:function:: void gfx_v7_0_tiling_mode_table_init(struct amdgpu_device *adev)

    init the hw tiling table

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_tiling_mode_table_init.description`:

Description
-----------

Starting with SI, the tiling setup is done globally in a
set of 32 tiling modes.  Rather than selecting each set of
parameters per surface as on older asics, we just select
which index in the tiling table we want to use, and the
surface uses those parameters (CIK).

.. _`gfx_v7_0_select_se_sh`:

gfx_v7_0_select_se_sh
=====================

.. c:function:: void gfx_v7_0_select_se_sh(struct amdgpu_device *adev, u32 se_num, u32 sh_num, u32 instance)

    select which SE, SH to address

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param se_num:
        shader engine to address
    :type se_num: u32

    :param sh_num:
        sh block to address
    :type sh_num: u32

    :param instance:
        *undescribed*
    :type instance: u32

.. _`gfx_v7_0_select_se_sh.description`:

Description
-----------

Select which SE, SH combinations to address. Certain
registers are instanced per SE or SH.  0xffffffff means
broadcast to all SEs or SHs (CIK).

.. _`gfx_v7_0_get_rb_active_bitmap`:

gfx_v7_0_get_rb_active_bitmap
=============================

.. c:function:: u32 gfx_v7_0_get_rb_active_bitmap(struct amdgpu_device *adev)

    computes the mask of enabled RBs

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_get_rb_active_bitmap.description`:

Description
-----------

Calculates the bitmask of enabled RBs (CIK).
Returns the enabled RB bitmask.

.. _`gfx_v7_0_setup_rb`:

gfx_v7_0_setup_rb
=================

.. c:function:: void gfx_v7_0_setup_rb(struct amdgpu_device *adev)

    setup the RBs on the asic

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_setup_rb.description`:

Description
-----------

Configures per-SE/SH RB registers (CIK).

.. _`default_sh_mem_bases`:

DEFAULT_SH_MEM_BASES
====================

.. c:function::  DEFAULT_SH_MEM_BASES()

    gart enable

.. _`default_sh_mem_bases.description`:

Description
-----------

Initialize compute vmid sh_mem registers

.. _`gfx_v7_0_constants_init`:

gfx_v7_0_constants_init
=======================

.. c:function:: void gfx_v7_0_constants_init(struct amdgpu_device *adev)

    setup the 3D engine

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_constants_init.description`:

Description
-----------

init the gfx constants such as the 3D engine, tiling configuration
registers, maximum number of quad pipes, render backends...

.. _`gfx_v7_0_scratch_init`:

gfx_v7_0_scratch_init
=====================

.. c:function:: void gfx_v7_0_scratch_init(struct amdgpu_device *adev)

    setup driver info for CP scratch regs

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_scratch_init.description`:

Description
-----------

Set up the number and offset of the CP scratch registers.

.. _`gfx_v7_0_scratch_init.note`:

NOTE
----

use of CP scratch registers is a legacy inferface and
is not used by default on newer asics (r6xx+).  On newer asics,
memory buffers are used for fences rather than scratch regs.

.. _`gfx_v7_0_ring_test_ring`:

gfx_v7_0_ring_test_ring
=======================

.. c:function:: int gfx_v7_0_ring_test_ring(struct amdgpu_ring *ring)

    basic gfx ring test

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

.. _`gfx_v7_0_ring_test_ring.description`:

Description
-----------

Allocate a scratch register and write to it using the gfx ring (CIK).
Provides a basic gfx ring test to verify that the ring is working.
Used by \ :c:func:`gfx_v7_0_cp_gfx_resume`\ ;
Returns 0 on success, error on failure.

.. _`gfx_v7_0_ring_emit_hdp_flush`:

gfx_v7_0_ring_emit_hdp_flush
============================

.. c:function:: void gfx_v7_0_ring_emit_hdp_flush(struct amdgpu_ring *ring)

    emit an hdp flush on the cp

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

.. _`gfx_v7_0_ring_emit_hdp_flush.description`:

Description
-----------

Emits an hdp flush on the cp.

.. _`gfx_v7_0_ring_emit_fence_gfx`:

gfx_v7_0_ring_emit_fence_gfx
============================

.. c:function:: void gfx_v7_0_ring_emit_fence_gfx(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit a fence on the gfx ring

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

    :param addr:
        *undescribed*
    :type addr: u64

    :param seq:
        *undescribed*
    :type seq: u64

    :param flags:
        *undescribed*
    :type flags: unsigned

.. _`gfx_v7_0_ring_emit_fence_gfx.description`:

Description
-----------

Emits a fence sequnce number on the gfx ring and flushes
GPU caches.

.. _`gfx_v7_0_ring_emit_fence_compute`:

gfx_v7_0_ring_emit_fence_compute
================================

.. c:function:: void gfx_v7_0_ring_emit_fence_compute(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit a fence on the compute ring

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

    :param addr:
        *undescribed*
    :type addr: u64

    :param seq:
        *undescribed*
    :type seq: u64

    :param flags:
        *undescribed*
    :type flags: unsigned

.. _`gfx_v7_0_ring_emit_fence_compute.description`:

Description
-----------

Emits a fence sequnce number on the compute ring and flushes
GPU caches.

.. _`gfx_v7_0_ring_emit_ib_gfx`:

gfx_v7_0_ring_emit_ib_gfx
=========================

.. c:function:: void gfx_v7_0_ring_emit_ib_gfx(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    emit an IB (Indirect Buffer) on the ring

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

    :param ib:
        amdgpu indirect buffer object
    :type ib: struct amdgpu_ib \*

    :param vmid:
        *undescribed*
    :type vmid: unsigned

    :param ctx_switch:
        *undescribed*
    :type ctx_switch: bool

.. _`gfx_v7_0_ring_emit_ib_gfx.description`:

Description
-----------

Emits an DE (drawing engine) or CE (constant engine) IB
on the gfx ring.  IBs are usually generated by userspace
acceleration drivers and submitted to the kernel for
sheduling on the ring.  This function schedules the IB
on the gfx ring for execution by the GPU.

.. _`gfx_v7_0_ring_test_ib`:

gfx_v7_0_ring_test_ib
=====================

.. c:function:: int gfx_v7_0_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    basic ring IB test

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

    :param timeout:
        *undescribed*
    :type timeout: long

.. _`gfx_v7_0_ring_test_ib.description`:

Description
-----------

Allocate an IB and execute it on the gfx ring (CIK).
Provides a basic gfx ring test to verify that IBs are working.
Returns 0 on success, error on failure.

.. _`gfx_v7_0_cp_gfx_enable`:

gfx_v7_0_cp_gfx_enable
======================

.. c:function:: void gfx_v7_0_cp_gfx_enable(struct amdgpu_device *adev, bool enable)

    enable/disable the gfx CP MEs

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param enable:
        enable or disable the MEs
    :type enable: bool

.. _`gfx_v7_0_cp_gfx_enable.description`:

Description
-----------

Halts or unhalts the gfx MEs.

.. _`gfx_v7_0_cp_gfx_load_microcode`:

gfx_v7_0_cp_gfx_load_microcode
==============================

.. c:function:: int gfx_v7_0_cp_gfx_load_microcode(struct amdgpu_device *adev)

    load the gfx CP ME ucode

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_cp_gfx_load_microcode.description`:

Description
-----------

Loads the gfx PFP, ME, and CE ucode.
Returns 0 for success, -EINVAL if the ucode is not available.

.. _`gfx_v7_0_cp_gfx_start`:

gfx_v7_0_cp_gfx_start
=====================

.. c:function:: int gfx_v7_0_cp_gfx_start(struct amdgpu_device *adev)

    start the gfx ring

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_cp_gfx_start.description`:

Description
-----------

Enables the ring and loads the clear state context and other
packets required to init the ring.
Returns 0 for success, error for failure.

.. _`gfx_v7_0_cp_gfx_resume`:

gfx_v7_0_cp_gfx_resume
======================

.. c:function:: int gfx_v7_0_cp_gfx_resume(struct amdgpu_device *adev)

    setup the gfx ring buffer registers

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_cp_gfx_resume.description`:

Description
-----------

Program the location and size of the gfx ring buffer
and test it to make sure it's working.
Returns 0 for success, error for failure.

.. _`gfx_v7_0_cp_compute_enable`:

gfx_v7_0_cp_compute_enable
==========================

.. c:function:: void gfx_v7_0_cp_compute_enable(struct amdgpu_device *adev, bool enable)

    enable/disable the compute CP MEs

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param enable:
        enable or disable the MEs
    :type enable: bool

.. _`gfx_v7_0_cp_compute_enable.description`:

Description
-----------

Halts or unhalts the compute MEs.

.. _`gfx_v7_0_cp_compute_load_microcode`:

gfx_v7_0_cp_compute_load_microcode
==================================

.. c:function:: int gfx_v7_0_cp_compute_load_microcode(struct amdgpu_device *adev)

    load the compute CP ME ucode

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_cp_compute_load_microcode.description`:

Description
-----------

Loads the compute MEC1&2 ucode.
Returns 0 for success, -EINVAL if the ucode is not available.

.. _`gfx_v7_0_cp_compute_fini`:

gfx_v7_0_cp_compute_fini
========================

.. c:function:: void gfx_v7_0_cp_compute_fini(struct amdgpu_device *adev)

    stop the compute queues

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_cp_compute_fini.description`:

Description
-----------

Stop the compute queues and tear down the driver queue
info.

.. _`gfx_v7_0_cp_compute_resume`:

gfx_v7_0_cp_compute_resume
==========================

.. c:function:: int gfx_v7_0_cp_compute_resume(struct amdgpu_device *adev)

    setup the compute queue registers

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_cp_compute_resume.description`:

Description
-----------

Program the compute queues and test them to make sure they
are working.
Returns 0 for success, error for failure.

.. _`gfx_v7_0_ring_emit_pipeline_sync`:

gfx_v7_0_ring_emit_pipeline_sync
================================

.. c:function:: void gfx_v7_0_ring_emit_pipeline_sync(struct amdgpu_ring *ring)

    cik vm flush using the CP

    :param ring:
        the ring to emmit the commands to
    :type ring: struct amdgpu_ring \*

.. _`gfx_v7_0_ring_emit_pipeline_sync.description`:

Description
-----------

Sync the command pipeline with the PFP. E.g. wait for everything
to be completed.

.. _`gfx_v7_0_ring_emit_vm_flush`:

gfx_v7_0_ring_emit_vm_flush
===========================

.. c:function:: void gfx_v7_0_ring_emit_vm_flush(struct amdgpu_ring *ring, unsigned vmid, uint64_t pd_addr)

    cik vm flush using the CP

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

    :param vmid:
        *undescribed*
    :type vmid: unsigned

    :param pd_addr:
        *undescribed*
    :type pd_addr: uint64_t

.. _`gfx_v7_0_ring_emit_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using the CP (CIK).

.. _`gfx_v7_0_rlc_stop`:

gfx_v7_0_rlc_stop
=================

.. c:function:: void gfx_v7_0_rlc_stop(struct amdgpu_device *adev)

    stop the RLC ME

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_rlc_stop.description`:

Description
-----------

Halt the RLC ME (MicroEngine) (CIK).

.. _`gfx_v7_0_rlc_start`:

gfx_v7_0_rlc_start
==================

.. c:function:: void gfx_v7_0_rlc_start(struct amdgpu_device *adev)

    start the RLC ME

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_rlc_start.description`:

Description
-----------

Unhalt the RLC ME (MicroEngine) (CIK).

.. _`gfx_v7_0_rlc_resume`:

gfx_v7_0_rlc_resume
===================

.. c:function:: int gfx_v7_0_rlc_resume(struct amdgpu_device *adev)

    setup the RLC hw

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_rlc_resume.description`:

Description
-----------

Initialize the RLC registers, load the ucode,
and start the RLC (CIK).
Returns 0 for success, -EINVAL if the ucode is not available.

.. _`gfx_v7_0_get_gpu_clock_counter`:

gfx_v7_0_get_gpu_clock_counter
==============================

.. c:function:: uint64_t gfx_v7_0_get_gpu_clock_counter(struct amdgpu_device *adev)

    return GPU clock counter snapshot

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v7_0_get_gpu_clock_counter.description`:

Description
-----------

Fetches a GPU clock counter snapshot (SI).
Returns the 64 bit clock counter snapshot.

.. This file was automatic generated / don't edit.

