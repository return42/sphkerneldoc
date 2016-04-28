.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-console-write:

==================
uart_console_write
==================

*man uart_console_write(9)*

*4.6.0-rc5*

write a console message to a serial port


Synopsis
========

.. c:function:: void uart_console_write( struct uart_port * port, const char * s, unsigned int count, void (*putchar) struct uart_port *, int )

Arguments
=========

``port``
    the port to write the message

``s``
    array of characters

``count``
    number of characters in string to write

``putchar``
    function to write character to port


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
