.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/r600_dma.c

.. _`r600_dma_get_rptr`:

r600_dma_get_rptr
=================

.. c:function:: uint32_t r600_dma_get_rptr(struct radeon_device *rdev, struct radeon_ring *ring)

    get the current read pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon ring pointer

.. _`r600_dma_get_rptr.description`:

Description
-----------

Get the current rptr from the hardware (r6xx+).

.. _`r600_dma_get_wptr`:

r600_dma_get_wptr
=================

.. c:function:: uint32_t r600_dma_get_wptr(struct radeon_device *rdev, struct radeon_ring *ring)

    get the current write pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon ring pointer

.. _`r600_dma_get_wptr.description`:

Description
-----------

Get the current wptr from the hardware (r6xx+).

.. _`r600_dma_set_wptr`:

r600_dma_set_wptr
=================

.. c:function:: void r600_dma_set_wptr(struct radeon_device *rdev, struct radeon_ring *ring)

    commit the write pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon ring pointer

.. _`r600_dma_set_wptr.description`:

Description
-----------

Write the wptr back to the hardware (r6xx+).

.. _`r600_dma_stop`:

r600_dma_stop
=============

.. c:function:: void r600_dma_stop(struct radeon_device *rdev)

    stop the async dma engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`r600_dma_stop.description`:

Description
-----------

Stop the async dma engine (r6xx-evergreen).

.. _`r600_dma_resume`:

r600_dma_resume
===============

.. c:function:: int r600_dma_resume(struct radeon_device *rdev)

    setup and start the async dma engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`r600_dma_resume.description`:

Description
-----------

Set up the DMA ring buffer and enable it. (r6xx-evergreen).
Returns 0 for success, error for failure.

.. _`r600_dma_fini`:

r600_dma_fini
=============

.. c:function:: void r600_dma_fini(struct radeon_device *rdev)

    tear down the async dma engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`r600_dma_fini.description`:

Description
-----------

Stop the async dma engine and free the ring (r6xx-evergreen).

.. _`r600_dma_is_lockup`:

r600_dma_is_lockup
==================

.. c:function:: bool r600_dma_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`r600_dma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up.
Returns true if the engine appears to be locked up, false if not.

.. _`r600_dma_ring_test`:

r600_dma_ring_test
==================

.. c:function:: int r600_dma_ring_test(struct radeon_device *rdev, struct radeon_ring *ring)

    simple async dma engine test

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`r600_dma_ring_test.description`:

Description
-----------

Test the DMA engine by writing using it to write an
value to memory. (r6xx-SI).
Returns 0 for success, error for failure.

.. _`r600_dma_fence_ring_emit`:

r600_dma_fence_ring_emit
========================

.. c:function:: void r600_dma_fence_ring_emit(struct radeon_device *rdev, struct radeon_fence *fence)

    emit a fence on the DMA ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        radeon fence object

.. _`r600_dma_fence_ring_emit.description`:

Description
-----------

Add a DMA fence packet to the ring to write
the fence seq number and DMA trap packet to generate
an interrupt if needed (r6xx-r7xx).

.. _`r600_dma_semaphore_ring_emit`:

r600_dma_semaphore_ring_emit
============================

.. c:function:: bool r600_dma_semaphore_ring_emit(struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit a semaphore on the dma ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

    :param struct radeon_semaphore \*semaphore:
        radeon semaphore object

    :param bool emit_wait:
        wait or signal semaphore

.. _`r600_dma_semaphore_ring_emit.description`:

Description
-----------

Add a DMA semaphore packet to the ring wait on or signal
other rings (r6xx-SI).

.. _`r600_dma_ib_test`:

r600_dma_ib_test
================

.. c:function:: int r600_dma_ib_test(struct radeon_device *rdev, struct radeon_ring *ring)

    test an IB on the DMA engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`r600_dma_ib_test.description`:

Description
-----------

Test a simple IB in the DMA ring (r6xx-SI).
Returns 0 on success, error on failure.

.. _`r600_dma_ring_ib_execute`:

r600_dma_ring_ib_execute
========================

.. c:function:: void r600_dma_ring_ib_execute(struct radeon_device *rdev, struct radeon_ib *ib)

    Schedule an IB on the DMA engine

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        IB object to schedule

.. _`r600_dma_ring_ib_execute.description`:

Description
-----------

Schedule an IB in the DMA ring (r6xx-r7xx).

.. _`r600_copy_dma`:

r600_copy_dma
=============

.. c:function:: struct radeon_fence *r600_copy_dma(struct radeon_device *rdev, uint64_t src_offset, uint64_t dst_offset, unsigned num_gpu_pages, struct reservation_object *resv)

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

.. _`r600_copy_dma.description`:

Description
-----------

Copy GPU paging using the DMA engine (r6xx).
Used by the radeon ttm implementation to move pages if
registered as the asic copy callback.

.. This file was automatic generated / don't edit.

