.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-register-driver:

===================
usb_register_driver
===================

*man usb_register_driver(9)*

*4.6.0-rc5*

register a USB interface driver


Synopsis
========

.. c:function:: int usb_register_driver( struct usb_driver * new_driver, struct module * owner, const char * mod_name )

Arguments
=========

``new_driver``
    USB operations for the interface driver

``owner``
    module owner of this driver.

``mod_name``
    module name string


Description
===========

Registers a USB interface driver with the USB core. The list of
unattached interfaces will be rescanned whenever a new driver is added,
allowing the new driver to attach to any recognized interfaces.


Return
======

A negative error code on failure and 0 on success.


NOTE
====

if you want your driver to use the USB major number, you must call
``usb_register_dev`` to enable that functionality. This function no
longer takes care of that.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
