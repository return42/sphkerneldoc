.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-bitbang.c

.. _`spi_bitbang_setup`:

spi_bitbang_setup
=================

.. c:function:: int spi_bitbang_setup(struct spi_device *spi)

    default setup for per-word I/O loops

    :param struct spi_device \*spi:
        *undescribed*

.. _`spi_bitbang_cleanup`:

spi_bitbang_cleanup
===================

.. c:function:: void spi_bitbang_cleanup(struct spi_device *spi)

    default cleanup for per-word I/O loops

    :param struct spi_device \*spi:
        *undescribed*

.. _`spi_bitbang_start`:

spi_bitbang_start
=================

.. c:function:: int spi_bitbang_start(struct spi_bitbang *bitbang)

    start up a polled/bitbanging SPI master driver

    :param struct spi_bitbang \*bitbang:
        driver handle

.. _`spi_bitbang_start.description`:

Description
-----------

Caller should have zero-initialized all parts of the structure, and then
provided callbacks for chip selection and I/O loops.  If the master has
a transfer method, its final step should call spi_bitbang_transfer; or,
that's the default if the transfer routine is not initialized.  It should
also set up the bus number and number of chipselects.

For i/o loops, provide callbacks either per-word (for bitbanging, or for
hardware that basically exposes a shift register) or per-spi_transfer
(which takes better advantage of hardware like fifos or DMA engines).

Drivers using per-word I/O loops should use (or call) spi_bitbang_setup,
spi_bitbang_cleanup and spi_bitbang_setup_transfer to handle those spi
master methods.  Those methods are the defaults if the bitbang->txrx_bufs
routine isn't initialized.

This routine registers the spi_master, which will process requests in a
dedicated task, keeping IRQs unblocked most of the time.  To stop
processing those requests, call \ :c:func:`spi_bitbang_stop`\ .

On success, this routine will take a reference to master. The caller is
responsible for calling \ :c:func:`spi_bitbang_stop`\  to decrement the reference and
\ :c:func:`spi_master_put`\  as counterpart of \ :c:func:`spi_alloc_master`\  to prevent a memory
leak.

.. _`spi_bitbang_stop`:

spi_bitbang_stop
================

.. c:function:: void spi_bitbang_stop(struct spi_bitbang *bitbang)

    stops the task providing spi communication

    :param struct spi_bitbang \*bitbang:
        *undescribed*

.. This file was automatic generated / don't edit.

