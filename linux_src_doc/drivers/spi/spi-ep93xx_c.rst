.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-ep93xx.c

.. _`ep93xx_spi`:

struct ep93xx_spi
=================

.. c:type:: struct ep93xx_spi

    EP93xx SPI controller structure

.. _`ep93xx_spi.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_spi {
        struct clk *clk;
        void __iomem *mmio;
        unsigned long sspdr_phys;
        size_t tx;
        size_t rx;
        size_t fifo_level;
        struct dma_chan *dma_rx;
        struct dma_chan *dma_tx;
        struct ep93xx_dma_data dma_rx_data;
        struct ep93xx_dma_data dma_tx_data;
        struct sg_table rx_sgt;
        struct sg_table tx_sgt;
        void *zeropage;
    }

.. _`ep93xx_spi.members`:

Members
-------

clk
    clock for the controller

mmio
    pointer to \ :c:func:`ioremap`\ 'd registers

sspdr_phys
    physical address of the SSPDR register

tx
    current byte in transfer to transmit

rx
    current byte in transfer to receive

fifo_level
    how full is FIFO (%0..%SPI_FIFO_SIZE - \ ``1``\ ). Receiving one
    frame decreases this level and sending one frame increases it.

dma_rx
    RX DMA channel

dma_tx
    TX DMA channel

dma_rx_data
    RX parameters passed to the DMA engine

dma_tx_data
    TX parameters passed to the DMA engine

rx_sgt
    sg table for RX transfers

tx_sgt
    sg table for TX transfers

zeropage
    dummy page used as RX buffer when only TX buffer is passed in by
    the client

.. _`ep93xx_spi_calc_divisors`:

ep93xx_spi_calc_divisors
========================

.. c:function:: int ep93xx_spi_calc_divisors(struct spi_master *master, u32 rate, u8 *div_cpsr, u8 *div_scr)

    calculates SPI clock divisors

    :param master:
        SPI master
    :type master: struct spi_master \*

    :param rate:
        desired SPI output clock rate
    :type rate: u32

    :param div_cpsr:
        pointer to return the cpsr (pre-scaler) divider
    :type div_cpsr: u8 \*

    :param div_scr:
        pointer to return the scr divider
    :type div_scr: u8 \*

.. _`ep93xx_spi_read_write`:

ep93xx_spi_read_write
=====================

.. c:function:: int ep93xx_spi_read_write(struct spi_master *master)

    perform next RX/TX transfer

    :param master:
        *undescribed*
    :type master: struct spi_master \*

.. _`ep93xx_spi_read_write.description`:

Description
-----------

This function transfers next bytes (or half-words) to/from RX/TX FIFOs. If
called several times, the whole transfer will be completed. Returns
\ ``-EINPROGRESS``\  when current transfer was not yet completed otherwise \ ``0``\ .

When this function is finished, RX FIFO should be empty and TX FIFO should be
full.

.. _`ep93xx_spi_dma_prepare`:

ep93xx_spi_dma_prepare
======================

.. c:function:: struct dma_async_tx_descriptor *ep93xx_spi_dma_prepare(struct spi_master *master, enum dma_data_direction dir)

    prepares a DMA transfer

    :param master:
        SPI master
    :type master: struct spi_master \*

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

.. _`ep93xx_spi_dma_prepare.description`:

Description
-----------

Function configures the DMA, maps the buffer and prepares the DMA
descriptor. Returns a valid DMA descriptor in case of success and ERR_PTR
in case of failure.

.. _`ep93xx_spi_dma_finish`:

ep93xx_spi_dma_finish
=====================

.. c:function:: void ep93xx_spi_dma_finish(struct spi_master *master, enum dma_data_direction dir)

    finishes with a DMA transfer

    :param master:
        SPI master
    :type master: struct spi_master \*

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

.. _`ep93xx_spi_dma_finish.description`:

Description
-----------

Function finishes with the DMA transfer. After this, the DMA buffer is
unmapped.

.. This file was automatic generated / don't edit.

