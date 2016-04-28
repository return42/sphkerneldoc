.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-ep-set-wedge:

================
usb_ep_set_wedge
================

*man usb_ep_set_wedge(9)*

*4.6.0-rc5*

sets the halt feature and ignores clear requests


Synopsis
========

.. c:function:: int usb_ep_set_wedge( struct usb_ep * ep )

Arguments
=========

``ep``
    the endpoint being wedged


Description
===========

Use this to stall an endpoint and ignore CLEAR_FEATURE(HALT_ENDPOINT)
requests. If the gadget driver clears the halt status, it will
automatically unwedge the endpoint.

Returns zero on success, else negative errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
