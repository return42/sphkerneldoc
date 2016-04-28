.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-set-options:

================
uart_set_options
================

*man uart_set_options(9)*

*4.6.0-rc5*

setup the serial console parameters


Synopsis
========

.. c:function:: int uart_set_options( struct uart_port * port, struct console * co, int baud, int parity, int bits, int flow )

Arguments
=========

``port``
    pointer to the serial ports uart_port structure

``co``
    console pointer

``baud``
    baud rate

``parity``
    parity character - 'n' (none), 'o' (odd), 'e' (even)

``bits``
    number of data bits

``flow``
    flow control character - 'r' (rts)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
