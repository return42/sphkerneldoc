.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-autopm-put-interface-async:

==============================
usb_autopm_put_interface_async
==============================

*man usb_autopm_put_interface_async(9)*

*4.6.0-rc5*

decrement a USB interface's PM-usage counter


Synopsis
========

.. c:function:: void usb_autopm_put_interface_async( struct usb_interface * intf )

Arguments
=========

``intf``
    the usb_interface whose counter should be decremented


Description
===========

This routine does much the same thing as ``usb_autopm_put_interface``:
It decrements ``intf``'s usage counter and schedules a delayed
autosuspend request if the counter is <= 0. The difference is that it
does not perform any synchronization; callers should hold a private lock
and handle all synchronization issues themselves.

Typically a driver would call this routine during an URB's completion
handler, if no more URBs were pending.

This routine can run in atomic context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
