.. -*- coding: utf-8; mode: rst -*-

.. _API-USB-DEVICE-INFO:

===============
USB_DEVICE_INFO
===============

*man USB_DEVICE_INFO(9)*

*4.6.0-rc5*

macro used to describe a class of usb devices


Synopsis
========

.. c:function:: USB_DEVICE_INFO( cl, sc, pr )

Arguments
=========

``cl``
    bDeviceClass value

``sc``
    bDeviceSubClass value

``pr``
    bDeviceProtocol value


Description
===========

This macro is used to create a struct usb_device_id that matches a
specific class of devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
