
.. _API-struct-usb-os-desc-table:

========================
struct usb_os_desc_table
========================

*man struct usb_os_desc_table(9)*

*4.6.0-rc1*

describes OS descriptors associated with one interface of a usb_function


Synopsis
========

.. code-block:: c

    struct usb_os_desc_table {
      int if_id;
      struct usb_os_desc * os_desc;
    };


Members
=======

if_id
    Interface id

os_desc
    "Extended Compatibility ID“and”Extended Properties" of the interface


Description
===========

Each interface can have at most one “Extended Compatibility ID” and a number of “Extended Properties”.
