.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-stm32.h

.. _`stm32_i2c_dma`:

struct stm32_i2c_dma
====================

.. c:type:: struct stm32_i2c_dma

    DMA specific data

.. _`stm32_i2c_dma.definition`:

Definition
----------

.. code-block:: c

    struct stm32_i2c_dma {
        struct dma_chan *chan_tx;
        struct dma_chan *chan_rx;
        struct dma_chan *chan_using;
        dma_addr_t dma_buf;
        unsigned int dma_len;
        enum dma_transfer_direction dma_transfer_dir;
        enum dma_data_direction dma_data_dir;
        struct completion dma_complete;
    }

.. _`stm32_i2c_dma.members`:

Members
-------

chan_tx
    dma channel for TX transfer

chan_rx
    dma channel for RX transfer

chan_using
    dma channel used for the current transfer (TX or RX)

dma_buf
    dma buffer

dma_len
    dma buffer len

dma_transfer_dir
    dma transfer direction indicator

dma_data_dir
    dma transfer mode indicator

dma_complete
    dma transfer completion

.. This file was automatic generated / don't edit.

