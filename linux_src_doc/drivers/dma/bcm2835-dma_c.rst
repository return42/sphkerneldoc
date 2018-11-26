.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/bcm2835-dma.c

.. _`bcm2835_dma_create_cb_chain`:

bcm2835_dma_create_cb_chain
===========================

.. c:function:: struct bcm2835_desc *bcm2835_dma_create_cb_chain(struct dma_chan *chan, enum dma_transfer_direction direction, bool cyclic, u32 info, u32 finalextrainfo, size_t frames, dma_addr_t src, dma_addr_t dst, size_t buf_len, size_t period_len, gfp_t gfp)

    create a control block and fills data in

    :param chan:
        the \ ``dma_chan``\  for which we run this
    :type chan: struct dma_chan \*

    :param direction:
        the direction in which we transfer
    :type direction: enum dma_transfer_direction

    :param cyclic:
        it is a cyclic transfer
    :type cyclic: bool

    :param info:
        the default info bits to apply per controlblock
    :type info: u32

    :param finalextrainfo:
        additional bits in last controlblock
        (or when period_len is reached in case of cyclic)
    :type finalextrainfo: u32

    :param frames:
        number of controlblocks to allocate
    :type frames: size_t

    :param src:
        the src address to assign (if the S_INC bit is set
        in \ ``info``\ , then it gets incremented)
    :type src: dma_addr_t

    :param dst:
        the dst address to assign (if the D_INC bit is set
        in \ ``info``\ , then it gets incremented)
    :type dst: dma_addr_t

    :param buf_len:
        the full buffer length (may also be 0)
    :type buf_len: size_t

    :param period_len:
        the period length when to apply \ ``finalextrainfo``\ 
        in addition to the last transfer
        this will also break some control-blocks early
    :type period_len: size_t

    :param gfp:
        the GFP flag to use for allocation
    :type gfp: gfp_t

.. This file was automatic generated / don't edit.

