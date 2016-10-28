.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_object.h

.. _`amdgpu_mem_type_to_domain`:

amdgpu_mem_type_to_domain
=========================

.. c:function:: unsigned amdgpu_mem_type_to_domain(u32 mem_type)

    return domain corresponding to mem_type

    :param u32 mem_type:
        ttm memory type

.. _`amdgpu_mem_type_to_domain.description`:

Description
-----------

Returns corresponding domain of the ttm mem_type

.. _`amdgpu_bo_reserve`:

amdgpu_bo_reserve
=================

.. c:function:: int amdgpu_bo_reserve(struct amdgpu_bo *bo, bool no_intr)

    reserve bo

    :param struct amdgpu_bo \*bo:
        bo structure

    :param bool no_intr:
        don't return -ERESTARTSYS on pending signal

.. _`amdgpu_bo_reserve.return`:

Return
------

-ERESTARTSYS: A wait for the buffer to become unreserved was interrupted by
a signal. Release all buffer reservations and return to user-space.

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

.. _`amdgpu_bo_mmap_offset`:

amdgpu_bo_mmap_offset
=====================

.. c:function:: u64 amdgpu_bo_mmap_offset(struct amdgpu_bo *bo)

    return mmap offset of bo

    :param struct amdgpu_bo \*bo:
        amdgpu object for which we query the offset

.. _`amdgpu_bo_mmap_offset.description`:

Description
-----------

Returns mmap offset of the object.

.. This file was automatic generated / don't edit.

