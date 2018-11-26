.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/zsmalloc.c

.. _`obj_to_location`:

obj_to_location
===============

.. c:function:: void obj_to_location(unsigned long obj, struct page **page, unsigned int *obj_idx)

    get (<page>, <obj_idx>) from encoded object value

    :param obj:
        the encoded object value
    :type obj: unsigned long

    :param page:
        page object resides in zspage
    :type page: struct page \*\*

    :param obj_idx:
        object index
    :type obj_idx: unsigned int \*

.. _`location_to_obj`:

location_to_obj
===============

.. c:function:: unsigned long location_to_obj(struct page *page, unsigned int obj_idx)

    get obj value encoded from (<page>, <obj_idx>)

    :param page:
        page object resides in zspage
    :type page: struct page \*

    :param obj_idx:
        object index
    :type obj_idx: unsigned int

.. _`zs_map_object`:

zs_map_object
=============

.. c:function:: void *zs_map_object(struct zs_pool *pool, unsigned long handle, enum zs_mapmode mm)

    get address of allocated object from handle.

    :param pool:
        pool from which the object was allocated
    :type pool: struct zs_pool \*

    :param handle:
        handle returned from zs_malloc
    :type handle: unsigned long

    :param mm:
        maping mode to use
    :type mm: enum zs_mapmode

.. _`zs_map_object.description`:

Description
-----------

Before using an object allocated from zs_malloc, it must be mapped using
this function. When done with the object, it must be unmapped using
zs_unmap_object.

Only one object can be mapped per cpu at a time. There is no protection
against nested mappings.

This function returns with preemption and page faults disabled.

.. _`zs_huge_class_size`:

zs_huge_class_size
==================

.. c:function:: size_t zs_huge_class_size(struct zs_pool *pool)

    Returns the size (in bytes) of the first huge zsmalloc \ :c:type:`struct size_class <size_class>`\ .

    :param pool:
        zsmalloc pool to use
    :type pool: struct zs_pool \*

.. _`zs_huge_class_size.description`:

Description
-----------

The function returns the size of the first huge class - any object of equal
or bigger size will be stored in zspage consisting of a single physical
page.

.. _`zs_huge_class_size.context`:

Context
-------

Any context.

.. _`zs_huge_class_size.return`:

Return
------

the size (in bytes) of the first huge zsmalloc \ :c:type:`struct size_class <size_class>`\ .

.. _`zs_malloc`:

zs_malloc
=========

.. c:function:: unsigned long zs_malloc(struct zs_pool *pool, size_t size, gfp_t gfp)

    Allocate block of given size from pool.

    :param pool:
        pool to allocate from
    :type pool: struct zs_pool \*

    :param size:
        size of block to allocate
    :type size: size_t

    :param gfp:
        gfp flags when allocating object
    :type gfp: gfp_t

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

    :param name:
        pool name to be created
    :type name: const char \*

.. _`zs_create_pool.description`:

Description
-----------

This function must be called before anything when using
the zsmalloc allocator.

On success, a pointer to the newly created pool is returned,
otherwise NULL.

.. This file was automatic generated / don't edit.

