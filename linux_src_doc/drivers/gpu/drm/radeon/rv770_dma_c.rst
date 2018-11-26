.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/rv770_dma.c

.. _`rv770_copy_dma`:

rv770_copy_dma
==============

.. c:function:: struct radeon_fence *rv770_copy_dma(struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

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

.. _`rv770_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (r7xx).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

.. This file was automatic generated / don't edit.

