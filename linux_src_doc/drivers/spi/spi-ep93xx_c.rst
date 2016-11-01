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
        const struct platform_device *pdev;
        struct clk *clk;
        void __iomem *regs_base;
        unsigned long sspdr_phys;
        struct completion wait;
        struct spi_message *current_msg;
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

pdev
    pointer to platform device

clk
    clock for the controller

regs_base
    pointer to \ :c:func:`ioremap`\ 'd registers

sspdr_phys
    physical address of the SSPDR register

wait
    wait here until given transfer is completed

current_msg
    message that is currently processed (or \ ``NULL``\  if none)

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

.. _`ep93xx_spi_chip`:

struct ep93xx_spi_chip
======================

.. c:type:: struct ep93xx_spi_chip

    SPI device hardware settings

.. _`ep93xx_spi_chip.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_spi_chip {
        const struct spi_device *spi;
        struct ep93xx_spi_chip_ops *ops;
    }

.. _`ep93xx_spi_chip.members`:

Members
-------

spi
    back pointer to the SPI device

ops
    private chip operations

.. _`ep93xx_spi_calc_divisors`:

ep93xx_spi_calc_divisors
========================

.. c:function:: int ep93xx_spi_calc_divisors(const struct ep93xx_spi *espi, u32 rate, u8 *div_cpsr, u8 *div_scr)

    calculates SPI clock divisors

    :param const struct ep93xx_spi \*espi:
        ep93xx SPI controller struct

    :param u32 rate:
        desired SPI output clock rate

    :param u8 \*div_cpsr:
        pointer to return the cpsr (pre-scaler) divider

    :param u8 \*div_scr:
        pointer to return the scr divider

.. _`ep93xx_spi_setup`:

ep93xx_spi_setup
================

.. c:function:: int ep93xx_spi_setup(struct spi_device *spi)

    setup an SPI device

    :param struct spi_device \*spi:
        SPI device to setup

.. _`ep93xx_spi_setup.description`:

Description
-----------

This function sets up SPI device mode, speed etc. Can be called multiple
times for a single device. Returns \ ``0``\  in case of success, negative error in
case of failure. When this function returns success, the device is
deselected.

.. _`ep93xx_spi_cleanup`:

ep93xx_spi_cleanup
==================

.. c:function:: void ep93xx_spi_cleanup(struct spi_device *spi)

    cleans up master controller specific state

    :param struct spi_device \*spi:
        SPI device to cleanup

.. _`ep93xx_spi_cleanup.description`:

Description
-----------

This function releases master controller specific state for given \ ``spi``\ 
device.

.. _`ep93xx_spi_chip_setup`:

ep93xx_spi_chip_setup
=====================

.. c:function:: int ep93xx_spi_chip_setup(const struct ep93xx_spi *espi, const struct ep93xx_spi_chip *chip, u32 speed_hz, u8 bits_per_word)

    configures hardware according to given \ ``chip``\ 

    :param const struct ep93xx_spi \*espi:
        ep93xx SPI controller struct

    :param const struct ep93xx_spi_chip \*chip:
        chip specific settings

    :param u32 speed_hz:
        transfer speed

    :param u8 bits_per_word:
        transfer bits_per_word

.. _`ep93xx_spi_read_write`:

ep93xx_spi_read_write
=====================

.. c:function:: int ep93xx_spi_read_write(struct ep93xx_spi *espi)

    perform next RX/TX transfer

    :param struct ep93xx_spi \*espi:
        ep93xx SPI controller struct

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

.. c:function:: struct dma_async_tx_descriptor *ep93xx_spi_dma_prepare(struct ep93xx_spi *espi, enum dma_transfer_direction dir)

    prepares a DMA transfer

    :param struct ep93xx_spi \*espi:
        ep93xx SPI controller struct

    :param enum dma_transfer_direction dir:
        DMA transfer direction

.. _`ep93xx_spi_dma_prepare.description`:

Description
-----------

Function configures the DMA, maps the buffer and prepares the DMA
descriptor. Returns a valid DMA descriptor in case of success and ERR_PTR
in case of failure.

.. _`ep93xx_spi_dma_finish`:

ep93xx_spi_dma_finish
=====================

.. c:function:: void ep93xx_spi_dma_finish(struct ep93xx_spi *espi, enum dma_transfer_direction dir)

    finishes with a DMA transfer

    :param struct ep93xx_spi \*espi:
        ep93xx SPI controller struct

    :param enum dma_transfer_direction dir:
        DMA transfer direction

.. _`ep93xx_spi_dma_finish.description`:

Description
-----------

Function finishes with the DMA transfer. After this, the DMA buffer is
unmapped.

.. _`ep93xx_spi_process_transfer`:

ep93xx_spi_process_transfer
===========================

.. c:function:: void ep93xx_spi_process_transfer(struct ep93xx_spi *espi, struct spi_message *msg, struct spi_transfer *t)

    processes one SPI transfer

    :param struct ep93xx_spi \*espi:
        ep93xx SPI controller struct

    :param struct spi_message \*msg:
        current message

    :param struct spi_transfer \*t:
        transfer to process

.. _`ep93xx_spi_process_transfer.description`:

Description
-----------

This function processes one SPI transfer given in \ ``t``\ . Function waits until
transfer is complete (may sleep) and updates \ ``msg``\ ->status based on whether
transfer was successfully processed or not.

.. This file was automatic generated / don't edit.

