.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ttm.c

.. _`amdgpu_find_mm_node`:

amdgpu_find_mm_node
===================

.. c:function:: struct drm_mm_node *amdgpu_find_mm_node(struct ttm_mem_reg *mem, unsigned long *offset)

    Helper function finds the drm_mm_node corresponding to \ ``offset``\ . It also modifies the offset to be within the drm_mm_node returned

    :param struct ttm_mem_reg \*mem:
        *undescribed*

    :param unsigned long \*offset:
        *undescribed*

.. _`amdgpu_ttm_copy_mem_to_mem`:

amdgpu_ttm_copy_mem_to_mem
==========================

.. c:function:: int amdgpu_ttm_copy_mem_to_mem(struct amdgpu_device *adev, struct amdgpu_copy_mem *src, struct amdgpu_copy_mem *dst, uint64_t size, struct reservation_object *resv, struct dma_fence **f)

    Helper function for copy

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct amdgpu_copy_mem \*src:
        *undescribed*

    :param struct amdgpu_copy_mem \*dst:
        *undescribed*

    :param uint64_t size:
        *undescribed*

    :param struct reservation_object \*resv:
        *undescribed*

    :param struct dma_fence \*\*f:
        Returns the last fence if multiple jobs are submitted.

.. _`amdgpu_ttm_copy_mem_to_mem.description`:

Description
-----------

The function copies \ ``size``\  bytes from {src->mem + src->offset} to
{dst->mem + dst->offset}. src->bo and dst->bo could be same BO for a
move and different for a BO to BO copy.

.. This file was automatic generated / don't edit.

