.. -*- coding: utf-8; mode: rst -*-

.. _API-USB-VENDOR-AND-INTERFACE-INFO:

=============================
USB_VENDOR_AND_INTERFACE_INFO
=============================

*man USB_VENDOR_AND_INTERFACE_INFO(9)*

*4.6.0-rc5*

describe a specific usb vendor with a class of usb interfaces


Synopsis
========

.. c:function:: USB_VENDOR_AND_INTERFACE_INFO( vend, cl, sc, pr )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``cl``
    bInterfaceClass value

``sc``
    bInterfaceSubClass value

``pr``
    bInterfaceProtocol value


Description
===========

This macro is used to create a struct usb_device_id that matches a
specific vendor with a specific class of interfaces.

This is especially useful when explicitly matching devices that have
vendor specific bDeviceClass values, but standards-compliant interfaces.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
