.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-sync-locked:

===============
spi_sync_locked
===============

*man spi_sync_locked(9)*

*4.6.0-rc5*

version of spi_sync with exclusive bus usage


Synopsis
========

.. c:function:: int spi_sync_locked( struct spi_device * spi, struct spi_message * message )

Arguments
=========

``spi``
    device with which data will be exchanged

``message``
    describes the data transfers


Context
=======

can sleep


Description
===========

This call may only be used from a context that may sleep. The sleep is
non-interruptible, and has no timeout. Low-overhead controller drivers
may DMA directly into and out of the message buffers.

This call should be used by drivers that require exclusive access to the
SPI bus. It has to be preceded by a spi_bus_lock call. The SPI bus
must be released by a spi_bus_unlock call when the exclusive access is
over.


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
