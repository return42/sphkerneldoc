
.. _API-usb-for-each-dev:

================
usb_for_each_dev
================

*man usb_for_each_dev(9)*

*4.6.0-rc1*

iterate over all USB devices in the system


Synopsis
========

.. c:function:: int usb_for_each_dev( void * data, int (*fn) struct usb_device *, void * )

Arguments
=========

``data``
    data pointer that will be handed to the callback function

``fn``
    callback function to be called for each USB device


Description
===========

Iterate over all USB devices and call ``fn`` for each, passing it ``data``. If it returns anything other than 0, we break the iteration prematurely and return that value.
