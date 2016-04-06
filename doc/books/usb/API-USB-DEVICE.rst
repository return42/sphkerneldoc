
.. _API-USB-DEVICE:

==========
USB_DEVICE
==========

*man USB_DEVICE(9)*

*4.6.0-rc1*

macro used to describe a specific usb device


Synopsis
========

.. c:function:: USB_DEVICE( vend, prod )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``prod``
    the 16 bit USB Product ID


Description
===========

This macro is used to create a struct usb_device_id that matches a specific device.
