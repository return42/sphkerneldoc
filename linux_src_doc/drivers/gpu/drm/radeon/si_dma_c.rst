.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/si_dma.c

.. _`si_dma_is_lockup`:

si_dma_is_lockup
================

.. c:function:: bool si_dma_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

.. _`si_dma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up.
Returns true if the engine appears to be locked up, false if not.

.. _`si_dma_vm_copy_pages`:

si_dma_vm_copy_pages
====================

.. c:function:: void si_dma_vm_copy_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t src, unsigned count)

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
        src addr where to copy from
    :type src: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

.. _`si_dma_vm_copy_pages.description`:

Description
-----------

Update PTEs by copying them from the GART using the DMA (SI).

.. _`si_dma_vm_write_pages`:

si_dma_vm_write_pages
=====================

.. c:function:: void si_dma_vm_write_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

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

.. _`si_dma_vm_write_pages.description`:

Description
-----------

Update PTEs by writing them manually using the DMA (SI).

.. _`si_dma_vm_set_pages`:

si_dma_vm_set_pages
===================

.. c:function:: void si_dma_vm_set_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    update the page tables using the DMA

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

.. _`si_dma_vm_set_pages.description`:

Description
-----------

Update the page tables using the DMA (SI).

.. _`si_copy_dma`:

si_copy_dma
===========

.. c:function:: struct radeon_fence *si_copy_dma(struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

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

.. _`si_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (SI).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

.. This file was automatic generated / don't edit.

