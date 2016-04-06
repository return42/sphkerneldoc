
.. _API-USB-DEVICE-AND-INTERFACE-INFO:

=============================
USB_DEVICE_AND_INTERFACE_INFO
=============================

*man USB_DEVICE_AND_INTERFACE_INFO(9)*

*4.6.0-rc1*

describe a specific usb device with a class of usb interfaces


Synopsis
========

.. c:function:: USB_DEVICE_AND_INTERFACE_INFO( vend, prod, cl, sc, pr )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``prod``
    the 16 bit USB Product ID

``cl``
    bInterfaceClass value

``sc``
    bInterfaceSubClass value

``pr``
    bInterfaceProtocol value


Description
===========

This macro is used to create a struct usb_device_id that matches a specific device with a specific class of interfaces.

This is especially useful when explicitly matching devices that have vendor specific bDeviceClass values, but standards-compliant interfaces.
