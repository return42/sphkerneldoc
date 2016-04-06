
.. _API-spi-unregister-device:

=====================
spi_unregister_device
=====================

*man spi_unregister_device(9)*

*4.6.0-rc1*

unregister a single SPI device


Synopsis
========

.. c:function:: void spi_unregister_device( struct spi_device * spi )

Arguments
=========

``spi``
    spi_device to unregister


Description
===========

Start making the passed SPI device vanish. Normally this would be handled by ``spi_unregister_master``.
