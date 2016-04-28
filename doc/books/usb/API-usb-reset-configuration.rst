.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-reset-configuration:

=======================
usb_reset_configuration
=======================

*man usb_reset_configuration(9)*

*4.6.0-rc5*

lightweight device reset


Synopsis
========

.. c:function:: int usb_reset_configuration( struct usb_device * dev )

Arguments
=========

``dev``
    the device whose configuration is being reset


Description
===========

This issues a standard SET_CONFIGURATION request to the device using
the current configuration. The effect is to reset most USB-related state
in the device, including interface altsettings (reset to zero), endpoint
halts (cleared), and endpoint state (only for bulk and interrupt
endpoints). Other usbcore state is unchanged, including bindings of usb
device drivers to interfaces.

Because this affects multiple interfaces, avoid using this with
composite (multi-interface) devices. Instead, the driver for each
interface may use ``usb_set_interface`` on the interfaces it claims. Be
careful though; some devices don't support the SET_INTERFACE request,
and others won't reset all the interface state (notably endpoint state).
Resetting the whole configuration would affect other drivers'
interfaces.

The caller must own the device lock.


Return
======

Zero on success, else a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
