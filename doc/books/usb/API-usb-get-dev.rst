.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-get-dev:

===========
usb_get_dev
===========

*man usb_get_dev(9)*

*4.6.0-rc5*

increments the reference count of the usb device structure


Synopsis
========

.. c:function:: struct usb_device * usb_get_dev( struct usb_device * dev )

Arguments
=========

``dev``
    the device being referenced


Description
===========

Each live reference to a device should be refcounted.

Drivers for USB interfaces should normally record such references in
their ``probe`` methods, when they bind to an interface, and release
them by calling ``usb_put_dev``, in their ``disconnect`` methods.


Return
======

A pointer to the device with the incremented reference counter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
