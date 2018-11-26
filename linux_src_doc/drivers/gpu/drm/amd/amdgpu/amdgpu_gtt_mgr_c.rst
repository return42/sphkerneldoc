.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gtt_mgr.c

.. _`amdgpu_gtt_mgr_init`:

amdgpu_gtt_mgr_init
===================

.. c:function:: int amdgpu_gtt_mgr_init(struct ttm_mem_type_manager *man, unsigned long p_size)

    init GTT manager and DRM MM

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param p_size:
        maximum size of GTT
    :type p_size: unsigned long

.. _`amdgpu_gtt_mgr_init.description`:

Description
-----------

Allocate and initialize the GTT manager.

.. _`amdgpu_gtt_mgr_fini`:

amdgpu_gtt_mgr_fini
===================

.. c:function:: int amdgpu_gtt_mgr_fini(struct ttm_mem_type_manager *man)

    free and destroy GTT manager

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

.. _`amdgpu_gtt_mgr_fini.description`:

Description
-----------

Destroy and free the GTT manager, returns -EBUSY if ranges are still
allocated inside it.

.. _`amdgpu_gtt_mgr_has_gart_addr`:

amdgpu_gtt_mgr_has_gart_addr
============================

.. c:function:: bool amdgpu_gtt_mgr_has_gart_addr(struct ttm_mem_reg *mem)

    Check if mem has address space

    :param mem:
        the mem object to check
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_gtt_mgr_has_gart_addr.description`:

Description
-----------

Check if a mem object has already address space allocated.

.. _`amdgpu_gtt_mgr_alloc`:

amdgpu_gtt_mgr_alloc
====================

.. c:function:: int amdgpu_gtt_mgr_alloc(struct ttm_mem_type_manager *man, struct ttm_buffer_object *tbo, const struct ttm_place *place, struct ttm_mem_reg *mem)

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

.. _`amdgpu_gtt_mgr_alloc.description`:

Description
-----------

Allocate the address space for a node.

.. _`amdgpu_gtt_mgr_new`:

amdgpu_gtt_mgr_new
==================

.. c:function:: int amdgpu_gtt_mgr_new(struct ttm_mem_type_manager *man, struct ttm_buffer_object *tbo, const struct ttm_place *place, struct ttm_mem_reg *mem)

    allocate a new node

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

.. _`amdgpu_gtt_mgr_new.description`:

Description
-----------

Dummy, allocate the node but no space for it yet.

.. _`amdgpu_gtt_mgr_del`:

amdgpu_gtt_mgr_del
==================

.. c:function:: void amdgpu_gtt_mgr_del(struct ttm_mem_type_manager *man, struct ttm_mem_reg *mem)

    free ranges

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param mem:
        TTM memory object
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_gtt_mgr_del.description`:

Description
-----------

Free the allocated GTT again.

.. _`amdgpu_gtt_mgr_usage`:

amdgpu_gtt_mgr_usage
====================

.. c:function:: uint64_t amdgpu_gtt_mgr_usage(struct ttm_mem_type_manager *man)

    return usage of GTT domain

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

.. _`amdgpu_gtt_mgr_usage.description`:

Description
-----------

Return how many bytes are used in the GTT domain

.. _`amdgpu_gtt_mgr_debug`:

amdgpu_gtt_mgr_debug
====================

.. c:function:: void amdgpu_gtt_mgr_debug(struct ttm_mem_type_manager *man, struct drm_printer *printer)

    dump VRAM table

    :param man:
        TTM memory type manager
    :type man: struct ttm_mem_type_manager \*

    :param printer:
        DRM printer to use
    :type printer: struct drm_printer \*

.. _`amdgpu_gtt_mgr_debug.description`:

Description
-----------

Dump the table content using printk.

.. This file was automatic generated / don't edit.

