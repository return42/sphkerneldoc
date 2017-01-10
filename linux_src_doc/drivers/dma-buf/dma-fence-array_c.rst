.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/dma-fence-array.c

.. _`dma_fence_array_create`:

dma_fence_array_create
======================

.. c:function:: struct dma_fence_array *dma_fence_array_create(int num_fences, struct dma_fence **fences, u64 context, unsigned seqno, bool signal_on_any)

    Create a custom fence array

    :param int num_fences:
        [in]    number of fences to add in the array

    :param struct dma_fence \*\*fences:
        [in]    array containing the fences

    :param u64 context:
        [in]    fence context to use

    :param unsigned seqno:
        [in]    sequence number to use

    :param bool signal_on_any:
        [in]    signal on any fence in the array

.. _`dma_fence_array_create.description`:

Description
-----------

Allocate a dma_fence_array object and initialize the base fence with
\ :c:func:`dma_fence_init`\ .
In case of error it returns NULL.

The caller should allocate the fences array with num_fences size
and fill it with the fences it wants to add to the object. Ownership of this
array is taken and \ :c:func:`dma_fence_put`\  is used on each fence on release.

If \ ``signal_on_any``\  is true the fence array signals if any fence in the array
signals, otherwise it signals when all fences in the array signal.

.. This file was automatic generated / don't edit.

