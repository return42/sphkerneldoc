.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-enable-autosuspend:

======================
usb_enable_autosuspend
======================

*man usb_enable_autosuspend(9)*

*4.6.0-rc5*

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

This routine allows ``udev`` to be autosuspended. An autosuspend won't
take place until the autosuspend_delay has elapsed and all the other
necessary conditions are satisfied.

The caller must hold ``udev``'s device lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
