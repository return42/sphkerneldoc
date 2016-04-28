.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-spi-register-master:

========================
devm_spi_register_master
========================

*man devm_spi_register_master(9)*

*4.6.0-rc5*

register managed SPI master controller


Synopsis
========

.. c:function:: int devm_spi_register_master( struct device * dev, struct spi_master * master )

Arguments
=========

``dev``
    device managing SPI master

``master``
    initialized master, originally from ``spi_alloc_master``


Context
=======

can sleep


Description
===========

Register a SPI device as with ``spi_register_master`` which will
automatically be unregister


Return
======

zero on success, else a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
