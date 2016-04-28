.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-vbus-connect:

=======================
usb_gadget_vbus_connect
=======================

*man usb_gadget_vbus_connect(9)*

*4.6.0-rc5*

Notify controller that VBUS is powered


Synopsis
========

.. c:function:: int usb_gadget_vbus_connect( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    The device which now has VBUS power.


Context
=======

can sleep


Description
===========

This call is used by a driver for an external transceiver (or GPIO) that
detects a VBUS power session starting. Common responses include resuming
the controller, activating the D+ (or D-) pullup to let the host detect
that a USB device is attached, and starting to draw power (8mA or
possibly more, especially after SET_CONFIGURATION).

Returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
