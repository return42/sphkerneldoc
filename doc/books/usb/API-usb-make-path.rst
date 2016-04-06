
.. _API-usb-make-path:

=============
usb_make_path
=============

*man usb_make_path(9)*

*4.6.0-rc1*

returns stable device path in the usb tree


Synopsis
========

.. c:function:: int usb_make_path( struct usb_device * dev, char * buf, size_t size )

Arguments
=========

``dev``
    the device whose path is being constructed

``buf``
    where to put the string

``size``
    how big is “buf”?


Return
======

Length of the string (> 0) or negative if size was too small.


Note
====

This identifier is intended to be “stable”, reflecting physical paths in hardware such as physical bus addresses for host controllers or ports on USB hubs. That makes it stay the
same until systems are physically reconfigured, by re-cabling a tree of USB devices or by moving USB host controllers. Adding and removing devices, including virtual root hubs in
host controller driver modules, does not change these path identifiers; neither does rebooting or re-enumerating. These are more useful identifiers than changeable (“unstable”)
ones like bus numbers or device addresses.

With a partial exception for devices connected to USB 2.0 root hubs, these identifiers are also predictable. So long as the device tree isn't changed, plugging any USB device into
a given hub port always gives it the same path. Because of the use of “companion” controllers, devices connected to ports on USB 2.0 root hubs (EHCI host controllers) will get one
path ID if they are high speed, and a different one if they are full or low speed.
