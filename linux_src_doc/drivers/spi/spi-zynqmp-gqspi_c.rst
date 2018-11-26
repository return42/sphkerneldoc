.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-zynqmp-gqspi.c

.. _`zynqmp_qspi`:

struct zynqmp_qspi
==================

.. c:type:: struct zynqmp_qspi

    Defines qspi driver instance

.. _`zynqmp_qspi.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_qspi {
        void __iomem *regs;
        struct clk *refclk;
        struct clk *pclk;
        int irq;
        struct device *dev;
        const void *txbuf;
        void *rxbuf;
        int bytes_to_transfer;
        int bytes_to_receive;
        u32 genfifocs;
        u32 genfifobus;
        u32 dma_rx_bytes;
        dma_addr_t dma_addr;
        u32 genfifoentry;
        enum mode_type mode;
    }

.. _`zynqmp_qspi.members`:

Members
-------

regs
    Virtual address of the QSPI controller registers

refclk
    Pointer to the peripheral clock

pclk
    Pointer to the APB clock

irq
    IRQ number

dev
    Pointer to struct device

txbuf
    Pointer to the TX buffer

rxbuf
    Pointer to the RX buffer

bytes_to_transfer
    Number of bytes left to transfer

bytes_to_receive
    Number of bytes left to receive

genfifocs
    Used for chip select

genfifobus
    Used to select the upper or lower bus

dma_rx_bytes
    Remaining bytes to receive by DMA mode

dma_addr
    DMA address after mapping the kernel buffer

genfifoentry
    Used for storing the genfifoentry instruction.

mode
    Defines the mode in which QSPI is operating

.. _`zynqmp_gqspi_read`:

zynqmp_gqspi_read
=================

.. c:function:: u32 zynqmp_gqspi_read(struct zynqmp_qspi *xqspi, u32 offset)

    For GQSPI controller read operation

    :param xqspi:
        Pointer to the zynqmp_qspi structure
    :type xqspi: struct zynqmp_qspi \*

    :param offset:
        Offset from where to read
    :type offset: u32

.. _`zynqmp_gqspi_write`:

zynqmp_gqspi_write
==================

.. c:function:: void zynqmp_gqspi_write(struct zynqmp_qspi *xqspi, u32 offset, u32 val)

    For GQSPI controller write operation

    :param xqspi:
        Pointer to the zynqmp_qspi structure
    :type xqspi: struct zynqmp_qspi \*

    :param offset:
        Offset where to write
    :type offset: u32

    :param val:
        Value to be written
    :type val: u32

.. _`zynqmp_gqspi_selectslave`:

zynqmp_gqspi_selectslave
========================

.. c:function:: void zynqmp_gqspi_selectslave(struct zynqmp_qspi *instanceptr, u8 slavecs, u8 slavebus)

    For selection of slave device

    :param instanceptr:
        Pointer to the zynqmp_qspi structure
    :type instanceptr: struct zynqmp_qspi \*

    :param slavecs:
        *undescribed*
    :type slavecs: u8

    :param slavebus:
        *undescribed*
    :type slavebus: u8

.. _`zynqmp_qspi_init_hw`:

zynqmp_qspi_init_hw
===================

.. c:function:: void zynqmp_qspi_init_hw(struct zynqmp_qspi *xqspi)

    Initialize the hardware

    :param xqspi:
        Pointer to the zynqmp_qspi structure
    :type xqspi: struct zynqmp_qspi \*

.. _`zynqmp_qspi_init_hw.description`:

Description
-----------

The default settings of the QSPI controller's configurable parameters on
reset are
- Master mode
- TX threshold set to 1
- RX threshold set to 1
- Flash memory interface mode enabled
This function performs the following actions
- Disable and clear all the interrupts
- Enable manual slave select
- Enable manual start
- Deselect all the chip select lines
- Set the little endian mode of TX FIFO and
- Enable the QSPI controller

.. _`zynqmp_qspi_copy_read_data`:

zynqmp_qspi_copy_read_data
==========================

.. c:function:: void zynqmp_qspi_copy_read_data(struct zynqmp_qspi *xqspi, ulong data, u8 size)

    Copy data to RX buffer

    :param xqspi:
        Pointer to the zynqmp_qspi structure
    :type xqspi: struct zynqmp_qspi \*

    :param data:
        The variable where data is stored
    :type data: ulong

    :param size:
        Number of bytes to be copied from data to RX buffer
    :type size: u8

.. _`zynqmp_prepare_transfer_hardware`:

zynqmp_prepare_transfer_hardware
================================

.. c:function:: int zynqmp_prepare_transfer_hardware(struct spi_master *master)

    Prepares hardware for transfer.

    :param master:
        Pointer to the spi_master structure which provides
        information about the controller.
    :type master: struct spi_master \*

.. _`zynqmp_prepare_transfer_hardware.description`:

Description
-----------

This function enables SPI master controller.

.. _`zynqmp_prepare_transfer_hardware.return`:

Return
------

0 on success; error value otherwise

.. _`zynqmp_unprepare_transfer_hardware`:

zynqmp_unprepare_transfer_hardware
==================================

.. c:function:: int zynqmp_unprepare_transfer_hardware(struct spi_master *master)

    Relaxes hardware after transfer

    :param master:
        Pointer to the spi_master structure which provides
        information about the controller.
    :type master: struct spi_master \*

.. _`zynqmp_unprepare_transfer_hardware.description`:

Description
-----------

This function disables the SPI master controller.

.. _`zynqmp_unprepare_transfer_hardware.return`:

Return
------

Always 0

.. _`zynqmp_qspi_chipselect`:

zynqmp_qspi_chipselect
======================

.. c:function:: void zynqmp_qspi_chipselect(struct spi_device *qspi, bool is_high)

    Select or deselect the chip select line

    :param qspi:
        Pointer to the spi_device structure
    :type qspi: struct spi_device \*

    :param is_high:
        Select(0) or deselect (1) the chip select line
    :type is_high: bool

.. _`zynqmp_qspi_setup_transfer`:

zynqmp_qspi_setup_transfer
==========================

.. c:function:: int zynqmp_qspi_setup_transfer(struct spi_device *qspi, struct spi_transfer *transfer)

    Configure QSPI controller for specified transfer

    :param qspi:
        Pointer to the spi_device structure
    :type qspi: struct spi_device \*

    :param transfer:
        Pointer to the spi_transfer structure which provides
        information about next transfer setup parameters
    :type transfer: struct spi_transfer \*

.. _`zynqmp_qspi_setup_transfer.description`:

Description
-----------

Sets the operational mode of QSPI controller for the next QSPI transfer and
sets the requested clock frequency.

.. _`zynqmp_qspi_setup_transfer.return`:

Return
------

Always 0

.. _`zynqmp_qspi_setup_transfer.note`:

Note
----

If the requested frequency is not an exact match with what can be
obtained using the pre-scalar value, the driver sets the clock
frequency which is lower than the requested frequency (maximum lower)
for the transfer.

If the requested frequency is higher or lower than that is supported
by the QSPI controller the driver will set the highest or lowest
frequency supported by controller.

.. _`zynqmp_qspi_setup`:

zynqmp_qspi_setup
=================

.. c:function:: int zynqmp_qspi_setup(struct spi_device *qspi)

    Configure the QSPI controller

    :param qspi:
        Pointer to the spi_device structure
    :type qspi: struct spi_device \*

.. _`zynqmp_qspi_setup.description`:

Description
-----------

Sets the operational mode of QSPI controller for the next QSPI transfer,
baud rate and divisor value to setup the requested qspi clock.

.. _`zynqmp_qspi_setup.return`:

Return
------

0 on success; error value otherwise.

.. _`zynqmp_qspi_filltxfifo`:

zynqmp_qspi_filltxfifo
======================

.. c:function:: void zynqmp_qspi_filltxfifo(struct zynqmp_qspi *xqspi, int size)

    Fills the TX FIFO as long as there is room in the FIFO or the bytes required to be transmitted.

    :param xqspi:
        Pointer to the zynqmp_qspi structure
    :type xqspi: struct zynqmp_qspi \*

    :param size:
        Number of bytes to be copied from TX buffer to TX FIFO
    :type size: int

.. _`zynqmp_qspi_readrxfifo`:

zynqmp_qspi_readrxfifo
======================

.. c:function:: void zynqmp_qspi_readrxfifo(struct zynqmp_qspi *xqspi, u32 size)

    Fills the RX FIFO as long as there is room in the FIFO.

    :param xqspi:
        Pointer to the zynqmp_qspi structure
    :type xqspi: struct zynqmp_qspi \*

    :param size:
        Number of bytes to be copied from RX buffer to RX FIFO
    :type size: u32

.. _`zynqmp_process_dma_irq`:

zynqmp_process_dma_irq
======================

.. c:function:: void zynqmp_process_dma_irq(struct zynqmp_qspi *xqspi)

    Handler for DMA done interrupt of QSPI controller

    :param xqspi:
        zynqmp_qspi instance pointer
    :type xqspi: struct zynqmp_qspi \*

.. _`zynqmp_process_dma_irq.description`:

Description
-----------

This function handles DMA interrupt only.

.. _`zynqmp_qspi_irq`:

zynqmp_qspi_irq
===============

.. c:function:: irqreturn_t zynqmp_qspi_irq(int irq, void *dev_id)

    Interrupt service routine of the QSPI controller

    :param irq:
        IRQ number
    :type irq: int

    :param dev_id:
        Pointer to the xqspi structure
    :type dev_id: void \*

.. _`zynqmp_qspi_irq.description`:

Description
-----------

This function handles TX empty only.
On TX empty interrupt this function reads the received data from RX FIFO
and fills the TX FIFO if there is any data remaining to be transferred.

.. _`zynqmp_qspi_irq.return`:

Return
------

IRQ_HANDLED when interrupt is handled
IRQ_NONE otherwise.

.. _`zynqmp_qspi_selectspimode`:

zynqmp_qspi_selectspimode
=========================

.. c:function:: u32 zynqmp_qspi_selectspimode(struct zynqmp_qspi *xqspi, u8 spimode)

    Selects SPI mode - x1 or x2 or x4.

    :param xqspi:
        xqspi is a pointer to the GQSPI instance
    :type xqspi: struct zynqmp_qspi \*

    :param spimode:
        spimode - SPI or DUAL or QUAD.
    :type spimode: u8

.. _`zynqmp_qspi_selectspimode.return`:

Return
------

Mask to set desired SPI mode in GENFIFO entry.

.. _`zynq_qspi_setuprxdma`:

zynq_qspi_setuprxdma
====================

.. c:function:: void zynq_qspi_setuprxdma(struct zynqmp_qspi *xqspi)

    This function sets up the RX DMA operation

    :param xqspi:
        xqspi is a pointer to the GQSPI instance.
    :type xqspi: struct zynqmp_qspi \*

.. _`zynqmp_qspi_txrxsetup`:

zynqmp_qspi_txrxsetup
=====================

.. c:function:: void zynqmp_qspi_txrxsetup(struct zynqmp_qspi *xqspi, struct spi_transfer *transfer, u32 *genfifoentry)

    This function checks the TX/RX buffers in the transfer and sets up the GENFIFO entries, TX FIFO as required.

    :param xqspi:
        xqspi is a pointer to the GQSPI instance.
    :type xqspi: struct zynqmp_qspi \*

    :param transfer:
        It is a pointer to the structure containing transfer data.
    :type transfer: struct spi_transfer \*

    :param genfifoentry:
        genfifoentry is pointer to the variable in which
        GENFIFO mask is returned to calling function
    :type genfifoentry: u32 \*

.. _`zynqmp_qspi_start_transfer`:

zynqmp_qspi_start_transfer
==========================

.. c:function:: int zynqmp_qspi_start_transfer(struct spi_master *master, struct spi_device *qspi, struct spi_transfer *transfer)

    Initiates the QSPI transfer

    :param master:
        Pointer to the spi_master structure which provides
        information about the controller.
    :type master: struct spi_master \*

    :param qspi:
        Pointer to the spi_device structure
    :type qspi: struct spi_device \*

    :param transfer:
        Pointer to the spi_transfer structure which provide information
        about next transfer parameters
    :type transfer: struct spi_transfer \*

.. _`zynqmp_qspi_start_transfer.description`:

Description
-----------

This function fills the TX FIFO, starts the QSPI transfer, and waits for the
transfer to be completed.

.. _`zynqmp_qspi_start_transfer.return`:

Return
------

Number of bytes transferred in the last transfer

.. _`zynqmp_qspi_suspend`:

zynqmp_qspi_suspend
===================

.. c:function:: int __maybe_unused zynqmp_qspi_suspend(struct device *dev)

    Suspend method for the QSPI driver

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`zynqmp_qspi_suspend.description`:

Description
-----------

This function stops the QSPI driver queue and disables the QSPI controller

.. _`zynqmp_qspi_suspend.return`:

Return
------

Always 0

.. _`zynqmp_qspi_resume`:

zynqmp_qspi_resume
==================

.. c:function:: int __maybe_unused zynqmp_qspi_resume(struct device *dev)

    Resume method for the QSPI driver

    :param dev:
        Address of the platform_device structure
    :type dev: struct device \*

.. _`zynqmp_qspi_resume.description`:

Description
-----------

The function starts the QSPI driver queue and initializes the QSPI
controller

.. _`zynqmp_qspi_resume.return`:

Return
------

0 on success; error value otherwise

.. _`zynqmp_runtime_suspend`:

zynqmp_runtime_suspend
======================

.. c:function:: int __maybe_unused zynqmp_runtime_suspend(struct device *dev)

    Runtime suspend method for the SPI driver

    :param dev:
        Address of the platform_device structure
    :type dev: struct device \*

.. _`zynqmp_runtime_suspend.description`:

Description
-----------

This function disables the clocks

.. _`zynqmp_runtime_suspend.return`:

Return
------

Always 0

.. _`zynqmp_runtime_resume`:

zynqmp_runtime_resume
=====================

.. c:function:: int __maybe_unused zynqmp_runtime_resume(struct device *dev)

    Runtime resume method for the SPI driver

    :param dev:
        Address of the platform_device structure
    :type dev: struct device \*

.. _`zynqmp_runtime_resume.description`:

Description
-----------

This function enables the clocks

.. _`zynqmp_runtime_resume.return`:

Return
------

0 on success and error value on error

.. _`zynqmp_qspi_probe`:

zynqmp_qspi_probe
=================

.. c:function:: int zynqmp_qspi_probe(struct platform_device *pdev)

    Probe method for the QSPI driver

    :param pdev:
        Pointer to the platform_device structure
    :type pdev: struct platform_device \*

.. _`zynqmp_qspi_probe.description`:

Description
-----------

This function initializes the driver data structures and the hardware.

.. _`zynqmp_qspi_probe.return`:

Return
------

0 on success; error value otherwise

.. _`zynqmp_qspi_remove`:

zynqmp_qspi_remove
==================

.. c:function:: int zynqmp_qspi_remove(struct platform_device *pdev)

    Remove method for the QSPI driver

    :param pdev:
        Pointer to the platform_device structure
    :type pdev: struct platform_device \*

.. _`zynqmp_qspi_remove.description`:

Description
-----------

This function is called if a device is physically removed from the system or
if the driver module is being unloaded. It frees all resources allocated to
the device.

.. _`zynqmp_qspi_remove.return`:

Return
------

0 Always

.. This file was automatic generated / don't edit.

