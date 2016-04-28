.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-deactivate:

=====================
usb_gadget_deactivate
=====================

*man usb_gadget_deactivate(9)*

*4.6.0-rc5*

deactivate function which is not ready to work


Synopsis
========

.. c:function:: int usb_gadget_deactivate( struct usb_gadget * gadget )

Arguments
=========

``gadget``
    the peripheral being deactivated


Description
===========

This routine may be used during the gadget driver ``bind`` call to
prevent the peripheral from ever being visible to the USB host, unless
later ``usb_gadget_activate`` is called. For example, user mode
components may need to be activated before the system can talk to hosts.

Returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
