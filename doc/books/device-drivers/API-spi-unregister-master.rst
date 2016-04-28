.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-unregister-master:

=====================
spi_unregister_master
=====================

*man spi_unregister_master(9)*

*4.6.0-rc5*

unregister SPI master controller


Synopsis
========

.. c:function:: void spi_unregister_master( struct spi_master * master )

Arguments
=========

``master``
    the master being unregistered


Context
=======

can sleep


Description
===========

This call is used only by SPI master controller drivers, which are the
only ones directly touching chip registers.

This must be called from context that can sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
