
.. _API-usb-gadget-activate:

===================
usb_gadget_activate
===================

*man usb_gadget_activate(9)*

*4.6.0-rc1*

activate function which is not ready to work


Synopsis
========

.. c:function:: int usb_gadget_activate( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the peripheral being activated


Description
===========

This routine activates gadget which was previously deactivated with ``usb_gadget_deactivate`` call. It calls ``usb_gadget_connect`` if needed.

Returns zero on success, else negative errno.
