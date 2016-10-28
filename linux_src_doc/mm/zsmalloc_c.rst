.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/zsmalloc.c

.. _`zs_map_object`:

zs_map_object
=============

.. c:function:: void *zs_map_object(struct zs_pool *pool, unsigned long handle, enum zs_mapmode mm)

    get address of allocated object from handle.

    :param struct zs_pool \*pool:
        pool from which the object was allocated

    :param unsigned long handle:
        handle returned from zs_malloc

    :param enum zs_mapmode mm:
        *undescribed*

.. _`zs_map_object.description`:

Description
-----------

Before using an object allocated from zs_malloc, it must be mapped using
this function. When done with the object, it must be unmapped using
zs_unmap_object.

Only one object can be mapped per cpu at a time. There is no protection
against nested mappings.

This function returns with preemption and page faults disabled.

.. _`zs_malloc`:

zs_malloc
=========

.. c:function:: unsigned long zs_malloc(struct zs_pool *pool, size_t size, gfp_t gfp)

    Allocate block of given size from pool.

    :param struct zs_pool \*pool:
        pool to allocate from

    :param size_t size:
        size of block to allocate

    :param gfp_t gfp:
        *undescribed*

.. _`zs_malloc.description`:

Description
-----------

On success, handle to the allocated object is returned,
otherwise 0.
Allocation requests with size > ZS_MAX_ALLOC_SIZE will fail.

.. _`zs_create_pool`:

zs_create_pool
==============

.. c:function:: struct zs_pool *zs_create_pool(const char *name)

    Creates an allocation pool to work from.

    :param const char \*name:
        *undescribed*

.. _`zs_create_pool.description`:

Description
-----------

This function must be called before anything when using
the zsmalloc allocator.

On success, a pointer to the newly created pool is returned,
otherwise NULL.

.. This file was automatic generated / don't edit.

