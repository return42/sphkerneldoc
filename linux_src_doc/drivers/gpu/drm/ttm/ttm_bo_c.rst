.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/ttm/ttm_bo.c

.. _`ttm_bo_cleanup_memtype_use`:

ttm_bo_cleanup_memtype_use
==========================

.. c:function:: void ttm_bo_cleanup_memtype_use(struct ttm_buffer_object *bo)

    :reserved. Will release GPU memory type usage on destruction. This is the place to put in driver specific hooks to release driver private resources. Will release the bo::reserved lock.

    :param struct ttm_buffer_object \*bo:
        *undescribed*

.. _`ttm_bo_cleanup_refs`:

ttm_bo_cleanup_refs
===================

.. c:function:: int ttm_bo_cleanup_refs(struct ttm_buffer_object *bo, bool interruptible, bool no_wait_gpu, bool unlock_resv)

    If bo idle, remove from delayed- and lru lists, and unref. If not idle, do nothing.

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param bool interruptible:
        *undescribed*

    :param bool no_wait_gpu:
        *undescribed*

    :param bool unlock_resv:
        *undescribed*

.. _`ttm_bo_cleanup_refs.description`:

Description
-----------

Must be called with lru_lock and reservation held, this function
will drop the lru lock and optionally the reservation lock before returning.

\ ``interruptible``\          Any sleeps should occur interruptibly.
\ ``no_wait_gpu``\            Never wait for gpu. Return -EBUSY instead.
\ ``unlock_resv``\            Unlock the reservation lock as well.

.. _`ttm_bo_delayed_delete`:

ttm_bo_delayed_delete
=====================

.. c:function:: bool ttm_bo_delayed_delete(struct ttm_bo_device *bdev, bool remove_all)

    encountered buffers.

    :param struct ttm_bo_device \*bdev:
        *undescribed*

    :param bool remove_all:
        *undescribed*

.. _`ttm_bo_evict_swapout_allowable`:

ttm_bo_evict_swapout_allowable
==============================

.. c:function:: bool ttm_bo_evict_swapout_allowable(struct ttm_buffer_object *bo, struct ttm_operation_ctx *ctx, bool *locked)

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

    :param bool \*locked:
        *undescribed*

.. _`ttm_bo_evict_swapout_allowable.description`:

Description
-----------

a. if share same reservation object with ctx->resv, have assumption
reservation objects should already be locked, so not lock again and
return true directly when either the opreation allow_reserved_eviction
or the target bo already is in delayed free list;

b. Otherwise, trylock it.

.. _`ttm_bo_add_move_fence`:

ttm_bo_add_move_fence
=====================

.. c:function:: int ttm_bo_add_move_fence(struct ttm_buffer_object *bo, struct ttm_mem_type_manager *man, struct ttm_mem_reg *mem)

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param struct ttm_mem_type_manager \*man:
        *undescribed*

    :param struct ttm_mem_reg \*mem:
        *undescribed*

.. _`ttm_bo_mem_force_space`:

ttm_bo_mem_force_space
======================

.. c:function:: int ttm_bo_mem_force_space(struct ttm_buffer_object *bo, uint32_t mem_type, const struct ttm_place *place, struct ttm_mem_reg *mem, struct ttm_operation_ctx *ctx)

    space, or we've evicted everything and there isn't enough space.

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param uint32_t mem_type:
        *undescribed*

    :param const struct ttm_place \*place:
        *undescribed*

    :param struct ttm_mem_reg \*mem:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

.. _`ttm_bo_mem_space`:

ttm_bo_mem_space
================

.. c:function:: int ttm_bo_mem_space(struct ttm_buffer_object *bo, struct ttm_placement *placement, struct ttm_mem_reg *mem, struct ttm_operation_ctx *ctx)

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param struct ttm_placement \*placement:
        *undescribed*

    :param struct ttm_mem_reg \*mem:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

.. _`ttm_bo_mem_space.description`:

Description
-----------

This function first searches for free space in compatible memory types in
the priority order defined by the driver.  If free space isn't found, then
ttm_bo_mem_force_space is attempted in priority order to evict and find
space.

.. _`ttm_bo_swapout`:

ttm_bo_swapout
==============

.. c:function:: int ttm_bo_swapout(struct ttm_bo_global *glob, struct ttm_operation_ctx *ctx)

    buffer object on the bo_global::swap_lru list.

    :param struct ttm_bo_global \*glob:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

.. _`ttm_bo_wait_unreserved`:

ttm_bo_wait_unreserved
======================

.. c:function:: int ttm_bo_wait_unreserved(struct ttm_buffer_object *bo)

    interruptible wait for a buffer object to become unreserved

    :param struct ttm_buffer_object \*bo:
        Pointer to buffer

.. This file was automatic generated / don't edit.

