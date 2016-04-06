
.. _API-spi-register-board-info:

=======================
spi_register_board_info
=======================

*man spi_register_board_info(9)*

*4.6.0-rc1*

register SPI devices for a given board


Synopsis
========

.. c:function:: int spi_register_board_info( struct spi_board_info const * info, unsigned n )

Arguments
=========

``info``
    array of chip descriptors

``n``
    how many descriptors are provided


Context
=======

can sleep


Description
===========

Board-specific early init code calls this (probably during arch_initcall) with segments of the SPI device table. Any device nodes are created later, after the relevant parent SPI
controller (bus_num) is defined. We keep this table of devices forever, so that reloading a controller driver will not make Linux forget about these hard-wired devices.

Other code can also call this, e.g. a particular add-on board might provide SPI devices through its expansion connector, so code initializing that board would naturally declare its
SPI devices.

The board info passed can safely be __initdata ... but be careful of any embedded pointers (platform_data, etc), they're copied as-is.


Return
======

zero on success, else a negative error code.
