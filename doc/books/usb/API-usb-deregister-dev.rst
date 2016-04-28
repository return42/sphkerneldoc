.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-deregister-dev:

==================
usb_deregister_dev
==================

*man usb_deregister_dev(9)*

*4.6.0-rc5*

deregister a USB device's dynamic minor.


Synopsis
========

.. c:function:: void usb_deregister_dev( struct usb_interface * intf, struct usb_class_driver * class_driver )

Arguments
=========

``intf``
    pointer to the usb_interface that is being deregistered

``class_driver``
    pointer to the usb_class_driver for this device


Description
===========

Used in conjunction with ``usb_register_dev``. This function is called
when the USB driver is finished with the minor numbers gotten from a
call to ``usb_register_dev`` (usually when the device is disconnected
from the system.)

This function also removes the usb class device from the sysfs tree.

This should be called by all drivers that use the USB major number.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
