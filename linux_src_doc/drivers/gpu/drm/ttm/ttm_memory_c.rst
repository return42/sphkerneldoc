.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/ttm/ttm_memory.c

.. _`ttm_shrink`:

ttm_shrink
==========

.. c:function:: void ttm_shrink(struct ttm_mem_global *glob, bool from_wq, uint64_t extra, struct ttm_operation_ctx *ctx)

    Extend this if needed, perhaps using a linked list of callbacks.

    :param glob:
        *undescribed*
    :type glob: struct ttm_mem_global \*

    :param from_wq:
        *undescribed*
    :type from_wq: bool

    :param extra:
        *undescribed*
    :type extra: uint64_t

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`ttm_shrink.note-that-this-function-is-reentrant`:

Note that this function is reentrant
------------------------------------

many threads may try to swap out at any given time.

.. This file was automatic generated / don't edit.

