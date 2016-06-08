.. -*- coding: utf-8; mode: rst -*-

.. _introduction:

************
Introduction
************

The Linux MUSB subsystem is part of the larger Linux USB subsystem. It
provides support for embedded USB Device Controllers (UDC) that do not
use Universal Host Controller Interface (UHCI) or Open Host Controller
Interface (OHCI).

Instead, these embedded UDC rely on the USB On-the-Go (OTG)
specification which they implement at least partially. The silicon
reference design used in most cases is the Multipoint USB Highspeed
Dual-Role Controller (MUSB HDRC) found in the Mentor Graphics Inventra™
design.

As a self-taught exercise I have written an MUSB glue layer for the
Ingenic JZ4740 SoC, modelled after the many MUSB glue layers in the
kernel source tree. This layer can be found at
drivers/usb/musb/jz4740.c. In this documentation I will walk through the
basics of the jz4740.c glue layer, explaining the different pieces and
what needs to be done in order to write your own device glue layer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
