.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gtt_mgr.c

.. _`amdgpu_gtt_mgr_init`:

amdgpu_gtt_mgr_init
===================

.. c:function:: int amdgpu_gtt_mgr_init(struct ttm_mem_type_manager *man, unsigned long p_size)

    init GTT manager and DRM MM

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param unsigned long p_size:
        maximum size of GTT

.. _`amdgpu_gtt_mgr_init.description`:

Description
-----------

Allocate and initialize the GTT manager.

.. _`amdgpu_gtt_mgr_fini`:

amdgpu_gtt_mgr_fini
===================

.. c:function:: int amdgpu_gtt_mgr_fini(struct ttm_mem_type_manager *man)

    free and destroy GTT manager

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

.. _`amdgpu_gtt_mgr_fini.description`:

Description
-----------

Destroy and free the GTT manager, returns -EBUSY if ranges are still
allocated inside it.

.. _`amdgpu_gtt_mgr_alloc`:

amdgpu_gtt_mgr_alloc
====================

.. c:function:: int amdgpu_gtt_mgr_alloc(struct ttm_mem_type_manager *man, struct ttm_buffer_object *tbo, const struct ttm_place *place, struct ttm_mem_reg *mem)

    allocate new ranges

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param struct ttm_buffer_object \*tbo:
        TTM BO we need this range for

    :param const struct ttm_place \*place:
        placement flags and restrictions

    :param struct ttm_mem_reg \*mem:
        the resulting mem object

.. _`amdgpu_gtt_mgr_alloc.description`:

Description
-----------

Allocate the address space for a node.

.. _`amdgpu_gtt_mgr_new`:

amdgpu_gtt_mgr_new
==================

.. c:function:: int amdgpu_gtt_mgr_new(struct ttm_mem_type_manager *man, struct ttm_buffer_object *tbo, const struct ttm_place *place, struct ttm_mem_reg *mem)

    allocate a new node

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param struct ttm_buffer_object \*tbo:
        TTM BO we need this range for

    :param const struct ttm_place \*place:
        placement flags and restrictions

    :param struct ttm_mem_reg \*mem:
        the resulting mem object

.. _`amdgpu_gtt_mgr_new.description`:

Description
-----------

Dummy, allocate the node but no space for it yet.

.. _`amdgpu_gtt_mgr_del`:

amdgpu_gtt_mgr_del
==================

.. c:function:: void amdgpu_gtt_mgr_del(struct ttm_mem_type_manager *man, struct ttm_mem_reg *mem)

    free ranges

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param struct ttm_mem_reg \*mem:
        TTM memory object

.. _`amdgpu_gtt_mgr_del.description`:

Description
-----------

Free the allocated GTT again.

.. _`amdgpu_gtt_mgr_debug`:

amdgpu_gtt_mgr_debug
====================

.. c:function:: void amdgpu_gtt_mgr_debug(struct ttm_mem_type_manager *man, const char *prefix)

    dump VRAM table

    :param struct ttm_mem_type_manager \*man:
        TTM memory type manager

    :param const char \*prefix:
        text prefix

.. _`amdgpu_gtt_mgr_debug.description`:

Description
-----------

Dump the table content using printk.

.. This file was automatic generated / don't edit.

