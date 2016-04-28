.. -*- coding: utf-8; mode: rst -*-

.. _API-USB-DEVICE-VER:

==============
USB_DEVICE_VER
==============

*man USB_DEVICE_VER(9)*

*4.6.0-rc5*

describe a specific usb device with a version range


Synopsis
========

.. c:function:: USB_DEVICE_VER( vend, prod, lo, hi )

Arguments
=========

``vend``
    the 16 bit USB Vendor ID

``prod``
    the 16 bit USB Product ID

``lo``
    the bcdDevice_lo value

``hi``
    the bcdDevice_hi value


Description
===========

This macro is used to create a struct usb_device_id that matches a
specific device, with a version range.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
