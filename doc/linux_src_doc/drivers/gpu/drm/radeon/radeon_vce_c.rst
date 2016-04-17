.. -*- coding: utf-8; mode: rst -*-

============
radeon_vce.c
============


.. _`radeon_vce_init`:

radeon_vce_init
===============

.. c:function:: int radeon_vce_init (struct radeon_device *rdev)

    allocate memory, load vce firmware

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`radeon_vce_init.description`:

Description
-----------

First step to get VCE online, allocate memory and load the firmware



.. _`radeon_vce_fini`:

radeon_vce_fini
===============

.. c:function:: void radeon_vce_fini (struct radeon_device *rdev)

    free memory

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`radeon_vce_fini.description`:

Description
-----------

Last step on VCE teardown, free firmware memory



.. _`radeon_vce_suspend`:

radeon_vce_suspend
==================

.. c:function:: int radeon_vce_suspend (struct radeon_device *rdev)

    unpin VCE fw memory

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`radeon_vce_resume`:

radeon_vce_resume
=================

.. c:function:: int radeon_vce_resume (struct radeon_device *rdev)

    pin VCE fw memory

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`radeon_vce_idle_work_handler`:

radeon_vce_idle_work_handler
============================

.. c:function:: void radeon_vce_idle_work_handler (struct work_struct *work)

    power off VCE

    :param struct work_struct \*work:
        pointer to work structure



.. _`radeon_vce_idle_work_handler.description`:

Description
-----------

power of VCE when it's not used any more



.. _`radeon_vce_note_usage`:

radeon_vce_note_usage
=====================

.. c:function:: void radeon_vce_note_usage (struct radeon_device *rdev)

    power up VCE

    :param struct radeon_device \*rdev:
        radeon_device pointer



.. _`radeon_vce_note_usage.description`:

Description
-----------

Make sure VCE is powerd up when we want to use it



.. _`radeon_vce_free_handles`:

radeon_vce_free_handles
=======================

.. c:function:: void radeon_vce_free_handles (struct radeon_device *rdev, struct drm_file *filp)

    free still open VCE handles

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct drm_file \*filp:
        drm file pointer



.. _`radeon_vce_free_handles.description`:

Description
-----------

Close all VCE handles still open by this file pointer



.. _`radeon_vce_get_create_msg`:

radeon_vce_get_create_msg
=========================

.. c:function:: int radeon_vce_get_create_msg (struct radeon_device *rdev, int ring, uint32_t handle, struct radeon_fence **fence)

    generate a VCE create msg

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ring:
        ring we should submit the msg to

    :param uint32_t handle:
        VCE session handle to use

    :param struct radeon_fence \*\*fence:
        optional fence to return



.. _`radeon_vce_get_create_msg.description`:

Description
-----------

Open up a stream for HW test



.. _`radeon_vce_get_destroy_msg`:

radeon_vce_get_destroy_msg
==========================

.. c:function:: int radeon_vce_get_destroy_msg (struct radeon_device *rdev, int ring, uint32_t handle, struct radeon_fence **fence)

    generate a VCE destroy msg

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ring:
        ring we should submit the msg to

    :param uint32_t handle:
        VCE session handle to use

    :param struct radeon_fence \*\*fence:
        optional fence to return



.. _`radeon_vce_get_destroy_msg.description`:

Description
-----------

Close up a stream for HW test or if userspace failed to do so



.. _`radeon_vce_cs_reloc`:

radeon_vce_cs_reloc
===================

.. c:function:: int radeon_vce_cs_reloc (struct radeon_cs_parser *p, int lo, int hi, unsigned size)

    command submission relocation

    :param struct radeon_cs_parser \*p:
        parser context

    :param int lo:
        address of lower dword

    :param int hi:
        address of higher dword

    :param unsigned size:
        size of checker for relocation buffer



.. _`radeon_vce_cs_reloc.description`:

Description
-----------

Patch relocation inside command stream with real buffer address



.. _`radeon_vce_validate_handle`:

radeon_vce_validate_handle
==========================

.. c:function:: int radeon_vce_validate_handle (struct radeon_cs_parser *p, uint32_t handle, bool *allocated)

    validate stream handle

    :param struct radeon_cs_parser \*p:
        parser context

    :param uint32_t handle:
        handle to validate

    :param bool \*allocated:
        allocated a new handle?



.. _`radeon_vce_validate_handle.description`:

Description
-----------

Validates the handle and return the found session index or -EINVAL
we we don't have another free session index.



.. _`radeon_vce_cs_parse`:

radeon_vce_cs_parse
===================

.. c:function:: int radeon_vce_cs_parse (struct radeon_cs_parser *p)

    parse and validate the command stream

    :param struct radeon_cs_parser \*p:
        parser context



.. _`radeon_vce_semaphore_emit`:

radeon_vce_semaphore_emit
=========================

.. c:function:: bool radeon_vce_semaphore_emit (struct radeon_device *rdev, struct radeon_ring *ring, struct radeon_semaphore *semaphore, bool emit_wait)

    emit a semaphore command

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        engine to use

    :param struct radeon_semaphore \*semaphore:
        address of semaphore

    :param bool emit_wait:
        true=emit wait, false=emit signal



.. _`radeon_vce_ib_execute`:

radeon_vce_ib_execute
=====================

.. c:function:: void radeon_vce_ib_execute (struct radeon_device *rdev, struct radeon_ib *ib)

    execute indirect buffer

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ib \*ib:
        the IB to execute



.. _`radeon_vce_fence_emit`:

radeon_vce_fence_emit
=====================

.. c:function:: void radeon_vce_fence_emit (struct radeon_device *rdev, struct radeon_fence *fence)

    add a fence command to the ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*fence:
        the fence



.. _`radeon_vce_ring_test`:

radeon_vce_ring_test
====================

.. c:function:: int radeon_vce_ring_test (struct radeon_device *rdev, struct radeon_ring *ring)

    test if VCE ring is working

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        the engine to test on



.. _`radeon_vce_ib_test`:

radeon_vce_ib_test
==================

.. c:function:: int radeon_vce_ib_test (struct radeon_device *rdev, struct radeon_ring *ring)

    test if VCE IBs are working

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        the engine to test on

