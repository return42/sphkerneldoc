.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_object.h

.. _`amdgpu_mem_type_to_domain`:

amdgpu_mem_type_to_domain
=========================

.. c:function:: unsigned amdgpu_mem_type_to_domain(u32 mem_type)

    return domain corresponding to mem_type

    :param mem_type:
        ttm memory type
    :type mem_type: u32

.. _`amdgpu_mem_type_to_domain.description`:

Description
-----------

Returns corresponding domain of the ttm mem_type

.. _`amdgpu_bo_reserve`:

amdgpu_bo_reserve
=================

.. c:function:: int amdgpu_bo_reserve(struct amdgpu_bo *bo, bool no_intr)

    reserve bo

    :param bo:
        bo structure
    :type bo: struct amdgpu_bo \*

    :param no_intr:
        don't return -ERESTARTSYS on pending signal
    :type no_intr: bool

.. _`amdgpu_bo_reserve.return`:

Return
------

-ERESTARTSYS: A wait for the buffer to become unreserved was interrupted by
a signal. Release all buffer reservations and return to user-space.

.. _`amdgpu_bo_mmap_offset`:

amdgpu_bo_mmap_offset
=====================

.. c:function:: u64 amdgpu_bo_mmap_offset(struct amdgpu_bo *bo)

    return mmap offset of bo

    :param bo:
        amdgpu object for which we query the offset
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_mmap_offset.description`:

Description
-----------

Returns mmap offset of the object.

.. _`amdgpu_bo_in_cpu_visible_vram`:

amdgpu_bo_in_cpu_visible_vram
=============================

.. c:function:: bool amdgpu_bo_in_cpu_visible_vram(struct amdgpu_bo *bo)

    check if BO is (partly) in visible VRAM

    :param bo:
        *undescribed*
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_explicit_sync`:

amdgpu_bo_explicit_sync
=======================

.. c:function:: bool amdgpu_bo_explicit_sync(struct amdgpu_bo *bo)

    return whether the bo is explicitly synced

    :param bo:
        *undescribed*
    :type bo: struct amdgpu_bo \*

.. This file was automatic generated / don't edit.

