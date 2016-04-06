
.. _API-spi-res-add:

===========
spi_res_add
===========

*man spi_res_add(9)*

*4.6.0-rc1*

add a spi_res to the spi_message


Synopsis
========

.. c:function:: void spi_res_add( struct spi_message * message, void * res )

Arguments
=========

``message``
    the spi message

``res``
    the spi_resource
