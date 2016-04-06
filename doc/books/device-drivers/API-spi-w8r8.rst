
.. _API-spi-w8r8:

========
spi_w8r8
========

*man spi_w8r8(9)*

*4.6.0-rc1*

SPI synchronous 8 bit write followed by 8 bit read


Synopsis
========

.. c:function:: ssize_t spi_w8r8( struct spi_device * spi, u8 cmd )

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

Callable only from contexts that can sleep.


Return
======

the (unsigned) eight bit number returned by the device, or else a negative error code.
