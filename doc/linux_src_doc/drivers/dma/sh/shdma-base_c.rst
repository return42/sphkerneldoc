.. -*- coding: utf-8; mode: rst -*-

============
shdma-base.c
============


.. _`shdma_add_desc`:

shdma_add_desc
==============

.. c:function:: struct shdma_desc *shdma_add_desc (struct shdma_chan *schan, unsigned long flags, dma_addr_t *dst, dma_addr_t *src, size_t *len, struct shdma_desc **first, enum dma_transfer_direction direction)

    get, set up and return one transfer descriptor

    :param struct shdma_chan \*schan:
        DMA channel

    :param unsigned long flags:
        DMA transfer flags

    :param dma_addr_t \*dst:
        destination DMA address, incremented when direction equals
        DMA_DEV_TO_MEM or DMA_MEM_TO_MEM

    :param dma_addr_t \*src:
        source DMA address, incremented when direction equals
        DMA_MEM_TO_DEV or DMA_MEM_TO_MEM

    :param size_t \*len:
        DMA transfer length

    :param struct shdma_desc \*\*first:
        if NULL, set to the current descriptor and cookie set to -EBUSY

    :param enum dma_transfer_direction direction:
        needed for slave DMA to decide which address to keep constant,
        equals DMA_MEM_TO_MEM for MEMCPY

        Returns 0 or an error



.. _`shdma_add_desc.locks`:

Locks
-----

called with desc_lock held

