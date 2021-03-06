.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/usbstring.c

.. _`usb_gadget_get_string`:

usb_gadget_get_string
=====================

.. c:function:: int usb_gadget_get_string(const struct usb_gadget_strings *table, int id, u8 *buf)

    fill out a string descriptor

    :param table:
        of c strings encoded using UTF-8
    :type table: const struct usb_gadget_strings \*

    :param id:
        string id, from low byte of wValue in get string descriptor
    :type id: int

    :param buf:
        at least 256 bytes, must be 16-bit aligned
    :type buf: u8 \*

.. _`usb_gadget_get_string.description`:

Description
-----------

Finds the UTF-8 string matching the ID, and converts it into a
string descriptor in utf16-le.
Returns length of descriptor (always even) or negative errno

If your driver needs stings in multiple languages, you'll probably
"switch (wIndex) { ... }"  in your ep0 string descriptor logic,
using this routine after choosing which set of UTF-8 strings to use.
Note that US-ASCII is a strict subset of UTF-8; any string bytes with
the eighth bit set will be multibyte UTF-8 characters, not ISO-8859/1
characters (which are also widely used in C strings).

.. This file was automatic generated / don't edit.

