
.. _API-USB-INTERFACE-INFO:

==================
USB_INTERFACE_INFO
==================

*man USB_INTERFACE_INFO(9)*

*4.6.0-rc1*

macro used to describe a class of usb interfaces


Synopsis
========

.. c:function:: USB_INTERFACE_INFO( cl, sc, pr )

Arguments
=========

``cl``
    bInterfaceClass value

``sc``
    bInterfaceSubClass value

``pr``
    bInterfaceProtocol value


Description
===========

This macro is used to create a struct usb_device_id that matches a specific class of interfaces.
