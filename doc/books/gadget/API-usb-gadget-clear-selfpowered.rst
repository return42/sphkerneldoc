
.. _API-usb-gadget-clear-selfpowered:

============================
usb_gadget_clear_selfpowered
============================

*man usb_gadget_clear_selfpowered(9)*

*4.6.0-rc1*

clear the device selfpowered feature.


Synopsis
========

.. c:function:: int usb_gadget_clear_selfpowered( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the device being declared as bus-powered


Description
===========

this affects the device status reported by the hardware driver. some hardware may not support bus-powered operation, in which case this feature's value can never change.

returns zero on success, else negative errno.
