.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-get-maximum-speed:

=====================
usb_get_maximum_speed
=====================

*man usb_get_maximum_speed(9)*

*4.6.0-rc5*

Get maximum requested speed for a given USB controller.


Synopsis
========

.. c:function:: enum usb_device_speed usb_get_maximum_speed( struct device * dev )

Arguments
=========

``dev``
    Pointer to the given USB controller device


Description
===========

The function gets the maximum speed string from property
“maximum-speed”, and returns the corresponding enum usb_device_speed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
