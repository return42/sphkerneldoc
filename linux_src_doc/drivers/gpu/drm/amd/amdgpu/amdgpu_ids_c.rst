.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ids.c

.. _`amdgpu_pasid_alloc`:

amdgpu_pasid_alloc
==================

.. c:function:: int amdgpu_pasid_alloc(unsigned int bits)

    Allocate a PASID

    :param unsigned int bits:
        Maximum width of the PASID in bits, must be at least 1

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

    :param unsigned int pasid:
        PASID to free

.. _`amdgpu_pasid_free_delayed`:

amdgpu_pasid_free_delayed
=========================

.. c:function:: void amdgpu_pasid_free_delayed(struct reservation_object *resv, unsigned int pasid)

    free pasid when fences signal

    :param struct reservation_object \*resv:
        reservation object with the fences to wait for

    :param unsigned int pasid:
        pasid to free

.. _`amdgpu_pasid_free_delayed.description`:

Description
-----------

Free the pasid only after all the fences in resv are signaled.

.. _`amdgpu_vmid_had_gpu_reset`:

amdgpu_vmid_had_gpu_reset
=========================

.. c:function:: bool amdgpu_vmid_had_gpu_reset(struct amdgpu_device *adev, struct amdgpu_vmid *id)

    check if reset occured since last use

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vmid \*id:
        VMID structure

.. _`amdgpu_vmid_had_gpu_reset.description`:

Description
-----------

Check if GPU reset occured since last use of the VMID.

.. _`amdgpu_vmid_grab_idle`:

amdgpu_vmid_grab_idle
=====================

.. c:function:: int amdgpu_vmid_grab_idle(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct amdgpu_vmid **idle)

    grab idle VMID

    :param struct amdgpu_vm \*vm:
        vm to allocate id for

    :param struct amdgpu_ring \*ring:
        ring we want to submit job to

    :param struct amdgpu_sync \*sync:
        sync object where we add dependencies

    :param struct amdgpu_vmid \*\*idle:
        resulting idle VMID

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

    :param struct amdgpu_vm \*vm:
        vm to allocate id for

    :param struct amdgpu_ring \*ring:
        ring we want to submit job to

    :param struct amdgpu_sync \*sync:
        sync object where we add dependencies

    :param struct dma_fence \*fence:
        fence protecting ID from reuse

    :param struct amdgpu_job \*job:
        job who wants to use the VMID

    :param struct amdgpu_vmid \*\*id:
        *undescribed*

.. _`amdgpu_vmid_grab_reserved.description`:

Description
-----------

Try to assign a reserved VMID.

.. _`amdgpu_vmid_grab_used`:

amdgpu_vmid_grab_used
=====================

.. c:function:: int amdgpu_vmid_grab_used(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct dma_fence *fence, struct amdgpu_job *job, struct amdgpu_vmid **id)

    try to reuse a VMID

    :param struct amdgpu_vm \*vm:
        vm to allocate id for

    :param struct amdgpu_ring \*ring:
        ring we want to submit job to

    :param struct amdgpu_sync \*sync:
        sync object where we add dependencies

    :param struct dma_fence \*fence:
        fence protecting ID from reuse

    :param struct amdgpu_job \*job:
        job who wants to use the VMID

    :param struct amdgpu_vmid \*\*id:
        resulting VMID

.. _`amdgpu_vmid_grab_used.description`:

Description
-----------

Try to reuse a VMID for this submission.

.. _`amdgpu_vmid_grab`:

amdgpu_vmid_grab
================

.. c:function:: int amdgpu_vmid_grab(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct dma_fence *fence, struct amdgpu_job *job)

    allocate the next free VMID

    :param struct amdgpu_vm \*vm:
        vm to allocate id for

    :param struct amdgpu_ring \*ring:
        ring we want to submit job to

    :param struct amdgpu_sync \*sync:
        sync object where we add dependencies

    :param struct dma_fence \*fence:
        fence protecting ID from reuse

    :param struct amdgpu_job \*job:
        job who wants to use the VMID

.. _`amdgpu_vmid_grab.description`:

Description
-----------

Allocate an id for the vm, adding fences to the sync obj as necessary.

.. _`amdgpu_vmid_reset`:

amdgpu_vmid_reset
=================

.. c:function:: void amdgpu_vmid_reset(struct amdgpu_device *adev, unsigned vmhub, unsigned vmid)

    reset VMID to zero

    :param struct amdgpu_device \*adev:
        amdgpu device structure

    :param unsigned vmhub:
        *undescribed*

    :param unsigned vmid:
        vmid number to use

.. _`amdgpu_vmid_reset.description`:

Description
-----------

Reset saved GDW, GWS and OA to force switch on next flush.

.. _`amdgpu_vmid_reset_all`:

amdgpu_vmid_reset_all
=====================

.. c:function:: void amdgpu_vmid_reset_all(struct amdgpu_device *adev)

    reset VMID to zero

    :param struct amdgpu_device \*adev:
        amdgpu device structure

.. _`amdgpu_vmid_reset_all.description`:

Description
-----------

Reset VMID to force flush on next use

.. _`amdgpu_vmid_mgr_init`:

amdgpu_vmid_mgr_init
====================

.. c:function:: void amdgpu_vmid_mgr_init(struct amdgpu_device *adev)

    init the VMID manager

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vmid_mgr_init.description`:

Description
-----------

Initialize the VM manager structures

.. _`amdgpu_vmid_mgr_fini`:

amdgpu_vmid_mgr_fini
====================

.. c:function:: void amdgpu_vmid_mgr_fini(struct amdgpu_device *adev)

    cleanup VM manager

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vmid_mgr_fini.description`:

Description
-----------

Cleanup the VM manager and free resources.

.. This file was automatic generated / don't edit.

