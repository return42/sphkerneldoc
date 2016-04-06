
.. _API-spi-busnum-to-master:

====================
spi_busnum_to_master
====================

*man spi_busnum_to_master(9)*

*4.6.0-rc1*

look up master associated with bus_num


Synopsis
========

.. c:function:: struct spi_master ⋆ spi_busnum_to_master( u16 bus_num )

Arguments
=========

``bus_num``
    the master's bus number


Context
=======

can sleep


Description
===========

This call may be used with devices that are registered after arch init time. It returns a refcounted pointer to the relevant spi_master (which the caller must release), or NULL if
there is no such master registered.


Return
======

the SPI master structure on success, else NULL.
