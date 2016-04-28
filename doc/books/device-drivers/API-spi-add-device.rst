.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-add-device:

==============
spi_add_device
==============

*man spi_add_device(9)*

*4.6.0-rc5*

Add spi_device allocated with spi_alloc_device


Synopsis
========

.. c:function:: int spi_add_device( struct spi_device * spi )

Arguments
=========

``spi``
    spi_device to register


Description
===========

Companion function to spi_alloc_device. Devices allocated with
spi_alloc_device can be added onto the spi bus with this function.


Return
======

0 on success; negative errno on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
