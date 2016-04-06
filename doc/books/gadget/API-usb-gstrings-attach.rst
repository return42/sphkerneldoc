
.. _API-usb-gstrings-attach:

===================
usb_gstrings_attach
===================

*man usb_gstrings_attach(9)*

*4.6.0-rc1*

attach gadget strings to a cdev and assign ids


Synopsis
========

.. c:function:: struct usb_string ⋆ usb_gstrings_attach( struct usb_composite_dev * cdev, struct usb_gadget_strings ** sp, unsigned n_strings )

Arguments
=========

``cdev``
    the device whose string descriptor IDs are being allocated and attached.

``sp``
    an array of usb_gadget_strings to attach.

``n_strings``
    number of entries in each usb_strings array (sp[]->strings)


Description
===========

This function will create a deep copy of usb_gadget_strings and usb_string and attach it to the cdev. The actual string (usb_string.s) will not be copied but only a referenced
will be made. The struct usb_gadget_strings array may contain multiple languages and should be NULL terminated. The ->language pointer of each struct usb_gadget_strings has to
contain the same amount of entries.


For instance
============

sp[0] is en-US, sp[1] is es-ES. It is expected that the first usb_string entry of es-ES contains the translation of the first usb_string entry of en-US. Therefore both entries
become the same id assign.
