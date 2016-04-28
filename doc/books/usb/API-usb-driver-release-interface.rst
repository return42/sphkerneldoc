.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-driver-release-interface:

============================
usb_driver_release_interface
============================

*man usb_driver_release_interface(9)*

*4.6.0-rc5*

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

This can be used by drivers to release an interface without waiting for
their ``disconnect`` methods to be called. In typical cases this also
causes the driver ``disconnect`` method to be called.

This call is synchronous, and may not be used in an interrupt context.
Callers must own the device lock, so driver ``disconnect`` entries don't
need extra locking, but other call contexts may need to explicitly claim
that lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
