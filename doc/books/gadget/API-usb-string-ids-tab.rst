
.. _API-usb-string-ids-tab:

==================
usb_string_ids_tab
==================

*man usb_string_ids_tab(9)*

*4.6.0-rc1*

allocate unused string IDs in batch


Synopsis
========

.. c:function:: int usb_string_ids_tab( struct usb_composite_dev * cdev, struct usb_string * str )

Arguments
=========

``cdev``
    the device whose string descriptor IDs are being allocated

``str``
    an array of usb_string objects to assign numbers to


Context
=======

single threaded during gadget setup


Description
===========

``usb_string_ids``\ () is called from ``bind`` callbacks to allocate string IDs. Drivers for functions, configurations, or gadgets will then copy IDs from the string table to the
appropriate descriptors and string table for other languages.

All string identifier should be allocated using this, ``usb_string_id``\ () or ``usb_string_ids_n``\ () routine, to ensure that for example different functions don't wrongly assign
different meanings to the same identifier.
