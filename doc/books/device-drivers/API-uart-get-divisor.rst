.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-get-divisor:

================
uart_get_divisor
================

*man uart_get_divisor(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
