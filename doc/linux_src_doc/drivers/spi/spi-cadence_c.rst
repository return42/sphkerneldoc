.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-cadence.c

.. _`cdns_spi`:

struct cdns_spi
===============

.. c:type:: struct cdns_spi

    This definition defines spi driver instance

.. _`cdns_spi.definition`:

Definition
----------

.. code-block:: c

    struct cdns_spi {
        void __iomem *regs;
        struct clk *ref_clk;
        struct clk *pclk;
        u32 speed_hz;
        const u8 *txbuf;
        u8 *rxbuf;
        int tx_bytes;
        int rx_bytes;
        u8 dev_busy;
        u32 is_decoded_cs;
    }

.. _`cdns_spi.members`:

Members
-------

regs
    Virtual address of the SPI controller registers

ref_clk
    Pointer to the peripheral clock

pclk
    Pointer to the APB clock

speed_hz
    Current SPI bus clock speed in Hz

txbuf
    Pointer to the TX buffer

rxbuf
    Pointer to the RX buffer

tx_bytes
    Number of bytes left to transfer

rx_bytes
    Number of bytes requested

dev_busy
    Device busy flag

is_decoded_cs
    Flag for decoder property set or not

.. _`cdns_spi_init_hw`:

cdns_spi_init_hw
================

.. c:function:: void cdns_spi_init_hw(struct cdns_spi *xspi)

    Initialize the hardware and configure the SPI controller

    :param struct cdns_spi \*xspi:
        Pointer to the cdns_spi structure

.. _`cdns_spi_init_hw.description`:

Description
-----------

On reset the SPI controller is configured to be in master mode, baud rate
divisor is set to 4, threshold value for TX FIFO not full interrupt is set
to 1 and size of the word to be transferred as 8 bit.
This function initializes the SPI controller to disable and clear all the
interrupts, enable manual slave select and manual start, deselect all the
chip select lines, and enable the SPI controller.

.. _`cdns_spi_chipselect`:

cdns_spi_chipselect
===================

.. c:function:: void cdns_spi_chipselect(struct spi_device *spi, bool is_high)

    Select or deselect the chip select line

    :param struct spi_device \*spi:
        Pointer to the spi_device structure

    :param bool is_high:
        Select(0) or deselect (1) the chip select line

.. _`cdns_spi_config_clock_mode`:

cdns_spi_config_clock_mode
==========================

.. c:function:: void cdns_spi_config_clock_mode(struct spi_device *spi)

    Sets clock polarity and phase

    :param struct spi_device \*spi:
        Pointer to the spi_device structure

.. _`cdns_spi_config_clock_mode.description`:

Description
-----------

Sets the requested clock polarity and phase.

.. _`cdns_spi_config_clock_freq`:

cdns_spi_config_clock_freq
==========================

.. c:function:: void cdns_spi_config_clock_freq(struct spi_device *spi, struct spi_transfer *transfer)

    Sets clock frequency

    :param struct spi_device \*spi:
        Pointer to the spi_device structure

    :param struct spi_transfer \*transfer:
        Pointer to the spi_transfer structure which provides
        information about next transfer setup parameters

.. _`cdns_spi_config_clock_freq.description`:

Description
-----------

Sets the requested clock frequency.

.. _`cdns_spi_config_clock_freq.note`:

Note
----

If the requested frequency is not an exact match with what can be
obtained using the prescalar value the driver sets the clock frequency which
is lower than the requested frequency (maximum lower) for the transfer. If
the requested frequency is higher or lower than that is supported by the SPI
controller the driver will set the highest or lowest frequency supported by
controller.

.. _`cdns_spi_setup_transfer`:

cdns_spi_setup_transfer
=======================

.. c:function:: int cdns_spi_setup_transfer(struct spi_device *spi, struct spi_transfer *transfer)

    Configure SPI controller for specified transfer

    :param struct spi_device \*spi:
        Pointer to the spi_device structure

    :param struct spi_transfer \*transfer:
        Pointer to the spi_transfer structure which provides
        information about next transfer setup parameters

.. _`cdns_spi_setup_transfer.description`:

Description
-----------

Sets the operational mode of SPI controller for the next SPI transfer and
sets the requested clock frequency.

.. _`cdns_spi_setup_transfer.return`:

Return
------

Always 0

.. _`cdns_spi_fill_tx_fifo`:

cdns_spi_fill_tx_fifo
=====================

.. c:function:: void cdns_spi_fill_tx_fifo(struct cdns_spi *xspi)

    Fills the TX FIFO with as many bytes as possible

    :param struct cdns_spi \*xspi:
        Pointer to the cdns_spi structure

.. _`cdns_spi_irq`:

cdns_spi_irq
============

.. c:function:: irqreturn_t cdns_spi_irq(int irq, void *dev_id)

    Interrupt service routine of the SPI controller

    :param int irq:
        IRQ number

    :param void \*dev_id:
        Pointer to the xspi structure

.. _`cdns_spi_irq.description`:

Description
-----------

This function handles TX empty and Mode Fault interrupts only.
On TX empty interrupt this function reads the received data from RX FIFO and
fills the TX FIFO if there is any data remaining to be transferred.
On Mode Fault interrupt this function indicates that transfer is completed,
the SPI subsystem will identify the error as the remaining bytes to be
transferred is non-zero.

.. _`cdns_spi_irq.return`:

Return
------

IRQ_HANDLED when handled; IRQ_NONE otherwise.

.. _`cdns_transfer_one`:

cdns_transfer_one
=================

.. c:function:: int cdns_transfer_one(struct spi_master *master, struct spi_device *spi, struct spi_transfer *transfer)

    Initiates the SPI transfer

    :param struct spi_master \*master:
        Pointer to spi_master structure

    :param struct spi_device \*spi:
        Pointer to the spi_device structure

    :param struct spi_transfer \*transfer:
        Pointer to the spi_transfer structure which provides
        information about next transfer parameters

.. _`cdns_transfer_one.description`:

Description
-----------

This function fills the TX FIFO, starts the SPI transfer and
returns a positive transfer count so that core will wait for completion.

.. _`cdns_transfer_one.return`:

Return
------

Number of bytes transferred in the last transfer

.. _`cdns_prepare_transfer_hardware`:

cdns_prepare_transfer_hardware
==============================

.. c:function:: int cdns_prepare_transfer_hardware(struct spi_master *master)

    Prepares hardware for transfer.

    :param struct spi_master \*master:
        Pointer to the spi_master structure which provides
        information about the controller.

.. _`cdns_prepare_transfer_hardware.description`:

Description
-----------

This function enables SPI master controller.

.. _`cdns_prepare_transfer_hardware.return`:

Return
------

0 always

.. _`cdns_unprepare_transfer_hardware`:

cdns_unprepare_transfer_hardware
================================

.. c:function:: int cdns_unprepare_transfer_hardware(struct spi_master *master)

    Relaxes hardware after transfer

    :param struct spi_master \*master:
        Pointer to the spi_master structure which provides
        information about the controller.

.. _`cdns_unprepare_transfer_hardware.description`:

Description
-----------

This function disables the SPI master controller.

.. _`cdns_unprepare_transfer_hardware.return`:

Return
------

0 always

.. _`cdns_spi_probe`:

cdns_spi_probe
==============

.. c:function:: int cdns_spi_probe(struct platform_device *pdev)

    Probe method for the SPI driver

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`cdns_spi_probe.description`:

Description
-----------

This function initializes the driver data structures and the hardware.

.. _`cdns_spi_probe.return`:

Return
------

0 on success and error value on error

.. _`cdns_spi_remove`:

cdns_spi_remove
===============

.. c:function:: int cdns_spi_remove(struct platform_device *pdev)

    Remove method for the SPI driver

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`cdns_spi_remove.description`:

Description
-----------

This function is called if a device is physically removed from the system or
if the driver module is being unloaded. It frees all resources allocated to
the device.

.. _`cdns_spi_remove.return`:

Return
------

0 on success and error value on error

.. _`cdns_spi_suspend`:

cdns_spi_suspend
================

.. c:function:: int __maybe_unused cdns_spi_suspend(struct device *dev)

    Suspend method for the SPI driver

    :param struct device \*dev:
        Address of the platform_device structure

.. _`cdns_spi_suspend.description`:

Description
-----------

This function disables the SPI controller and
changes the driver state to "suspend"

.. _`cdns_spi_suspend.return`:

Return
------

0 on success and error value on error

.. _`cdns_spi_resume`:

cdns_spi_resume
===============

.. c:function:: int __maybe_unused cdns_spi_resume(struct device *dev)

    Resume method for the SPI driver

    :param struct device \*dev:
        Address of the platform_device structure

.. _`cdns_spi_resume.description`:

Description
-----------

This function changes the driver state to "ready"

.. _`cdns_spi_resume.return`:

Return
------

0 on success and error value on error

.. _`cnds_runtime_resume`:

cnds_runtime_resume
===================

.. c:function:: int __maybe_unused cnds_runtime_resume(struct device *dev)

    Runtime resume method for the SPI driver

    :param struct device \*dev:
        Address of the platform_device structure

.. _`cnds_runtime_resume.description`:

Description
-----------

This function enables the clocks

.. _`cnds_runtime_resume.return`:

Return
------

0 on success and error value on error

.. _`cnds_runtime_suspend`:

cnds_runtime_suspend
====================

.. c:function:: int __maybe_unused cnds_runtime_suspend(struct device *dev)

    Runtime suspend method for the SPI driver

    :param struct device \*dev:
        Address of the platform_device structure

.. _`cnds_runtime_suspend.description`:

Description
-----------

This function disables the clocks

.. _`cnds_runtime_suspend.return`:

Return
------

Always 0

.. This file was automatic generated / don't edit.

