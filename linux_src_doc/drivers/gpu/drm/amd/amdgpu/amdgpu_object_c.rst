.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_object.c

.. _`amdgpu_bo_create_reserved`:

amdgpu_bo_create_reserved
=========================

.. c:function:: int amdgpu_bo_create_reserved(struct amdgpu_device *adev, unsigned long size, int align, u32 domain, struct amdgpu_bo **bo_ptr, u64 *gpu_addr, void **cpu_addr)

    create reserved BO for kernel use

    :param struct amdgpu_device \*adev:
        amdgpu device object

    :param unsigned long size:
        size for the new BO

    :param int align:
        alignment for the new BO

    :param u32 domain:
        where to place it

    :param struct amdgpu_bo \*\*bo_ptr:
        resulting BO

    :param u64 \*gpu_addr:
        GPU addr of the pinned BO

    :param void \*\*cpu_addr:
        optional CPU address mapping

.. _`amdgpu_bo_create_reserved.description`:

Description
-----------

Allocates and pins a BO for kernel internal use, and returns it still
reserved.

Returns 0 on success, negative error code otherwise.

.. _`amdgpu_bo_create_kernel`:

amdgpu_bo_create_kernel
=======================

.. c:function:: int amdgpu_bo_create_kernel(struct amdgpu_device *adev, unsigned long size, int align, u32 domain, struct amdgpu_bo **bo_ptr, u64 *gpu_addr, void **cpu_addr)

    create BO for kernel use

    :param struct amdgpu_device \*adev:
        amdgpu device object

    :param unsigned long size:
        size for the new BO

    :param int align:
        alignment for the new BO

    :param u32 domain:
        where to place it

    :param struct amdgpu_bo \*\*bo_ptr:
        resulting BO

    :param u64 \*gpu_addr:
        GPU addr of the pinned BO

    :param void \*\*cpu_addr:
        optional CPU address mapping

.. _`amdgpu_bo_create_kernel.description`:

Description
-----------

Allocates and pins a BO for kernel internal use.

Returns 0 on success, negative error code otherwise.

.. _`amdgpu_bo_free_kernel`:

amdgpu_bo_free_kernel
=====================

.. c:function:: void amdgpu_bo_free_kernel(struct amdgpu_bo **bo, u64 *gpu_addr, void **cpu_addr)

    free BO for kernel use

    :param struct amdgpu_bo \*\*bo:
        amdgpu BO to free

    :param u64 \*gpu_addr:
        *undescribed*

    :param void \*\*cpu_addr:
        *undescribed*

.. _`amdgpu_bo_free_kernel.description`:

Description
-----------

unmaps and unpin a BO for kernel internal use.

.. _`amdgpu_bo_fence`:

amdgpu_bo_fence
===============

.. c:function:: void amdgpu_bo_fence(struct amdgpu_bo *bo, struct dma_fence *fence, bool shared)

    add fence to buffer object

    :param struct amdgpu_bo \*bo:
        buffer object in question

    :param struct dma_fence \*fence:
        fence to add

    :param bool shared:
        true if fence should be added shared

.. _`amdgpu_bo_gpu_offset`:

amdgpu_bo_gpu_offset
====================

.. c:function:: u64 amdgpu_bo_gpu_offset(struct amdgpu_bo *bo)

    return GPU offset of bo

    :param struct amdgpu_bo \*bo:
        amdgpu object for which we query the offset

.. _`amdgpu_bo_gpu_offset.description`:

Description
-----------

Returns current GPU offset of the object.

.. _`amdgpu_bo_gpu_offset.note`:

Note
----

object should either be pinned or reserved when calling this
function, it might be useful to add check for this for debugging.

.. This file was automatic generated / don't edit.

