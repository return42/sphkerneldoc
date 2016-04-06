
.. _API-spi-w8r16:

=========
spi_w8r16
=========

*man spi_w8r16(9)*

*4.6.0-rc1*

SPI synchronous 8 bit write followed by 16 bit read


Synopsis
========

.. c:function:: ssize_t spi_w8r16( struct spi_device * spi, u8 cmd )

Arguments
=========

``spi``
    device with which data will be exchanged

``cmd``
    command to be written before data is read back


Context
=======

can sleep


Description
===========

The number is returned in wire-order, which is at least sometimes big-endian.

Callable only from contexts that can sleep.


Return
======

the (unsigned) sixteen bit number returned by the device, or else a negative error code.
