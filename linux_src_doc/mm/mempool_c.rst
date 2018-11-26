.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/mempool.c

.. _`mempool_exit`:

mempool_exit
============

.. c:function:: void mempool_exit(mempool_t *pool)

    exit a mempool initialized with \ :c:func:`mempool_init`\ 

    :param pool:
        pointer to the memory pool which was initialized with
        \ :c:func:`mempool_init`\ .
    :type pool: mempool_t \*

.. _`mempool_exit.description`:

Description
-----------

Free all reserved elements in \ ``pool``\  and \ ``pool``\  itself.  This function
only sleeps if the \ :c:func:`free_fn`\  function sleeps.

May be called on a zeroed but uninitialized mempool (i.e. allocated with
\ :c:func:`kzalloc`\ ).

.. _`mempool_destroy`:

mempool_destroy
===============

.. c:function:: void mempool_destroy(mempool_t *pool)

    deallocate a memory pool

    :param pool:
        pointer to the memory pool which was allocated via
        \ :c:func:`mempool_create`\ .
    :type pool: mempool_t \*

.. _`mempool_destroy.description`:

Description
-----------

Free all reserved elements in \ ``pool``\  and \ ``pool``\  itself.  This function
only sleeps if the \ :c:func:`free_fn`\  function sleeps.

.. _`mempool_init`:

mempool_init
============

.. c:function:: int mempool_init(mempool_t *pool, int min_nr, mempool_alloc_t *alloc_fn, mempool_free_t *free_fn, void *pool_data)

    initialize a memory pool

    :param pool:
        pointer to the memory pool that should be initialized
    :type pool: mempool_t \*

    :param min_nr:
        the minimum number of elements guaranteed to be
        allocated for this pool.
    :type min_nr: int

    :param alloc_fn:
        user-defined element-allocation function.
    :type alloc_fn: mempool_alloc_t \*

    :param free_fn:
        user-defined element-freeing function.
    :type free_fn: mempool_free_t \*

    :param pool_data:
        optional private data available to the user-defined functions.
    :type pool_data: void \*

.. _`mempool_init.description`:

Description
-----------

Like \ :c:func:`mempool_create`\ , but initializes the pool in (i.e. embedded in another
structure).

.. _`mempool_create`:

mempool_create
==============

.. c:function:: mempool_t *mempool_create(int min_nr, mempool_alloc_t *alloc_fn, mempool_free_t *free_fn, void *pool_data)

    create a memory pool

    :param min_nr:
        the minimum number of elements guaranteed to be
        allocated for this pool.
    :type min_nr: int

    :param alloc_fn:
        user-defined element-allocation function.
    :type alloc_fn: mempool_alloc_t \*

    :param free_fn:
        user-defined element-freeing function.
    :type free_fn: mempool_free_t \*

    :param pool_data:
        optional private data available to the user-defined functions.
    :type pool_data: void \*

.. _`mempool_create.description`:

Description
-----------

this function creates and allocates a guaranteed size, preallocated
memory pool. The pool can be used from the \ :c:func:`mempool_alloc`\  and \ :c:func:`mempool_free`\ 
functions. This function might sleep. Both the \ :c:func:`alloc_fn`\  and the \ :c:func:`free_fn`\ 
functions might sleep - as long as the \ :c:func:`mempool_alloc`\  function is not called
from IRQ contexts.

.. _`mempool_resize`:

mempool_resize
==============

.. c:function:: int mempool_resize(mempool_t *pool, int new_min_nr)

    resize an existing memory pool

    :param pool:
        pointer to the memory pool which was allocated via
        \ :c:func:`mempool_create`\ .
    :type pool: mempool_t \*

    :param new_min_nr:
        the new minimum number of elements guaranteed to be
        allocated for this pool.
    :type new_min_nr: int

.. _`mempool_resize.description`:

Description
-----------

This function shrinks/grows the pool. In the case of growing,
it cannot be guaranteed that the pool will be grown to the new
size immediately, but new \ :c:func:`mempool_free`\  calls will refill it.
This function may sleep.

Note, the caller must guarantee that no mempool_destroy is called
while this function is running. \ :c:func:`mempool_alloc`\  & \ :c:func:`mempool_free`\ 
might be called (eg. from IRQ contexts) while this function executes.

.. _`mempool_alloc`:

mempool_alloc
=============

.. c:function:: void *mempool_alloc(mempool_t *pool, gfp_t gfp_mask)

    allocate an element from a specific memory pool

    :param pool:
        pointer to the memory pool which was allocated via
        \ :c:func:`mempool_create`\ .
    :type pool: mempool_t \*

    :param gfp_mask:
        the usual allocation bitmask.
    :type gfp_mask: gfp_t

.. _`mempool_alloc.description`:

Description
-----------

this function only sleeps if the \ :c:func:`alloc_fn`\  function sleeps or
returns NULL. Note that due to preallocation, this function
*never* fails when called from process contexts. (it might
fail if called from an IRQ context.)

.. _`mempool_alloc.note`:

Note
----

using __GFP_ZERO is not supported.

.. _`mempool_free`:

mempool_free
============

.. c:function:: void mempool_free(void *element, mempool_t *pool)

    return an element to the pool.

    :param element:
        pool element pointer.
    :type element: void \*

    :param pool:
        pointer to the memory pool which was allocated via
        \ :c:func:`mempool_create`\ .
    :type pool: mempool_t \*

.. _`mempool_free.description`:

Description
-----------

this function only sleeps if the \ :c:func:`free_fn`\  function sleeps.

.. This file was automatic generated / don't edit.

