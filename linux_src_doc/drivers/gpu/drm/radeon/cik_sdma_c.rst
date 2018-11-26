.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/cik_sdma.c

.. _`cik_sdma_get_rptr`:

cik_sdma_get_rptr
=================

.. c:function:: uint32_t cik_sdma_get_rptr(struct radeon_device *rdev, struct radeon_ring *ring)

    get the current read pointer

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon ring pointer
    :type ring: struct radeon_ring \*

.. _`cik_sdma_get_rptr.description`:

Description
-----------

Get the current rptr from the hardware (CIK+).

.. _`cik_sdma_get_wptr`:

cik_sdma_get_wptr
=================

.. c:function:: uint32_t cik_sdma_get_wptr(struct radeon_device *rdev, struct radeon_ring *ring)

    get the current write pointer

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon ring pointer
    :type ring: struct radeon_ring \*

.. _`cik_sdma_get_wptr.description`:

Description
-----------

Get the current wptr from the hardware (CIK+).

.. _`cik_sdma_set_wptr`:

cik_sdma_set_wptr
=================

.. c:function:: void cik_sdma_set_wptr(struct radeon_device *rdev, struct radeon_ring *ring)

    commit the write pointer

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon ring pointer
    :type ring: struct radeon_ring \*

.. _`cik_sdma_set_wptr.description`:

Description
-----------

Write the wptr back to the hardware (CIK+).

.. _`cik_sdma_ring_ib_execute`:

cik_sdma_ring_ib_execute
========================

.. c:function:: void cik_sdma_ring_ib_execute(struct radeon_device *rdev, struct radeon_ib *ib)

    Schedule an IB on the DMA engine

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        IB object to schedule
    :type ib: struct radeon_ib \*

.. _`cik_sdma_ring_ib_execute.description`:

Description
-----------

Schedule an IB in the DMA ring (CIK).

.. _`cik_sdma_hdp_flush_ring_emit`:

cik_sdma_hdp_flush_ring_emit
============================

.. c:function:: void cik_sdma_hdp_flush_ring_emit(struct radeon_device *rdev, int ridx)

    emit an hdp flush on the DMA ring

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ridx:
        radeon ring index
    :type ridx: int

.. _`cik_sdma_hdp_flush_ring_emit.description`:

Description
-----------

Emit an hdp flush packet on the requested DMA ring.

.. _`cik_sdma_fence_ring_emit`:

cik_sdma_fence_ring_emit
========================

.. c:function:: void cik_sdma_fence_ring_emit(struct radeon_device *rdev, struct radeon_fence *fence)

    emit a fence on the DMA ring

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param fence:
        radeon fence object
    :type fence: struct radeon_fence \*

.. _`cik_sdma_fence_ring_emit.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (CIK).

.. _`cik_sdma_semaphore_ring_emit`:

cik_sdma_semaphore_ring_emit
============================

.. c:function:: bool cik_sdma_semaphore_ring_emit(struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit a semaphore on the dma ring

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

    :param semaphore:
        radeon semaphore object
    :type semaphore: struct radeon_semaphore \*

    :param emit_wait:
        wait or signal semaphore
    :type emit_wait: bool

.. _`cik_sdma_semaphore_ring_emit.description`:

Description
-----------

Add a DMA semaphore packet to the ring wait on or signal
other rings (CIK).

.. _`cik_sdma_gfx_stop`:

cik_sdma_gfx_stop
=================

.. c:function:: void cik_sdma_gfx_stop(struct radeon_device *rdev)

    stop the gfx async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_gfx_stop.description`:

Description
-----------

Stop the gfx async dma ring buffers (CIK).

.. _`cik_sdma_rlc_stop`:

cik_sdma_rlc_stop
=================

.. c:function:: void cik_sdma_rlc_stop(struct radeon_device *rdev)

    stop the compute async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_rlc_stop.description`:

Description
-----------

Stop the compute async dma queues (CIK).

.. _`cik_sdma_ctx_switch_enable`:

cik_sdma_ctx_switch_enable
==========================

.. c:function:: void cik_sdma_ctx_switch_enable(struct radeon_device *rdev, bool enable)

    enable/disable sdma engine preemption

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param enable:
        enable/disable preemption.
    :type enable: bool

.. _`cik_sdma_ctx_switch_enable.description`:

Description
-----------

Halt or unhalt the async dma engines (CIK).

.. _`cik_sdma_enable`:

cik_sdma_enable
===============

.. c:function:: void cik_sdma_enable(struct radeon_device *rdev, bool enable)

    stop the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param enable:
        enable/disable the DMA MEs.
    :type enable: bool

.. _`cik_sdma_enable.description`:

Description
-----------

Halt or unhalt the async dma engines (CIK).

.. _`cik_sdma_gfx_resume`:

cik_sdma_gfx_resume
===================

.. c:function:: int cik_sdma_gfx_resume(struct radeon_device *rdev)

    setup and start the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_gfx_resume.description`:

Description
-----------

Set up the gfx DMA ring buffers and enable them (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_rlc_resume`:

cik_sdma_rlc_resume
===================

.. c:function:: int cik_sdma_rlc_resume(struct radeon_device *rdev)

    setup and start the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_rlc_resume.description`:

Description
-----------

Set up the compute DMA queues and enable them (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_load_microcode`:

cik_sdma_load_microcode
=======================

.. c:function:: int cik_sdma_load_microcode(struct radeon_device *rdev)

    load the sDMA ME ucode

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_load_microcode.description`:

Description
-----------

Loads the sDMA0/1 ucode.
Returns 0 for success, -EINVAL if the ucode is not available.

.. _`cik_sdma_resume`:

cik_sdma_resume
===============

.. c:function:: int cik_sdma_resume(struct radeon_device *rdev)

    setup and start the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_resume.description`:

Description
-----------

Set up the DMA engines and enable them (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_fini`:

cik_sdma_fini
=============

.. c:function:: void cik_sdma_fini(struct radeon_device *rdev)

    tear down the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cik_sdma_fini.description`:

Description
-----------

Stop the async dma engines and free the rings (CIK).

.. _`cik_copy_dma`:

cik_copy_dma
============

.. c:function:: struct radeon_fence *cik_copy_dma(struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

    copy pages using the DMA engine

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param src_offset:
        src GPU address
    :type src_offset: uint64_t

    :param dst_offset:
        dst GPU address
    :type dst_offset: uint64_t

    :param num_gpu_pages:
        number of GPU pages to xfer
    :type num_gpu_pages: unsigned

    :param resv:
        reservation object to sync to
    :type resv: struct reservation_object \*

.. _`cik_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (CIK).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

.. _`cik_sdma_ring_test`:

cik_sdma_ring_test
==================

.. c:function:: int cik_sdma_ring_test(struct radeon_device *rdev, struct radeon_ring *ring)

    simple async dma engine test

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

.. _`cik_sdma_ring_test.description`:

Description
-----------

Test the DMA engine by writing using it to write an
value to memory. (CIK).
Returns 0 for success, error for failure.

.. _`cik_sdma_ib_test`:

cik_sdma_ib_test
================

.. c:function:: int cik_sdma_ib_test(struct radeon_device *rdev, struct radeon_ring *ring)

    test an IB on the DMA engine

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

.. _`cik_sdma_ib_test.description`:

Description
-----------

Test a simple IB in the DMA ring (CIK).
Returns 0 on success, error on failure.

.. _`cik_sdma_is_lockup`:

cik_sdma_is_lockup
==================

.. c:function:: bool cik_sdma_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

.. _`cik_sdma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up (CIK).
Returns true if the engine appears to be locked up, false if not.

.. _`cik_sdma_vm_copy_pages`:

cik_sdma_vm_copy_pages
======================

.. c:function:: void cik_sdma_vm_copy_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t src, unsigned count)

    update PTEs by copying them from the GART

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct radeon_ib \*

    :param pe:
        addr of the page entry
    :type pe: uint64_t

    :param src:
        src addr to copy from
    :type src: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

.. _`cik_sdma_vm_copy_pages.description`:

Description
-----------

Update PTEs by copying them from the GART using sDMA (CIK).

.. _`cik_sdma_vm_write_pages`:

cik_sdma_vm_write_pages
=======================

.. c:function:: void cik_sdma_vm_write_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    update PTEs by writing them manually

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct radeon_ib \*

    :param pe:
        addr of the page entry
    :type pe: uint64_t

    :param addr:
        dst addr to write into pe
    :type addr: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

    :param incr:
        increase next addr by incr bytes
    :type incr: uint32_t

    :param flags:
        access flags
    :type flags: uint32_t

.. _`cik_sdma_vm_write_pages.description`:

Description
-----------

Update PTEs by writing them manually using sDMA (CIK).

.. _`cik_sdma_vm_set_pages`:

cik_sdma_vm_set_pages
=====================

.. c:function:: void cik_sdma_vm_set_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    update the page tables using sDMA

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct radeon_ib \*

    :param pe:
        addr of the page entry
    :type pe: uint64_t

    :param addr:
        dst addr to write into pe
    :type addr: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

    :param incr:
        increase next addr by incr bytes
    :type incr: uint32_t

    :param flags:
        access flags
    :type flags: uint32_t

.. _`cik_sdma_vm_set_pages.description`:

Description
-----------

Update the page tables using sDMA (CIK).

.. _`cik_sdma_vm_pad_ib`:

cik_sdma_vm_pad_ib
==================

.. c:function:: void cik_sdma_vm_pad_ib(struct radeon_ib *ib)

    pad the IB to the required number of dw

    :param ib:
        indirect buffer to fill with padding
    :type ib: struct radeon_ib \*

.. _`cik_dma_vm_flush`:

cik_dma_vm_flush
================

.. c:function:: void cik_dma_vm_flush(struct radeon_device *rdev, struct radeon_ring *ring, unsigned vm_id, uint64_t pd_addr)

    cik vm flush using sDMA

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        *undescribed*
    :type ring: struct radeon_ring \*

    :param vm_id:
        *undescribed*
    :type vm_id: unsigned

    :param pd_addr:
        *undescribed*
    :type pd_addr: uint64_t

.. _`cik_dma_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using sDMA (CIK).

.. This file was automatic generated / don't edit.

