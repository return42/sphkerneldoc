
.. _API-usb-gadget-frame-number:

=======================
usb_gadget_frame_number
=======================

*man usb_gadget_frame_number(9)*

*4.6.0-rc1*

returns the current frame number


Synopsis
========

.. c:function:: int usb_gadget_frame_number( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    controller that reports the frame number


Description
===========

Returns the usb frame number, normally eleven bits from a SOF packet, or negative errno if this device doesn't support this capability.
