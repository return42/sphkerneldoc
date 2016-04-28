.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-reset-endpoint:

==================
usb_reset_endpoint
==================

*man usb_reset_endpoint(9)*

*4.6.0-rc5*

Reset an endpoint's state.


Synopsis
========

.. c:function:: void usb_reset_endpoint( struct usb_device * dev, unsigned int epaddr )

Arguments
=========

``dev``
    the device whose endpoint is to be reset

``epaddr``
    the endpoint's address. Endpoint number for output, endpoint number
    + USB_DIR_IN for input


Description
===========

Resets any host-side endpoint state such as the toggle bit, sequence
number or current window.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
