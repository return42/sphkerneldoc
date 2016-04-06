
.. _API-usb-get-maximum-speed:

=====================
usb_get_maximum_speed
=====================

*man usb_get_maximum_speed(9)*

*4.6.0-rc1*

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

The function gets the maximum speed string from property “maximum-speed”, and returns the corresponding enum usb_device_speed.
