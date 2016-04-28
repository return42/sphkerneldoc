.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-register-dev:

================
usb_register_dev
================

*man usb_register_dev(9)*

*4.6.0-rc5*

register a USB device, and ask for a minor number


Synopsis
========

.. c:function:: int usb_register_dev( struct usb_interface * intf, struct usb_class_driver * class_driver )

Arguments
=========

``intf``
    pointer to the usb_interface that is being registered

``class_driver``
    pointer to the usb_class_driver for this device


Description
===========

This should be called by all USB drivers that use the USB major number.
If CONFIG_USB_DYNAMIC_MINORS is enabled, the minor number will be
dynamically allocated out of the list of available ones. If it is not
enabled, the minor number will be based on the next available free
minor, starting at the class_driver->minor_base.

This function also creates a usb class device in the sysfs tree.

``usb_deregister_dev`` must be called when the driver is done with the
minor numbers given out by this function.


Return
======

-EINVAL if something bad happens with trying to register a device, and 0
on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
