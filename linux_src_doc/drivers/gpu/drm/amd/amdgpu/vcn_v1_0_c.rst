.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/vcn_v1_0.c

.. _`vcn_v1_0_early_init`:

vcn_v1_0_early_init
===================

.. c:function:: int vcn_v1_0_early_init(void *handle)

    set function pointers

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_early_init.description`:

Description
-----------

Set ring and irq function pointers

.. _`vcn_v1_0_sw_init`:

vcn_v1_0_sw_init
================

.. c:function:: int vcn_v1_0_sw_init(void *handle)

    sw init for VCN block

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_sw_init.description`:

Description
-----------

Load firmware and sw initialization

.. _`vcn_v1_0_sw_fini`:

vcn_v1_0_sw_fini
================

.. c:function:: int vcn_v1_0_sw_fini(void *handle)

    sw fini for VCN block

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_sw_fini.description`:

Description
-----------

VCN suspend and free up sw allocation

.. _`vcn_v1_0_hw_init`:

vcn_v1_0_hw_init
================

.. c:function:: int vcn_v1_0_hw_init(void *handle)

    start and test VCN block

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_hw_init.description`:

Description
-----------

Initialize the hardware, boot up the VCPU and do some testing

.. _`vcn_v1_0_hw_fini`:

vcn_v1_0_hw_fini
================

.. c:function:: int vcn_v1_0_hw_fini(void *handle)

    stop the hardware block

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_hw_fini.description`:

Description
-----------

Stop the VCN block, mark ring as not ready any more

.. _`vcn_v1_0_suspend`:

vcn_v1_0_suspend
================

.. c:function:: int vcn_v1_0_suspend(void *handle)

    suspend VCN block

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_suspend.description`:

Description
-----------

HW fini and suspend VCN block

.. _`vcn_v1_0_resume`:

vcn_v1_0_resume
===============

.. c:function:: int vcn_v1_0_resume(void *handle)

    resume VCN block

    :param void \*handle:
        amdgpu_device pointer

.. _`vcn_v1_0_resume.description`:

Description
-----------

Resume firmware and hw init VCN block

.. _`vcn_v1_0_mc_resume`:

vcn_v1_0_mc_resume
==================

.. c:function:: void vcn_v1_0_mc_resume(struct amdgpu_device *adev)

    memory controller programming

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`vcn_v1_0_mc_resume.description`:

Description
-----------

Let the VCN memory controller know it's offsets

.. _`vcn_v1_0_disable_clock_gating`:

vcn_v1_0_disable_clock_gating
=============================

.. c:function:: void vcn_v1_0_disable_clock_gating(struct amdgpu_device *adev)

    disable VCN clock gating

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`vcn_v1_0_disable_clock_gating.description`:

Description
-----------

Disable clock gating for VCN block

.. _`vcn_v1_0_enable_clock_gating`:

vcn_v1_0_enable_clock_gating
============================

.. c:function:: void vcn_v1_0_enable_clock_gating(struct amdgpu_device *adev)

    enable VCN clock gating

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`vcn_v1_0_enable_clock_gating.description`:

Description
-----------

Enable clock gating for VCN block

.. _`vcn_v1_0_start`:

vcn_v1_0_start
==============

.. c:function:: int vcn_v1_0_start(struct amdgpu_device *adev)

    start VCN block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`vcn_v1_0_start.description`:

Description
-----------

Setup and start the VCN block

.. _`vcn_v1_0_stop`:

vcn_v1_0_stop
=============

.. c:function:: int vcn_v1_0_stop(struct amdgpu_device *adev)

    stop VCN block

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`vcn_v1_0_stop.description`:

Description
-----------

stop the VCN block

.. _`vcn_v1_0_dec_ring_get_rptr`:

vcn_v1_0_dec_ring_get_rptr
==========================

.. c:function:: uint64_t vcn_v1_0_dec_ring_get_rptr(struct amdgpu_ring *ring)

    get read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`vcn_v1_0_dec_ring_get_rptr.description`:

Description
-----------

Returns the current hardware read pointer

.. _`vcn_v1_0_dec_ring_get_wptr`:

vcn_v1_0_dec_ring_get_wptr
==========================

.. c:function:: uint64_t vcn_v1_0_dec_ring_get_wptr(struct amdgpu_ring *ring)

    get write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`vcn_v1_0_dec_ring_get_wptr.description`:

Description
-----------

Returns the current hardware write pointer

.. _`vcn_v1_0_dec_ring_set_wptr`:

vcn_v1_0_dec_ring_set_wptr
==========================

.. c:function:: void vcn_v1_0_dec_ring_set_wptr(struct amdgpu_ring *ring)

    set write pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`vcn_v1_0_dec_ring_set_wptr.description`:

Description
-----------

Commits the write pointer to the hardware

.. _`vcn_v1_0_dec_ring_insert_start`:

vcn_v1_0_dec_ring_insert_start
==============================

.. c:function:: void vcn_v1_0_dec_ring_insert_start(struct amdgpu_ring *ring)

    insert a start command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`vcn_v1_0_dec_ring_insert_start.description`:

Description
-----------

Write a start command to the ring.

.. _`vcn_v1_0_dec_ring_insert_end`:

vcn_v1_0_dec_ring_insert_end
============================

.. c:function:: void vcn_v1_0_dec_ring_insert_end(struct amdgpu_ring *ring)

    insert a end command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`vcn_v1_0_dec_ring_insert_end.description`:

Description
-----------

Write a end command to the ring.

.. _`vcn_v1_0_dec_ring_emit_fence`:

vcn_v1_0_dec_ring_emit_fence
============================

.. c:function:: void vcn_v1_0_dec_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an fence & trap command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`vcn_v1_0_dec_ring_emit_fence.description`:

Description
-----------

Write a fence and a trap command to the ring.

.. _`vcn_v1_0_dec_ring_emit_ib`:

vcn_v1_0_dec_ring_emit_ib
=========================

.. c:function:: void vcn_v1_0_dec_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    execute indirect buffer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param struct amdgpu_ib \*ib:
        indirect buffer to execute

    :param unsigned vmid:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`vcn_v1_0_dec_ring_emit_ib.description`:

Description
-----------

Write ring commands to execute the indirect buffer

.. _`vcn_v1_0_enc_ring_get_rptr`:

vcn_v1_0_enc_ring_get_rptr
==========================

.. c:function:: uint64_t vcn_v1_0_enc_ring_get_rptr(struct amdgpu_ring *ring)

    get enc read pointer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

.. _`vcn_v1_0_enc_ring_get_rptr.description`:

Description
-----------

Returns the current hardware enc read pointer

.. _`vcn_v1_0_enc_ring_emit_fence`:

vcn_v1_0_enc_ring_emit_fence
============================

.. c:function:: void vcn_v1_0_enc_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    emit an enc fence & trap command

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param u64 addr:
        *undescribed*

    :param u64 seq:
        *undescribed*

    :param unsigned flags:
        *undescribed*

.. _`vcn_v1_0_enc_ring_emit_fence.description`:

Description
-----------

Write enc a fence and a trap command to the ring.

.. _`vcn_v1_0_enc_ring_emit_ib`:

vcn_v1_0_enc_ring_emit_ib
=========================

.. c:function:: void vcn_v1_0_enc_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned int vmid, bool ctx_switch)

    enc execute indirect buffer

    :param struct amdgpu_ring \*ring:
        amdgpu_ring pointer

    :param struct amdgpu_ib \*ib:
        indirect buffer to execute

    :param unsigned int vmid:
        *undescribed*

    :param bool ctx_switch:
        *undescribed*

.. _`vcn_v1_0_enc_ring_emit_ib.description`:

Description
-----------

Write enc ring commands to execute the indirect buffer

.. This file was automatic generated / don't edit.

