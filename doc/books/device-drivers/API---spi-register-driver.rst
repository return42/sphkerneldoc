
.. _API---spi-register-driver:

=====================
__spi_register_driver
=====================

*man __spi_register_driver(9)*

*4.6.0-rc1*

register a SPI driver


Synopsis
========

.. c:function:: int __spi_register_driver( struct module * owner, struct spi_driver * sdrv )

Arguments
=========

``owner``
    owner module of the driver to register

``sdrv``
    the driver to register


Context
=======

can sleep


Return
======

zero on success, else a negative error code.
