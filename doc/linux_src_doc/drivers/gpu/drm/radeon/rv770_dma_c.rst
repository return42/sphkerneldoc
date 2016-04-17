.. -*- coding: utf-8; mode: rst -*-

===========
rv770_dma.c
===========


.. _`rv770_copy_dma`:

rv770_copy_dma
==============

.. c:function:: struct radeon_fence *rv770_copy_dma (struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

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



.. _`rv770_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (r7xx).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

