.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/cik_sdma.c

.. _`cik_sdma_init_microcode`:

cik_sdma_init_microcode
=======================

.. c:function:: int cik_sdma_init_microcode(struct amdgpu_device *adev)

    load ucode images from disk

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.

.. _`cik_sdma_ring_get_rptr`:

cik_sdma_ring_get_rptr
======================

.. c:function:: uint64_t cik_sdma_ring_get_rptr(struct amdgpu_ring *ring)

    get the current read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`cik_sdma_ring_get_rptr.description`:

Description
-----------

Get the current rptr from the hardware (CIK+).

.. _`cik_sdma_ring_get_wptr`:

cik_sdma_ring_get_wptr
======================

.. c:function:: uint64_t cik_sdma_ring_get_wptr(struct amdgpu_ring *ring)

    get the current write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`cik_sdma_ring_get_wptr.description`:

Description
-----------

Get the current wptr from the hardware (CIK+).

.. _`cik_sdma_ring_set_wptr`:

cik_sdma_ring_set_wptr
======================

.. c:function:: void cik_sdma_ring_set_wptr(struct amdgpu_ring *ring)

    commit the write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`cik_sdma_ring_set_wptr.description`:

Description
-----------

Write the wptr back to the hardware (CIK+).

.. _`cik_sdma_ring_emit_ib`:

cik_sdma_ring_emit_ib
=====================

.. c:function:: void cik_sdma_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    Schedule an IB on the DMA engine

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

    :param struct amdgpu_ib \*ib:
        IB object to schedule

    :param unsigned vmid:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`cik_sdma_ring_emit_ib.description`:

Description
-----------

Schedule an IB in the DMA ring (CIK).

.. _`cik_sdma_ring_emit_hdp_flush`:

cik_sdma_ring_emit_hdp_flush
============================

.. c:function:: void cik_sdma_ring_emit_hdp_flush(struct amdgpu_ring *ring)

    emit an hdp flush on the DMA ring

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

.. _`cik_sdma_ring_emit_hdp_flush.description`:

Description
-----------

Emit an hdp flush packet on the requested DMA ring.

.. _`cik_sdma_ring_emit_fence`:

cik_sdma_ring_emit_fence
========================

.. c:function:: void cik_sdma_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit a fence on the DMA ring

    :param struct amdgpu_ring \*ring:
        amdgpu ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`cik_sdma_ring_emit_fence.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (CIK).

.. _`cik_sdma_gfx_stop`:

cik_sdma_gfx_stop
=================

.. c:function:: void cik_sdma_gfx_stop(struct amdgpu_device *adev)

    stop the gfx async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_gfx_stop.description`:

Description
-----------

Stop the gfx async dma ring buffers (CIK).

.. _`cik_sdma_rlc_stop`:

cik_sdma_rlc_stop
=================

.. c:function:: void cik_sdma_rlc_stop(struct amdgpu_device *adev)

    stop the compute async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_rlc_stop.description`:

Description
-----------

Stop the compute async dma queues (CIK).

.. _`cik_ctx_switch_enable`:

cik_ctx_switch_enable
=====================

.. c:function:: void cik_ctx_switch_enable(struct amdgpu_device *adev, bool enable)

    stop the async dma engines context switch

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param bool enable:
        enable/disable the DMA MEs context switch.

.. _`cik_ctx_switch_enable.description`:

Description
-----------

Halt or unhalt the async dma engines context switch (VI).

.. _`cik_sdma_enable`:

cik_sdma_enable
===============

.. c:function:: void cik_sdma_enable(struct amdgpu_device *adev, bool enable)

    stop the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param bool enable:
        enable/disable the DMA MEs.

.. _`cik_sdma_enable.description`:

Description
-----------

Halt or unhalt the async dma engines (CIK).

.. _`cik_sdma_gfx_resume`:

cik_sdma_gfx_resume
===================

.. c:function:: int cik_sdma_gfx_resume(struct amdgpu_device *adev)

    setup and start the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_gfx_resume.description`:

Description
-----------

Set up the gfx DMA ring buffers and enable them (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_rlc_resume`:

cik_sdma_rlc_resume
===================

.. c:function:: int cik_sdma_rlc_resume(struct amdgpu_device *adev)

    setup and start the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_rlc_resume.description`:

Description
-----------

Set up the compute DMA queues and enable them (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_load_microcode`:

cik_sdma_load_microcode
=======================

.. c:function:: int cik_sdma_load_microcode(struct amdgpu_device *adev)

    load the sDMA ME ucode

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_load_microcode.description`:

Description
-----------

Loads the sDMA0/1 ucode.
Returns 0 for success, -EINVAL if the ucode is not available.

.. _`cik_sdma_start`:

cik_sdma_start
==============

.. c:function:: int cik_sdma_start(struct amdgpu_device *adev)

    setup and start the async dma engines

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_sdma_start.description`:

Description
-----------

Set up the DMA engines and enable them (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_ring_test_ring`:

cik_sdma_ring_test_ring
=======================

.. c:function:: int cik_sdma_ring_test_ring(struct amdgpu_ring *ring)

    simple async dma engine test

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

.. _`cik_sdma_ring_test_ring.description`:

Description
-----------

Test the DMA engine by writing using it to write an
value to memory. (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_ring_test_ib`:

cik_sdma_ring_test_ib
=====================

.. c:function:: int cik_sdma_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test an IB on the DMA engine

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

    :param long timeout:
        *undescribed*

.. _`cik_sdma_ring_test_ib.description`:

Description
-----------

Test a simple IB in the DMA ring (CIK).
Returns 0 on success, error on failure.

.. _`cik_sdma_vm_copy_pte`:

cik_sdma_vm_copy_pte
====================

.. c:function:: void cik_sdma_vm_copy_pte(struct amdgpu_ib *ib, uint64_t pe, uint64_t src, unsigned count)

    update PTEs by copying them from the GART

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t src:
        src addr to copy from

    :param unsigned count:
        number of page entries to update

.. _`cik_sdma_vm_copy_pte.description`:

Description
-----------

Update PTEs by copying them from the GART using sDMA (CIK).

.. _`cik_sdma_vm_write_pte`:

cik_sdma_vm_write_pte
=====================

.. c:function:: void cik_sdma_vm_write_pte(struct amdgpu_ib *ib, uint64_t pe, uint64_t value, unsigned count, uint32_t incr)

    update PTEs by writing them manually

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t value:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

.. _`cik_sdma_vm_write_pte.description`:

Description
-----------

Update PTEs by writing them manually using sDMA (CIK).

.. _`cik_sdma_vm_set_pte_pde`:

cik_sdma_vm_set_pte_pde
=======================

.. c:function:: void cik_sdma_vm_set_pte_pde(struct amdgpu_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

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

.. _`cik_sdma_vm_set_pte_pde.description`:

Description
-----------

Update the page tables using sDMA (CIK).

.. _`cik_sdma_ring_pad_ib`:

cik_sdma_ring_pad_ib
====================

.. c:function:: void cik_sdma_ring_pad_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib)

    pad the IB to the required number of dw

    :param struct amdgpu_ring \*ring:
        *undescribed*

    :param struct amdgpu_ib \*ib:
        indirect buffer to fill with padding

.. _`cik_sdma_ring_emit_pipeline_sync`:

cik_sdma_ring_emit_pipeline_sync
================================

.. c:function:: void cik_sdma_ring_emit_pipeline_sync(struct amdgpu_ring *ring)

    sync the pipeline

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`cik_sdma_ring_emit_pipeline_sync.description`:

Description
-----------

Make sure all previous operations are completed (CIK).

.. _`cik_sdma_ring_emit_vm_flush`:

cik_sdma_ring_emit_vm_flush
===========================

.. c:function:: void cik_sdma_ring_emit_vm_flush(struct amdgpu_ring *ring, unsigned vmid, uint64_t pd_addr)

    cik vm flush using sDMA

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param unsigned vmid:
        *undescribed*

    :param uint64_t pd_addr:
        *undescribed*

.. _`cik_sdma_ring_emit_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using sDMA (CIK).

.. _`cik_sdma_emit_copy_buffer`:

cik_sdma_emit_copy_buffer
=========================

.. c:function:: void cik_sdma_emit_copy_buffer(struct amdgpu_ib *ib, uint64_t src_offset, uint64_t dst_offset, uint32_t byte_count)

    copy buffer using the sDMA engine

    :param struct amdgpu_ib \*ib:
        *undescribed*

    :param uint64_t src_offset:
        src GPU address

    :param uint64_t dst_offset:
        dst GPU address

    :param uint32_t byte_count:
        number of bytes to xfer

.. _`cik_sdma_emit_copy_buffer.description`:

Description
-----------

Copy GPU buffers using the DMA engine (CIK).
Used by the amdgpu ttm implementation to move pages if
registered as the asic copy callback.

.. _`cik_sdma_emit_fill_buffer`:

cik_sdma_emit_fill_buffer
=========================

.. c:function:: void cik_sdma_emit_fill_buffer(struct amdgpu_ib *ib, uint32_t src_data, uint64_t dst_offset, uint32_t byte_count)

    fill buffer using the sDMA engine

    :param struct amdgpu_ib \*ib:
        *undescribed*

    :param uint32_t src_data:
        value to write to buffer

    :param uint64_t dst_offset:
        dst GPU address

    :param uint32_t byte_count:
        number of bytes to xfer

.. _`cik_sdma_emit_fill_buffer.description`:

Description
-----------

Fill GPU buffers using the DMA engine (CIK).

.. This file was automatic generated / don't edit.

