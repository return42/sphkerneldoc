
.. _API-uart-add-one-port:

=================
uart_add_one_port
=================

*man uart_add_one_port(9)*

*4.6.0-rc1*

attach a driver-defined port structure


Synopsis
========

.. c:function:: int uart_add_one_port( struct uart_driver * drv, struct uart_port * uport )

Arguments
=========

``drv``
    pointer to the uart low level driver structure for this port

``uport``
    uart port structure to use for this port.


Description
===========

This allows the driver to register its own uart_port structure with the core driver. The main purpose is to allow the low level uart drivers to expand uart_port, rather than
having yet more levels of structures.
