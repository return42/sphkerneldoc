.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-bus-lock:

============
spi_bus_lock
============

*man spi_bus_lock(9)*

*4.6.0-rc5*

obtain a lock for exclusive SPI bus usage


Synopsis
========

.. c:function:: int spi_bus_lock( struct spi_master * master )

Arguments
=========

``master``
    SPI bus master that should be locked for exclusive bus access


Context
=======

can sleep


Description
===========

This call may only be used from a context that may sleep. The sleep is
non-interruptible, and has no timeout.

This call should be used by drivers that require exclusive access to the
SPI bus. The SPI bus must be released by a spi_bus_unlock call when
the exclusive access is over. Data transfer must be done by
spi_sync_locked and spi_async_locked calls when the SPI bus lock is
held.


Return
======

always zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
