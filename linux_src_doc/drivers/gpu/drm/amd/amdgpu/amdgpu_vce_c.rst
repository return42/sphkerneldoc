.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_vce.c

.. _`amdgpu_vce_sw_init`:

amdgpu_vce_sw_init
==================

.. c:function:: int amdgpu_vce_sw_init(struct amdgpu_device *adev, unsigned long size)

    allocate memory, load vce firmware

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param size:
        *undescribed*
    :type size: unsigned long

.. _`amdgpu_vce_sw_init.description`:

Description
-----------

First step to get VCE online, allocate memory and load the firmware

.. _`amdgpu_vce_sw_fini`:

amdgpu_vce_sw_fini
==================

.. c:function:: int amdgpu_vce_sw_fini(struct amdgpu_device *adev)

    free memory

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vce_sw_fini.description`:

Description
-----------

Last step on VCE teardown, free firmware memory

.. _`amdgpu_vce_entity_init`:

amdgpu_vce_entity_init
======================

.. c:function:: int amdgpu_vce_entity_init(struct amdgpu_device *adev)

    init entity

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vce_suspend`:

amdgpu_vce_suspend
==================

.. c:function:: int amdgpu_vce_suspend(struct amdgpu_device *adev)

    unpin VCE fw memory

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vce_resume`:

amdgpu_vce_resume
=================

.. c:function:: int amdgpu_vce_resume(struct amdgpu_device *adev)

    pin VCE fw memory

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vce_idle_work_handler`:

amdgpu_vce_idle_work_handler
============================

.. c:function:: void amdgpu_vce_idle_work_handler(struct work_struct *work)

    power off VCE

    :param work:
        pointer to work structure
    :type work: struct work_struct \*

.. _`amdgpu_vce_idle_work_handler.description`:

Description
-----------

power of VCE when it's not used any more

.. _`amdgpu_vce_ring_begin_use`:

amdgpu_vce_ring_begin_use
=========================

.. c:function:: void amdgpu_vce_ring_begin_use(struct amdgpu_ring *ring)

    power up VCE

    :param ring:
        amdgpu ring
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_vce_ring_begin_use.description`:

Description
-----------

Make sure VCE is powerd up when we want to use it

.. _`amdgpu_vce_ring_end_use`:

amdgpu_vce_ring_end_use
=======================

.. c:function:: void amdgpu_vce_ring_end_use(struct amdgpu_ring *ring)

    power VCE down

    :param ring:
        amdgpu ring
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_vce_ring_end_use.description`:

Description
-----------

Schedule work to power VCE down again

.. _`amdgpu_vce_free_handles`:

amdgpu_vce_free_handles
=======================

.. c:function:: void amdgpu_vce_free_handles(struct amdgpu_device *adev, struct drm_file *filp)

    free still open VCE handles

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param filp:
        drm file pointer
    :type filp: struct drm_file \*

.. _`amdgpu_vce_free_handles.description`:

Description
-----------

Close all VCE handles still open by this file pointer

.. _`amdgpu_vce_get_create_msg`:

amdgpu_vce_get_create_msg
=========================

.. c:function:: int amdgpu_vce_get_create_msg(struct amdgpu_ring *ring, uint32_t handle, struct dma_fence **fence)

    generate a VCE create msg

    :param ring:
        ring we should submit the msg to
    :type ring: struct amdgpu_ring \*

    :param handle:
        VCE session handle to use
    :type handle: uint32_t

    :param fence:
        optional fence to return
    :type fence: struct dma_fence \*\*

.. _`amdgpu_vce_get_create_msg.description`:

Description
-----------

Open up a stream for HW test

.. _`amdgpu_vce_get_destroy_msg`:

amdgpu_vce_get_destroy_msg
==========================

.. c:function:: int amdgpu_vce_get_destroy_msg(struct amdgpu_ring *ring, uint32_t handle, bool direct, struct dma_fence **fence)

    generate a VCE destroy msg

    :param ring:
        ring we should submit the msg to
    :type ring: struct amdgpu_ring \*

    :param handle:
        VCE session handle to use
    :type handle: uint32_t

    :param direct:
        *undescribed*
    :type direct: bool

    :param fence:
        optional fence to return
    :type fence: struct dma_fence \*\*

.. _`amdgpu_vce_get_destroy_msg.description`:

Description
-----------

Close up a stream for HW test or if userspace failed to do so

.. _`amdgpu_vce_validate_bo`:

amdgpu_vce_validate_bo
======================

.. c:function:: int amdgpu_vce_validate_bo(struct amdgpu_cs_parser *p, uint32_t ib_idx, int lo, int hi, unsigned size, int32_t index)

    make sure not to cross 4GB boundary

    :param p:
        parser context
    :type p: struct amdgpu_cs_parser \*

    :param ib_idx:
        *undescribed*
    :type ib_idx: uint32_t

    :param lo:
        address of lower dword
    :type lo: int

    :param hi:
        address of higher dword
    :type hi: int

    :param size:
        minimum size
    :type size: unsigned

    :param index:
        bs/fb index
    :type index: int32_t

.. _`amdgpu_vce_validate_bo.description`:

Description
-----------

Make sure that no BO cross a 4GB boundary.

.. _`amdgpu_vce_cs_reloc`:

amdgpu_vce_cs_reloc
===================

.. c:function:: int amdgpu_vce_cs_reloc(struct amdgpu_cs_parser *p, uint32_t ib_idx, int lo, int hi, unsigned size, uint32_t index)

    command submission relocation

    :param p:
        parser context
    :type p: struct amdgpu_cs_parser \*

    :param ib_idx:
        *undescribed*
    :type ib_idx: uint32_t

    :param lo:
        address of lower dword
    :type lo: int

    :param hi:
        address of higher dword
    :type hi: int

    :param size:
        minimum size
    :type size: unsigned

    :param index:
        *undescribed*
    :type index: uint32_t

.. _`amdgpu_vce_cs_reloc.description`:

Description
-----------

Patch relocation inside command stream with real buffer address

.. _`amdgpu_vce_validate_handle`:

amdgpu_vce_validate_handle
==========================

.. c:function:: int amdgpu_vce_validate_handle(struct amdgpu_cs_parser *p, uint32_t handle, uint32_t *allocated)

    validate stream handle

    :param p:
        parser context
    :type p: struct amdgpu_cs_parser \*

    :param handle:
        handle to validate
    :type handle: uint32_t

    :param allocated:
        allocated a new handle?
    :type allocated: uint32_t \*

.. _`amdgpu_vce_validate_handle.description`:

Description
-----------

Validates the handle and return the found session index or -EINVAL
we we don't have another free session index.

.. _`amdgpu_vce_ring_parse_cs`:

amdgpu_vce_ring_parse_cs
========================

.. c:function:: int amdgpu_vce_ring_parse_cs(struct amdgpu_cs_parser *p, uint32_t ib_idx)

    parse and validate the command stream

    :param p:
        parser context
    :type p: struct amdgpu_cs_parser \*

    :param ib_idx:
        *undescribed*
    :type ib_idx: uint32_t

.. _`amdgpu_vce_ring_parse_cs_vm`:

amdgpu_vce_ring_parse_cs_vm
===========================

.. c:function:: int amdgpu_vce_ring_parse_cs_vm(struct amdgpu_cs_parser *p, uint32_t ib_idx)

    parse the command stream in VM mode

    :param p:
        parser context
    :type p: struct amdgpu_cs_parser \*

    :param ib_idx:
        *undescribed*
    :type ib_idx: uint32_t

.. _`amdgpu_vce_ring_emit_ib`:

amdgpu_vce_ring_emit_ib
=======================

.. c:function:: void amdgpu_vce_ring_emit_ib(struct amdgpu_ring *ring, struct amdgpu_ib *ib, unsigned vmid, bool ctx_switch)

    execute indirect buffer

    :param ring:
        engine to use
    :type ring: struct amdgpu_ring \*

    :param ib:
        the IB to execute
    :type ib: struct amdgpu_ib \*

    :param vmid:
        *undescribed*
    :type vmid: unsigned

    :param ctx_switch:
        *undescribed*
    :type ctx_switch: bool

.. _`amdgpu_vce_ring_emit_fence`:

amdgpu_vce_ring_emit_fence
==========================

.. c:function:: void amdgpu_vce_ring_emit_fence(struct amdgpu_ring *ring, u64 addr, u64 seq, unsigned flags)

    add a fence command to the ring

    :param ring:
        engine to use
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

.. _`amdgpu_vce_ring_test_ring`:

amdgpu_vce_ring_test_ring
=========================

.. c:function:: int amdgpu_vce_ring_test_ring(struct amdgpu_ring *ring)

    test if VCE ring is working

    :param ring:
        the engine to test on
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_vce_ring_test_ib`:

amdgpu_vce_ring_test_ib
=======================

.. c:function:: int amdgpu_vce_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test if VCE IBs are working

    :param ring:
        the engine to test on
    :type ring: struct amdgpu_ring \*

    :param timeout:
        *undescribed*
    :type timeout: long

.. This file was automatic generated / don't edit.

