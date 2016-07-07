.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/mv_xor.c

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

