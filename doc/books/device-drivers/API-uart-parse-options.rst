.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-parse-options:

==================
uart_parse_options
==================

*man uart_parse_options(9)*

*4.6.0-rc5*

Parse serial port baud/parity/bits/flow control.


Synopsis
========

.. c:function:: void uart_parse_options( char * options, int * baud, int * parity, int * bits, int * flow )

Arguments
=========

``options``
    pointer to option string

``baud``
    pointer to an 'int' variable for the baud rate.

``parity``
    pointer to an 'int' variable for the parity.

``bits``
    pointer to an 'int' variable for the number of data bits.

``flow``
    pointer to an 'int' variable for the flow control character.


Description
===========

uart_parse_options decodes a string containing the serial console
options. The format of the string is <baud><parity><bits><flow>,


eg
==

115200n8r


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
