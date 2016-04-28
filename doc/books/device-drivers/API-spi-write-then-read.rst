.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-write-then-read:

===================
spi_write_then_read
===================

*man spi_write_then_read(9)*

*4.6.0-rc5*

SPI synchronous write followed by read


Synopsis
========

.. c:function:: int spi_write_then_read( struct spi_device * spi, const void * txbuf, unsigned n_tx, void * rxbuf, unsigned n_rx )

Arguments
=========

``spi``
    device with which data will be exchanged

``txbuf``
    data to be written (need not be dma-safe)

``n_tx``
    size of txbuf, in bytes

``rxbuf``
    buffer into which data will be read (need not be dma-safe)

``n_rx``
    size of rxbuf, in bytes


Context
=======

can sleep


Description
===========

This performs a half duplex MicroWire style transaction with the device,
sending txbuf and then reading rxbuf. The return value is zero for
success, else a negative errno status code. This call may only be used
from a context that may sleep.

Parameters to this routine are always copied using a small buffer;
portable code should never use this for more than 32 bytes.
Performance-sensitive or bulk transfer code should instead use
spi_{async,sync}() calls with dma-safe buffers.


Return
======

zero on success, else a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
