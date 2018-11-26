.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/uvd_v3_1.c

.. _`uvd_v3_1_semaphore_emit`:

uvd_v3_1_semaphore_emit
=======================

.. c:function:: bool uvd_v3_1_semaphore_emit(struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit semaphore command

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        radeon_ring pointer
    :type ring: struct radeon_ring \*

    :param semaphore:
        semaphore to emit commands for
    :type semaphore: struct radeon_semaphore \*

    :param emit_wait:
        true if we should emit a wait command
    :type emit_wait: bool

.. _`uvd_v3_1_semaphore_emit.description`:

Description
-----------

Emit a semaphore command (either wait or signal) to the UVD ring.

.. This file was automatic generated / don't edit.

