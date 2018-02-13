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
        *undescribed*

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

