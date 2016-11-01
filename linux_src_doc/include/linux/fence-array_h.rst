.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fence-array.h

.. _`fence_array_cb`:

struct fence_array_cb
=====================

.. c:type:: struct fence_array_cb

    callback helper for fence array

.. _`fence_array_cb.definition`:

Definition
----------

.. code-block:: c

    struct fence_array_cb {
        struct fence_cb cb;
        struct fence_array *array;
    }

.. _`fence_array_cb.members`:

Members
-------

cb
    fence callback structure for signaling

array
    reference to the parent fence array object

.. _`fence_array`:

struct fence_array
==================

.. c:type:: struct fence_array

    fence to represent an array of fences

.. _`fence_array.definition`:

Definition
----------

.. code-block:: c

    struct fence_array {
        struct fence base;
        spinlock_t lock;
        unsigned num_fences;
        atomic_t num_pending;
        struct fence **fences;
    }

.. _`fence_array.members`:

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

.. _`fence_is_array`:

fence_is_array
==============

.. c:function:: bool fence_is_array(struct fence *fence)

    check if a fence is from the array subsclass

    :param struct fence \*fence:
        *undescribed*

.. _`fence_is_array.description`:

Description
-----------

Return true if it is a fence_array and false otherwise.

.. _`to_fence_array`:

to_fence_array
==============

.. c:function:: struct fence_array *to_fence_array(struct fence *fence)

    cast a fence to a fence_array

    :param struct fence \*fence:
        fence to cast to a fence_array

.. _`to_fence_array.description`:

Description
-----------

Returns NULL if the fence is not a fence_array,
or the fence_array otherwise.

.. This file was automatic generated / don't edit.

