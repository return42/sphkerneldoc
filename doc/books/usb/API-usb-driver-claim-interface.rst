
.. _API-usb-driver-claim-interface:

==========================
usb_driver_claim_interface
==========================

*man usb_driver_claim_interface(9)*

*4.6.0-rc1*

bind a driver to an interface


Synopsis
========

.. c:function:: int usb_driver_claim_interface( struct usb_driver * driver, struct usb_interface * iface, void * priv )

Arguments
=========

``driver``
    the driver to be bound

``iface``
    the interface to which it will be bound; must be in the usb device's active configuration

``priv``
    driver data associated with that interface


Description
===========

This is used by usb device drivers that need to claim more than one interface on a device when probing (audio and acm are current examples). No device driver should directly modify
internal usb_interface or usb_device structure members.

Few drivers should need to use this routine, since the most natural way to bind to an interface is to return the private data from the driver's ``probe`` method.

Callers must own the device lock, so driver ``probe`` entries don't need extra locking, but other call contexts may need to explicitly claim that lock.


Return
======

0 on success.
