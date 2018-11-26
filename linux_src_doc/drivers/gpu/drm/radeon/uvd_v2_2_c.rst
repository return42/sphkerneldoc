.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/uvd_v2_2.c

.. _`uvd_v2_2_fence_emit`:

uvd_v2_2_fence_emit
===================

.. c:function:: void uvd_v2_2_fence_emit(struct radeon_device *rdev, struct radeon_fence *fence)

    emit an fence & trap command

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param fence:
        fence to emit
    :type fence: struct radeon_fence \*

.. _`uvd_v2_2_fence_emit.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`uvd_v2_2_semaphore_emit`:

uvd_v2_2_semaphore_emit
=======================

.. c:function:: bool uvd_v2_2_semaphore_emit(struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

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

.. _`uvd_v2_2_semaphore_emit.description`:

Description
-----------

Emit a semaphore command (either wait or signal) to the UVD ring.

.. _`uvd_v2_2_resume`:

uvd_v2_2_resume
===============

.. c:function:: int uvd_v2_2_resume(struct radeon_device *rdev)

    memory controller programming

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`uvd_v2_2_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets

.. This file was automatic generated / don't edit.

