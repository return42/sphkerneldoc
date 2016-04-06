
.. _API-module-spi-driver:

=================
module_spi_driver
=================

*man module_spi_driver(9)*

*4.6.0-rc1*

Helper macro for registering a SPI driver


Synopsis
========

.. c:function:: module_spi_driver( __spi_driver )

Arguments
=========

``__spi_driver``
    spi_driver struct


Description
===========

Helper macro for SPI drivers which do not do anything special in module init/exit. This eliminates a lot of boilerplate. Each module may only use this macro once, and calling it
replaces ``module_init`` and ``module_exit``
