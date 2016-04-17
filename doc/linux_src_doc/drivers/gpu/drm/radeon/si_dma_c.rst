.. -*- coding: utf-8; mode: rst -*-

========
si_dma.c
========


.. _`si_dma_is_lockup`:

si_dma_is_lockup
================

.. c:function:: bool si_dma_is_lockup (struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information



.. _`si_dma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up.
Returns true if the engine appears to be locked up, false if not.



.. _`si_dma_vm_copy_pages`:

si_dma_vm_copy_pages
====================

.. c:function:: void si_dma_vm_copy_pages (struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t src, unsigned count)

    update PTEs by copying them from the GART

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t src:
        src addr where to copy from

    :param unsigned count:
        number of page entries to update



.. _`si_dma_vm_copy_pages.description`:

Description
-----------

Update PTEs by copying them from the GART using the DMA (SI).



.. _`si_dma_vm_write_pages`:

si_dma_vm_write_pages
=====================

.. c:function:: void si_dma_vm_write_pages (struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    update PTEs by writing them manually

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint32_t flags:
        access flags



.. _`si_dma_vm_write_pages.description`:

Description
-----------

Update PTEs by writing them manually using the DMA (SI).



.. _`si_dma_vm_set_pages`:

si_dma_vm_set_pages
===================

.. c:function:: void si_dma_vm_set_pages (struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    update the page tables using the DMA

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        indirect buffer to fill with commands

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint32_t flags:
        access flags



.. _`si_dma_vm_set_pages.description`:

Description
-----------

Update the page tables using the DMA (SI).



.. _`si_copy_dma`:

si_copy_dma
===========

.. c:function:: struct radeon_fence *si_copy_dma (struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

    copy pages using the DMA engine

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



.. _`si_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (SI).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

