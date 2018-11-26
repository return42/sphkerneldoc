.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ids.c

.. _`amdgpu_pasid_alloc`:

amdgpu_pasid_alloc
==================

.. c:function:: int amdgpu_pasid_alloc(unsigned int bits)

    Allocate a PASID

    :param bits:
        Maximum width of the PASID in bits, must be at least 1
    :type bits: unsigned int

.. _`amdgpu_pasid_alloc.description`:

Description
-----------

Allocates a PASID of the given width while keeping smaller PASIDs
available if possible.

Returns a positive integer on success. Returns \ ``-EINVAL``\  if bits==0.
Returns \ ``-ENOSPC``\  if no PASID was available. Returns \ ``-ENOMEM``\  on
memory allocation failure.

.. _`amdgpu_pasid_free`:

amdgpu_pasid_free
=================

.. c:function:: void amdgpu_pasid_free(unsigned int pasid)

    Free a PASID

    :param pasid:
        PASID to free
    :type pasid: unsigned int

.. _`amdgpu_pasid_free_delayed`:

amdgpu_pasid_free_delayed
=========================

.. c:function:: void amdgpu_pasid_free_delayed(struct reservation_object *resv, unsigned int pasid)

    free pasid when fences signal

    :param resv:
        reservation object with the fences to wait for
    :type resv: struct reservation_object \*

    :param pasid:
        pasid to free
    :type pasid: unsigned int

.. _`amdgpu_pasid_free_delayed.description`:

Description
-----------

Free the pasid only after all the fences in resv are signaled.

.. _`amdgpu_vmid_had_gpu_reset`:

amdgpu_vmid_had_gpu_reset
=========================

.. c:function:: bool amdgpu_vmid_had_gpu_reset(struct amdgpu_device *adev, struct amdgpu_vmid *id)

    check if reset occured since last use

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param id:
        VMID structure
    :type id: struct amdgpu_vmid \*

.. _`amdgpu_vmid_had_gpu_reset.description`:

Description
-----------

Check if GPU reset occured since last use of the VMID.

.. _`amdgpu_vmid_grab_idle`:

amdgpu_vmid_grab_idle
=====================

.. c:function:: int amdgpu_vmid_grab_idle(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct amdgpu_vmid **idle)

    grab idle VMID

    :param vm:
        vm to allocate id for
    :type vm: struct amdgpu_vm \*

    :param ring:
        ring we want to submit job to
    :type ring: struct amdgpu_ring \*

    :param sync:
        sync object where we add dependencies
    :type sync: struct amdgpu_sync \*

    :param idle:
        resulting idle VMID
    :type idle: struct amdgpu_vmid \*\*

.. _`amdgpu_vmid_grab_idle.description`:

Description
-----------

Try to find an idle VMID, if none is idle add a fence to wait to the sync
object. Returns -ENOMEM when we are out of memory.

.. _`amdgpu_vmid_grab_reserved`:

amdgpu_vmid_grab_reserved
=========================

.. c:function:: int amdgpu_vmid_grab_reserved(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct dma_fence *fence, struct amdgpu_job *job, struct amdgpu_vmid **id)

    try to assign reserved VMID

    :param vm:
        vm to allocate id for
    :type vm: struct amdgpu_vm \*

    :param ring:
        ring we want to submit job to
    :type ring: struct amdgpu_ring \*

    :param sync:
        sync object where we add dependencies
    :type sync: struct amdgpu_sync \*

    :param fence:
        fence protecting ID from reuse
    :type fence: struct dma_fence \*

    :param job:
        job who wants to use the VMID
    :type job: struct amdgpu_job \*

    :param id:
        *undescribed*
    :type id: struct amdgpu_vmid \*\*

.. _`amdgpu_vmid_grab_reserved.description`:

Description
-----------

Try to assign a reserved VMID.

.. _`amdgpu_vmid_grab_used`:

amdgpu_vmid_grab_used
=====================

.. c:function:: int amdgpu_vmid_grab_used(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct dma_fence *fence, struct amdgpu_job *job, struct amdgpu_vmid **id)

    try to reuse a VMID

    :param vm:
        vm to allocate id for
    :type vm: struct amdgpu_vm \*

    :param ring:
        ring we want to submit job to
    :type ring: struct amdgpu_ring \*

    :param sync:
        sync object where we add dependencies
    :type sync: struct amdgpu_sync \*

    :param fence:
        fence protecting ID from reuse
    :type fence: struct dma_fence \*

    :param job:
        job who wants to use the VMID
    :type job: struct amdgpu_job \*

    :param id:
        resulting VMID
    :type id: struct amdgpu_vmid \*\*

.. _`amdgpu_vmid_grab_used.description`:

Description
-----------

Try to reuse a VMID for this submission.

.. _`amdgpu_vmid_grab`:

amdgpu_vmid_grab
================

.. c:function:: int amdgpu_vmid_grab(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct dma_fence *fence, struct amdgpu_job *job)

    allocate the next free VMID

    :param vm:
        vm to allocate id for
    :type vm: struct amdgpu_vm \*

    :param ring:
        ring we want to submit job to
    :type ring: struct amdgpu_ring \*

    :param sync:
        sync object where we add dependencies
    :type sync: struct amdgpu_sync \*

    :param fence:
        fence protecting ID from reuse
    :type fence: struct dma_fence \*

    :param job:
        job who wants to use the VMID
    :type job: struct amdgpu_job \*

.. _`amdgpu_vmid_grab.description`:

Description
-----------

Allocate an id for the vm, adding fences to the sync obj as necessary.

.. _`amdgpu_vmid_reset`:

amdgpu_vmid_reset
=================

.. c:function:: void amdgpu_vmid_reset(struct amdgpu_device *adev, unsigned vmhub, unsigned vmid)

    reset VMID to zero

    :param adev:
        amdgpu device structure
    :type adev: struct amdgpu_device \*

    :param vmhub:
        *undescribed*
    :type vmhub: unsigned

    :param vmid:
        vmid number to use
    :type vmid: unsigned

.. _`amdgpu_vmid_reset.description`:

Description
-----------

Reset saved GDW, GWS and OA to force switch on next flush.

.. _`amdgpu_vmid_reset_all`:

amdgpu_vmid_reset_all
=====================

.. c:function:: void amdgpu_vmid_reset_all(struct amdgpu_device *adev)

    reset VMID to zero

    :param adev:
        amdgpu device structure
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vmid_reset_all.description`:

Description
-----------

Reset VMID to force flush on next use

.. _`amdgpu_vmid_mgr_init`:

amdgpu_vmid_mgr_init
====================

.. c:function:: void amdgpu_vmid_mgr_init(struct amdgpu_device *adev)

    init the VMID manager

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vmid_mgr_init.description`:

Description
-----------

Initialize the VM manager structures

.. _`amdgpu_vmid_mgr_fini`:

amdgpu_vmid_mgr_fini
====================

.. c:function:: void amdgpu_vmid_mgr_fini(struct amdgpu_device *adev)

    cleanup VM manager

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vmid_mgr_fini.description`:

Description
-----------

Cleanup the VM manager and free resources.

.. This file was automatic generated / don't edit.

