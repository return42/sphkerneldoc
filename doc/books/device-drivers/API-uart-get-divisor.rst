
.. _API-uart-get-divisor:

================
uart_get_divisor
================

*man uart_get_divisor(9)*

*4.6.0-rc1*

return uart clock divisor


Synopsis
========

.. c:function:: unsigned int uart_get_divisor( struct uart_port * port, unsigned int baud )

Arguments
=========

``port``
    uart_port structure describing the port.

``baud``
    desired baud rate


Description
===========

Calculate the uart clock divisor for the port.
