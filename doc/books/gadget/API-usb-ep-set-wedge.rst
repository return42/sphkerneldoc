
.. _API-usb-ep-set-wedge:

================
usb_ep_set_wedge
================

*man usb_ep_set_wedge(9)*

*4.6.0-rc1*

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

Use this to stall an endpoint and ignore CLEAR_FEATURE(HALT_ENDPOINT) requests. If the gadget driver clears the halt status, it will automatically unwedge the endpoint.

Returns zero on success, else negative errno.
