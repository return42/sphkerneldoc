.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/uvd_v2_2.c

.. _`uvd_v2_2_fence_emit`:

uvd_v2_2_fence_emit
===================

.. c:function:: void uvd_v2_2_fence_emit(struct radeon_device *rdev, struct radeon_fence *fence)

    emit an fence & trap command

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        fence to emit

.. _`uvd_v2_2_fence_emit.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`uvd_v2_2_semaphore_emit`:

uvd_v2_2_semaphore_emit
=======================

.. c:function:: bool uvd_v2_2_semaphore_emit(struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit semaphore command

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer

    :param struct radeon_semaphore \*semaphore:
        semaphore to emit commands for

    :param bool emit_wait:
        true if we should emit a wait command

.. _`uvd_v2_2_semaphore_emit.description`:

Description
-----------

Emit a semaphore command (either wait or signal) to the UVD ring.

.. _`uvd_v2_2_resume`:

uvd_v2_2_resume
===============

.. c:function:: int uvd_v2_2_resume(struct radeon_device *rdev)

    memory controller programming

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`uvd_v2_2_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets

.. This file was automatic generated / don't edit.

