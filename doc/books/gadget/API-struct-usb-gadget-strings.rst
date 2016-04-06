
.. _API-struct-usb-gadget-strings:

=========================
struct usb_gadget_strings
=========================

*man struct usb_gadget_strings(9)*

*4.6.0-rc1*

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

If you're using ``usb_gadget_get_string``, use this to wrap all the strings for a given language.
