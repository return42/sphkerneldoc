.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-usb-ep-caps:

==================
struct usb_ep_caps
==================

*man struct usb_ep_caps(9)*

*4.6.0-rc5*

endpoint capabilities description


Synopsis
========

.. code-block:: c

    struct usb_ep_caps {
      unsigned type_control:1;
      unsigned type_iso:1;
      unsigned type_bulk:1;
      unsigned type_int:1;
      unsigned dir_in:1;
      unsigned dir_out:1;
    };


Members
=======

type_control
    Endpoint supports control type (reserved for ep0).

type_iso
    Endpoint supports isochronous transfers.

type_bulk
    Endpoint supports bulk transfers.

type_int
    Endpoint supports interrupt transfers.

dir_in
    Endpoint supports IN direction.

dir_out
    Endpoint supports OUT direction.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
