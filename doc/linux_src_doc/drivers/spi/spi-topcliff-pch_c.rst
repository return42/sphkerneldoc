.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-topcliff-pch.c

.. _`pch_spi_data`:

struct pch_spi_data
===================

.. c:type:: struct pch_spi_data

    Holds the SPI channel specific details

.. _`pch_spi_data.definition`:

Definition
----------

.. code-block:: c

    struct pch_spi_data {
        void __iomem *io_remap_addr;
        unsigned long io_base_addr;
        struct spi_master *master;
        struct work_struct work;
        struct workqueue_struct *wk;
        wait_queue_head_t wait;
        u8 transfer_complete;
        u8 bcurrent_msg_processing;
        spinlock_t lock;
        struct list_head queue;
        u8 status;
        u32 bpw_len;
        u8 transfer_active;
        u32 tx_index;
        u32 rx_index;
        u16 *pkt_tx_buff;
        u16 *pkt_rx_buff;
        u8 n_curnt_chip;
        struct spi_device *current_chip;
        struct spi_message *current_msg;
        struct spi_transfer *cur_trans;
        struct pch_spi_board_data *board_dat;
        struct platform_device *plat_dev;
        int ch;
        struct pch_spi_dma_ctrl dma;
        int use_dma;
        u8 irq_reg_sts;
        int save_total_len;
    }

.. _`pch_spi_data.members`:

Members
-------

io_remap_addr
    The remapped PCI base address

io_base_addr
    *undescribed*

master
    Pointer to the SPI master structure

work
    Reference to work queue handler

wk
    Workqueue for carrying out execution of the
    requests

wait
    Wait queue for waking up upon receiving an
    interrupt.

transfer_complete
    Status of SPI Transfer

bcurrent_msg_processing
    Status flag for message processing

lock
    Lock for protecting this structure

queue
    SPI Message queue

status
    Status of the SPI driver

bpw_len
    Length of data to be transferred in bits per
    word

transfer_active
    Flag showing active transfer

tx_index
    Transmit data count; for bookkeeping during
    transfer

rx_index
    Buffer for Received data

pkt_tx_buff
    *undescribed*

pkt_rx_buff
    *undescribed*

n_curnt_chip
    The chip number that this SPI driver currently
    operates on

current_chip
    Reference to the current chip that this SPI
    driver currently operates on

current_msg
    The current message that this SPI driver is
    handling

cur_trans
    The current transfer that this SPI driver is
    handling

board_dat
    Reference to the SPI device data structure

plat_dev
    platform_device structure

ch
    SPI channel number

dma
    *undescribed*

use_dma
    *undescribed*

irq_reg_sts
    Status of IRQ registration

save_total_len
    *undescribed*

.. _`pch_spi_board_data`:

struct pch_spi_board_data
=========================

.. c:type:: struct pch_spi_board_data

    Holds the SPI device specific details

.. _`pch_spi_board_data.definition`:

Definition
----------

.. code-block:: c

    struct pch_spi_board_data {
        struct pci_dev *pdev;
        u8 suspend_sts;
        int num;
    }

.. _`pch_spi_board_data.members`:

Members
-------

pdev
    Pointer to the PCI device

suspend_sts
    Status of suspend

num
    The number of SPI device instance

.. _`pch_spi_writereg`:

pch_spi_writereg
================

.. c:function:: void pch_spi_writereg(struct spi_master *master, int idx, u32 val)

    Performs  register writes

    :param struct spi_master \*master:
        Pointer to struct spi_master.

    :param int idx:
        Register offset.

    :param u32 val:
        Value to be written to register.

.. _`pch_spi_readreg`:

pch_spi_readreg
===============

.. c:function:: u32 pch_spi_readreg(struct spi_master *master, int idx)

    Performs register reads

    :param struct spi_master \*master:
        Pointer to struct spi_master.

    :param int idx:
        Register offset.

.. _`pch_spi_clear_fifo`:

pch_spi_clear_fifo
==================

.. c:function:: void pch_spi_clear_fifo(struct spi_master *master)

    Clears the Transmit and Receive FIFOs

    :param struct spi_master \*master:
        Pointer to struct spi_master.

.. _`pch_spi_handler`:

pch_spi_handler
===============

.. c:function:: irqreturn_t pch_spi_handler(int irq, void *dev_id)

    Interrupt handler

    :param int irq:
        The interrupt number.

    :param void \*dev_id:
        Pointer to struct pch_spi_board_data.

.. _`pch_spi_set_baud_rate`:

pch_spi_set_baud_rate
=====================

.. c:function:: void pch_spi_set_baud_rate(struct spi_master *master, u32 speed_hz)

    Sets SPBR field in SPBRR

    :param struct spi_master \*master:
        Pointer to struct spi_master.

    :param u32 speed_hz:
        Baud rate.

.. _`pch_spi_set_bits_per_word`:

pch_spi_set_bits_per_word
=========================

.. c:function:: void pch_spi_set_bits_per_word(struct spi_master *master, u8 bits_per_word)

    Sets SIZE field in SPBRR

    :param struct spi_master \*master:
        Pointer to struct spi_master.

    :param u8 bits_per_word:
        Bits per word for SPI transfer.

.. _`pch_spi_setup_transfer`:

pch_spi_setup_transfer
======================

.. c:function:: void pch_spi_setup_transfer(struct spi_device *spi)

    Configures the PCH SPI hardware for transfer

    :param struct spi_device \*spi:
        Pointer to struct spi_device.

.. _`pch_spi_reset`:

pch_spi_reset
=============

.. c:function:: void pch_spi_reset(struct spi_master *master)

    Clears SPI registers

    :param struct spi_master \*master:
        Pointer to struct spi_master.

.. This file was automatic generated / don't edit.

