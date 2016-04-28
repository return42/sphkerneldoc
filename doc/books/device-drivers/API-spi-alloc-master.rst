.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-alloc-master:

================
spi_alloc_master
================

*man spi_alloc_master(9)*

*4.6.0-rc5*

allocate SPI master controller


Synopsis
========

.. c:function:: struct spi_master * spi_alloc_master( struct device * dev, unsigned size )

Arguments
=========

``dev``
    the controller, possibly using the platform_bus

``size``
    how much zeroed driver-private data to allocate; the pointer to this
    memory is in the driver_data field of the returned device,
    accessible with ``spi_master_get_devdata``.


Context
=======

can sleep


Description
===========

This call is used only by SPI master controller drivers, which are the
only ones directly touching chip registers. It's how they allocate an
spi_master structure, prior to calling ``spi_register_master``.

This must be called from context that can sleep.

The caller is responsible for assigning the bus number and initializing
the master's methods before calling ``spi_register_master``; and (after
errors adding the device) calling ``spi_master_put`` to prevent a memory
leak.


Return
======

the SPI master structure on success, else NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
