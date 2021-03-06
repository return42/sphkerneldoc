.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/genalloc.h

.. _`long`:

long
====

.. c:function:: unsigned long(*genpool_algo_t)(unsigned long *map#unsigned long size#unsigned long start#unsigned int nr# void *data# struct gen_pool *pool)

    Allocation callback function type definition

    :param pool:
        the pool being allocated from
    :type pool: \*genpool_algo_t)(unsigned long \*map#unsigned long size#unsigned long start#unsigned int nr# void \*data# struct gen_pool \*

.. _`gen_pool_add`:

gen_pool_add
============

.. c:function:: int gen_pool_add(struct gen_pool *pool, unsigned long addr, size_t size, int nid)

    add a new chunk of special memory to the pool

    :param pool:
        pool to add new memory chunk to
    :type pool: struct gen_pool \*

    :param addr:
        starting address of memory chunk to add to pool
    :type addr: unsigned long

    :param size:
        size in bytes of the memory chunk to add to pool
    :type size: size_t

    :param nid:
        node id of the node the chunk structure and bitmap should be
        allocated on, or -1
    :type nid: int

.. _`gen_pool_add.description`:

Description
-----------

Add a new chunk of special memory to the specified pool.

Returns 0 on success or a -ve errno on failure.

.. This file was automatic generated / don't edit.

