
.. _API-usb-gadget-connect:

==================
usb_gadget_connect
==================

*man usb_gadget_connect(9)*

*4.6.0-rc1*

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

Enables the D+ (or potentially D-) pullup. The host will start enumerating this gadget when the pullup is active and a VBUS session is active (the link is powered). This pullup is
always enabled unless ``usb_gadget_disconnect`` has been used to disable it.

Returns zero on success, else negative errno.
