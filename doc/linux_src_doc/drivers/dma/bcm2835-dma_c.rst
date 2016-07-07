.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/bcm2835-dma.c

.. _`bcm2835_dma_create_cb_chain`:

bcm2835_dma_create_cb_chain
===========================

.. c:function:: struct bcm2835_desc *bcm2835_dma_create_cb_chain(struct dma_chan *chan, enum dma_transfer_direction direction, bool cyclic, u32 info, u32 finalextrainfo, size_t frames, dma_addr_t src, dma_addr_t dst, size_t buf_len, size_t period_len, gfp_t gfp)

    create a control block and fills data in

    :param struct dma_chan \*chan:
        the \ ``dma_chan``\  for which we run this

    :param enum dma_transfer_direction direction:
        the direction in which we transfer

    :param bool cyclic:
        it is a cyclic transfer

    :param u32 info:
        the default info bits to apply per controlblock

    :param u32 finalextrainfo:
        additional bits in last controlblock
        (or when period_len is reached in case of cyclic)

    :param size_t frames:
        number of controlblocks to allocate

    :param dma_addr_t src:
        the src address to assign (if the S_INC bit is set
        in \ ``info``\ , then it gets incremented)

    :param dma_addr_t dst:
        the dst address to assign (if the D_INC bit is set
        in \ ``info``\ , then it gets incremented)

    :param size_t buf_len:
        the full buffer length (may also be 0)

    :param size_t period_len:
        the period length when to apply \ ``finalextrainfo``\ 
        in addition to the last transfer
        this will also break some control-blocks early

    :param gfp_t gfp:
        the GFP flag to use for allocation

.. This file was automatic generated / don't edit.

