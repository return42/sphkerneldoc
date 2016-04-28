.. -*- coding: utf-8; mode: rst -*-

.. _API---spi-register-driver:

=====================
__spi_register_driver
=====================

*man __spi_register_driver(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
