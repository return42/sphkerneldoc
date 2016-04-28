.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-w8r8:

========
spi_w8r8
========

*man spi_w8r8(9)*

*4.6.0-rc5*

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

the (unsigned) eight bit number returned by the device, or else a
negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
