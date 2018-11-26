.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/uvd_v7_0.c

.. _`uvd_v7_0_ring_get_rptr`:

uvd_v7_0_ring_get_rptr
======================

.. c:function:: uint64_t uvd_v7_0_ring_get_rptr(struct amdgpu_ring *ring)

    get read pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_ring_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer

.. _`uvd_v7_0_enc_ring_get_rptr`:

uvd_v7_0_enc_ring_get_rptr
==========================

.. c:function:: uint64_t uvd_v7_0_enc_ring_get_rptr(struct amdgpu_ring *ring)

    get enc read pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_enc_ring_get_rptr.description`:

Description
-----------

Returns the current hardware enc read pointer

.. _`uvd_v7_0_ring_get_wptr`:

uvd_v7_0_ring_get_wptr
======================

.. c:function:: uint64_t uvd_v7_0_ring_get_wptr(struct amdgpu_ring *ring)

    get write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_ring_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer

.. _`uvd_v7_0_enc_ring_get_wptr`:

uvd_v7_0_enc_ring_get_wptr
==========================

.. c:function:: uint64_t uvd_v7_0_enc_ring_get_wptr(struct amdgpu_ring *ring)

    get enc write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_enc_ring_get_wptr.description`:

Description
-----------

Returns the current hardware enc write pointer

.. _`uvd_v7_0_ring_set_wptr`:

uvd_v7_0_ring_set_wptr
======================

.. c:function:: void uvd_v7_0_ring_set_wptr(struct amdgpu_ring *ring)

    set write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_ring_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware

.. _`uvd_v7_0_enc_ring_set_wptr`:

uvd_v7_0_enc_ring_set_wptr
==========================

.. c:function:: void uvd_v7_0_enc_ring_set_wptr(struct amdgpu_ring *ring)

    set enc write pointer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_enc_ring_set_wptr.description`:

Description
-----------

Commits the enc write pointer to the hardware

.. _`uvd_v7_0_enc_ring_test_ring`:

uvd_v7_0_enc_ring_test_ring
===========================

.. c:function:: int uvd_v7_0_enc_ring_test_ring(struct amdgpu_ring *ring)

    test if UVD ENC ring is working

    :param ring:
        the engine to test on
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_enc_get_create_msg`:

uvd_v7_0_enc_get_create_msg
===========================

.. c:function:: int uvd_v7_0_enc_get_create_msg(struct amdgpu_ring *ring, uint32_t handle, struct dma_fence **fence)

    generate a UVD ENC create msg

    :param ring:
        ring we should submit the msg to
    :type ring: struct amdgpu_ring \*

    :param handle:
        session handle to use
    :type handle: uint32_t

    :param fence:
        optional fence to return
    :type fence: struct dma_fence \*\*

.. _`uvd_v7_0_enc_get_create_msg.description`:

Description
-----------

Open up a stream for HW test

.. _`uvd_v7_0_enc_get_destroy_msg`:

uvd_v7_0_enc_get_destroy_msg
============================

.. c:function:: int uvd_v7_0_enc_get_destroy_msg(struct amdgpu_ring *ring, uint32_t handle, struct dma_fence **fence)

    generate a UVD ENC destroy msg

    :param ring:
        ring we should submit the msg to
    :type ring: struct amdgpu_ring \*

    :param handle:
        session handle to use
    :type handle: uint32_t

    :param fence:
        optional fence to return
    :type fence: struct dma_fence \*\*

.. _`uvd_v7_0_enc_get_destroy_msg.description`:

Description
-----------

Close up a stream for HW test or if userspace failed to do so

.. _`uvd_v7_0_enc_ring_test_ib`:

uvd_v7_0_enc_ring_test_ib
=========================

.. c:function:: int uvd_v7_0_enc_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test if UVD ENC IBs are working

    :param ring:
        the engine to test on
    :type ring: struct amdgpu_ring \*

    :param timeout:
        *undescribed*
    :type timeout: long

.. _`uvd_v7_0_hw_init`:

uvd_v7_0_hw_init
================

.. c:function:: int uvd_v7_0_hw_init(void *handle)

    start and test UVD block

    :param handle:
        *undescribed*
    :type handle: void \*

.. _`uvd_v7_0_hw_init.description`:

Description
-----------

Initialize the hardware, boot up the VCPU and do some testing

.. _`uvd_v7_0_hw_fini`:

uvd_v7_0_hw_fini
================

.. c:function:: int uvd_v7_0_hw_fini(void *handle)

    stop the hardware block

    :param handle:
        *undescribed*
    :type handle: void \*

.. _`uvd_v7_0_hw_fini.description`:

Description
-----------

Stop the UVD block, mark ring as not ready any more

.. _`uvd_v7_0_mc_resume`:

uvd_v7_0_mc_resume
==================

.. c:function:: void uvd_v7_0_mc_resume(struct amdgpu_device *adev)

    memory controller programming

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`uvd_v7_0_mc_resume.description`:

Description
-----------

Let the UVD memory controller know it's offsets

.. _`uvd_v7_0_start`:

uvd_v7_0_start
==============

.. c:function:: int uvd_v7_0_start(struct amdgpu_device *adev)

    start UVD block

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`uvd_v7_0_start.description`:

Description
-----------

Setup and start the UVD block

.. _`uvd_v7_0_stop`:

uvd_v7_0_stop
=============

.. c:function:: void uvd_v7_0_stop(struct amdgpu_device *adev)

    stop UVD block

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`uvd_v7_0_stop.description`:

Description
-----------

stop the UVD block

.. _`uvd_v7_0_ring_emit_fence`:

uvd_v7_0_ring_emit_fence
========================

.. c:function:: void uvd_v7_0_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

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

.. _`uvd_v7_0_ring_emit_fence.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`uvd_v7_0_enc_ring_emit_fence`:

uvd_v7_0_enc_ring_emit_fence
============================

.. c:function:: void uvd_v7_0_enc_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an enc fence & trap command

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

.. _`uvd_v7_0_enc_ring_emit_fence.description`:

Description
-----------

Write enc a fence and a trap command to the ring.

.. _`uvd_v7_0_ring_emit_hdp_flush`:

uvd_v7_0_ring_emit_hdp_flush
============================

.. c:function:: void uvd_v7_0_ring_emit_hdp_flush(struct amdgpu_ring *ring)

    skip HDP flushing

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_ring_test_ring`:

uvd_v7_0_ring_test_ring
=======================

.. c:function:: int uvd_v7_0_ring_test_ring(struct amdgpu_ring *ring)

    register write test

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

.. _`uvd_v7_0_ring_test_ring.description`:

Description
-----------

Test if we can successfully write to the context register

.. _`uvd_v7_0_ring_patch_cs_in_place`:

uvd_v7_0_ring_patch_cs_in_place
===============================

.. c:function:: int uvd_v7_0_ring_patch_cs_in_place(struct amdgpu_cs_parser *p, uint32_t ib_idx)

    Patch the IB for command submission.

    :param p:
        the CS parser with the IBs
    :type p: struct amdgpu_cs_parser \*

    :param ib_idx:
        which IB to patch
    :type ib_idx: uint32_t

.. _`uvd_v7_0_ring_emit_ib`:

uvd_v7_0_ring_emit_ib
=====================

.. c:function:: void uvd_v7_0_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

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

.. _`uvd_v7_0_ring_emit_ib.description`:

Description
-----------

Write ring commands to execute the indirect buffer

.. _`uvd_v7_0_enc_ring_emit_ib`:

uvd_v7_0_enc_ring_emit_ib
=========================

.. c:function:: void uvd_v7_0_enc_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned int vmid, bool ctx_switch)

    enc execute indirect buffer

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

    :param ib:
        indirect buffer to execute
    :type ib: struct amdgpu_ib \*

    :param vmid:
        *undescribed*
    :type vmid: unsigned int

    :param ctx_switch:
        *undescribed*
    :type ctx_switch: bool

.. _`uvd_v7_0_enc_ring_emit_ib.description`:

Description
-----------

Write enc ring commands to execute the indirect buffer

.. This file was automatic generated / don't edit.

