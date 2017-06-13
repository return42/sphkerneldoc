.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/dmapool.c

.. _`dma_pool_create`:

dma_pool_create
===============

.. c:function:: struct dma_pool *dma_pool_create(const char *name, struct device *dev, size_t size, size_t align, size_t boundary)

    Creates a pool of consistent memory blocks, for dma.

    :param const char \*name:
        name of pool, for diagnostics

    :param struct device \*dev:
        device that will be doing the DMA

    :param size_t size:
        size of the blocks in this pool.

    :param size_t align:
        alignment requirement for blocks; must be a power of two

    :param size_t boundary:
        returned blocks won't cross this power of two boundary

.. _`dma_pool_create.context`:

Context
-------

!in_interrupt()

.. _`dma_pool_create.description`:

Description
-----------

Returns a dma allocation pool with the requested characteristics, or
null if one can't be created.  Given one of these pools, \ :c:func:`dma_pool_alloc`\ 
may be used to allocate memory.  Such memory will all have "consistent"
DMA mappings, accessible by the device and its driver without using
cache flushing primitives.  The actual size of blocks allocated may be
larger than requested because of alignment.

If \ ``boundary``\  is nonzero, objects returned from \ :c:func:`dma_pool_alloc`\  won't
cross that size boundary.  This is useful for devices which have
addressing restrictions on individual DMA transfers, such as not crossing
boundaries of 4KBytes.

.. _`dma_pool_destroy`:

dma_pool_destroy
================

.. c:function:: void dma_pool_destroy(struct dma_pool *pool)

    destroys a pool of dma memory blocks.

    :param struct dma_pool \*pool:
        dma pool that will be destroyed

.. _`dma_pool_destroy.context`:

Context
-------

!in_interrupt()

.. _`dma_pool_destroy.description`:

Description
-----------

Caller guarantees that no more memory from the pool is in use,
and that nothing will try to use the pool after this call.

.. _`dma_pool_alloc`:

dma_pool_alloc
==============

.. c:function:: void *dma_pool_alloc(struct dma_pool *pool, gfp_t mem_flags, dma_addr_t *handle)

    get a block of consistent memory

    :param struct dma_pool \*pool:
        dma pool that will produce the block

    :param gfp_t mem_flags:
        GFP_* bitmask

    :param dma_addr_t \*handle:
        pointer to dma address of block

.. _`dma_pool_alloc.description`:

Description
-----------

This returns the kernel virtual address of a currently unused block,
and reports its dma address through the handle.
If such a memory block can't be allocated, \ ``NULL``\  is returned.

.. _`dma_pool_free`:

dma_pool_free
=============

.. c:function:: void dma_pool_free(struct dma_pool *pool, void *vaddr, dma_addr_t dma)

    put block back into dma pool

    :param struct dma_pool \*pool:
        the dma pool holding the block

    :param void \*vaddr:
        virtual address of block

    :param dma_addr_t dma:
        dma address of block

.. _`dma_pool_free.description`:

Description
-----------

Caller promises neither device nor driver will again touch this block
unless it is first re-allocated.

.. _`dmam_pool_create`:

dmam_pool_create
================

.. c:function:: struct dma_pool *dmam_pool_create(const char *name, struct device *dev, size_t size, size_t align, size_t allocation)

    Managed \ :c:func:`dma_pool_create`\ 

    :param const char \*name:
        name of pool, for diagnostics

    :param struct device \*dev:
        device that will be doing the DMA

    :param size_t size:
        size of the blocks in this pool.

    :param size_t align:
        alignment requirement for blocks; must be a power of two

    :param size_t allocation:
        returned blocks won't cross this boundary (or zero)

.. _`dmam_pool_create.description`:

Description
-----------

Managed \ :c:func:`dma_pool_create`\ .  DMA pool created with this function is
automatically destroyed on driver detach.

.. _`dmam_pool_destroy`:

dmam_pool_destroy
=================

.. c:function:: void dmam_pool_destroy(struct dma_pool *pool)

    Managed \ :c:func:`dma_pool_destroy`\ 

    :param struct dma_pool \*pool:
        dma pool that will be destroyed

.. _`dmam_pool_destroy.description`:

Description
-----------

Managed \ :c:func:`dma_pool_destroy`\ .

.. This file was automatic generated / don't edit.

