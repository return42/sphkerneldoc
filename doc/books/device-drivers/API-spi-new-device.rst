
.. _API-spi-new-device:

==============
spi_new_device
==============

*man spi_new_device(9)*

*4.6.0-rc1*

instantiate one new SPI device


Synopsis
========

.. c:function:: struct spi_device ⋆ spi_new_device( struct spi_master * master, struct spi_board_info * chip )

Arguments
=========

``master``
    Controller to which device is connected

``chip``
    Describes the SPI device


Context
=======

can sleep


Description
===========

On typical mainboards, this is purely internal; and it's not needed after board init creates the hard-wired devices. Some development platforms may not be able to use
spi_register_board_info though, and this is exported so that for example a USB or parport based adapter driver could add devices (which it would learn about out-of-band).


Return
======

the new device, or NULL.
