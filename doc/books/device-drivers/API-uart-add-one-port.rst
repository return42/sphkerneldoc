.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-add-one-port:

=================
uart_add_one_port
=================

*man uart_add_one_port(9)*

*4.6.0-rc5*

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

This allows the driver to register its own uart_port structure with the
core driver. The main purpose is to allow the low level uart drivers to
expand uart_port, rather than having yet more levels of structures.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
