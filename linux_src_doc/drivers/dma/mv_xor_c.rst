.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/mv_xor.c

.. _`mv_xor_prep_dma_sg`:

mv_xor_prep_dma_sg
==================

.. c:function:: struct dma_async_tx_descriptor *mv_xor_prep_dma_sg(struct dma_chan *chan, struct scatterlist *dst_sg, unsigned int dst_sg_len, struct scatterlist *src_sg, unsigned int src_sg_len, unsigned long flags)

    prepare descriptors for a memory sg transaction

    :param struct dma_chan \*chan:
        DMA channel

    :param struct scatterlist \*dst_sg:
        Destination scatter list

    :param unsigned int dst_sg_len:
        Number of entries in destination scatter list

    :param struct scatterlist \*src_sg:
        Source scatter list

    :param unsigned int src_sg_len:
        Number of entries in source scatter list

    :param unsigned long flags:
        transfer ack flags

.. _`mv_xor_prep_dma_sg.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`mv_xor_status`:

mv_xor_status
=============

.. c:function:: enum dma_status mv_xor_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    poll the status of an XOR transaction

    :param struct dma_chan \*chan:
        XOR channel handle

    :param dma_cookie_t cookie:
        XOR transaction identifier

    :param struct dma_tx_state \*txstate:
        XOR transactions state holder (or NULL)

.. This file was automatic generated / don't edit.

