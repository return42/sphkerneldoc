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

.. _`amdgpu_ring_backup`:

amdgpu_ring_backup
==================

.. c:function:: unsigned amdgpu_ring_backup(struct amdgpu_ring *ring, uint32_t **data)

    Back up the content of a ring

    :param struct amdgpu_ring \*ring:
        the ring we want to back up

    :param uint32_t \*\*data:
        *undescribed*

.. _`amdgpu_ring_backup.description`:

Description
-----------

Saves all unprocessed commits from a ring, returns the number of dwords saved.

.. _`amdgpu_ring_restore`:

amdgpu_ring_restore
===================

.. c:function:: int amdgpu_ring_restore(struct amdgpu_ring *ring, unsigned size, uint32_t *data)

    append saved commands to the ring again

    :param struct amdgpu_ring \*ring:
        ring to append commands to

    :param unsigned size:
        number of dwords we want to write

    :param uint32_t \*data:
        saved commands

.. _`amdgpu_ring_restore.description`:

Description
-----------

Allocates space on the ring and restore the previously saved commands.

.. _`amdgpu_ring_init`:

amdgpu_ring_init
================

.. c:function:: int amdgpu_ring_init(struct amdgpu_device *adev, struct amdgpu_ring *ring, unsigned max_dw, u32 nop, u32 align_mask, struct amdgpu_irq_src *irq_src, unsigned irq_type, enum amdgpu_ring_type ring_type)

    init driver ring struct.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring structure holding ring information

    :param unsigned max_dw:
        *undescribed*

    :param u32 nop:
        nop packet for this ring

    :param u32 align_mask:
        *undescribed*

    :param struct amdgpu_irq_src \*irq_src:
        *undescribed*

    :param unsigned irq_type:
        *undescribed*

    :param enum amdgpu_ring_type ring_type:
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

.. This file was automatic generated / don't edit.

