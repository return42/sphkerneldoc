.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/uvd_v3_1.c

.. _`uvd_v3_1_semaphore_emit`:

uvd_v3_1_semaphore_emit
=======================

.. c:function:: bool uvd_v3_1_semaphore_emit(struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit semaphore command

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer

    :param struct radeon_semaphore \*semaphore:
        semaphore to emit commands for

    :param bool emit_wait:
        true if we should emit a wait command

.. _`uvd_v3_1_semaphore_emit.description`:

Description
-----------

Emit a semaphore command (either wait or signal) to the UVD ring.

.. This file was automatic generated / don't edit.

