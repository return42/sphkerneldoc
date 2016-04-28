.. -*- coding: utf-8; mode: rst -*-

.. _API-USB-DEVICE:

==========
USB_DEVICE
==========

*man USB_DEVICE(9)*

*4.6.0-rc5*

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

This macro is used to create a struct usb_device_id that matches a
specific device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
