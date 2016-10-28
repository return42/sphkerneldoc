.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-pl022.c

.. _`vendor_data`:

struct vendor_data
==================

.. c:type:: struct vendor_data

    vendor-specific config parameters for PL022 derivates

.. _`vendor_data.definition`:

Definition
----------

.. code-block:: c

    struct vendor_data {
        int fifodepth;
        int max_bpw;
        bool unidir;
        bool extended_cr;
        bool pl023;
        bool loopback;
        bool internal_cs_ctrl;
    }

.. _`vendor_data.members`:

Members
-------

fifodepth
    depth of FIFOs (both)

max_bpw
    maximum number of bits per word

unidir
    supports unidirection transfers

extended_cr
    32 bit wide control register 0 with extra
    features and extra features in CR1 as found in the ST variants

pl023
    supports a subset of the ST extensions called "PL023"

loopback
    *undescribed*

internal_cs_ctrl
    supports chip select control register

.. _`pl022`:

struct pl022
============

.. c:type:: struct pl022

    This is the private SSP driver data structure

.. _`pl022.definition`:

Definition
----------

.. code-block:: c

    struct pl022 {
        struct amba_device *adev;
        struct vendor_data *vendor;
        resource_size_t phybase;
        void __iomem *virtbase;
        struct clk *clk;
        struct spi_master *master;
        struct pl022_ssp_controller *master_info;
        struct tasklet_struct pump_transfers;
        struct spi_message *cur_msg;
        struct spi_transfer *cur_transfer;
        struct chip_data *cur_chip;
        bool next_msg_cs_active;
        void *tx;
        void *tx_end;
        void *rx;
        void *rx_end;
        enum ssp_reading read;
        enum ssp_writing write;
        u32 exp_fifo_level;
        enum ssp_rx_level_trig rx_lev_trig;
        enum ssp_tx_level_trig tx_lev_trig;
    #ifdef CONFIG_DMA_ENGINE
        struct dma_chan *dma_rx_channel;
        struct dma_chan *dma_tx_channel;
        struct sg_table sgt_rx;
        struct sg_table sgt_tx;
        char *dummypage;
        bool dma_running;
    #endif
        int cur_cs;
        int *chipselects;
    }

.. _`pl022.members`:

Members
-------

adev
    AMBA device model hookup

vendor
    vendor data for the IP block

phybase
    the physical memory where the SSP device resides

virtbase
    the virtual memory where the SSP is mapped

clk
    outgoing clock "SPICLK" for the SPI bus

master
    SPI framework hookup

master_info
    controller-specific data from machine setup

pump_transfers
    Tasklet used in Interrupt Transfer mode

cur_msg
    Pointer to current spi_message being processed

cur_transfer
    Pointer to current spi_transfer

cur_chip
    pointer to current clients chip(assigned from controller_state)

next_msg_cs_active
    the next message in the queue has been examined
    and it was found that it uses the same chip select as the previous
    message, so we left it active after the previous transfer, and it's
    active already.

tx
    current position in TX buffer to be read

tx_end
    end position in TX buffer to be read

rx
    current position in RX buffer to be written

rx_end
    end position in RX buffer to be written

read
    the type of read currently going on

write
    the type of write currently going on

exp_fifo_level
    expected FIFO level

rx_lev_trig
    *undescribed*

tx_lev_trig
    *undescribed*

dma_rx_channel
    optional channel for RX DMA

dma_tx_channel
    optional channel for TX DMA

sgt_rx
    scattertable for the RX transfer

sgt_tx
    scattertable for the TX transfer

dummypage
    a dummy page used for driving data on the bus with DMA

dma_running
    *undescribed*

cur_cs
    current chip select (gpio)

chipselects
    list of chipselects (gpios)

.. _`chip_data`:

struct chip_data
================

.. c:type:: struct chip_data

    To maintain runtime state of SSP for each client chip

.. _`chip_data.definition`:

Definition
----------

.. code-block:: c

    struct chip_data {
        u32 cr0;
        u16 cr1;
        u16 dmacr;
        u16 cpsr;
        u8 n_bytes;
        bool enable_dma;
        enum ssp_reading read;
        enum ssp_writing write;
        void (*cs_control)(u32 command);
        int xfer_type;
    }

.. _`chip_data.members`:

Members
-------

cr0
    Value of control register CR0 of SSP - on later ST variants this
    register is 32 bits wide rather than just 16

cr1
    Value of control register CR1 of SSP

dmacr
    Value of DMA control Register of SSP

cpsr
    Value of Clock prescale register

n_bytes
    how many bytes(power of 2) reqd for a given data width of client

enable_dma
    Whether to enable DMA or not

read
    function ptr to be used to read when doing xfer for this chip

write
    function ptr to be used to write when doing xfer for this chip

cs_control
    chip select callback provided by chip

xfer_type
    polling/interrupt/DMA

.. _`chip_data.description`:

Description
-----------

Runtime state of the SSP controller, maintained per chip,
This would be set according to the current message that would be served

.. _`null_cs_control`:

null_cs_control
===============

.. c:function:: void null_cs_control(u32 command)

    Dummy chip select function

    :param u32 command:
        select/delect the chip

.. _`null_cs_control.description`:

Description
-----------

If no chip select function is provided by client this is used as dummy
chip select

.. _`internal_cs_control`:

internal_cs_control
===================

.. c:function:: void internal_cs_control(struct pl022 *pl022, u32 command)

    Control chip select signals via SSP_CSR.

    :param struct pl022 \*pl022:
        SSP driver private data structure

    :param u32 command:
        select/delect the chip

.. _`internal_cs_control.description`:

Description
-----------

Used on controller with internal chip select control via SSP_CSR register
(vendor extension). Each of the 5 LSB in the register controls one chip
select signal.

.. _`giveback`:

giveback
========

.. c:function:: void giveback(struct pl022 *pl022)

    current spi_message is over, schedule next message and call callback of this message. Assumes that caller already set message->status; dma and pio irqs are blocked

    :param struct pl022 \*pl022:
        SSP driver private data structure

.. _`flush`:

flush
=====

.. c:function:: int flush(struct pl022 *pl022)

    flush the FIFO to reach a clean state

    :param struct pl022 \*pl022:
        SSP driver private data structure

.. _`restore_state`:

restore_state
=============

.. c:function:: void restore_state(struct pl022 *pl022)

    Load configuration of current chip

    :param struct pl022 \*pl022:
        SSP driver private data structure

.. _`load_ssp_default_config`:

load_ssp_default_config
=======================

.. c:function:: void load_ssp_default_config(struct pl022 *pl022)

    Load default configuration for SSP

    :param struct pl022 \*pl022:
        SSP driver private data structure

.. _`readwriter`:

readwriter
==========

.. c:function:: void readwriter(struct pl022 *pl022)

    set in pl022.

    :param struct pl022 \*pl022:
        *undescribed*

.. _`next_transfer`:

next_transfer
=============

.. c:function:: void *next_transfer(struct pl022 *pl022)

    Move to the Next transfer in the current spi message

    :param struct pl022 \*pl022:
        SSP driver private data structure

.. _`next_transfer.description`:

Description
-----------

This function moves though the linked list of spi transfers in the
current spi message and returns with the state of current spi
message i.e whether its last transfer is done(STATE_DONE) or
Next transfer is ready(STATE_RUNNING)

.. _`configure_dma`:

configure_dma
=============

.. c:function:: int configure_dma(struct pl022 *pl022)

    configures the channels for the next transfer

    :param struct pl022 \*pl022:
        SSP driver's private data structure

.. _`pl022_interrupt_handler`:

pl022_interrupt_handler
=======================

.. c:function:: irqreturn_t pl022_interrupt_handler(int irq, void *dev_id)

    Interrupt handler for SSP controller

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        *undescribed*

.. _`pl022_interrupt_handler.description`:

Description
-----------

This function handles interrupts generated for an interrupt based transfer.
If a receive overrun (ROR) interrupt is there then we disable SSP, flag the
current message's state as STATE_ERROR and schedule the tasklet
pump_transfers which will do the postprocessing of the current message by
calling \ :c:func:`giveback`\ . Otherwise it reads data from RX FIFO till there is no
more data, and writes data in TX FIFO till it is not full. If we complete
the transfer we move to the next transfer and schedule the tasklet.

.. _`set_up_next_transfer`:

set_up_next_transfer
====================

.. c:function:: int set_up_next_transfer(struct pl022 *pl022, struct spi_transfer *transfer)

    send out on the SPI bus.

    :param struct pl022 \*pl022:
        *undescribed*

    :param struct spi_transfer \*transfer:
        *undescribed*

.. _`pump_transfers`:

pump_transfers
==============

.. c:function:: void pump_transfers(unsigned long data)

    Tasklet function which schedules next transfer when running in interrupt or DMA transfer mode.

    :param unsigned long data:
        SSP driver private data structure

.. _`pl022_setup`:

pl022_setup
===========

.. c:function:: int pl022_setup(struct spi_device *spi)

    setup function registered to SPI master framework

    :param struct spi_device \*spi:
        spi device which is requesting setup

.. _`pl022_setup.description`:

Description
-----------

This function is registered to the SPI framework for this SPI master
controller. If it is the first time when setup is called by this device,
this function will initialize the runtime state for this chip and save
the same in the device structure. Else it will update the runtime info
with the updated chip info. Nothing is really being written to the
controller hardware here, that is not done until the actual transfer
commence.

.. _`pl022_cleanup`:

pl022_cleanup
=============

.. c:function:: void pl022_cleanup(struct spi_device *spi)

    cleanup function registered to SPI master framework

    :param struct spi_device \*spi:
        spi device which is requesting cleanup

.. _`pl022_cleanup.description`:

Description
-----------

This function is registered to the SPI framework for this SPI master
controller. It will free the runtime state of chip.

.. This file was automatic generated / don't edit.

