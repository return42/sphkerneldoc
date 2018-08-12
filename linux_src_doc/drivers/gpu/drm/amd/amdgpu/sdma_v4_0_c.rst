.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/sdma_v4_0.c

.. _`sdma_v4_0_init_microcode`:

sdma_v4_0_init_microcode
========================

.. c:function:: int sdma_v4_0_init_microcode(struct amdgpu_device *adev)

    load ucode images from disk

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.

.. _`sdma_v4_0_ring_get_rptr`:

sdma_v4_0_ring_get_rptr
=======================

.. c:function:: uint64_t sdma_v4_0_ring_get_rptr(struct amdgpu_ring *ring)

    get the current read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`sdma_v4_0_ring_get_rptr.description`:

Description
-----------

Get the current rptr from the hardware (VEGA10+).

.. _`sdma_v4_0_ring_get_wptr`:

sdma_v4_0_ring_get_wptr
=======================

.. c:function:: uint64_t sdma_v4_0_ring_get_wptr(struct amdgpu_ring *ring)

    get the current write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`sdma_v4_0_ring_get_wptr.description`:

Description
-----------

Get the current wptr from the hardware (VEGA10+).

.. _`sdma_v4_0_ring_set_wptr`:

sdma_v4_0_ring_set_wptr
=======================

.. c:function:: void sdma_v4_0_ring_set_wptr(struct amdgpu_ring *ring)

    commit the write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`sdma_v4_0_ring_set_wptr.description`:

Description
-----------

Write the wptr back to the hardware (VEGA10+).

.. _`sdma_v4_0_ring_emit_ib`:

sdma_v4_0_ring_emit_ib
======================

.. c:function:: void sdma_v4_0_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    Schedule an IB on the DMA engine

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

    :param struct amdgpu_ib \*ib:
        IB object to schedule

    :param unsigned vmid:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`sdma_v4_0_ring_emit_ib.description`:

Description
-----------

Schedule an IB in the DMA ring (VEGA10).

.. _`sdma_v4_0_ring_emit_hdp_flush`:

sdma_v4_0_ring_emit_hdp_flush
=============================

.. c:function:: void sdma_v4_0_ring_emit_hdp_flush(struct amdgpu_ring *ring)

    emit an hdp flush on the DMA ring

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`sdma_v4_0_ring_emit_hdp_flush.description`:

Description
-----------

Emit an hdp flush packet on the requested DMA ring.

.. _`sdma_v4_0_ring_emit_fence`:

sdma_v4_0_ring_emit_fence
=========================

.. c:function:: void sdma_v4_0_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit a fence on the DMA ring

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`sdma_v4_0_ring_emit_fence.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (VEGA10).

.. _`sdma_v4_0_gfx_stop`:

sdma_v4_0_gfx_stop
==================

.. c:function:: void sdma_v4_0_gfx_stop(struct amdgpu_device *adev)

    stop the gfx async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_gfx_stop.description`:

Description
-----------

Stop the gfx async dma ring buffers (VEGA10).

.. _`sdma_v4_0_rlc_stop`:

sdma_v4_0_rlc_stop
==================

.. c:function:: void sdma_v4_0_rlc_stop(struct amdgpu_device *adev)

    stop the compute async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_rlc_stop.description`:

Description
-----------

Stop the compute async dma queues (VEGA10).

.. _`sdma_v4_0_ctx_switch_enable`:

sdma_v4_0_ctx_switch_enable
===========================

.. c:function:: void sdma_v4_0_ctx_switch_enable(struct amdgpu_device *adev, bool enable)

    stop the async dma engines context switch

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param bool enable:
        enable/disable the DMA MEs context switch.

.. _`sdma_v4_0_ctx_switch_enable.description`:

Description
-----------

Halt or unhalt the async dma engines context switch (VEGA10).

.. _`sdma_v4_0_enable`:

sdma_v4_0_enable
================

.. c:function:: void sdma_v4_0_enable(struct amdgpu_device *adev, bool enable)

    stop the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param bool enable:
        enable/disable the DMA MEs.

.. _`sdma_v4_0_enable.description`:

Description
-----------

Halt or unhalt the async dma engines (VEGA10).

.. _`sdma_v4_0_gfx_resume`:

sdma_v4_0_gfx_resume
====================

.. c:function:: int sdma_v4_0_gfx_resume(struct amdgpu_device *adev)

    setup and start the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_gfx_resume.description`:

Description
-----------

Set up the gfx DMA ring buffers and enable them (VEGA10).
Returns 0 for success, error for failure.

.. _`sdma_v4_0_rlc_resume`:

sdma_v4_0_rlc_resume
====================

.. c:function:: int sdma_v4_0_rlc_resume(struct amdgpu_device *adev)

    setup and start the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_rlc_resume.description`:

Description
-----------

Set up the compute DMA queues and enable them (VEGA10).
Returns 0 for success, error for failure.

.. _`sdma_v4_0_load_microcode`:

sdma_v4_0_load_microcode
========================

.. c:function:: int sdma_v4_0_load_microcode(struct amdgpu_device *adev)

    load the sDMA ME ucode

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_load_microcode.description`:

Description
-----------

Loads the sDMA0/1 ucode.
Returns 0 for success, -EINVAL if the ucode is not available.

.. _`sdma_v4_0_start`:

sdma_v4_0_start
===============

.. c:function:: int sdma_v4_0_start(struct amdgpu_device *adev)

    setup and start the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`sdma_v4_0_start.description`:

Description
-----------

Set up the DMA engines and enable them (VEGA10).
Returns 0 for success, error for failure.

.. _`sdma_v4_0_ring_test_ring`:

sdma_v4_0_ring_test_ring
========================

.. c:function:: int sdma_v4_0_ring_test_ring(struct amdgpu_ring *ring)

    simple async dma engine test

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

.. _`sdma_v4_0_ring_test_ring.description`:

Description
-----------

Test the DMA engine by writing using it to write an
value to memory. (VEGA10).
Returns 0 for success, error for failure.

.. _`sdma_v4_0_ring_test_ib`:

sdma_v4_0_ring_test_ib
======================

.. c:function:: int sdma_v4_0_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test an IB on the DMA engine

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

    :param long timeout:
        *undescribed*

.. _`sdma_v4_0_ring_test_ib.description`:

Description
-----------

Test a simple IB in the DMA ring (VEGA10).
Returns 0 on success, error on failure.

.. _`sdma_v4_0_vm_copy_pte`:

sdma_v4_0_vm_copy_pte
=====================

.. c:function:: void sdma_v4_0_vm_copy_pte(struct amdgpu_ib *ib, uint64_t pe, uint64_t src, unsigned count)

    update PTEs by copying them from the GART

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t src:
        src addr to copy from

    :param unsigned count:
        number of page entries to update

.. _`sdma_v4_0_vm_copy_pte.description`:

Description
-----------

Update PTEs by copying them from the GART using sDMA (VEGA10).

.. _`sdma_v4_0_vm_write_pte`:

sdma_v4_0_vm_write_pte
======================

.. c:function:: void sdma_v4_0_vm_write_pte(struct amdgpu_ib *ib, uint64_t pe, uint64_t value, unsigned count, uint32_t incr)

    update PTEs by writing them manually

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t value:
        *undescribed*

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

.. _`sdma_v4_0_vm_write_pte.description`:

Description
-----------

Update PTEs by writing them manually using sDMA (VEGA10).

.. _`sdma_v4_0_vm_set_pte_pde`:

sdma_v4_0_vm_set_pte_pde
========================

.. c:function:: void sdma_v4_0_vm_set_pte_pde(struct amdgpu_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    update the page tables using sDMA

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint64_t flags:
        access flags

.. _`sdma_v4_0_vm_set_pte_pde.description`:

Description
-----------

Update the page tables using sDMA (VEGA10).

.. _`sdma_v4_0_ring_pad_ib`:

sdma_v4_0_ring_pad_ib
=====================

.. c:function:: void sdma_v4_0_ring_pad_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib)

    pad the IB to the required number of dw

    :param struct amdgpu_ring \*ring:
        *undescribed*

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with padding

.. _`sdma_v4_0_ring_emit_pipeline_sync`:

sdma_v4_0_ring_emit_pipeline_sync
=================================

.. c:function:: void sdma_v4_0_ring_emit_pipeline_sync(struct amdgpu_ring *ring)

    sync the pipeline

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`sdma_v4_0_ring_emit_pipeline_sync.description`:

Description
-----------

Make sure all previous operations are completed (CIK).

.. _`sdma_v4_0_ring_emit_vm_flush`:

sdma_v4_0_ring_emit_vm_flush
============================

.. c:function:: void sdma_v4_0_ring_emit_vm_flush(struct amdgpu_ring *ring, unsigned vmid, uint64_t pd_addr)

    vm flush using sDMA

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param unsigned vmid:
        *undescribed*

    :param uint64_t pd_addr:
        *undescribed*

.. _`sdma_v4_0_ring_emit_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using sDMA (VEGA10).

.. _`sdma_v4_0_emit_copy_buffer`:

sdma_v4_0_emit_copy_buffer
==========================

.. c:function:: void sdma_v4_0_emit_copy_buffer(struct amdgpu_ib *ib, uint64_t src_offset, uint64_t dst_offset, uint32_t byte_count)

    copy buffer using the sDMA engine

    :param struct amdgpu_ib \*ib:
        *undescribed*

    :param uint64_t src_offset:
        src GPU address

    :param uint64_t dst_offset:
        dst GPU address

    :param uint32_t byte_count:
        number of bytes to xfer

.. _`sdma_v4_0_emit_copy_buffer.description`:

Description
-----------

Copy GPU buffers using the DMA engine (VEGA10/12).
Used by the amdgpu ttm implementation to move pages if
registered as the asic copy callback.

.. _`sdma_v4_0_emit_fill_buffer`:

sdma_v4_0_emit_fill_buffer
==========================

.. c:function:: void sdma_v4_0_emit_fill_buffer(struct amdgpu_ib *ib, uint32_t src_data, uint64_t dst_offset, uint32_t byte_count)

    fill buffer using the sDMA engine

    :param struct amdgpu_ib \*ib:
        *undescribed*

    :param uint32_t src_data:
        value to write to buffer

    :param uint64_t dst_offset:
        dst GPU address

    :param uint32_t byte_count:
        number of bytes to xfer

.. _`sdma_v4_0_emit_fill_buffer.description`:

Description
-----------

Fill GPU buffers using the DMA engine (VEGA10/12).

.. This file was automatic generated / don't edit.

