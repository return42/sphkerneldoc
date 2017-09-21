.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_vram_mgr.c

.. _`amdgpu_vram_mgr_init`:

amdgpu_vram_mgr_init
====================

.. c:function:: int amdgpu_vram_mgr_init(struct ttm_mem_type_manager *man, unsigned long p_size)

    init VRAM manager and DRM MM

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param unsigned long p_size:
        maximum size of VRAM

.. _`amdgpu_vram_mgr_init.description`:

Description
-----------

Allocate and initialize the VRAM manager.

.. _`amdgpu_vram_mgr_fini`:

amdgpu_vram_mgr_fini
====================

.. c:function:: int amdgpu_vram_mgr_fini(struct ttm_mem_type_manager *man)

    free and destroy VRAM manager

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

.. _`amdgpu_vram_mgr_fini.description`:

Description
-----------

Destroy and free the VRAM manager, returns -EBUSY if ranges are still
allocated inside it.

.. _`amdgpu_vram_mgr_vis_size`:

amdgpu_vram_mgr_vis_size
========================

.. c:function:: u64 amdgpu_vram_mgr_vis_size(struct amdgpu_device *adev, struct drm_mm_node *node)

    Calculate visible node size

    :param struct amdgpu_device \*adev:
        amdgpu device structure

    :param struct drm_mm_node \*node:
        MM node structure

.. _`amdgpu_vram_mgr_vis_size.description`:

Description
-----------

Calculate how many bytes of the MM node are inside visible VRAM

.. _`amdgpu_vram_mgr_new`:

amdgpu_vram_mgr_new
===================

.. c:function:: int amdgpu_vram_mgr_new(struct ttm_mem_type_manager *man, struct ttm_buffer_object *tbo, const struct ttm_place *place, struct ttm_mem_reg *mem)

    allocate new ranges

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param struct ttm_buffer_object \*tbo:
        TTM BO we need this range for

    :param const struct ttm_place \*place:
        placement flags and restrictions

    :param struct ttm_mem_reg \*mem:
        the resulting mem object

.. _`amdgpu_vram_mgr_new.description`:

Description
-----------

Allocate VRAM for the given BO.

.. _`amdgpu_vram_mgr_del`:

amdgpu_vram_mgr_del
===================

.. c:function:: void amdgpu_vram_mgr_del(struct ttm_mem_type_manager *man, struct ttm_mem_reg *mem)

    free ranges

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param struct ttm_mem_reg \*mem:
        TTM memory object

.. _`amdgpu_vram_mgr_del.description`:

Description
-----------

Free the allocated VRAM again.

.. _`amdgpu_vram_mgr_usage`:

amdgpu_vram_mgr_usage
=====================

.. c:function:: uint64_t amdgpu_vram_mgr_usage(struct ttm_mem_type_manager *man)

    how many bytes are used in this domain

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

.. _`amdgpu_vram_mgr_usage.description`:

Description
-----------

Returns how many bytes are used in this domain.

.. _`amdgpu_vram_mgr_vis_usage`:

amdgpu_vram_mgr_vis_usage
=========================

.. c:function:: uint64_t amdgpu_vram_mgr_vis_usage(struct ttm_mem_type_manager *man)

    how many bytes are used in the visible part

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

.. _`amdgpu_vram_mgr_vis_usage.description`:

Description
-----------

Returns how many bytes are used in the visible part of VRAM

.. _`amdgpu_vram_mgr_debug`:

amdgpu_vram_mgr_debug
=====================

.. c:function:: void amdgpu_vram_mgr_debug(struct ttm_mem_type_manager *man, struct drm_printer *printer)

    dump VRAM table

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param struct drm_printer \*printer:
        DRM printer to use

.. _`amdgpu_vram_mgr_debug.description`:

Description
-----------

Dump the table content using printk.

.. This file was automatic generated / don't edit.

