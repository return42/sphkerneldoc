
.. _API-usb-disable-autosuspend:

=======================
usb_disable_autosuspend
=======================

*man usb_disable_autosuspend(9)*

*4.6.0-rc1*

prevent a USB device from being autosuspended


Synopsis
========

.. c:function:: void usb_disable_autosuspend( struct usb_device * udev )

Arguments
=========

``udev``
    the USB device which may not be autosuspended


Description
===========

This routine prevents ``udev`` from being autosuspended and wakes it up if it is already autosuspended.

The caller must hold ``udev``'s device lock.
