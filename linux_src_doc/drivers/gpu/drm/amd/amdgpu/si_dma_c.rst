.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/si_dma.c

.. _`si_dma_ring_emit_fence`:

si_dma_ring_emit_fence
======================

.. c:function:: void si_dma_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit a fence on the DMA ring

    :param ring:
        amdgpu ring pointer
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

.. _`si_dma_ring_emit_fence.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (VI).

.. _`si_dma_ring_test_ring`:

si_dma_ring_test_ring
=====================

.. c:function:: int si_dma_ring_test_ring(struct amdgpu_ring *ring)

    simple async dma engine test

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

.. _`si_dma_ring_test_ring.description`:

Description
-----------

Test the DMA engine by writing using it to write an
value to memory. (VI).
Returns 0 for success, error for failure.

.. _`si_dma_ring_test_ib`:

si_dma_ring_test_ib
===================

.. c:function:: int si_dma_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test an IB on the DMA engine

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

    :param timeout:
        *undescribed*
    :type timeout: long

.. _`si_dma_ring_test_ib.description`:

Description
-----------

Test a simple IB in the DMA ring (VI).
Returns 0 on success, error on failure.

.. _`si_dma_vm_copy_pte`:

si_dma_vm_copy_pte
==================

.. c:function:: void si_dma_vm_copy_pte(struct amdgpu_ib *ib, uint64_t pe, uint64_t src, unsigned count)

    update PTEs by copying them from the GART

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct amdgpu_ib \*

    :param pe:
        addr of the page entry
    :type pe: uint64_t

    :param src:
        src addr to copy from
    :type src: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

.. _`si_dma_vm_copy_pte.description`:

Description
-----------

Update PTEs by copying them from the GART using DMA (SI).

.. _`si_dma_vm_write_pte`:

si_dma_vm_write_pte
===================

.. c:function:: void si_dma_vm_write_pte(struct amdgpu_ib *ib, uint64_t pe, uint64_t value, unsigned count, uint32_t incr)

    update PTEs by writing them manually

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct amdgpu_ib \*

    :param pe:
        addr of the page entry
    :type pe: uint64_t

    :param value:
        dst addr to write into pe
    :type value: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

    :param incr:
        increase next addr by incr bytes
    :type incr: uint32_t

.. _`si_dma_vm_write_pte.description`:

Description
-----------

Update PTEs by writing them manually using DMA (SI).

.. _`si_dma_vm_set_pte_pde`:

si_dma_vm_set_pte_pde
=====================

.. c:function:: void si_dma_vm_set_pte_pde(struct amdgpu_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    update the page tables using sDMA

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct amdgpu_ib \*

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
    :type flags: uint64_t

.. _`si_dma_vm_set_pte_pde.description`:

Description
-----------

Update the page tables using sDMA (CIK).

.. _`si_dma_ring_pad_ib`:

si_dma_ring_pad_ib
==================

.. c:function:: void si_dma_ring_pad_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib)

    pad the IB to the required number of dw

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

    :param ib:
        indirect buffer to fill with padding
    :type ib: struct amdgpu_ib \*

.. _`si_dma_ring_emit_pipeline_sync`:

si_dma_ring_emit_pipeline_sync
==============================

.. c:function:: void si_dma_ring_emit_pipeline_sync(struct amdgpu_ring *ring)

    sync the pipeline

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`si_dma_ring_emit_pipeline_sync.description`:

Description
-----------

Make sure all previous operations are completed (CIK).

.. _`si_dma_ring_emit_vm_flush`:

si_dma_ring_emit_vm_flush
=========================

.. c:function:: void si_dma_ring_emit_vm_flush(struct amdgpu_ring *ring, unsigned vmid, uint64_t pd_addr)

    cik vm flush using sDMA

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

    :param vmid:
        *undescribed*
    :type vmid: unsigned

    :param pd_addr:
        *undescribed*
    :type pd_addr: uint64_t

.. _`si_dma_ring_emit_vm_flush.description`:

Description
-----------

Update the page table base and flush the VM TLB
using sDMA (VI).

.. _`si_dma_emit_copy_buffer`:

si_dma_emit_copy_buffer
=======================

.. c:function:: void si_dma_emit_copy_buffer(struct amdgpu_ib *ib, uint64_t src_offset, uint64_t dst_offset, uint32_t byte_count)

    copy buffer using the sDMA engine

    :param ib:
        *undescribed*
    :type ib: struct amdgpu_ib \*

    :param src_offset:
        src GPU address
    :type src_offset: uint64_t

    :param dst_offset:
        dst GPU address
    :type dst_offset: uint64_t

    :param byte_count:
        number of bytes to xfer
    :type byte_count: uint32_t

.. _`si_dma_emit_copy_buffer.description`:

Description
-----------

Copy GPU buffers using the DMA engine (VI).
Used by the amdgpu ttm implementation to move pages if
registered as the asic copy callback.

.. _`si_dma_emit_fill_buffer`:

si_dma_emit_fill_buffer
=======================

.. c:function:: void si_dma_emit_fill_buffer(struct amdgpu_ib *ib, uint32_t src_data, uint64_t dst_offset, uint32_t byte_count)

    fill buffer using the sDMA engine

    :param ib:
        *undescribed*
    :type ib: struct amdgpu_ib \*

    :param src_data:
        value to write to buffer
    :type src_data: uint32_t

    :param dst_offset:
        dst GPU address
    :type dst_offset: uint64_t

    :param byte_count:
        number of bytes to xfer
    :type byte_count: uint32_t

.. _`si_dma_emit_fill_buffer.description`:

Description
-----------

Fill GPU buffers using the DMA engine (VI).

.. This file was automatic generated / don't edit.

