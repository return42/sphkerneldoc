.. -*- coding: utf-8; mode: rst -*-

===============
evergreen_dma.c
===============


.. _`evergreen_dma_fence_ring_emit`:

evergreen_dma_fence_ring_emit
=============================

.. c:function:: void evergreen_dma_fence_ring_emit (struct radeon_device *rdev, struct radeon_fence *fence)

    emit a fence on the DMA ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        radeon fence object



.. _`evergreen_dma_fence_ring_emit.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (evergreen-SI).



.. _`evergreen_dma_ring_ib_execute`:

evergreen_dma_ring_ib_execute
=============================

.. c:function:: void evergreen_dma_ring_ib_execute (struct radeon_device *rdev, struct radeon_ib *ib)

    schedule an IB on the DMA engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        IB object to schedule



.. _`evergreen_dma_ring_ib_execute.description`:

Description
-----------

Schedule an IB in the DMA ring (evergreen).



.. _`evergreen_copy_dma`:

evergreen_copy_dma
==================

.. c:function:: struct radeon_fence *evergreen_copy_dma (struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

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

        *undescribed*



.. _`evergreen_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (evergreen-cayman).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.



.. _`evergreen_dma_is_lockup`:

evergreen_dma_is_lockup
=======================

.. c:function:: bool evergreen_dma_is_lockup (struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information



.. _`evergreen_dma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up.
Returns true if the engine appears to be locked up, false if not.

