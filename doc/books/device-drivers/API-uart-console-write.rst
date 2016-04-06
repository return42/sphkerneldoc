
.. _API-uart-console-write:

==================
uart_console_write
==================

*man uart_console_write(9)*

*4.6.0-rc1*

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
