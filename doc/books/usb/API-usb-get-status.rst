
.. _API-usb-get-status:

==============
usb_get_status
==============

*man usb_get_status(9)*

*4.6.0-rc1*

issues a GET_STATUS call


Synopsis
========

.. c:function:: int usb_get_status( struct usb_device * dev, int type, int target, void * data )

Arguments
=========

``dev``
    the device whose status is being checked

``type``
    USB_RECIP_⋆; for device, interface, or endpoint

``target``
    zero (for device), else interface or endpoint number

``data``
    pointer to two bytes of bitmap data


Context
=======

!in_interrupt ()


Description
===========

Returns device, interface, or endpoint status. Normally only of interest to see if the device is self powered, or has enabled the remote wakeup facility; or whether a bulk or
interrupt endpoint is halted (“stalled”).

Bits in these status bitmaps are set using the SET_FEATURE request, and cleared using the CLEAR_FEATURE request. The ``usb_clear_halt`` function should be used to clear halt
(“stall”) status.

This call is synchronous, and may not be used in an interrupt context.

Returns 0 and the status value in ⋆\ ``data`` (in host byte order) on success, or else the status code from the underlying ``usb_control_msg`` call.
