.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ring.c

.. _`amdgpu_ring_alloc`:

amdgpu_ring_alloc
=================

.. c:function:: int amdgpu_ring_alloc(struct amdgpu_ring *ring, unsigned ndw)

    allocate space on the ring buffer

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

    :param ndw:
        number of dwords to allocate in the ring buffer
    :type ndw: unsigned

.. _`amdgpu_ring_alloc.description`:

Description
-----------

Allocate \ ``ndw``\  dwords in the ring buffer (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_ring_commit`:

amdgpu_ring_commit
==================

.. c:function:: void amdgpu_ring_commit(struct amdgpu_ring *ring)

    tell the GPU to execute the new commands on the ring buffer

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_ring_commit.description`:

Description
-----------

Update the wptr (write pointer) to tell the GPU to
execute new commands on the ring buffer (all asics).

.. _`amdgpu_ring_undo`:

amdgpu_ring_undo
================

.. c:function:: void amdgpu_ring_undo(struct amdgpu_ring *ring)

    reset the wptr

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_ring_undo.description`:

Description
-----------

Reset the driver's copy of the wptr (all asics).

.. _`amdgpu_ring_priority_put`:

amdgpu_ring_priority_put
========================

.. c:function:: void amdgpu_ring_priority_put(struct amdgpu_ring *ring, enum drm_sched_priority priority)

    restore a ring's priority

    :param ring:
        amdgpu_ring structure holding the information
    :type ring: struct amdgpu_ring \*

    :param priority:
        target priority
    :type priority: enum drm_sched_priority

.. _`amdgpu_ring_priority_put.description`:

Description
-----------

Release a request for executing at \ ``priority``\ 

.. _`amdgpu_ring_priority_get`:

amdgpu_ring_priority_get
========================

.. c:function:: void amdgpu_ring_priority_get(struct amdgpu_ring *ring, enum drm_sched_priority priority)

    change the ring's priority

    :param ring:
        amdgpu_ring structure holding the information
    :type ring: struct amdgpu_ring \*

    :param priority:
        target priority
    :type priority: enum drm_sched_priority

.. _`amdgpu_ring_priority_get.description`:

Description
-----------

Request a ring's priority to be raised to \ ``priority``\  (refcounted).

.. _`amdgpu_ring_init`:

amdgpu_ring_init
================

.. c:function:: int amdgpu_ring_init(struct amdgpu_device *adev, struct amdgpu_ring *ring, unsigned max_dw, struct amdgpu_irq_src *irq_src, unsigned irq_type)

    init driver ring struct.

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

    :param max_dw:
        *undescribed*
    :type max_dw: unsigned

    :param irq_src:
        *undescribed*
    :type irq_src: struct amdgpu_irq_src \*

    :param irq_type:
        *undescribed*
    :type irq_type: unsigned

.. _`amdgpu_ring_init.description`:

Description
-----------

Initialize the driver information for the selected ring (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_ring_fini`:

amdgpu_ring_fini
================

.. c:function:: void amdgpu_ring_fini(struct amdgpu_ring *ring)

    tear down the driver ring struct.

    :param ring:
        amdgpu_ring structure holding ring information
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_ring_fini.description`:

Description
-----------

Tear down the driver information for the selected ring (all asics).

.. _`amdgpu_ring_emit_reg_write_reg_wait_helper`:

amdgpu_ring_emit_reg_write_reg_wait_helper
==========================================

.. c:function:: void amdgpu_ring_emit_reg_write_reg_wait_helper(struct amdgpu_ring *ring, uint32_t reg0, uint32_t reg1, uint32_t ref, uint32_t mask)

    ring helper

    :param ring:
        *undescribed*
    :type ring: struct amdgpu_ring \*

    :param reg0:
        register to write
    :type reg0: uint32_t

    :param reg1:
        register to wait on
    :type reg1: uint32_t

    :param ref:
        reference value to write/wait on
    :type ref: uint32_t

    :param mask:
        mask to wait on
    :type mask: uint32_t

.. _`amdgpu_ring_emit_reg_write_reg_wait_helper.description`:

Description
-----------

Helper for rings that don't support write and wait in a
single oneshot packet.

.. _`amdgpu_ring_soft_recovery`:

amdgpu_ring_soft_recovery
=========================

.. c:function:: bool amdgpu_ring_soft_recovery(struct amdgpu_ring *ring, unsigned int vmid, struct dma_fence *fence)

    try to soft recover a ring lockup

    :param ring:
        ring to try the recovery on
    :type ring: struct amdgpu_ring \*

    :param vmid:
        VMID we try to get going again
    :type vmid: unsigned int

    :param fence:
        timedout fence
    :type fence: struct dma_fence \*

.. _`amdgpu_ring_soft_recovery.description`:

Description
-----------

Tries to get a ring proceeding again when it is stuck.

.. This file was automatic generated / don't edit.

