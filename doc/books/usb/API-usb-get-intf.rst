.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-get-intf:

============
usb_get_intf
============

*man usb_get_intf(9)*

*4.6.0-rc5*

increments the reference count of the usb interface structure


Synopsis
========

.. c:function:: struct usb_interface * usb_get_intf( struct usb_interface * intf )

Arguments
=========

``intf``
    the interface being referenced


Description
===========

Each live reference to a interface must be refcounted.

Drivers for USB interfaces should normally record such references in
their ``probe`` methods, when they bind to an interface, and release
them by calling ``usb_put_intf``, in their ``disconnect`` methods.


Return
======

A pointer to the interface with the incremented reference counter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
