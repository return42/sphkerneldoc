.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_object.h

.. _`radeon_mem_type_to_domain`:

radeon_mem_type_to_domain
=========================

.. c:function:: unsigned radeon_mem_type_to_domain(u32 mem_type)

    return domain corresponding to mem_type

    :param mem_type:
        ttm memory type
    :type mem_type: u32

.. _`radeon_mem_type_to_domain.description`:

Description
-----------

Returns corresponding domain of the ttm mem_type

.. _`radeon_bo_reserve`:

radeon_bo_reserve
=================

.. c:function:: int radeon_bo_reserve(struct radeon_bo *bo, bool no_intr)

    reserve bo

    :param bo:
        bo structure
    :type bo: struct radeon_bo \*

    :param no_intr:
        don't return -ERESTARTSYS on pending signal
    :type no_intr: bool

.. _`radeon_bo_reserve.return`:

Return
------

-ERESTARTSYS: A wait for the buffer to become unreserved was interrupted by
a signal. Release all buffer reservations and return to user-space.

.. _`radeon_bo_gpu_offset`:

radeon_bo_gpu_offset
====================

.. c:function:: u64 radeon_bo_gpu_offset(struct radeon_bo *bo)

    return GPU offset of bo

    :param bo:
        radeon object for which we query the offset
    :type bo: struct radeon_bo \*

.. _`radeon_bo_gpu_offset.description`:

Description
-----------

Returns current GPU offset of the object.

.. _`radeon_bo_gpu_offset.note`:

Note
----

object should either be pinned or reserved when calling this
function, it might be useful to add check for this for debugging.

.. _`radeon_bo_mmap_offset`:

radeon_bo_mmap_offset
=====================

.. c:function:: u64 radeon_bo_mmap_offset(struct radeon_bo *bo)

    return mmap offset of bo

    :param bo:
        radeon object for which we query the offset
    :type bo: struct radeon_bo \*

.. _`radeon_bo_mmap_offset.description`:

Description
-----------

Returns mmap offset of the object.

.. This file was automatic generated / don't edit.

