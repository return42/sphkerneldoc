.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-string:

=================
struct usb_string
=================

*man struct usb_string(9)*

*4.6.0-rc5*

wraps a C string and its USB id


Synopsis
========

.. code-block:: c

    struct usb_string {
      u8 id;
      const char * s;
    };


Members
=======

id
    the (nonzero) ID for this string

s
    the string, in UTF-8 encoding


Description
===========

If you're using ``usb_gadget_get_string``, use this to wrap a string
together with its ID.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
