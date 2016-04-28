.. -*- coding: utf-8; mode: rst -*-

.. _API-USB-DEVICE-INTERFACE-NUMBER:

===========================
USB_DEVICE_INTERFACE_NUMBER
===========================

*man USB_DEVICE_INTERFACE_NUMBER(9)*

*4.6.0-rc5*

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

This macro is used to create a struct usb_device_id that matches a
specific interface number of devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
