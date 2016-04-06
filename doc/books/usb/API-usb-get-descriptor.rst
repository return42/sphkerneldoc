
.. _API-usb-get-descriptor:

==================
usb_get_descriptor
==================

*man usb_get_descriptor(9)*

*4.6.0-rc1*

issues a generic GET_DESCRIPTOR request


Synopsis
========

.. c:function:: int usb_get_descriptor( struct usb_device * dev, unsigned char type, unsigned char index, void * buf, int size )

Arguments
=========

``dev``
    the device whose descriptor is being retrieved

``type``
    the descriptor type (USB_DT_⋆)

``index``
    the number of the descriptor

``buf``
    where to put the descriptor

``size``
    how big is “buf”?


Context
=======

!in_interrupt ()


Description
===========

Gets a USB descriptor. Convenience functions exist to simplify getting some types of descriptors. Use ``usb_get_string`` or ``usb_string`` for USB_DT_STRING. Device
(USB_DT_DEVICE) and configuration descriptors (USB_DT_CONFIG) are part of the device structure. In addition to a number of USB-standard descriptors, some devices also use
class-specific or vendor-specific descriptors.

This call is synchronous, and may not be used in an interrupt context.


Return
======

The number of bytes received on success, or else the status code returned by the underlying ``usb_control_msg`` call.
