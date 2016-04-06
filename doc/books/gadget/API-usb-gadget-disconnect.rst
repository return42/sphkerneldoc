
.. _API-usb-gadget-disconnect:

=====================
usb_gadget_disconnect
=====================

*man usb_gadget_disconnect(9)*

*4.6.0-rc1*

software-controlled disconnect from USB host


Synopsis
========

.. c:function:: int usb_gadget_disconnect( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the peripheral being disconnected


Description
===========

Disables the D+ (or potentially D-) pullup, which the host may see as a disconnect (when a VBUS session is active). Not all systems support software pullup controls.

Returns zero on success, else negative errno.
