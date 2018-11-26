.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/sh/shdma-base.c

.. _`shdma_add_desc`:

shdma_add_desc
==============

.. c:function:: struct shdma_desc *shdma_add_desc(struct shdma_chan *schan, unsigned long flags, dma_addr_t *dst, dma_addr_t *src, size_t *len, struct shdma_desc **first, enum dma_transfer_direction direction)

    get, set up and return one transfer descriptor

    :param schan:
        DMA channel
    :type schan: struct shdma_chan \*

    :param flags:
        DMA transfer flags
    :type flags: unsigned long

    :param dst:
        destination DMA address, incremented when direction equals
        DMA_DEV_TO_MEM or DMA_MEM_TO_MEM
    :type dst: dma_addr_t \*

    :param src:
        source DMA address, incremented when direction equals
        DMA_MEM_TO_DEV or DMA_MEM_TO_MEM
    :type src: dma_addr_t \*

    :param len:
        DMA transfer length
    :type len: size_t \*

    :param first:
        if NULL, set to the current descriptor and cookie set to -EBUSY
    :type first: struct shdma_desc \*\*

    :param direction:
        needed for slave DMA to decide which address to keep constant,
        equals DMA_MEM_TO_MEM for MEMCPY
        Returns 0 or an error
    :type direction: enum dma_transfer_direction

.. _`shdma_add_desc.locks`:

Locks
-----

called with desc_lock held

.. This file was automatic generated / don't edit.

