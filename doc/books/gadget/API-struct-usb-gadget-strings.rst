.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-gadget-strings:

=========================
struct usb_gadget_strings
=========================

*man struct usb_gadget_strings(9)*

*4.6.0-rc5*

a set of USB strings in a given language


Synopsis
========

.. code-block:: c

    struct usb_gadget_strings {
      u16 language;
      struct usb_string * strings;
    };


Members
=======

language
    identifies the strings' language (0x0409 for en-us)

strings
    array of strings with their ids


Description
===========

If you're using ``usb_gadget_get_string``, use this to wrap all the
strings for a given language.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
