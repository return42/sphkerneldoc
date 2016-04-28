.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-deregister:

==============
usb_deregister
==============

*man usb_deregister(9)*

*4.6.0-rc5*

unregister a USB interface driver


Synopsis
========

.. c:function:: void usb_deregister( struct usb_driver * driver )

Arguments
=========

``driver``
    USB operations of the interface driver to unregister


Context
=======

must be able to sleep


Description
===========

Unlinks the specified driver from the internal USB driver list.


NOTE
====

If you called ``usb_register_dev``, you still need to call
``usb_deregister_dev`` to clean up your driver's allocated minor
numbers, this * call will no longer do it for you.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
