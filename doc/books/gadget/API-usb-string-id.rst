.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-string-id:

=============
usb_string_id
=============

*man usb_string_id(9)*

*4.6.0-rc5*

allocate an unused string ID


Synopsis
========

.. c:function:: int usb_string_id( struct usb_composite_dev * cdev )

Arguments
=========

``cdev``
    the device whose string descriptor IDs are being allocated


Context
=======

single threaded during gadget setup


Description
===========

``usb_string_id``\ () is called from ``bind`` callbacks to allocate
string IDs. Drivers for functions, configurations, or gadgets will then
store that ID in the appropriate descriptors and string table.

All string identifier should be allocated using this,
``usb_string_ids_tab``\ () or ``usb_string_ids_n``\ () routine, to
ensure that for example different functions don't wrongly assign
different meanings to the same identifier.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
