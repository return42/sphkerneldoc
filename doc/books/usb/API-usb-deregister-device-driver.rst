.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-deregister-device-driver:

============================
usb_deregister_device_driver
============================

*man usb_deregister_device_driver(9)*

*4.6.0-rc5*

unregister a USB device (not interface) driver


Synopsis
========

.. c:function:: void usb_deregister_device_driver( struct usb_device_driver * udriver )

Arguments
=========

``udriver``
    USB operations of the device driver to unregister


Context
=======

must be able to sleep


Description
===========

Unlinks the specified driver from the internal USB driver list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
