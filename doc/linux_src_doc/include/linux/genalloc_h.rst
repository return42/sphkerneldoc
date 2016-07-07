.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/genalloc.h

.. _`long`:

long
====

.. c:function:: typedef unsigned long(*genpool_algo_t)

    :param \*genpool_algo_t:
        *undescribed*

.. _`gen_pool_add`:

gen_pool_add
============

.. c:function:: int gen_pool_add(struct gen_pool *pool, unsigned long addr, size_t size, int nid)

    add a new chunk of special memory to the pool

    :param struct gen_pool \*pool:
        pool to add new memory chunk to

    :param unsigned long addr:
        starting address of memory chunk to add to pool

    :param size_t size:
        size in bytes of the memory chunk to add to pool

    :param int nid:
        node id of the node the chunk structure and bitmap should be
        allocated on, or -1

.. _`gen_pool_add.description`:

Description
-----------

Add a new chunk of special memory to the specified pool.

Returns 0 on success or a -ve errno on failure.

.. This file was automatic generated / don't edit.

