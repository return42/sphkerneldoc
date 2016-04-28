.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-connect:

==================
usb_gadget_connect
==================

*man usb_gadget_connect(9)*

*4.6.0-rc5*

software-controlled connect to USB host


Synopsis
========

.. c:function:: int usb_gadget_connect( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the peripheral being connected


Description
===========

Enables the D+ (or potentially D-) pullup. The host will start
enumerating this gadget when the pullup is active and a VBUS session is
active (the link is powered). This pullup is always enabled unless
``usb_gadget_disconnect`` has been used to disable it.

Returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
