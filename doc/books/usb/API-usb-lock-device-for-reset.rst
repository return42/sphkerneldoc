
.. _API-usb-lock-device-for-reset:

=========================
usb_lock_device_for_reset
=========================

*man usb_lock_device_for_reset(9)*

*4.6.0-rc1*

cautiously acquire the lock for a usb device structure


Synopsis
========

.. c:function:: int usb_lock_device_for_reset( struct usb_device * udev, const struct usb_interface * iface )

Arguments
=========

``udev``
    device that's being locked

``iface``
    interface bound to the driver making the request (optional)


Description
===========

Attempts to acquire the device lock, but fails if the device is NOTATTACHED or SUSPENDED, or if iface is specified and the interface is neither BINDING nor BOUND. Rather than
sleeping to wait for the lock, the routine polls repeatedly. This is to prevent deadlock with disconnect; in some drivers (such as usb-storage) the ``disconnect`` or ``suspend``
method will block waiting for a device reset to complete.


Return
======

A negative error code for failure, otherwise 0.
