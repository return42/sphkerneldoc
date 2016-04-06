
.. _API-usb-register-device-driver:

==========================
usb_register_device_driver
==========================

*man usb_register_device_driver(9)*

*4.6.0-rc1*

register a USB device (not interface) driver


Synopsis
========

.. c:function:: int usb_register_device_driver( struct usb_device_driver * new_udriver, struct module * owner )

Arguments
=========

``new_udriver``
    USB operations for the device driver

``owner``
    module owner of this driver.


Description
===========

Registers a USB device driver with the USB core. The list of unattached devices will be rescanned whenever a new driver is added, allowing the new driver to attach to any
recognized devices.


Return
======

A negative error code on failure and 0 on success.
