.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-stm32.c

.. _`stm32_spi`:

struct stm32_spi
================

.. c:type:: struct stm32_spi

    private data of the SPI controller

.. _`stm32_spi.definition`:

Definition
----------

.. code-block:: c

    struct stm32_spi {
        struct device *dev;
        struct spi_master *master;
        void __iomem *base;
        struct clk *clk;
        u32 clk_rate;
        struct reset_control *rst;
        spinlock_t lock;
        int irq;
        unsigned int fifo_size;
        unsigned int cur_midi;
        unsigned int cur_speed;
        unsigned int cur_bpw;
        unsigned int cur_fthlv;
        unsigned int cur_comm;
        unsigned int cur_xferlen;
        bool cur_usedma;
        const void *tx_buf;
        void *rx_buf;
        int tx_len;
        int rx_len;
        struct dma_chan *dma_tx;
        struct dma_chan *dma_rx;
        dma_addr_t phys_addr;
    }

.. _`stm32_spi.members`:

Members
-------

dev
    driver model representation of the controller

master
    controller master interface

base
    virtual memory area

clk
    hw kernel clock feeding the SPI clock generator

clk_rate
    rate of the hw kernel clock feeding the SPI clock generator

rst
    SPI controller reset line

lock
    prevent I/O concurrent access

irq
    SPI controller interrupt line

fifo_size
    size of the embedded fifo in bytes

cur_midi
    master inter-data idleness in ns

cur_speed
    speed configured in Hz

cur_bpw
    number of bits in a single SPI data frame

cur_fthlv
    fifo threshold level (data frames in a single data packet)

cur_comm
    SPI communication mode

cur_xferlen
    current transfer length in bytes

cur_usedma
    boolean to know if dma is used in current transfer

tx_buf
    data to be written, or NULL

rx_buf
    data to be read, or NULL

tx_len
    number of data to be written in bytes

rx_len
    number of data to be read in bytes

dma_tx
    dma channel for TX transfer

dma_rx
    dma channel for RX transfer

phys_addr
    SPI registers physical base address

.. _`stm32_spi_get_fifo_size`:

stm32_spi_get_fifo_size
=======================

.. c:function:: int stm32_spi_get_fifo_size(struct stm32_spi *spi)

    Return fifo size

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

.. _`stm32_spi_get_bpw_mask`:

stm32_spi_get_bpw_mask
======================

.. c:function:: int stm32_spi_get_bpw_mask(struct stm32_spi *spi)

    Return bits per word mask

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

.. _`stm32_spi_prepare_mbr`:

stm32_spi_prepare_mbr
=====================

.. c:function:: int stm32_spi_prepare_mbr(struct stm32_spi *spi, u32 speed_hz)

    Determine SPI_CFG1.MBR value

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

    :param speed_hz:
        requested speed
    :type speed_hz: u32

.. _`stm32_spi_prepare_mbr.description`:

Description
-----------

Return SPI_CFG1.MBR value in case of success or -EINVAL

.. _`stm32_spi_prepare_fthlv`:

stm32_spi_prepare_fthlv
=======================

.. c:function:: u32 stm32_spi_prepare_fthlv(struct stm32_spi *spi)

    Determine FIFO threshold level

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

.. _`stm32_spi_write_txfifo`:

stm32_spi_write_txfifo
======================

.. c:function:: void stm32_spi_write_txfifo(struct stm32_spi *spi)

    Write bytes in Transmit Data Register

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

.. _`stm32_spi_write_txfifo.description`:

Description
-----------

Read from tx_buf depends on remaining bytes to avoid to read beyond
tx_buf end.

.. _`stm32_spi_read_rxfifo`:

stm32_spi_read_rxfifo
=====================

.. c:function:: void stm32_spi_read_rxfifo(struct stm32_spi *spi, bool flush)

    Read bytes in Receive Data Register

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

    :param flush:
        *undescribed*
    :type flush: bool

.. _`stm32_spi_read_rxfifo.description`:

Description
-----------

Write in rx_buf depends on remaining bytes to avoid to write beyond
rx_buf end.

.. _`stm32_spi_enable`:

stm32_spi_enable
================

.. c:function:: void stm32_spi_enable(struct stm32_spi *spi)

    Enable SPI controller

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

.. _`stm32_spi_enable.description`:

Description
-----------

SPI data transfer is enabled but spi_ker_ck is idle.
SPI_CFG1 and SPI_CFG2 are now write protected.

.. _`stm32_spi_disable`:

stm32_spi_disable
=================

.. c:function:: void stm32_spi_disable(struct stm32_spi *spi)

    Disable SPI controller

    :param spi:
        pointer to the spi controller data structure
    :type spi: struct stm32_spi \*

.. _`stm32_spi_disable.description`:

Description
-----------

RX-Fifo is flushed when SPI controller is disabled. To prevent any data
loss, use stm32_spi_read_rxfifo(flush) to read the remaining bytes in
RX-Fifo.

.. _`stm32_spi_can_dma`:

stm32_spi_can_dma
=================

.. c:function:: bool stm32_spi_can_dma(struct spi_master *master, struct spi_device *spi_dev, struct spi_transfer *transfer)

    Determine if the transfer is eligible for DMA use

    :param master:
        *undescribed*
    :type master: struct spi_master \*

    :param spi_dev:
        *undescribed*
    :type spi_dev: struct spi_device \*

    :param transfer:
        *undescribed*
    :type transfer: struct spi_transfer \*

.. _`stm32_spi_can_dma.description`:

Description
-----------

If the current transfer size is greater than fifo size, use DMA.

.. _`stm32_spi_irq`:

stm32_spi_irq
=============

.. c:function:: irqreturn_t stm32_spi_irq(int irq, void *dev_id)

    Interrupt handler for SPI controller events

    :param irq:
        interrupt line
    :type irq: int

    :param dev_id:
        SPI controller master interface
    :type dev_id: void \*

.. _`stm32_spi_setup`:

stm32_spi_setup
===============

.. c:function:: int stm32_spi_setup(struct spi_device *spi_dev)

    setup device chip select

    :param spi_dev:
        *undescribed*
    :type spi_dev: struct spi_device \*

.. _`stm32_spi_prepare_msg`:

stm32_spi_prepare_msg
=====================

.. c:function:: int stm32_spi_prepare_msg(struct spi_master *master, struct spi_message *msg)

    set up the controller to transfer a single message

    :param master:
        *undescribed*
    :type master: struct spi_master \*

    :param msg:
        *undescribed*
    :type msg: struct spi_message \*

.. _`stm32_spi_dma_cb`:

stm32_spi_dma_cb
================

.. c:function:: void stm32_spi_dma_cb(void *data)

    dma callback

    :param data:
        *undescribed*
    :type data: void \*

.. _`stm32_spi_dma_cb.description`:

Description
-----------

DMA callback is called when the transfer is complete or when an error
occurs. If the transfer is complete, EOT flag is raised.

.. _`stm32_spi_dma_config`:

stm32_spi_dma_config
====================

.. c:function:: void stm32_spi_dma_config(struct stm32_spi *spi, struct dma_slave_config *dma_conf, enum dma_transfer_direction dir)

    configure dma slave channel depending on current transfer bits_per_word.

    :param spi:
        *undescribed*
    :type spi: struct stm32_spi \*

    :param dma_conf:
        *undescribed*
    :type dma_conf: struct dma_slave_config \*

    :param dir:
        *undescribed*
    :type dir: enum dma_transfer_direction

.. _`stm32_spi_transfer_one_irq`:

stm32_spi_transfer_one_irq
==========================

.. c:function:: int stm32_spi_transfer_one_irq(struct stm32_spi *spi)

    transfer a single spi_transfer using interrupts

    :param spi:
        *undescribed*
    :type spi: struct stm32_spi \*

.. _`stm32_spi_transfer_one_irq.description`:

Description
-----------

It must returns 0 if the transfer is finished or 1 if the transfer is still
in progress.

.. _`stm32_spi_transfer_one_dma`:

stm32_spi_transfer_one_dma
==========================

.. c:function:: int stm32_spi_transfer_one_dma(struct stm32_spi *spi, struct spi_transfer *xfer)

    transfer a single spi_transfer using DMA

    :param spi:
        *undescribed*
    :type spi: struct stm32_spi \*

    :param xfer:
        *undescribed*
    :type xfer: struct spi_transfer \*

.. _`stm32_spi_transfer_one_dma.description`:

Description
-----------

It must returns 0 if the transfer is finished or 1 if the transfer is still
in progress.

.. _`stm32_spi_transfer_one_setup`:

stm32_spi_transfer_one_setup
============================

.. c:function:: int stm32_spi_transfer_one_setup(struct stm32_spi *spi, struct spi_device *spi_dev, struct spi_transfer *transfer)

    common setup to transfer a single spi_transfer either using DMA or interrupts.

    :param spi:
        *undescribed*
    :type spi: struct stm32_spi \*

    :param spi_dev:
        *undescribed*
    :type spi_dev: struct spi_device \*

    :param transfer:
        *undescribed*
    :type transfer: struct spi_transfer \*

.. _`stm32_spi_transfer_one`:

stm32_spi_transfer_one
======================

.. c:function:: int stm32_spi_transfer_one(struct spi_master *master, struct spi_device *spi_dev, struct spi_transfer *transfer)

    transfer a single spi_transfer

    :param master:
        *undescribed*
    :type master: struct spi_master \*

    :param spi_dev:
        *undescribed*
    :type spi_dev: struct spi_device \*

    :param transfer:
        *undescribed*
    :type transfer: struct spi_transfer \*

.. _`stm32_spi_transfer_one.description`:

Description
-----------

It must return 0 if the transfer is finished or 1 if the transfer is still
in progress.

.. _`stm32_spi_unprepare_msg`:

stm32_spi_unprepare_msg
=======================

.. c:function:: int stm32_spi_unprepare_msg(struct spi_master *master, struct spi_message *msg)

    relax the hardware

    :param master:
        *undescribed*
    :type master: struct spi_master \*

    :param msg:
        *undescribed*
    :type msg: struct spi_message \*

.. _`stm32_spi_unprepare_msg.description`:

Description
-----------

Normally, if TSIZE has been configured, we should relax the hardware at the
reception of the EOT interrupt. But in case of error, EOT will not be
raised. So the subsystem unprepare_message call allows us to properly
complete the transfer from an hardware point of view.

.. _`stm32_spi_config`:

stm32_spi_config
================

.. c:function:: int stm32_spi_config(struct stm32_spi *spi)

    Configure SPI controller as SPI master

    :param spi:
        *undescribed*
    :type spi: struct stm32_spi \*

.. This file was automatic generated / don't edit.

