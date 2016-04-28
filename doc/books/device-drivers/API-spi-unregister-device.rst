.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-unregister-device:

=====================
spi_unregister_device
=====================

*man spi_unregister_device(9)*

*4.6.0-rc5*

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

Start making the passed SPI device vanish. Normally this would be
handled by ``spi_unregister_master``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
