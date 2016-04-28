.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-autopm-get-interface-async:

==============================
usb_autopm_get_interface_async
==============================

*man usb_autopm_get_interface_async(9)*

*4.6.0-rc5*

increment a USB interface's PM-usage counter


Synopsis
========

.. c:function:: int usb_autopm_get_interface_async( struct usb_interface * intf )

Arguments
=========

``intf``
    the usb_interface whose counter should be incremented


Description
===========

This routine does much the same thing as ``usb_autopm_get_interface``:
It increments ``intf``'s usage counter and queues an autoresume request
if the device is suspended. The differences are that it does not perform
any synchronization (callers should hold a private lock and handle all
synchronization issues themselves), and it does not autoresume the
device directly (it only queues a request). After a successful call, the
device may not yet be resumed.

This routine can run in atomic context.


Return
======

0 on success. A negative error code otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
