.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-set-selfpowered:

==========================
usb_gadget_set_selfpowered
==========================

*man usb_gadget_set_selfpowered(9)*

*4.6.0-rc5*

sets the device selfpowered feature.


Synopsis
========

.. c:function:: int usb_gadget_set_selfpowered( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the device being declared as self-powered


Description
===========

this affects the device status reported by the hardware driver to
reflect that it now has a local power supply.

returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
