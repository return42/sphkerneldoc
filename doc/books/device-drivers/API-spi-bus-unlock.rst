
.. _API-spi-bus-unlock:

==============
spi_bus_unlock
==============

*man spi_bus_unlock(9)*

*4.6.0-rc1*

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

This call may only be used from a context that may sleep. The sleep is non-interruptible, and has no timeout.

This call releases an SPI bus lock previously obtained by an spi_bus_lock call.


Return
======

always zero.
