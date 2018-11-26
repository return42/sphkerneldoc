.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/mv_xor.c

.. _`mv_xor_status`:

mv_xor_status
=============

.. c:function:: enum dma_status mv_xor_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    poll the status of an XOR transaction

    :param chan:
        XOR channel handle
    :type chan: struct dma_chan \*

    :param cookie:
        XOR transaction identifier
    :type cookie: dma_cookie_t

    :param txstate:
        XOR transactions state holder (or NULL)
    :type txstate: struct dma_tx_state \*

.. This file was automatic generated / don't edit.

