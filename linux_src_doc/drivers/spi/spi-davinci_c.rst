.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-davinci.c

.. _`davinci_spi_get_prescale`:

davinci_spi_get_prescale
========================

.. c:function:: int davinci_spi_get_prescale(struct davinci_spi *dspi, u32 max_speed_hz)

    Calculates the correct prescale value

    :param dspi:
        *undescribed*
    :type dspi: struct davinci_spi \*

    :param max_speed_hz:
        *undescribed*
    :type max_speed_hz: u32

.. _`davinci_spi_get_prescale.description`:

Description
-----------

This function calculates the prescale value that generates a clock rate
less than or equal to the specified maximum.

.. _`davinci_spi_get_prescale.return`:

Return
------

calculated prescale value for easy programming into SPI registers
or negative error number if valid prescalar cannot be updated.

.. _`davinci_spi_setup_transfer`:

davinci_spi_setup_transfer
==========================

.. c:function:: int davinci_spi_setup_transfer(struct spi_device *spi, struct spi_transfer *t)

    This functions will determine transfer method

    :param spi:
        spi device on which data transfer to be done
    :type spi: struct spi_device \*

    :param t:
        spi transfer in which transfer info is filled
    :type t: struct spi_transfer \*

.. _`davinci_spi_setup_transfer.description`:

Description
-----------

This function determines data transfer method (8/16/32 bit transfer).
It will also set the SPI Clock Control register according to
SPI slave device freq.

.. _`davinci_spi_setup`:

davinci_spi_setup
=================

.. c:function:: int davinci_spi_setup(struct spi_device *spi)

    This functions will set default transfer method

    :param spi:
        spi device on which data transfer to be done
    :type spi: struct spi_device \*

.. _`davinci_spi_setup.description`:

Description
-----------

This functions sets the default transfer method.

.. _`davinci_spi_process_events`:

davinci_spi_process_events
==========================

.. c:function:: int davinci_spi_process_events(struct davinci_spi *dspi)

    check for and handle any SPI controller events

    :param dspi:
        the controller data
    :type dspi: struct davinci_spi \*

.. _`davinci_spi_process_events.description`:

Description
-----------

This function will check the SPIFLG register and handle any events that are
detected there

.. _`davinci_spi_bufs`:

davinci_spi_bufs
================

.. c:function:: int davinci_spi_bufs(struct spi_device *spi, struct spi_transfer *t)

    functions which will handle transfer data

    :param spi:
        spi device on which data transfer to be done
    :type spi: struct spi_device \*

    :param t:
        spi transfer in which transfer info is filled
    :type t: struct spi_transfer \*

.. _`davinci_spi_bufs.description`:

Description
-----------

This function will put data to be transferred into data register
of SPI controller and then wait until the completion will be marked
by the IRQ Handler.

.. _`dummy_thread_fn`:

dummy_thread_fn
===============

.. c:function:: irqreturn_t dummy_thread_fn(s32 irq, void *data)

    dummy thread function

    :param irq:
        IRQ number for this SPI Master
    :type irq: s32

    :param data:
        *undescribed*
    :type data: void \*

.. _`dummy_thread_fn.description`:

Description
-----------

This is to satisfy the \ :c:func:`request_threaded_irq`\  API so that the irq
handler is called in interrupt context.

.. _`davinci_spi_irq`:

davinci_spi_irq
===============

.. c:function:: irqreturn_t davinci_spi_irq(s32 irq, void *data)

    Interrupt handler for SPI Master Controller

    :param irq:
        IRQ number for this SPI Master
    :type irq: s32

    :param data:
        *undescribed*
    :type data: void \*

.. _`davinci_spi_irq.description`:

Description
-----------

ISR will determine that interrupt arrives either for READ or WRITE command.
According to command it will do the appropriate action. It will check
transfer length and if it is not zero then dispatch transfer command again.
If transfer length is zero then it will indicate the COMPLETION so that
davinci_spi_bufs function can go ahead.

.. _`spi_davinci_get_pdata`:

spi_davinci_get_pdata
=====================

.. c:function:: int spi_davinci_get_pdata(struct platform_device *pdev, struct davinci_spi *dspi)

    Get platform data from DTS binding

    :param pdev:
        ptr to platform data
    :type pdev: struct platform_device \*

    :param dspi:
        ptr to driver data
    :type dspi: struct davinci_spi \*

.. _`spi_davinci_get_pdata.description`:

Description
-----------

Parses and populates pdata in dspi from device tree bindings.

.. _`spi_davinci_get_pdata.note`:

NOTE
----

Not all platform data params are supported currently.

.. _`davinci_spi_probe`:

davinci_spi_probe
=================

.. c:function:: int davinci_spi_probe(struct platform_device *pdev)

    probe function for SPI Master Controller

    :param pdev:
        platform_device structure which contains plateform specific data
    :type pdev: struct platform_device \*

.. _`davinci_spi_probe.description`:

Description
-----------

According to Linux Device Model this function will be invoked by Linux
with platform_device struct which contains the device specific info.
This function will map the SPI controller's memory, register IRQ,
Reset SPI controller and setting its registers to default value.
It will invoke spi_bitbang_start to create work queue so that client driver
can register transfer method to work queue.

.. _`davinci_spi_remove`:

davinci_spi_remove
==================

.. c:function:: int davinci_spi_remove(struct platform_device *pdev)

    remove function for SPI Master Controller

    :param pdev:
        platform_device structure which contains plateform specific data
    :type pdev: struct platform_device \*

.. _`davinci_spi_remove.description`:

Description
-----------

This function will do the reverse action of davinci_spi_probe function
It will free the IRQ and SPI controller's memory region.
It will also call spi_bitbang_stop to destroy the work queue which was
created by spi_bitbang_start.

.. This file was automatic generated / don't edit.

