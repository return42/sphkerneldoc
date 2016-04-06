
.. _API-uart-remove-one-port:

====================
uart_remove_one_port
====================

*man uart_remove_one_port(9)*

*4.6.0-rc1*

detach a driver defined port structure


Synopsis
========

.. c:function:: int uart_remove_one_port( struct uart_driver * drv, struct uart_port * uport )

Arguments
=========

``drv``
    pointer to the uart low level driver structure for this port

``uport``
    uart port structure for this port


Description
===========

This unhooks (and hangs up) the specified port structure from the core driver. No further calls will be made to the low-level code for this port.
