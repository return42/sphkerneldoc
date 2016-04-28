.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-remove-one-port:

====================
uart_remove_one_port
====================

*man uart_remove_one_port(9)*

*4.6.0-rc5*

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

This unhooks (and hangs up) the specified port structure from the core
driver. No further calls will be made to the low-level code for this
port.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
