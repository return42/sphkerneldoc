
.. _API-spi-unregister-master:

=====================
spi_unregister_master
=====================

*man spi_unregister_master(9)*

*4.6.0-rc1*

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

This call is used only by SPI master controller drivers, which are the only ones directly touching chip registers.

This must be called from context that can sleep.
