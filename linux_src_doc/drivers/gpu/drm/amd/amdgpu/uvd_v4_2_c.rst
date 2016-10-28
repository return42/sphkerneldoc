.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/uvd_v4_2.c

.. _`uvd_v4_2_ring_get_rptr`:

uvd_v4_2_ring_get_rptr
======================

.. c:function:: uint32_t uvd_v4_2_ring_get_rptr(struct amdgpu_ring *ring)

    get read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v4_2_ring_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer

.. _`uvd_v4_2_ring_get_wptr`:

uvd_v4_2_ring_get_wptr
======================

.. c:function:: uint32_t uvd_v4_2_ring_get_wptr(struct amdgpu_ring *ring)

    get write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v4_2_ring_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer

.. _`uvd_v4_2_ring_set_wptr`:

uvd_v4_2_ring_set_wptr
======================

.. c:function:: void uvd_v4_2_ring_set_wptr(struct amdgpu_ring *ring)

    set write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v4_2_ring_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware

.. _`uvd_v4_2_hw_init`:

uvd_v4_2_hw_init
================

.. c:function:: int uvd_v4_2_hw_init(void *handle)

    start and test UVD block

    :param void \*handle:
        *undescribed*

.. _`uvd_v4_2_hw_init.description`:

Description
-----------

Initialize the hardware, boot up the VCPU and do some testing

.. _`uvd_v4_2_hw_fini`:

uvd_v4_2_hw_fini
================

.. c:function:: int uvd_v4_2_hw_fini(void *handle)

    stop the hardware block

    :param void \*handle:
        *undescribed*

.. _`uvd_v4_2_hw_fini.description`:

Description
-----------

Stop the UVD block, mark ring as not ready any more

.. _`uvd_v4_2_start`:

uvd_v4_2_start
==============

.. c:function:: int uvd_v4_2_start(struct amdgpu_device *adev)

    start UVD block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`uvd_v4_2_start.description`:

Description
-----------

Setup and start the UVD block

.. _`uvd_v4_2_stop`:

uvd_v4_2_stop
=============

.. c:function:: void uvd_v4_2_stop(struct amdgpu_device *adev)

    stop UVD block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`uvd_v4_2_stop.description`:

Description
-----------

stop the UVD block

.. _`uvd_v4_2_ring_emit_fence`:

uvd_v4_2_ring_emit_fence
========================

.. c:function:: void uvd_v4_2_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an fence & trap command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`uvd_v4_2_ring_emit_fence.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`uvd_v4_2_ring_test_ring`:

uvd_v4_2_ring_test_ring
=======================

.. c:function:: int uvd_v4_2_ring_test_ring(struct amdgpu_ring *ring)

    register write test

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v4_2_ring_test_ring.description`:

Description
-----------

Test if we can successfully write to the context register

.. _`uvd_v4_2_ring_emit_ib`:

uvd_v4_2_ring_emit_ib
=====================

.. c:function:: void uvd_v4_2_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vm_id, bool ctx_switch)

    execute indirect buffer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param struct amdgpu_ib \*ib:
        indirect buffer to execute

    :param unsigned vm_id:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`uvd_v4_2_ring_emit_ib.description`:

Description
-----------

Write ring commands to execute the indirect buffer

.. _`uvd_v4_2_ring_test_ib`:

uvd_v4_2_ring_test_ib
=====================

.. c:function:: int uvd_v4_2_ring_test_ib(struct amdgpu_ring *ring)

    test ib execution

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v4_2_ring_test_ib.description`:

Description
-----------

Test if we can successfully execute an IB

.. _`uvd_v4_2_mc_resume`:

uvd_v4_2_mc_resume
==================

.. c:function:: void uvd_v4_2_mc_resume(struct amdgpu_device *adev)

    memory controller programming

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`uvd_v4_2_mc_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets

.. This file was automatic generated / don't edit.

