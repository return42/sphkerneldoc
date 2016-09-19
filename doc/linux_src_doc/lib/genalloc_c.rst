.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/genalloc.c

.. _`gen_pool_create`:

gen_pool_create
===============

.. c:function:: struct gen_pool *gen_pool_create(int min_alloc_order, int nid)

    create a new special memory pool

    :param int min_alloc_order:
        log base 2 of number of bytes each bitmap bit represents

    :param int nid:
        node id of the node the pool structure should be allocated on, or -1

.. _`gen_pool_create.description`:

Description
-----------

Create a new special memory pool that can be used to manage special purpose
memory not managed by the regular kmalloc/kfree interface.

.. _`gen_pool_add_virt`:

gen_pool_add_virt
=================

.. c:function:: int gen_pool_add_virt(struct gen_pool *pool, unsigned long virt, phys_addr_t phys, size_t size, int nid)

    add a new chunk of special memory to the pool

    :param struct gen_pool \*pool:
        pool to add new memory chunk to

    :param unsigned long virt:
        virtual starting address of memory chunk to add to pool

    :param phys_addr_t phys:
        physical starting address of memory chunk to add to pool

    :param size_t size:
        size in bytes of the memory chunk to add to pool

    :param int nid:
        node id of the node the chunk structure and bitmap should be
        allocated on, or -1

.. _`gen_pool_add_virt.description`:

Description
-----------

Add a new chunk of special memory to the specified pool.

Returns 0 on success or a -ve errno on failure.

.. _`gen_pool_virt_to_phys`:

gen_pool_virt_to_phys
=====================

.. c:function:: phys_addr_t gen_pool_virt_to_phys(struct gen_pool *pool, unsigned long addr)

    return the physical address of memory

    :param struct gen_pool \*pool:
        pool to allocate from

    :param unsigned long addr:
        starting address of memory

.. _`gen_pool_virt_to_phys.description`:

Description
-----------

Returns the physical address on success, or -1 on error.

.. _`gen_pool_destroy`:

gen_pool_destroy
================

.. c:function:: void gen_pool_destroy(struct gen_pool *pool)

    destroy a special memory pool

    :param struct gen_pool \*pool:
        pool to destroy

.. _`gen_pool_destroy.description`:

Description
-----------

Destroy the specified special memory pool. Verifies that there are no
outstanding allocations.

.. _`gen_pool_alloc`:

gen_pool_alloc
==============

.. c:function:: unsigned long gen_pool_alloc(struct gen_pool *pool, size_t size)

    allocate special memory from the pool

    :param struct gen_pool \*pool:
        pool to allocate from

    :param size_t size:
        number of bytes to allocate from the pool

.. _`gen_pool_alloc.description`:

Description
-----------

Allocate the requested number of bytes from the specified pool.
Uses the pool allocation function (with first-fit algorithm by default).
Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

.. _`gen_pool_alloc_algo`:

gen_pool_alloc_algo
===================

.. c:function:: unsigned long gen_pool_alloc_algo(struct gen_pool *pool, size_t size, genpool_algo_t algo, void *data)

    allocate special memory from the pool

    :param struct gen_pool \*pool:
        pool to allocate from

    :param size_t size:
        number of bytes to allocate from the pool

    :param genpool_algo_t algo:
        algorithm passed from caller

    :param void \*data:
        data passed to algorithm

.. _`gen_pool_alloc_algo.description`:

Description
-----------

Allocate the requested number of bytes from the specified pool.
Uses the pool allocation function (with first-fit algorithm by default).
Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

.. _`gen_pool_dma_alloc`:

gen_pool_dma_alloc
==================

.. c:function:: void *gen_pool_dma_alloc(struct gen_pool *pool, size_t size, dma_addr_t *dma)

    allocate special memory from the pool for DMA usage

    :param struct gen_pool \*pool:
        pool to allocate from

    :param size_t size:
        number of bytes to allocate from the pool

    :param dma_addr_t \*dma:
        dma-view physical address return value.  Use NULL if unneeded.

.. _`gen_pool_dma_alloc.description`:

Description
-----------

Allocate the requested number of bytes from the specified pool.
Uses the pool allocation function (with first-fit algorithm by default).
Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

.. _`gen_pool_free`:

gen_pool_free
=============

.. c:function:: void gen_pool_free(struct gen_pool *pool, unsigned long addr, size_t size)

    free allocated special memory back to the pool

    :param struct gen_pool \*pool:
        pool to free to

    :param unsigned long addr:
        starting address of memory to free back to pool

    :param size_t size:
        size in bytes of memory to free

.. _`gen_pool_free.description`:

Description
-----------

Free previously allocated special memory back to the specified
pool.  Can not be used in NMI handler on architectures without
NMI-safe cmpxchg implementation.

.. _`gen_pool_for_each_chunk`:

gen_pool_for_each_chunk
=======================

.. c:function:: void gen_pool_for_each_chunk(struct gen_pool *pool, void (*func)(struct gen_pool *pool, struct gen_pool_chunk *chunk, void *data), void *data)

    call func for every chunk of generic memory pool

    :param struct gen_pool \*pool:
        the generic memory pool

    :param void (\*func)(struct gen_pool \*pool, struct gen_pool_chunk \*chunk, void \*data):
        func to call

    :param void \*data:
        additional data used by \ ``func``\ 

.. _`gen_pool_for_each_chunk.description`:

Description
-----------

Call \ ``func``\  for every chunk of generic memory pool.  The \ ``func``\  is
called with rcu_read_lock held.

.. _`addr_in_gen_pool`:

addr_in_gen_pool
================

.. c:function:: bool addr_in_gen_pool(struct gen_pool *pool, unsigned long start, size_t size)

    checks if an address falls within the range of a pool

    :param struct gen_pool \*pool:
        the generic memory pool

    :param unsigned long start:
        start address

    :param size_t size:
        size of the region

.. _`addr_in_gen_pool.description`:

Description
-----------

Check if the range of addresses falls within the specified pool. Returns
true if the entire range is contained in the pool and false otherwise.

.. _`gen_pool_avail`:

gen_pool_avail
==============

.. c:function:: size_t gen_pool_avail(struct gen_pool *pool)

    get available free space of the pool

    :param struct gen_pool \*pool:
        pool to get available free space

.. _`gen_pool_avail.description`:

Description
-----------

Return available free space of the specified pool.

.. _`gen_pool_size`:

gen_pool_size
=============

.. c:function:: size_t gen_pool_size(struct gen_pool *pool)

    get size in bytes of memory managed by the pool

    :param struct gen_pool \*pool:
        pool to get size

.. _`gen_pool_size.description`:

Description
-----------

Return size in bytes of memory managed by the pool.

.. _`gen_pool_set_algo`:

gen_pool_set_algo
=================

.. c:function:: void gen_pool_set_algo(struct gen_pool *pool, genpool_algo_t algo, void *data)

    set the allocation algorithm

    :param struct gen_pool \*pool:
        pool to change allocation algorithm

    :param genpool_algo_t algo:
        custom algorithm function

    :param void \*data:
        additional data used by \ ``algo``\ 

.. _`gen_pool_set_algo.description`:

Description
-----------

Call \ ``algo``\  for each memory allocation in the pool.
If \ ``algo``\  is NULL use gen_pool_first_fit as default
memory allocation function.

.. _`gen_pool_first_fit`:

gen_pool_first_fit
==================

.. c:function:: unsigned long gen_pool_first_fit(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, void *data, struct gen_pool *pool)

    find the first available region of memory matching the size requirement (no alignment constraint)

    :param unsigned long \*map:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long start:
        The bitnumber to start searching at

    :param unsigned int nr:
        The number of zeroed bits we're looking for

    :param void \*data:
        additional data - unused

    :param struct gen_pool \*pool:
        pool to find the fit region memory from

.. _`gen_pool_first_fit_align`:

gen_pool_first_fit_align
========================

.. c:function:: unsigned long gen_pool_first_fit_align(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, void *data, struct gen_pool *pool)

    find the first available region of memory matching the size requirement (alignment constraint)

    :param unsigned long \*map:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long start:
        The bitnumber to start searching at

    :param unsigned int nr:
        The number of zeroed bits we're looking for

    :param void \*data:
        data for alignment

    :param struct gen_pool \*pool:
        pool to get order from

.. _`gen_pool_fixed_alloc`:

gen_pool_fixed_alloc
====================

.. c:function:: unsigned long gen_pool_fixed_alloc(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, void *data, struct gen_pool *pool)

    reserve a specific region

    :param unsigned long \*map:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long start:
        The bitnumber to start searching at

    :param unsigned int nr:
        The number of zeroed bits we're looking for

    :param void \*data:
        data for alignment

    :param struct gen_pool \*pool:
        pool to get order from

.. _`gen_pool_first_fit_order_align`:

gen_pool_first_fit_order_align
==============================

.. c:function:: unsigned long gen_pool_first_fit_order_align(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, void *data, struct gen_pool *pool)

    find the first available region of memory matching the size requirement. The region will be aligned to the order of the size specified.

    :param unsigned long \*map:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long start:
        The bitnumber to start searching at

    :param unsigned int nr:
        The number of zeroed bits we're looking for

    :param void \*data:
        additional data - unused

    :param struct gen_pool \*pool:
        pool to find the fit region memory from

.. _`gen_pool_best_fit`:

gen_pool_best_fit
=================

.. c:function:: unsigned long gen_pool_best_fit(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, void *data, struct gen_pool *pool)

    find the best fitting region of memory macthing the size requirement (no alignment constraint)

    :param unsigned long \*map:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long start:
        The bitnumber to start searching at

    :param unsigned int nr:
        The number of zeroed bits we're looking for

    :param void \*data:
        additional data - unused

    :param struct gen_pool \*pool:
        pool to find the fit region memory from

.. _`gen_pool_best_fit.description`:

Description
-----------

Iterate over the bitmap to find the smallest free region
which we can allocate the memory.

.. _`gen_pool_get`:

gen_pool_get
============

.. c:function:: struct gen_pool *gen_pool_get(struct device *dev, const char *name)

    Obtain the gen_pool (if any) for a device

    :param struct device \*dev:
        device to retrieve the gen_pool from

    :param const char \*name:
        name of a gen_pool or NULL, identifies a particular gen_pool on device

.. _`gen_pool_get.description`:

Description
-----------

Returns the gen_pool for the device if one is present, or NULL.

.. _`devm_gen_pool_create`:

devm_gen_pool_create
====================

.. c:function:: struct gen_pool *devm_gen_pool_create(struct device *dev, int min_alloc_order, int nid, const char *name)

    managed gen_pool_create

    :param struct device \*dev:
        device that provides the gen_pool

    :param int min_alloc_order:
        log base 2 of number of bytes each bitmap bit represents

    :param int nid:
        node selector for allocated gen_pool, \ ``NUMA_NO_NODE``\  for all nodes

    :param const char \*name:
        name of a gen_pool or NULL, identifies a particular gen_pool on device

.. _`devm_gen_pool_create.description`:

Description
-----------

Create a new special memory pool that can be used to manage special purpose
memory not managed by the regular kmalloc/kfree interface. The pool will be
automatically destroyed by the device management code.

.. _`of_gen_pool_get`:

of_gen_pool_get
===============

.. c:function:: struct gen_pool *of_gen_pool_get(struct device_node *np, const char *propname, int index)

    find a pool by phandle property

    :param struct device_node \*np:
        device node

    :param const char \*propname:
        property name containing phandle(s)

    :param int index:
        index into the phandle array

.. _`of_gen_pool_get.description`:

Description
-----------

Returns the pool that contains the chunk starting at the physical
address of the device tree node pointed at by the phandle property,
or NULL if not found.

.. This file was automatic generated / don't edit.

