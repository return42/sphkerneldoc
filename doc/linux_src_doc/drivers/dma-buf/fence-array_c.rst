.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/fence-array.c

.. _`fence_array_create`:

fence_array_create
==================

.. c:function:: struct fence_array *fence_array_create(int num_fences, struct fence **fences, u64 context, unsigned seqno, bool signal_on_any)

    Create a custom fence array

    :param int num_fences:
        [in]    number of fences to add in the array

    :param struct fence \*\*fences:
        [in]    array containing the fences

    :param u64 context:
        [in]    fence context to use

    :param unsigned seqno:
        [in]    sequence number to use
        \ ``signal_on_any``\        [in]    signal on any fence in the array

    :param bool signal_on_any:
        *undescribed*

.. _`fence_array_create.description`:

Description
-----------

Allocate a fence_array object and initialize the base fence with \ :c:func:`fence_init`\ .
In case of error it returns NULL.

The caller should allocte the fences array with num_fences size
and fill it with the fences it wants to add to the object. Ownership of this
array is take and \ :c:func:`fence_put`\  is used on each fence on release.

If \ ``signal_on_any``\  is true the fence array signals if any fence in the array
signals, otherwise it signals when all fences in the array signal.

.. This file was automatic generated / don't edit.

