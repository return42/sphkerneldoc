.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_fence.c

.. _`amdkfd_fence_enable_signaling`:

amdkfd_fence_enable_signaling
=============================

.. c:function:: bool amdkfd_fence_enable_signaling(struct dma_fence *f)

    This gets called when TTM wants to evict a KFD BO and schedules a job to move the BO. If fence is already signaled return true. If fence is not signaled schedule a evict KFD process work item.

    :param struct dma_fence \*f:
        *undescribed*

.. _`amdkfd_fence_release`:

amdkfd_fence_release
====================

.. c:function:: void amdkfd_fence_release(struct dma_fence *f)

    callback that fence can be freed

    :param struct dma_fence \*f:
        *undescribed*

.. _`amdkfd_fence_release.description`:

Description
-----------

This function is called when the reference count becomes zero.
Drops the mm_struct reference and RCU schedules freeing up the fence.

.. _`amdkfd_fence_check_mm`:

amdkfd_fence_check_mm
=====================

.. c:function:: bool amdkfd_fence_check_mm(struct dma_fence *f, struct mm_struct *mm)

    Check if \ ``mm``\  is same as that of the fence \ ``f``\  if same return TRUE else return FALSE.

    :param struct dma_fence \*f:
        [IN] fence

    :param struct mm_struct \*mm:
        [IN] mm that needs to be verified

.. This file was automatic generated / don't edit.

