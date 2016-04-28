.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-w8r16be:

===========
spi_w8r16be
===========

*man spi_w8r16be(9)*

*4.6.0-rc5*

SPI synchronous 8 bit write followed by 16 bit big-endian read


Synopsis
========

.. c:function:: ssize_t spi_w8r16be( struct spi_device * spi, u8 cmd )

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

This function is similar to spi_w8r16, with the exception that it will
convert the read 16 bit data word from big-endian to native endianness.

Callable only from contexts that can sleep.


Return
======

the (unsigned) sixteen bit number returned by the device in cpu
endianness, or else a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
