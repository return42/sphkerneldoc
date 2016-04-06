
.. _API-usb-driver-set-configuration:

============================
usb_driver_set_configuration
============================

*man usb_driver_set_configuration(9)*

*4.6.0-rc1*

Provide a way for drivers to change device configurations


Synopsis
========

.. c:function:: int usb_driver_set_configuration( struct usb_device * udev, int config )

Arguments
=========

``udev``
    the device whose configuration is being updated

``config``
    the configuration being chosen.


Context
=======

In process context, must be able to sleep


Description
===========

Device interface drivers are not allowed to change device configurations. This is because changing configurations will destroy the interface the driver is bound to and create new
ones; it would be like a floppy-disk driver telling the computer to replace the floppy-disk drive with a tape drive!

Still, in certain specialized circumstances the need may arise. This routine gets around the normal restrictions by using a work thread to submit the change-config request.


Return
======

0 if the request was successfully queued, error code otherwise. The caller has no way to know whether the queued request will eventually succeed.
