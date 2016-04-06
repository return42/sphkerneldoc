
.. _API-usb-gadget-vbus-disconnect:

==========================
usb_gadget_vbus_disconnect
==========================

*man usb_gadget_vbus_disconnect(9)*

*4.6.0-rc1*

notify controller about VBUS session end


Synopsis
========

.. c:function:: int usb_gadget_vbus_disconnect( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the device whose VBUS supply is being described


Context
=======

can sleep


Description
===========

This call is used by a driver for an external transceiver (or GPIO) that detects a VBUS power session ending. Common responses include reversing everything done in
``usb_gadget_vbus_connect``.

Returns zero on success, else negative errno.
