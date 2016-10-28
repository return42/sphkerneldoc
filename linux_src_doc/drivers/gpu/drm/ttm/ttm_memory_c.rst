.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/ttm/ttm_memory.c

.. _`ttm_shrink`:

ttm_shrink
==========

.. c:function:: void ttm_shrink(struct ttm_mem_global *glob, bool from_wq, uint64_t extra)

    Extend this if needed, perhaps using a linked list of callbacks.

    :param struct ttm_mem_global \*glob:
        *undescribed*

    :param bool from_wq:
        *undescribed*

    :param uint64_t extra:
        *undescribed*

.. _`ttm_shrink.note-that-this-function-is-reentrant`:

Note that this function is reentrant
------------------------------------

many threads may try to swap out at any given time.

.. This file was automatic generated / don't edit.

