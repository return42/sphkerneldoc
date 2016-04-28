.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-insert-char:

================
uart_insert_char
================

*man uart_insert_char(9)*

*4.6.0-rc5*

push a char to the uart layer


Synopsis
========

.. c:function:: void uart_insert_char( struct uart_port * port, unsigned int status, unsigned int overrun, unsigned int ch, unsigned int flag )

Arguments
=========

``port``
    corresponding port

``status``
    state of the serial port RX buffer (LSR for 8250)

``overrun``
    mask of overrun bits in ``status``

``ch``
    character to push

``flag``
    flag for the character (see TTY_NORMAL and friends)


Description
===========

User is responsible to call tty_flip_buffer_push when they are done
with insertion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
