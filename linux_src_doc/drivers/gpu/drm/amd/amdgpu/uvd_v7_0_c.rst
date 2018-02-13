.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/uvd_v7_0.c

.. _`uvd_v7_0_ring_get_rptr`:

uvd_v7_0_ring_get_rptr
======================

.. c:function:: uint64_t uvd_v7_0_ring_get_rptr(struct amdgpu_ring *ring)

    get read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_ring_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer

.. _`uvd_v7_0_enc_ring_get_rptr`:

uvd_v7_0_enc_ring_get_rptr
==========================

.. c:function:: uint64_t uvd_v7_0_enc_ring_get_rptr(struct amdgpu_ring *ring)

    get enc read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_enc_ring_get_rptr.description`:

Description
-----------

Returns the current hardware enc read pointer

.. _`uvd_v7_0_ring_get_wptr`:

uvd_v7_0_ring_get_wptr
======================

.. c:function:: uint64_t uvd_v7_0_ring_get_wptr(struct amdgpu_ring *ring)

    get write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_ring_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer

.. _`uvd_v7_0_enc_ring_get_wptr`:

uvd_v7_0_enc_ring_get_wptr
==========================

.. c:function:: uint64_t uvd_v7_0_enc_ring_get_wptr(struct amdgpu_ring *ring)

    get enc write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_enc_ring_get_wptr.description`:

Description
-----------

Returns the current hardware enc write pointer

.. _`uvd_v7_0_ring_set_wptr`:

uvd_v7_0_ring_set_wptr
======================

.. c:function:: void uvd_v7_0_ring_set_wptr(struct amdgpu_ring *ring)

    set write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_ring_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware

.. _`uvd_v7_0_enc_ring_set_wptr`:

uvd_v7_0_enc_ring_set_wptr
==========================

.. c:function:: void uvd_v7_0_enc_ring_set_wptr(struct amdgpu_ring *ring)

    set enc write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_enc_ring_set_wptr.description`:

Description
-----------

Commits the enc write pointer to the hardware

.. _`uvd_v7_0_enc_ring_test_ring`:

uvd_v7_0_enc_ring_test_ring
===========================

.. c:function:: int uvd_v7_0_enc_ring_test_ring(struct amdgpu_ring *ring)

    test if UVD ENC ring is working

    :param struct amdgpu_ring \*ring:
        the engine to test on

.. _`uvd_v7_0_enc_get_create_msg`:

uvd_v7_0_enc_get_create_msg
===========================

.. c:function:: int uvd_v7_0_enc_get_create_msg(struct amdgpu_ring *ring, uint32_t handle, struct dma_fence **fence)

    generate a UVD ENC create msg

    :param struct amdgpu_ring \*ring:
        ring we should submit the msg to

    :param uint32_t handle:
        session handle to use

    :param struct dma_fence \*\*fence:
        optional fence to return

.. _`uvd_v7_0_enc_get_create_msg.description`:

Description
-----------

Open up a stream for HW test

.. _`uvd_v7_0_enc_get_destroy_msg`:

uvd_v7_0_enc_get_destroy_msg
============================

.. c:function:: int uvd_v7_0_enc_get_destroy_msg(struct amdgpu_ring *ring, uint32_t handle, bool direct, struct dma_fence **fence)

    generate a UVD ENC destroy msg

    :param struct amdgpu_ring \*ring:
        ring we should submit the msg to

    :param uint32_t handle:
        session handle to use

    :param bool direct:
        *undescribed*

    :param struct dma_fence \*\*fence:
        optional fence to return

.. _`uvd_v7_0_enc_get_destroy_msg.description`:

Description
-----------

Close up a stream for HW test or if userspace failed to do so

.. _`uvd_v7_0_enc_ring_test_ib`:

uvd_v7_0_enc_ring_test_ib
=========================

.. c:function:: int uvd_v7_0_enc_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test if UVD ENC IBs are working

    :param struct amdgpu_ring \*ring:
        the engine to test on

    :param long timeout:
        *undescribed*

.. _`uvd_v7_0_hw_init`:

uvd_v7_0_hw_init
================

.. c:function:: int uvd_v7_0_hw_init(void *handle)

    start and test UVD block

    :param void \*handle:
        *undescribed*

.. _`uvd_v7_0_hw_init.description`:

Description
-----------

Initialize the hardware, boot up the VCPU and do some testing

.. _`uvd_v7_0_hw_fini`:

uvd_v7_0_hw_fini
================

.. c:function:: int uvd_v7_0_hw_fini(void *handle)

    stop the hardware block

    :param void \*handle:
        *undescribed*

.. _`uvd_v7_0_hw_fini.description`:

Description
-----------

Stop the UVD block, mark ring as not ready any more

.. _`uvd_v7_0_mc_resume`:

uvd_v7_0_mc_resume
==================

.. c:function:: void uvd_v7_0_mc_resume(struct amdgpu_device *adev)

    memory controller programming

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`uvd_v7_0_mc_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets

.. _`uvd_v7_0_start`:

uvd_v7_0_start
==============

.. c:function:: int uvd_v7_0_start(struct amdgpu_device *adev)

    start UVD block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`uvd_v7_0_start.description`:

Description
-----------

Setup and start the UVD block

.. _`uvd_v7_0_stop`:

uvd_v7_0_stop
=============

.. c:function:: void uvd_v7_0_stop(struct amdgpu_device *adev)

    stop UVD block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`uvd_v7_0_stop.description`:

Description
-----------

stop the UVD block

.. _`uvd_v7_0_ring_emit_fence`:

uvd_v7_0_ring_emit_fence
========================

.. c:function:: void uvd_v7_0_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an fence & trap command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`uvd_v7_0_ring_emit_fence.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`uvd_v7_0_enc_ring_emit_fence`:

uvd_v7_0_enc_ring_emit_fence
============================

.. c:function:: void uvd_v7_0_enc_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an enc fence & trap command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`uvd_v7_0_enc_ring_emit_fence.description`:

Description
-----------

Write enc a fence and a trap command to the ring.

.. _`uvd_v7_0_ring_emit_hdp_flush`:

uvd_v7_0_ring_emit_hdp_flush
============================

.. c:function:: void uvd_v7_0_ring_emit_hdp_flush(struct amdgpu_ring *ring)

    emit an hdp flush

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_ring_emit_hdp_flush.description`:

Description
-----------

Emits an hdp flush.

.. _`uvd_v7_0_ring_emit_hdp_invalidate`:

uvd_v7_0_ring_emit_hdp_invalidate
=================================

.. c:function:: void uvd_v7_0_ring_emit_hdp_invalidate(struct amdgpu_ring *ring)

    emit an hdp invalidate

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_ring_emit_hdp_invalidate.description`:

Description
-----------

Emits an hdp invalidate.

.. _`uvd_v7_0_ring_test_ring`:

uvd_v7_0_ring_test_ring
=======================

.. c:function:: int uvd_v7_0_ring_test_ring(struct amdgpu_ring *ring)

    register write test

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`uvd_v7_0_ring_test_ring.description`:

Description
-----------

Test if we can successfully write to the context register

.. _`uvd_v7_0_ring_emit_ib`:

uvd_v7_0_ring_emit_ib
=====================

.. c:function:: void uvd_v7_0_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    execute indirect buffer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param struct amdgpu_ib \*ib:
        indirect buffer to execute

    :param unsigned vmid:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`uvd_v7_0_ring_emit_ib.description`:

Description
-----------

Write ring commands to execute the indirect buffer

.. _`uvd_v7_0_enc_ring_emit_ib`:

uvd_v7_0_enc_ring_emit_ib
=========================

.. c:function:: void uvd_v7_0_enc_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned int vmid, bool ctx_switch)

    enc execute indirect buffer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param struct amdgpu_ib \*ib:
        indirect buffer to execute

    :param unsigned int vmid:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`uvd_v7_0_enc_ring_emit_ib.description`:

Description
-----------

Write enc ring commands to execute the indirect buffer

.. This file was automatic generated / don't edit.

