.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/ni_dma.c

.. _`cayman_dma_get_rptr`:

cayman_dma_get_rptr
===================

.. c:function:: uint32_t cayman_dma_get_rptr(struct radeon_device *rdev, struct radeon_ring *ring)

    get the current read pointer

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon ring pointer
    :type ring: struct radeon_ring \*

.. _`cayman_dma_get_rptr.description`:

Description
-----------

Get the current rptr from the hardware (cayman+).

.. _`cayman_dma_get_wptr`:

cayman_dma_get_wptr
===================

.. c:function:: uint32_t cayman_dma_get_wptr(struct radeon_device *rdev, struct radeon_ring *ring)

    get the current write pointer

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon ring pointer
    :type ring: struct radeon_ring \*

.. _`cayman_dma_get_wptr.description`:

Description
-----------

Get the current wptr from the hardware (cayman+).

.. _`cayman_dma_set_wptr`:

cayman_dma_set_wptr
===================

.. c:function:: void cayman_dma_set_wptr(struct radeon_device *rdev, struct radeon_ring *ring)

    commit the write pointer

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon ring pointer
    :type ring: struct radeon_ring \*

.. _`cayman_dma_set_wptr.description`:

Description
-----------

Write the wptr back to the hardware (cayman+).

.. _`cayman_dma_ring_ib_execute`:

cayman_dma_ring_ib_execute
==========================

.. c:function:: void cayman_dma_ring_ib_execute(struct radeon_device *rdev, struct radeon_ib *ib)

    Schedule an IB on the DMA engine

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        IB object to schedule
    :type ib: struct radeon_ib \*

.. _`cayman_dma_ring_ib_execute.description`:

Description
-----------

Schedule an IB in the DMA ring (cayman-SI).

.. _`cayman_dma_stop`:

cayman_dma_stop
===============

.. c:function:: void cayman_dma_stop(struct radeon_device *rdev)

    stop the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cayman_dma_stop.description`:

Description
-----------

Stop the async dma engines (cayman-SI).

.. _`cayman_dma_resume`:

cayman_dma_resume
=================

.. c:function:: int cayman_dma_resume(struct radeon_device *rdev)

    setup and start the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cayman_dma_resume.description`:

Description
-----------

Set up the DMA ring buffers and enable them. (cayman-SI).
Returns 0 for success, error for failure.

.. _`cayman_dma_fini`:

cayman_dma_fini
===============

.. c:function:: void cayman_dma_fini(struct radeon_device *rdev)

    tear down the async dma engines

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`cayman_dma_fini.description`:

Description
-----------

Stop the async dma engines and free the rings (cayman-SI).

.. _`cayman_dma_is_lockup`:

cayman_dma_is_lockup
====================

.. c:function:: bool cayman_dma_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the DMA engine is locked up

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring structure holding ring information
    :type ring: struct radeon_ring \*

.. _`cayman_dma_is_lockup.description`:

Description
-----------

Check if the async DMA engine is locked up.
Returns true if the engine appears to be locked up, false if not.

.. _`cayman_dma_vm_copy_pages`:

cayman_dma_vm_copy_pages
========================

.. c:function:: void cayman_dma_vm_copy_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t src, unsigned count)

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

.. _`cayman_dma_vm_copy_pages.description`:

Description
-----------

Update PTEs by copying them from the GART using the DMA (cayman/TN).

.. _`cayman_dma_vm_write_pages`:

cayman_dma_vm_write_pages
=========================

.. c:function:: void cayman_dma_vm_write_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

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
        hw access flags
    :type flags: uint32_t

.. _`cayman_dma_vm_write_pages.description`:

Description
-----------

Update PTEs by writing them manually using the DMA (cayman/TN).

.. _`cayman_dma_vm_set_pages`:

cayman_dma_vm_set_pages
=======================

.. c:function:: void cayman_dma_vm_set_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

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
        hw access flags
    :type flags: uint32_t

.. _`cayman_dma_vm_set_pages.description`:

Description
-----------

Update the page tables using the DMA (cayman/TN).

.. _`cayman_dma_vm_pad_ib`:

cayman_dma_vm_pad_ib
====================

.. c:function:: void cayman_dma_vm_pad_ib(struct radeon_ib *ib)

    pad the IB to the required number of dw

    :param ib:
        indirect buffer to fill with padding
    :type ib: struct radeon_ib \*

.. This file was automatic generated / don't edit.

