.. -*- coding: utf-8; mode: rst -*-

.. _API---media-device-usb-init:

=======================
__media_device_usb_init
=======================

*man __media_device_usb_init(9)*

*4.6.0-rc5*

create and initialize a struct ``media_device`` from a PCI device.


Synopsis
========

.. c:function:: void __media_device_usb_init( struct media_device * mdev, struct usb_device * udev, const char * board_name, const char * driver_name )

Arguments
=========

``mdev``
    pointer to struct ``media_device``

``udev``
    pointer to struct usb_device

``board_name``
    media device name. If ``NULL``, the routine will use the usb product
    name, if available.

``driver_name``
    name of the driver. if ``NULL``, the routine will use the name given
    by udev->dev->driver->name, with is usually the wrong thing to do.


NOTE
====

It is better to call ``media_device_usb_init`` instead, as such macro
fills driver_name with ``KBUILD_MODNAME``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
