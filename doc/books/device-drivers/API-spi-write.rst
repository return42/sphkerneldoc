
.. _API-spi-write:

=========
spi_write
=========

*man spi_write(9)*

*4.6.0-rc1*

SPI synchronous write


Synopsis
========

.. c:function:: int spi_write( struct spi_device * spi, const void * buf, size_t len )

Arguments
=========

``spi``
    device to which data will be written

``buf``
    data buffer

``len``
    data buffer size


Context
=======

can sleep


Description
===========

This function writes the buffer ``buf``. Callable only from contexts that can sleep.


Return
======

zero on success, else a negative error code.
