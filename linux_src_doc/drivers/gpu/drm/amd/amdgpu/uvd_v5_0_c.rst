.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/uvd_v5_0.c

.. _`uvd_v5_0_ring_get_rptr`:

uvd_v5_0_ring_get_rptr
======================

.. c:function:: uint64_t uvd_v5_0_ring_get_rptr(struct amdgpu_ring *ring)

    get read pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v5_0_ring_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer

.. _`uvd_v5_0_ring_get_wptr`:

uvd_v5_0_ring_get_wptr
======================

.. c:function:: uint64_t uvd_v5_0_ring_get_wptr(struct amdgpu_ring *ring)

    get write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v5_0_ring_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer

.. _`uvd_v5_0_ring_set_wptr`:

uvd_v5_0_ring_set_wptr
======================

.. c:function:: void uvd_v5_0_ring_set_wptr(struct amdgpu_ring *ring)

    set write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v5_0_ring_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware

.. _`uvd_v5_0_hw_init`:

uvd_v5_0_hw_init
================

.. c:function:: int uvd_v5_0_hw_init(void *handle)

    start and test UVD block

    :param handle:
        *undescribed*
    :type handle: void \*

.. _`uvd_v5_0_hw_init.description`:

Description
-----------

Initialize the hardware, boot up the VCPU and do some testing

.. _`uvd_v5_0_hw_fini`:

uvd_v5_0_hw_fini
================

.. c:function:: int uvd_v5_0_hw_fini(void *handle)

    stop the hardware block

    :param handle:
        *undescribed*
    :type handle: void \*

.. _`uvd_v5_0_hw_fini.description`:

Description
-----------

Stop the UVD block, mark ring as not ready any more

.. _`uvd_v5_0_mc_resume`:

uvd_v5_0_mc_resume
==================

.. c:function:: void uvd_v5_0_mc_resume(struct amdgpu_device *adev)

    memory controller programming

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`uvd_v5_0_mc_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets

.. _`uvd_v5_0_start`:

uvd_v5_0_start
==============

.. c:function:: int uvd_v5_0_start(struct amdgpu_device *adev)

    start UVD block

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`uvd_v5_0_start.description`:

Description
-----------

Setup and start the UVD block

.. _`uvd_v5_0_stop`:

uvd_v5_0_stop
=============

.. c:function:: void uvd_v5_0_stop(struct amdgpu_device *adev)

    stop UVD block

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`uvd_v5_0_stop.description`:

Description
-----------

stop the UVD block

.. _`uvd_v5_0_ring_emit_fence`:

uvd_v5_0_ring_emit_fence
========================

.. c:function:: void uvd_v5_0_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an fence & trap command

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

    :param addr:
        *undescribed*
    :type addr: u64

    :param seq:
        *undescribed*
    :type seq: u64

    :param flags:
        *undescribed*
    :type flags: unsigned

.. _`uvd_v5_0_ring_emit_fence.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`uvd_v5_0_ring_test_ring`:

uvd_v5_0_ring_test_ring
=======================

.. c:function:: int uvd_v5_0_ring_test_ring(struct amdgpu_ring *ring)

    register write test

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v5_0_ring_test_ring.description`:

Description
-----------

Test if we can successfully write to the context register

.. _`uvd_v5_0_ring_emit_ib`:

uvd_v5_0_ring_emit_ib
=====================

.. c:function:: void uvd_v5_0_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    execute indirect buffer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

    :param ib:
        indirect buffer to execute
    :type ib: struct amdgpu_ib \*

    :param vmid:
        *undescribed*
    :type vmid: unsigned

    :param ctx_switch:
        *undescribed*
    :type ctx_switch: bool

.. _`uvd_v5_0_ring_emit_ib.description`:

Description
-----------

Write ring commands to execute the indirect buffer

.. This file was automatic generated / don't edit.

