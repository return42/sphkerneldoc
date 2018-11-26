.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/evergreen_dma.c

.. _`evergreen_dma_fence_ring_emit`:

evergreen_dma_fence_ring_emit
=============================

.. c:function:: void evergreen_dma_fence_ring_emit(struct radeon_device *rdev, struct radeon_fence *fence)

    emit a fence on the DMA ring

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param fence:
        radeon fence object
    :type fence: struct radeon_fence \*

.. _`evergreen_dma_fence_ring_emit.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (evergreen-SI).

.. _`evergreen_dma_ring_ib_execute`:

evergreen_dma_ring_ib_execute
=============================

.. c:function:: void evergreen_dma_ring_ib_execute(struct radeon_device *rdev, struct radeon_ib *ib)

    schedule an IB on the DMA engine

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        IB object to schedule
    :type ib: struct radeon_ib \*

.. _`evergreen_dma_ring_ib_execute.description`:

Description
-----------

Schedule an IB in the DMA ring (evergreen).

.. _`evergreen_copy_dma`:

evergreen_copy_dma
==================

.. c:function:: struct radeon_fence *evergreen_copy_dma(struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

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
        *undescribed*
    :type resv: struct reservation_object \*

.. _`evergreen_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (evergreen-cayman).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

.. _`evergreen_dma_is_lockup`:

evergreen_dma_is_lockup
=======================

.. c:function:: bool evergreen_dma_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

.. _`evergreen_dma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up.
Returns true if the engine appears to be locked up, false if not.

.. This file was automatic generated / don't edit.

