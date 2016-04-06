
.. _API-usb-reset-device:

================
usb_reset_device
================

*man usb_reset_device(9)*

*4.6.0-rc1*

warn interface drivers and perform a USB port reset


Synopsis
========

.. c:function:: int usb_reset_device( struct usb_device * udev )

Arguments
=========

``udev``
    device to reset (not in SUSPENDED or NOTATTACHED state)


Description
===========

Warns all drivers bound to registered interfaces (using their pre_reset method), performs the port reset, and then lets the drivers know that the reset is over (using their
post_reset method).


Return
======

The same as for ``usb_reset_and_verify_device``.


Note
====

The caller must own the device lock. For example, it's safe to use this from a driver ``probe`` routine after downloading new firmware. For calls that might not occur during
``probe``, drivers should lock the device using ``usb_lock_device_for_reset``.

If an interface is currently being probed or disconnected, we assume its driver knows how to handle resets. For all other interfaces, if the driver doesn't have pre_reset and
post_reset methods then we attempt to unbind it and rebind afterward.
