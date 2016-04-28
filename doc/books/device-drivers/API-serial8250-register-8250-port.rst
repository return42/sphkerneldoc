.. -*- coding: utf-8; mode: rst -*-

.. _API-serial8250-register-8250-port:

=============================
serial8250_register_8250_port
=============================

*man serial8250_register_8250_port(9)*

*4.6.0-rc5*

register a serial port


Synopsis
========

.. c:function:: int serial8250_register_8250_port( struct uart_8250_port * up )

Arguments
=========

``up``
    serial port template


Description
===========

Configure the serial port specified by the request. If the port exists
and is in use, it is hung up and unregistered first.

The port is then probed and if necessary the IRQ is autodetected If this
fails an error is returned.

On success the port is ready to use and the line number is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
