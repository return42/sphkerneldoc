.. -*- coding: utf-8; mode: rst -*-

.. _API-uart-parse-earlycon:

===================
uart_parse_earlycon
===================

*man uart_parse_earlycon(9)*

*4.6.0-rc5*

Parse earlycon options


Synopsis
========

.. c:function:: int uart_parse_earlycon( char * p, unsigned char * iotype, unsigned long * addr, char ** options )

Arguments
=========

``p``
    ptr to 2nd field (ie., just beyond '<name>,')

``iotype``
    ptr for decoded iotype (out)

``addr``
    ptr for decoded mapbase/iobase (out)

``options``
    ptr for <options> field; NULL if not present (out)


Description
===========

Decodes earlycon kernel command line parameters of the form
earlycon=<name>,io|mmio|mmio16|mmio32|mmio32be|mmio32native,<addr>,<options>
console=<name>,io|mmio|mmio16|mmio32|mmio32be|mmio32native,<addr>,<options>

The optional form earlycon=<name>,0x<addr>,<options>
console=<name>,0x<addr>,<options> is also accepted; the returned
``iotype`` will be UPIO_MEM.

Returns 0 on success or -EINVAL on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
