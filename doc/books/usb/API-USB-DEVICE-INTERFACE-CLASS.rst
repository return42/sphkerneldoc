
.. _API-USB-DEVICE-INTERFACE-CLASS:

==========================
USB_DEVICE_INTERFACE_CLASS
==========================

*man USB_DEVICE_INTERFACE_CLASS(9)*

*4.6.0-rc1*

describe a usb device with a specific interface class


Synopsis
========

.. c:function:: USB_DEVICE_INTERFACE_CLASS( vend, prod, cl )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``prod``
    the 16 bit USB Product ID

``cl``
    bInterfaceClass value


Description
===========

This macro is used to create a struct usb_device_id that matches a specific interface class of devices.
