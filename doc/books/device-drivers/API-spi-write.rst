.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-write:

=========
spi_write
=========

*man spi_write(9)*

*4.6.0-rc5*

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

This function writes the buffer ``buf``. Callable only from contexts
that can sleep.


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
