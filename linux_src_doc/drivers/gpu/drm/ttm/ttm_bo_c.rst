.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/ttm/ttm_bo.c

.. _`ttm_bo_cleanup_memtype_use`:

ttm_bo_cleanup_memtype_use
==========================

.. c:function:: void ttm_bo_cleanup_memtype_use(struct ttm_buffer_object *bo)

    :reserved. Will release GPU memory type usage on destruction. This is the place to put in driver specific hooks to release driver private resources. Will release the bo::reserved lock.

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

.. _`ttm_bo_cleanup_refs`:

ttm_bo_cleanup_refs
===================

.. c:function:: int ttm_bo_cleanup_refs(struct ttm_buffer_object *bo, bool interruptible, bool no_wait_gpu, bool unlock_resv)

    If bo idle, remove from delayed- and lru lists, and unref. If not idle, do nothing.

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param interruptible:
        *undescribed*
    :type interruptible: bool

    :param no_wait_gpu:
        *undescribed*
    :type no_wait_gpu: bool

    :param unlock_resv:
        *undescribed*
    :type unlock_resv: bool

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

    :param bdev:
        *undescribed*
    :type bdev: struct ttm_bo_device \*

    :param remove_all:
        *undescribed*
    :type remove_all: bool

.. _`ttm_bo_evict_swapout_allowable`:

ttm_bo_evict_swapout_allowable
==============================

.. c:function:: bool ttm_bo_evict_swapout_allowable(struct ttm_buffer_object *bo, struct ttm_operation_ctx *ctx, bool *locked)

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

    :param locked:
        *undescribed*
    :type locked: bool \*

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

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param man:
        *undescribed*
    :type man: struct ttm_mem_type_manager \*

    :param mem:
        *undescribed*
    :type mem: struct ttm_mem_reg \*

.. _`ttm_bo_mem_force_space`:

ttm_bo_mem_force_space
======================

.. c:function:: int ttm_bo_mem_force_space(struct ttm_buffer_object *bo, uint32_t mem_type, const struct ttm_place *place, struct ttm_mem_reg *mem, struct ttm_operation_ctx *ctx)

    space, or we've evicted everything and there isn't enough space.

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param mem_type:
        *undescribed*
    :type mem_type: uint32_t

    :param place:
        *undescribed*
    :type place: const struct ttm_place \*

    :param mem:
        *undescribed*
    :type mem: struct ttm_mem_reg \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`ttm_bo_mem_space`:

ttm_bo_mem_space
================

.. c:function:: int ttm_bo_mem_space(struct ttm_buffer_object *bo, struct ttm_placement *placement, struct ttm_mem_reg *mem, struct ttm_operation_ctx *ctx)

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param placement:
        *undescribed*
    :type placement: struct ttm_placement \*

    :param mem:
        *undescribed*
    :type mem: struct ttm_mem_reg \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

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

    :param glob:
        *undescribed*
    :type glob: struct ttm_bo_global \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`ttm_bo_wait_unreserved`:

ttm_bo_wait_unreserved
======================

.. c:function:: int ttm_bo_wait_unreserved(struct ttm_buffer_object *bo)

    interruptible wait for a buffer object to become unreserved

    :param bo:
        Pointer to buffer
    :type bo: struct ttm_buffer_object \*

.. This file was automatic generated / don't edit.

