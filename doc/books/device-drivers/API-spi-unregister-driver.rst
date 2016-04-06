
.. _API-spi-unregister-driver:

=====================
spi_unregister_driver
=====================

*man spi_unregister_driver(9)*

*4.6.0-rc1*

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
