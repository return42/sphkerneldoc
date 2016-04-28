.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-read:

========
spi_read
========

*man spi_read(9)*

*4.6.0-rc5*

SPI synchronous read


Synopsis
========

.. c:function:: int spi_read( struct spi_device * spi, void * buf, size_t len )

Arguments
=========

``spi``
    device from which data will be read

``buf``
    data buffer

``len``
    data buffer size


Context
=======

can sleep


Description
===========

This function reads the buffer ``buf``. Callable only from contexts that
can sleep.


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
