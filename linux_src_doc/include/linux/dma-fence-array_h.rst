.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-fence-array.h

.. _`dma_fence_array_cb`:

struct dma_fence_array_cb
=========================

.. c:type:: struct dma_fence_array_cb

    callback helper for fence array

.. _`dma_fence_array_cb.definition`:

Definition
----------

.. code-block:: c

    struct dma_fence_array_cb {
        struct dma_fence_cb cb;
        struct dma_fence_array *array;
    }

.. _`dma_fence_array_cb.members`:

Members
-------

cb
    fence callback structure for signaling

array
    reference to the parent fence array object

.. _`dma_fence_array`:

struct dma_fence_array
======================

.. c:type:: struct dma_fence_array

    fence to represent an array of fences

.. _`dma_fence_array.definition`:

Definition
----------

.. code-block:: c

    struct dma_fence_array {
        struct dma_fence base;
        spinlock_t lock;
        unsigned num_fences;
        atomic_t num_pending;
        struct dma_fence **fences;
        struct irq_work work;
    }

.. _`dma_fence_array.members`:

Members
-------

base
    fence base class

lock
    spinlock for fence handling

num_fences
    number of fences in the array

num_pending
    fences in the array still pending

fences
    array of the fences

work
    *undescribed*

.. _`dma_fence_is_array`:

dma_fence_is_array
==================

.. c:function:: bool dma_fence_is_array(struct dma_fence *fence)

    check if a fence is from the array subsclass

    :param fence:
        fence to test
    :type fence: struct dma_fence \*

.. _`dma_fence_is_array.description`:

Description
-----------

Return true if it is a dma_fence_array and false otherwise.

.. _`to_dma_fence_array`:

to_dma_fence_array
==================

.. c:function:: struct dma_fence_array *to_dma_fence_array(struct dma_fence *fence)

    cast a fence to a dma_fence_array

    :param fence:
        fence to cast to a dma_fence_array
    :type fence: struct dma_fence \*

.. _`to_dma_fence_array.description`:

Description
-----------

Returns NULL if the fence is not a dma_fence_array,
or the dma_fence_array otherwise.

.. This file was automatic generated / don't edit.

