.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-function-activate:

=====================
usb_function_activate
=====================

*man usb_function_activate(9)*

*4.6.0-rc5*

allow function and gadget enumeration


Synopsis
========

.. c:function:: int usb_function_activate( struct usb_function * function )

Arguments
=========

``function``
    function on which ``usb_function_activate`` was called


Description
===========

Reverses effect of ``usb_function_deactivate``. If no more functions are
delaying their activation, the gadget driver will respond to host
enumeration procedures.

Returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
