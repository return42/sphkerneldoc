
.. _API-usb-enable-autosuspend:

======================
usb_enable_autosuspend
======================

*man usb_enable_autosuspend(9)*

*4.6.0-rc1*

allow a USB device to be autosuspended


Synopsis
========

.. c:function:: void usb_enable_autosuspend( struct usb_device * udev )

Arguments
=========

``udev``
    the USB device which may be autosuspended


Description
===========

This routine allows ``udev`` to be autosuspended. An autosuspend won't take place until the autosuspend_delay has elapsed and all the other necessary conditions are satisfied.

The caller must hold ``udev``'s device lock.
