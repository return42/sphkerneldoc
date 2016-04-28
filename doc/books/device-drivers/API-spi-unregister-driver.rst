.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-unregister-driver:

=====================
spi_unregister_driver
=====================

*man spi_unregister_driver(9)*

*4.6.0-rc5*

reverse effect of spi_register_driver


Synopsis
========

.. c:function:: void spi_unregister_driver( struct spi_driver * sdrv )

Arguments
=========

``sdrv``
    the driver to unregister


Context
=======

can sleep


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
