.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-gadget-get-string:

=====================
usb_gadget_get_string
=====================

*man usb_gadget_get_string(9)*

*4.6.0-rc5*

fill out a string descriptor


Synopsis
========

.. c:function:: int usb_gadget_get_string( struct usb_gadget_strings * table, int id, u8 * buf )

Arguments
=========

``table``
    of c strings encoded using UTF-8

``id``
    string id, from low byte of wValue in get string descriptor

``buf``
    at least 256 bytes, must be 16-bit aligned


Description
===========

Finds the UTF-8 string matching the ID, and converts it into a string
descriptor in utf16-le. Returns length of descriptor (always even) or
negative errno

If your driver needs stings in multiple languages, you'll probably
“switch (wIndex) { ... }” in your ep0 string descriptor logic, using
this routine after choosing which set of UTF-8 strings to use. Note that
US-ASCII is a strict subset of UTF-8; any string bytes with the eighth
bit set will be multibyte UTF-8 characters, not ISO-8859/1 characters
(which are also widely used in C strings).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
