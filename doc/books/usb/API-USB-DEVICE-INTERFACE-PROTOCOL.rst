.. -*- coding: utf-8; mode: rst -*-

.. _API-USB-DEVICE-INTERFACE-PROTOCOL:

=============================
USB_DEVICE_INTERFACE_PROTOCOL
=============================

*man USB_DEVICE_INTERFACE_PROTOCOL(9)*

*4.6.0-rc5*

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

This macro is used to create a struct usb_device_id that matches a
specific interface protocol of devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
