
.. _API-spi-register-master:

===================
spi_register_master
===================

*man spi_register_master(9)*

*4.6.0-rc1*

register SPI master controller


Synopsis
========

.. c:function:: int spi_register_master( struct spi_master * master )

Arguments
=========

``master``
    initialized master, originally from ``spi_alloc_master``


Context
=======

can sleep


Description
===========

SPI master controllers connect to their drivers using some non-SPI bus, such as the platform bus. The final stage of ``probe`` in that code includes calling ``spi_register_master``
to hook up to this SPI bus glue.

SPI controllers use board specific (often SOC specific) bus numbers, and board-specific addressing for SPI devices combines those numbers with chip select numbers. Since SPI does
not directly support dynamic device identification, boards need configuration tables telling which chip is at which address.

This must be called from context that can sleep. It returns zero on success, else a negative error code (dropping the master's refcount). After a successful return, the caller is
responsible for calling ``spi_unregister_master``.


Return
======

zero on success, else a negative error code.
