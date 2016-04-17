.. -*- coding: utf-8; mode: rst -*-

==========
uvd_v1_0.c
==========


.. _`uvd_v1_0_get_rptr`:

uvd_v1_0_get_rptr
=================

.. c:function:: uint32_t uvd_v1_0_get_rptr (struct radeon_device *rdev, struct radeon_ring *ring)

    get read pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`uvd_v1_0_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer



.. _`uvd_v1_0_get_wptr`:

uvd_v1_0_get_wptr
=================

.. c:function:: uint32_t uvd_v1_0_get_wptr (struct radeon_device *rdev, struct radeon_ring *ring)

    get write pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`uvd_v1_0_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer



.. _`uvd_v1_0_set_wptr`:

uvd_v1_0_set_wptr
=================

.. c:function:: void uvd_v1_0_set_wptr (struct radeon_device *rdev, struct radeon_ring *ring)

    set write pointer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`uvd_v1_0_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware



.. _`uvd_v1_0_fence_emit`:

uvd_v1_0_fence_emit
===================

.. c:function:: void uvd_v1_0_fence_emit (struct radeon_device *rdev, struct radeon_fence *fence)

    emit an fence & trap command

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        fence to emit



.. _`uvd_v1_0_fence_emit.description`:

Description
-----------

Write a fence and a trap command to the ring.



.. _`uvd_v1_0_resume`:

uvd_v1_0_resume
===============

.. c:function:: int uvd_v1_0_resume (struct radeon_device *rdev)

    memory controller programming

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`uvd_v1_0_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets



.. _`uvd_v1_0_init`:

uvd_v1_0_init
=============

.. c:function:: int uvd_v1_0_init (struct radeon_device *rdev)

    start and test UVD block

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`uvd_v1_0_init.description`:

Description
-----------

Initialize the hardware, boot up the VCPU and do some testing



.. _`uvd_v1_0_fini`:

uvd_v1_0_fini
=============

.. c:function:: void uvd_v1_0_fini (struct radeon_device *rdev)

    stop the hardware block

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`uvd_v1_0_fini.description`:

Description
-----------

Stop the UVD block, mark ring as not ready any more



.. _`uvd_v1_0_start`:

uvd_v1_0_start
==============

.. c:function:: int uvd_v1_0_start (struct radeon_device *rdev)

    start UVD block

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`uvd_v1_0_start.description`:

Description
-----------

Setup and start the UVD block



.. _`uvd_v1_0_stop`:

uvd_v1_0_stop
=============

.. c:function:: void uvd_v1_0_stop (struct radeon_device *rdev)

    stop UVD block

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`uvd_v1_0_stop.description`:

Description
-----------

stop the UVD block



.. _`uvd_v1_0_ring_test`:

uvd_v1_0_ring_test
==================

.. c:function:: int uvd_v1_0_ring_test (struct radeon_device *rdev, struct radeon_ring *ring)

    register write test

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`uvd_v1_0_ring_test.description`:

Description
-----------

Test if we can successfully write to the context register



.. _`uvd_v1_0_semaphore_emit`:

uvd_v1_0_semaphore_emit
=======================

.. c:function:: bool uvd_v1_0_semaphore_emit (struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit semaphore command

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer

    :param struct radeon_semaphore \*semaphore:
        semaphore to emit commands for

    :param bool emit_wait:
        true if we should emit a wait command



.. _`uvd_v1_0_semaphore_emit.description`:

Description
-----------

Emit a semaphore command (either wait or signal) to the UVD ring.



.. _`uvd_v1_0_ib_execute`:

uvd_v1_0_ib_execute
===================

.. c:function:: void uvd_v1_0_ib_execute (struct radeon_device *rdev, struct radeon_ib *ib)

    execute indirect buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        indirect buffer to execute



.. _`uvd_v1_0_ib_execute.description`:

Description
-----------

Write ring commands to execute the indirect buffer



.. _`uvd_v1_0_ib_test`:

uvd_v1_0_ib_test
================

.. c:function:: int uvd_v1_0_ib_test (struct radeon_device *rdev, struct radeon_ring *ring)

    test ib execution

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring pointer



.. _`uvd_v1_0_ib_test.description`:

Description
-----------

Test if we can successfully execute an IB

