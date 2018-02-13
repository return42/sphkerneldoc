.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ring.c

.. _`amdgpu_ring_alloc`:

amdgpu_ring_alloc
=================

.. c:function:: int amdgpu_ring_alloc(struct amdgpu_ring *ring, unsigned ndw)

    allocate space on the ring buffer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

    :param unsigned ndw:
        number of dwords to allocate in the ring buffer

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

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

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

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

.. _`amdgpu_ring_undo.description`:

Description
-----------

Reset the driver's copy of the wptr (all asics).

.. _`amdgpu_ring_priority_put`:

amdgpu_ring_priority_put
========================

.. c:function:: void amdgpu_ring_priority_put(struct amdgpu_ring *ring, enum drm_sched_priority priority)

    restore a ring's priority

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding the information

    :param enum drm_sched_priority priority:
        target priority

.. _`amdgpu_ring_priority_put.description`:

Description
-----------

Release a request for executing at \ ``priority``\ 

.. _`amdgpu_ring_priority_get`:

amdgpu_ring_priority_get
========================

.. c:function:: void amdgpu_ring_priority_get(struct amdgpu_ring *ring, enum drm_sched_priority priority)

    change the ring's priority

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding the information

    :param enum drm_sched_priority priority:
        target priority

.. _`amdgpu_ring_priority_get.description`:

Description
-----------

Request a ring's priority to be raised to \ ``priority``\  (refcounted).

.. _`amdgpu_ring_init`:

amdgpu_ring_init
================

.. c:function:: int amdgpu_ring_init(struct amdgpu_device *adev, struct amdgpu_ring *ring, unsigned max_dw, struct amdgpu_irq_src *irq_src, unsigned irq_type)

    init driver ring struct.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

    :param unsigned max_dw:
        *undescribed*

    :param struct amdgpu_irq_src \*irq_src:
        *undescribed*

    :param unsigned irq_type:
        *undescribed*

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

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

.. _`amdgpu_ring_fini.description`:

Description
-----------

Tear down the driver information for the selected ring (all asics).

.. _`amdgpu_ring_lru_get`:

amdgpu_ring_lru_get
===================

.. c:function:: int amdgpu_ring_lru_get(struct amdgpu_device *adev, int type, int *blacklist, int num_blacklist, bool lru_pipe_order, struct amdgpu_ring **ring)

    get the least recently used ring for a HW IP block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param int type:
        amdgpu_ring_type enum

    :param int \*blacklist:
        blacklisted ring ids array

    :param int num_blacklist:
        number of entries in \ ``blacklist``\ 

    :param bool lru_pipe_order:
        find a ring from the least recently used pipe

    :param struct amdgpu_ring \*\*ring:
        output ring

.. _`amdgpu_ring_lru_get.description`:

Description
-----------

Retrieve the amdgpu_ring structure for the least recently used ring of
a specific IP block (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_ring_lru_touch`:

amdgpu_ring_lru_touch
=====================

.. c:function:: void amdgpu_ring_lru_touch(struct amdgpu_device *adev, struct amdgpu_ring *ring)

    mark a ring as recently being used

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_ring \*ring:
        ring to touch

.. _`amdgpu_ring_lru_touch.description`:

Description
-----------

Move \ ``ring``\  to the tail of the lru list

.. This file was automatic generated / don't edit.

