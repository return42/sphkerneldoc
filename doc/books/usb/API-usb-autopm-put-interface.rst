.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-autopm-put-interface:

========================
usb_autopm_put_interface
========================

*man usb_autopm_put_interface(9)*

*4.6.0-rc5*

decrement a USB interface's PM-usage counter


Synopsis
========

.. c:function:: void usb_autopm_put_interface( struct usb_interface * intf )

Arguments
=========

``intf``
    the usb_interface whose counter should be decremented


Description
===========

This routine should be called by an interface driver when it is finished
using ``intf`` and wants to allow it to autosuspend. A typical example
would be a character-device driver when its device file is closed.

The routine decrements ``intf``'s usage counter. When the counter
reaches 0, a delayed autosuspend request for ``intf``'s device is
attempted. The attempt may fail (see ``autosuspend_check``).

This routine can run only in process context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
