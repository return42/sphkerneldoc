.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-bus-unlock:

==============
spi_bus_unlock
==============

*man spi_bus_unlock(9)*

*4.6.0-rc5*

release the lock for exclusive SPI bus usage


Synopsis
========

.. c:function:: int spi_bus_unlock( struct spi_master * master )

Arguments
=========

``master``
    SPI bus master that was locked for exclusive bus access


Context
=======

can sleep


Description
===========

This call may only be used from a context that may sleep. The sleep is
non-interruptible, and has no timeout.

This call releases an SPI bus lock previously obtained by an
spi_bus_lock call.


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
