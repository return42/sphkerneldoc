
.. _API-usb-free-descriptors:

====================
usb_free_descriptors
====================

*man usb_free_descriptors(9)*

*4.6.0-rc1*

free descriptors returned by ``usb_copy_descriptors``


Synopsis
========

.. c:function:: void usb_free_descriptors( struct usb_descriptor_header ** v )

Arguments
=========

``v``
    vector of descriptors
