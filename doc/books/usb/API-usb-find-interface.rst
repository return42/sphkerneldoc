
.. _API-usb-find-interface:

==================
usb_find_interface
==================

*man usb_find_interface(9)*

*4.6.0-rc1*

find usb_interface pointer for driver and device


Synopsis
========

.. c:function:: struct usb_interface ⋆ usb_find_interface( struct usb_driver * drv, int minor )

Arguments
=========

``drv``
    the driver whose current configuration is considered

``minor``
    the minor number of the desired device


Description
===========

This walks the bus device list and returns a pointer to the interface with the matching minor and driver. Note, this only works for devices that share the USB major number.


Return
======

A pointer to the interface with the matching major and ``minor``.
