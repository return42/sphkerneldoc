
.. _API-spi-setup:

=========
spi_setup
=========

*man spi_setup(9)*

*4.6.0-rc1*

setup SPI mode and clock rate


Synopsis
========

.. c:function:: int spi_setup( struct spi_device * spi )

Arguments
=========

``spi``
    the device whose settings are being modified


Context
=======

can sleep, and no requests are queued to the device


Description
===========

SPI protocol drivers may need to update the transfer mode if the device doesn't work with its default. They may likewise need to update clock rates or word sizes from initial
values. This function changes those settings, and must be called from a context that can sleep. Except for SPI_CS_HIGH, which takes effect immediately, the changes take effect
the next time the device is selected and data is transferred to or from it. When this function returns, the spi device is deselected.

Note that this call will fail if the protocol driver specifies an option that the underlying controller or its driver does not support. For example, not all hardware supports wire
transfers using nine bit words, LSB-first wire encoding, or active-high chipselects.


Return
======

zero on success, else a negative error code.
