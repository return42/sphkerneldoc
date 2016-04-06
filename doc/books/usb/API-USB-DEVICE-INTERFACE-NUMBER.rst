
.. _API-USB-DEVICE-INTERFACE-NUMBER:

===========================
USB_DEVICE_INTERFACE_NUMBER
===========================

*man USB_DEVICE_INTERFACE_NUMBER(9)*

*4.6.0-rc1*

describe a usb device with a specific interface number


Synopsis
========

.. c:function:: USB_DEVICE_INTERFACE_NUMBER( vend, prod, num )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``prod``
    the 16 bit USB Product ID

``num``
    bInterfaceNumber value


Description
===========

This macro is used to create a struct usb_device_id that matches a specific interface number of devices.
