
.. _API-spi-alloc-device:

================
spi_alloc_device
================

*man spi_alloc_device(9)*

*4.6.0-rc1*

Allocate a new SPI device


Synopsis
========

.. c:function:: struct spi_device ⋆ spi_alloc_device( struct spi_master * master )

Arguments
=========

``master``
    Controller to which device is connected


Context
=======

can sleep


Description
===========

Allows a driver to allocate and initialize a spi_device without registering it immediately. This allows a driver to directly fill the spi_device with device parameters before
calling ``spi_add_device`` on it.

Caller is responsible to call ``spi_add_device`` on the returned spi_device structure to add it to the SPI master. If the caller needs to discard the spi_device without adding
it, then it should call ``spi_dev_put`` on it.


Return
======

a pointer to the new device, or NULL.
