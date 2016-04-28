.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-composite-unregister:

========================
usb_composite_unregister
========================

*man usb_composite_unregister(9)*

*4.6.0-rc5*

unregister a composite driver


Synopsis
========

.. c:function:: void usb_composite_unregister( struct usb_composite_driver * driver )

Arguments
=========

``driver``
    the driver to unregister


Description
===========

This function is used to unregister drivers using the composite driver
framework.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
