.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/serial.c

.. _`omap_serial_init_port`:

omap_serial_init_port
=====================

.. c:function:: void omap_serial_init_port(struct omap_board_data *bdata, struct omap_uart_port_info *info)

    initialize single serial port

    :param struct omap_board_data \*bdata:
        port specific board data pointer

    :param struct omap_uart_port_info \*info:
        platform specific data pointer

.. _`omap_serial_init_port.description`:

Description
-----------

This function initialies serial driver for given port only.
Platforms can call this function instead of \ :c:func:`omap_serial_init`\ 
if they don't plan to use all available UARTs as serial ports.

Don't mix calls to \ :c:func:`omap_serial_init_port`\  and \ :c:func:`omap_serial_init`\ ,
use only one of the two.

.. _`omap_serial_board_init`:

omap_serial_board_init
======================

.. c:function:: void omap_serial_board_init(struct omap_uart_port_info *info)

    initialize all supported serial ports

    :param struct omap_uart_port_info \*info:
        platform specific data pointer

.. _`omap_serial_board_init.description`:

Description
-----------

Initializes all available UARTs as serial ports. Platforms
can call this function when they want to have default behaviour
for serial ports (e.g initialize them all as serial ports).

.. _`omap_serial_init`:

omap_serial_init
================

.. c:function:: void omap_serial_init( void)

    initialize all supported serial ports

    :param  void:
        no arguments

.. _`omap_serial_init.description`:

Description
-----------

Initializes all available UARTs.
Platforms can call this function when they want to have default behaviour
for serial ports (e.g initialize them all as serial ports).

.. This file was automatic generated / don't edit.

