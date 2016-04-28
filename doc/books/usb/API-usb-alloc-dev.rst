.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-alloc-dev:

=============
usb_alloc_dev
=============

*man usb_alloc_dev(9)*

*4.6.0-rc5*

usb device constructor (usbcore-internal)


Synopsis
========

.. c:function:: struct usb_device * usb_alloc_dev( struct usb_device * parent, struct usb_bus * bus, unsigned port1 )

Arguments
=========

``parent``
    hub to which device is connected; null to allocate a root hub

``bus``
    bus used to access the device

``port1``
    one-based index of port; ignored for root hubs


Context
=======

!\ ``in_interrupt``


Description
===========

Only hub drivers (including virtual root hub drivers for host
controllers) should ever call this.

This call may not be used in a non-sleeping context.


Return
======

On success, a pointer to the allocated usb device. ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
