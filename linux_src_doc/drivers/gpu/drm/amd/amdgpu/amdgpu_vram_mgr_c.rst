.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_vram_mgr.c

.. _`amdgpu_vram_mgr_init`:

amdgpu_vram_mgr_init
====================

.. c:function:: int amdgpu_vram_mgr_init(struct ttm_mem_type_manager *man, unsigned long p_size)

    init VRAM manager and DRM MM

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param p_size:
        maximum size of VRAM
    :type p_size: unsigned long

.. _`amdgpu_vram_mgr_init.description`:

Description
-----------

Allocate and initialize the VRAM manager.

.. _`amdgpu_vram_mgr_fini`:

amdgpu_vram_mgr_fini
====================

.. c:function:: int amdgpu_vram_mgr_fini(struct ttm_mem_type_manager *man)

    free and destroy VRAM manager

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

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

    :param adev:
        amdgpu device structure
    :type adev: struct amdgpu_device \*

    :param node:
        MM node structure
    :type node: struct drm_mm_node \*

.. _`amdgpu_vram_mgr_vis_size.description`:

Description
-----------

Calculate how many bytes of the MM node are inside visible VRAM

.. _`amdgpu_vram_mgr_bo_visible_size`:

amdgpu_vram_mgr_bo_visible_size
===============================

.. c:function:: u64 amdgpu_vram_mgr_bo_visible_size(struct amdgpu_bo *bo)

    CPU visible BO size

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object (must be in VRAM)
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_vram_mgr_bo_visible_size.return`:

Return
------

How much of the given \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object lies in CPU visible VRAM.

.. _`amdgpu_vram_mgr_virt_start`:

amdgpu_vram_mgr_virt_start
==========================

.. c:function:: void amdgpu_vram_mgr_virt_start(struct ttm_mem_reg *mem, struct drm_mm_node *node)

    update virtual start address

    :param mem:
        ttm_mem_reg to update
    :type mem: struct ttm_mem_reg \*

    :param node:
        just allocated node
    :type node: struct drm_mm_node \*

.. _`amdgpu_vram_mgr_virt_start.description`:

Description
-----------

Calculate a virtual BO start address to easily check if everything is CPU
accessible.

.. _`amdgpu_vram_mgr_new`:

amdgpu_vram_mgr_new
===================

.. c:function:: int amdgpu_vram_mgr_new(struct ttm_mem_type_manager *man, struct ttm_buffer_object *tbo, const struct ttm_place *place, struct ttm_mem_reg *mem)

    allocate new ranges

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param tbo:
        TTM BO we need this range for
    :type tbo: struct ttm_buffer_object \*

    :param place:
        placement flags and restrictions
    :type place: const struct ttm_place \*

    :param mem:
        the resulting mem object
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_vram_mgr_new.description`:

Description
-----------

Allocate VRAM for the given BO.

.. _`amdgpu_vram_mgr_del`:

amdgpu_vram_mgr_del
===================

.. c:function:: void amdgpu_vram_mgr_del(struct ttm_mem_type_manager *man, struct ttm_mem_reg *mem)

    free ranges

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param mem:
        TTM memory object
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_vram_mgr_del.description`:

Description
-----------

Free the allocated VRAM again.

.. _`amdgpu_vram_mgr_usage`:

amdgpu_vram_mgr_usage
=====================

.. c:function:: uint64_t amdgpu_vram_mgr_usage(struct ttm_mem_type_manager *man)

    how many bytes are used in this domain

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

.. _`amdgpu_vram_mgr_usage.description`:

Description
-----------

Returns how many bytes are used in this domain.

.. _`amdgpu_vram_mgr_vis_usage`:

amdgpu_vram_mgr_vis_usage
=========================

.. c:function:: uint64_t amdgpu_vram_mgr_vis_usage(struct ttm_mem_type_manager *man)

    how many bytes are used in the visible part

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

.. _`amdgpu_vram_mgr_vis_usage.description`:

Description
-----------

Returns how many bytes are used in the visible part of VRAM

.. _`amdgpu_vram_mgr_debug`:

amdgpu_vram_mgr_debug
=====================

.. c:function:: void amdgpu_vram_mgr_debug(struct ttm_mem_type_manager *man, struct drm_printer *printer)

    dump VRAM table

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param printer:
        DRM printer to use
    :type printer: struct drm_printer \*

.. _`amdgpu_vram_mgr_debug.description`:

Description
-----------

Dump the table content using printk.

.. This file was automatic generated / don't edit.

