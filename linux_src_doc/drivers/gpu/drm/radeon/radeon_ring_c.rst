.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_ring.c

.. _`radeon_ring_supports_scratch_reg`:

radeon_ring_supports_scratch_reg
================================

.. c:function:: bool radeon_ring_supports_scratch_reg(struct radeon_device *rdev, struct radeon_ring *ring)

    check if the ring supports writing to scratch registers

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_supports_scratch_reg.description`:

Description
-----------

Check if a specific ring supports writing to scratch registers (all asics).
Returns true if the ring supports writing to scratch regs, false if not.

.. _`radeon_ring_free_size`:

radeon_ring_free_size
=====================

.. c:function:: void radeon_ring_free_size(struct radeon_device *rdev, struct radeon_ring *ring)

    update the free size

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_free_size.description`:

Description
-----------

Update the free dw slots in the ring buffer (all asics).

.. _`radeon_ring_alloc`:

radeon_ring_alloc
=================

.. c:function:: int radeon_ring_alloc(struct radeon_device *rdev, struct radeon_ring *ring, unsigned ndw)

    allocate space on the ring buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

    :param unsigned ndw:
        number of dwords to allocate in the ring buffer

.. _`radeon_ring_alloc.description`:

Description
-----------

Allocate \ ``ndw``\  dwords in the ring buffer (all asics).
Returns 0 on success, error on failure.

.. _`radeon_ring_lock`:

radeon_ring_lock
================

.. c:function:: int radeon_ring_lock(struct radeon_device *rdev, struct radeon_ring *ring, unsigned ndw)

    lock the ring and allocate space on it

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

    :param unsigned ndw:
        number of dwords to allocate in the ring buffer

.. _`radeon_ring_lock.description`:

Description
-----------

Lock the ring and allocate \ ``ndw``\  dwords in the ring buffer
(all asics).
Returns 0 on success, error on failure.

.. _`radeon_ring_commit`:

radeon_ring_commit
==================

.. c:function:: void radeon_ring_commit(struct radeon_device *rdev, struct radeon_ring *ring, bool hdp_flush)

    tell the GPU to execute the new commands on the ring buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

    :param bool hdp_flush:
        Whether or not to perform an HDP cache flush

.. _`radeon_ring_commit.description`:

Description
-----------

Update the wptr (write pointer) to tell the GPU to
execute new commands on the ring buffer (all asics).

.. _`radeon_ring_unlock_commit`:

radeon_ring_unlock_commit
=========================

.. c:function:: void radeon_ring_unlock_commit(struct radeon_device *rdev, struct radeon_ring *ring, bool hdp_flush)

    tell the GPU to execute the new commands on the ring buffer and unlock it

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

    :param bool hdp_flush:
        Whether or not to perform an HDP cache flush

.. _`radeon_ring_unlock_commit.description`:

Description
-----------

Call \ :c:func:`radeon_ring_commit`\  then unlock the ring (all asics).

.. _`radeon_ring_undo`:

radeon_ring_undo
================

.. c:function:: void radeon_ring_undo(struct radeon_ring *ring)

    reset the wptr

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_undo.description`:

Description
-----------

Reset the driver's copy of the wptr (all asics).

.. _`radeon_ring_unlock_undo`:

radeon_ring_unlock_undo
=======================

.. c:function:: void radeon_ring_unlock_undo(struct radeon_device *rdev, struct radeon_ring *ring)

    reset the wptr and unlock the ring

    :param struct radeon_device \*rdev:
        *undescribed*

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_unlock_undo.description`:

Description
-----------

Call \ :c:func:`radeon_ring_undo`\  then unlock the ring (all asics).

.. _`radeon_ring_lockup_update`:

radeon_ring_lockup_update
=========================

.. c:function:: void radeon_ring_lockup_update(struct radeon_device *rdev, struct radeon_ring *ring)

    update lockup variables

    :param struct radeon_device \*rdev:
        *undescribed*

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_lockup_update.description`:

Description
-----------

Update the last rptr value and timestamp (all asics).

.. _`radeon_ring_test_lockup`:

radeon_ring_test_lockup
=======================

.. c:function:: bool radeon_ring_test_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    check if ring is lockedup by recording information

    :param struct radeon_device \*rdev:
        radeon device structure

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_backup`:

radeon_ring_backup
==================

.. c:function:: unsigned radeon_ring_backup(struct radeon_device *rdev, struct radeon_ring *ring, uint32_t **data)

    Back up the content of a ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        the ring we want to back up

    :param uint32_t \*\*data:
        *undescribed*

.. _`radeon_ring_backup.description`:

Description
-----------

Saves all unprocessed commits from a ring, returns the number of dwords saved.

.. _`radeon_ring_restore`:

radeon_ring_restore
===================

.. c:function:: int radeon_ring_restore(struct radeon_device *rdev, struct radeon_ring *ring, unsigned size, uint32_t *data)

    append saved commands to the ring again

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        ring to append commands to

    :param unsigned size:
        number of dwords we want to write

    :param uint32_t \*data:
        saved commands

.. _`radeon_ring_restore.description`:

Description
-----------

Allocates space on the ring and restore the previously saved commands.

.. _`radeon_ring_init`:

radeon_ring_init
================

.. c:function:: int radeon_ring_init(struct radeon_device *rdev, struct radeon_ring *ring, unsigned ring_size, unsigned rptr_offs, u32 nop)

    init driver ring struct.

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

    :param unsigned ring_size:
        size of the ring

    :param unsigned rptr_offs:
        offset of the rptr writeback location in the WB buffer

    :param u32 nop:
        nop packet for this ring

.. _`radeon_ring_init.description`:

Description
-----------

Initialize the driver information for the selected ring (all asics).
Returns 0 on success, error on failure.

.. _`radeon_ring_fini`:

radeon_ring_fini
================

.. c:function:: void radeon_ring_fini(struct radeon_device *rdev, struct radeon_ring *ring)

    tear down the driver ring struct.

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`radeon_ring_fini.description`:

Description
-----------

Tear down the driver information for the selected ring (all asics).

.. This file was automatic generated / don't edit.

