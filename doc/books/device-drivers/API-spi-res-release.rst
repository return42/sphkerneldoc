
.. _API-spi-res-release:

===============
spi_res_release
===============

*man spi_res_release(9)*

*4.6.0-rc1*

release all spi resources for this message


Synopsis
========

.. c:function:: void spi_res_release( struct spi_master * master, struct spi_message * message )

Arguments
=========

``master``
    the ``spi_master``

``message``
    the ``spi_message``
