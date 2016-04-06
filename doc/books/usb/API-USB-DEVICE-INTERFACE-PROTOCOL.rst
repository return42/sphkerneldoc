
.. _API-USB-DEVICE-INTERFACE-PROTOCOL:

=============================
USB_DEVICE_INTERFACE_PROTOCOL
=============================

*man USB_DEVICE_INTERFACE_PROTOCOL(9)*

*4.6.0-rc1*

describe a usb device with a specific interface protocol


Synopsis
========

.. c:function:: USB_DEVICE_INTERFACE_PROTOCOL( vend, prod, pr )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``prod``
    the 16 bit USB Product ID

``pr``
    bInterfaceProtocol value


Description
===========

This macro is used to create a struct usb_device_id that matches a specific interface protocol of devices.
