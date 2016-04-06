
.. _API-usb-string-ids-n:

================
usb_string_ids_n
================

*man usb_string_ids_n(9)*

*4.6.0-rc1*

allocate unused string IDs in batch


Synopsis
========

.. c:function:: int usb_string_ids_n( struct usb_composite_dev * c, unsigned n )

Arguments
=========

``c``
    the device whose string descriptor IDs are being allocated

``n``
    number of string IDs to allocate


Context
=======

single threaded during gadget setup


Description
===========

Returns the first requested ID. This ID and next ``n``-1 IDs are now valid IDs. At least provided that ``n`` is non-zero because if it is, returns last requested ID which is now
very useful information.

``usb_string_ids_n``\ () is called from ``bind`` callbacks to allocate string IDs. Drivers for functions, configurations, or gadgets will then store that ID in the appropriate
descriptors and string table.

All string identifier should be allocated using this, ``usb_string_id``\ () or ``usb_string_ids_n``\ () routine, to ensure that for example different functions don't wrongly assign
different meanings to the same identifier.
