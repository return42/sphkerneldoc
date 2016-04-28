.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-string:

==========
usb_string
==========

*man usb_string(9)*

*4.6.0-rc5*

returns UTF-8 version of a string descriptor


Synopsis
========

.. c:function:: int usb_string( struct usb_device * dev, int index, char * buf, size_t size )

Arguments
=========

``dev``
    the device whose string descriptor is being retrieved

``index``
    the number of the descriptor

``buf``
    where to put the string

``size``
    how big is “buf”?


Context
=======

!in_interrupt ()


Description
===========

This converts the UTF-16LE encoded strings returned by devices, from
``usb_get_string_descriptor``, to null-terminated UTF-8 encoded ones
that are more usable in most kernel contexts. Note that this function
chooses strings in the first language supported by the device.

This call is synchronous, and may not be used in an interrupt context.


Return
======

length of the string (>= 0) or usb_control_msg status (< 0).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
