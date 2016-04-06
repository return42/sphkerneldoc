
.. _API-usb-driver-release-interface:

============================
usb_driver_release_interface
============================

*man usb_driver_release_interface(9)*

*4.6.0-rc1*

unbind a driver from an interface


Synopsis
========

.. c:function:: void usb_driver_release_interface( struct usb_driver * driver, struct usb_interface * iface )

Arguments
=========

``driver``
    the driver to be unbound

``iface``
    the interface from which it will be unbound


Description
===========

This can be used by drivers to release an interface without waiting for their ``disconnect`` methods to be called. In typical cases this also causes the driver ``disconnect``
method to be called.

This call is synchronous, and may not be used in an interrupt context. Callers must own the device lock, so driver ``disconnect`` entries don't need extra locking, but other call
contexts may need to explicitly claim that lock.
