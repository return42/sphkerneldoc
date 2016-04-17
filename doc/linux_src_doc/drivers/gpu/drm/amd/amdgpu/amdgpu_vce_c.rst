.. -*- coding: utf-8; mode: rst -*-

============
amdgpu_vce.c
============


.. _`amdgpu_vce_sw_init`:

amdgpu_vce_sw_init
==================

.. c:function:: int amdgpu_vce_sw_init (struct amdgpu_device *adev, unsigned long size)

    allocate memory, load vce firmware

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param unsigned long size:

        *undescribed*



.. _`amdgpu_vce_sw_init.description`:

Description
-----------

First step to get VCE online, allocate memory and load the firmware



.. _`amdgpu_vce_sw_fini`:

amdgpu_vce_sw_fini
==================

.. c:function:: int amdgpu_vce_sw_fini (struct amdgpu_device *adev)

    free memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`amdgpu_vce_sw_fini.description`:

Description
-----------

Last step on VCE teardown, free firmware memory



.. _`amdgpu_vce_suspend`:

amdgpu_vce_suspend
==================

.. c:function:: int amdgpu_vce_suspend (struct amdgpu_device *adev)

    unpin VCE fw memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`amdgpu_vce_resume`:

amdgpu_vce_resume
=================

.. c:function:: int amdgpu_vce_resume (struct amdgpu_device *adev)

    pin VCE fw memory

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`amdgpu_vce_idle_work_handler`:

amdgpu_vce_idle_work_handler
============================

.. c:function:: void amdgpu_vce_idle_work_handler (struct work_struct *work)

    power off VCE

    :param struct work_struct \*work:
        pointer to work structure



.. _`amdgpu_vce_idle_work_handler.description`:

Description
-----------

power of VCE when it's not used any more



.. _`amdgpu_vce_note_usage`:

amdgpu_vce_note_usage
=====================

.. c:function:: void amdgpu_vce_note_usage (struct amdgpu_device *adev)

    power up VCE

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`amdgpu_vce_note_usage.description`:

Description
-----------

Make sure VCE is powerd up when we want to use it



.. _`amdgpu_vce_free_handles`:

amdgpu_vce_free_handles
=======================

.. c:function:: void amdgpu_vce_free_handles (struct amdgpu_device *adev, struct drm_file *filp)

    free still open VCE handles

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct drm_file \*filp:
        drm file pointer



.. _`amdgpu_vce_free_handles.description`:

Description
-----------

Close all VCE handles still open by this file pointer



.. _`amdgpu_vce_get_create_msg`:

amdgpu_vce_get_create_msg
=========================

.. c:function:: int amdgpu_vce_get_create_msg (struct amdgpu_ring *ring, uint32_t handle, struct fence **fence)

    generate a VCE create msg

    :param struct amdgpu_ring \*ring:
        ring we should submit the msg to

    :param uint32_t handle:
        VCE session handle to use

    :param struct fence \*\*fence:
        optional fence to return



.. _`amdgpu_vce_get_create_msg.description`:

Description
-----------

Open up a stream for HW test



.. _`amdgpu_vce_get_destroy_msg`:

amdgpu_vce_get_destroy_msg
==========================

.. c:function:: int amdgpu_vce_get_destroy_msg (struct amdgpu_ring *ring, uint32_t handle, bool direct, struct fence **fence)

    generate a VCE destroy msg

    :param struct amdgpu_ring \*ring:
        ring we should submit the msg to

    :param uint32_t handle:
        VCE session handle to use

    :param bool direct:

        *undescribed*

    :param struct fence \*\*fence:
        optional fence to return



.. _`amdgpu_vce_get_destroy_msg.description`:

Description
-----------

Close up a stream for HW test or if userspace failed to do so



.. _`amdgpu_vce_cs_reloc`:

amdgpu_vce_cs_reloc
===================

.. c:function:: int amdgpu_vce_cs_reloc (struct amdgpu_cs_parser *p, uint32_t ib_idx, int lo, int hi, unsigned size, uint32_t index)

    command submission relocation

    :param struct amdgpu_cs_parser \*p:
        parser context

    :param uint32_t ib_idx:

        *undescribed*

    :param int lo:
        address of lower dword

    :param int hi:
        address of higher dword

    :param unsigned size:
        minimum size

    :param uint32_t index:

        *undescribed*



.. _`amdgpu_vce_cs_reloc.description`:

Description
-----------

Patch relocation inside command stream with real buffer address



.. _`amdgpu_vce_validate_handle`:

amdgpu_vce_validate_handle
==========================

.. c:function:: int amdgpu_vce_validate_handle (struct amdgpu_cs_parser *p, uint32_t handle, bool *allocated)

    validate stream handle

    :param struct amdgpu_cs_parser \*p:
        parser context

    :param uint32_t handle:
        handle to validate

    :param bool \*allocated:
        allocated a new handle?



.. _`amdgpu_vce_validate_handle.description`:

Description
-----------

Validates the handle and return the found session index or -EINVAL
we we don't have another free session index.



.. _`amdgpu_vce_ring_parse_cs`:

amdgpu_vce_ring_parse_cs
========================

.. c:function:: int amdgpu_vce_ring_parse_cs (struct amdgpu_cs_parser *p, uint32_t ib_idx)

    parse and validate the command stream

    :param struct amdgpu_cs_parser \*p:
        parser context

    :param uint32_t ib_idx:

        *undescribed*



.. _`amdgpu_vce_ring_emit_ib`:

amdgpu_vce_ring_emit_ib
=======================

.. c:function:: void amdgpu_vce_ring_emit_ib (struct amdgpu_ring *ring, struct amdgpu_ib *ib)

    execute indirect buffer

    :param struct amdgpu_ring \*ring:
        engine to use

    :param struct amdgpu_ib \*ib:
        the IB to execute



.. _`amdgpu_vce_ring_emit_fence`:

amdgpu_vce_ring_emit_fence
==========================

.. c:function:: void amdgpu_vce_ring_emit_fence (struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    add a fence command to the ring

    :param struct amdgpu_ring \*ring:
        engine to use

    :param u64 addr:

        *undescribed*

    :param u64 seq:

        *undescribed*

    :param unsigned flags:

        *undescribed*



.. _`amdgpu_vce_ring_test_ring`:

amdgpu_vce_ring_test_ring
=========================

.. c:function:: int amdgpu_vce_ring_test_ring (struct amdgpu_ring *ring)

    test if VCE ring is working

    :param struct amdgpu_ring \*ring:
        the engine to test on



.. _`amdgpu_vce_ring_test_ib`:

amdgpu_vce_ring_test_ib
=======================

.. c:function:: int amdgpu_vce_ring_test_ib (struct amdgpu_ring *ring)

    test if VCE IBs are working

    :param struct amdgpu_ring \*ring:
        the engine to test on

