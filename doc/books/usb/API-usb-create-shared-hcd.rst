.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-create-shared-hcd:

=====================
usb_create_shared_hcd
=====================

*man usb_create_shared_hcd(9)*

*4.6.0-rc5*

create and initialize an HCD structure


Synopsis
========

.. c:function:: struct usb_hcd * usb_create_shared_hcd( const struct hc_driver * driver, struct device * dev, const char * bus_name, struct usb_hcd * primary_hcd )

Arguments
=========

``driver``
    HC driver that will use this hcd

``dev``
    device for this HC, stored in hcd->self.controller

``bus_name``
    value to store in hcd->self.bus_name

``primary_hcd``
    a pointer to the usb_hcd structure that is sharing the PCI device.
    Only allocate certain resources for the primary HCD


Context
=======

!\ ``in_interrupt``


Description
===========

Allocate a struct usb_hcd, with extra space at the end for the HC
driver's private data. Initialize the generic members of the hcd
structure.


Return
======

On success, a pointer to the created and initialized HCD structure. On
failure (e.g. if memory is unavailable), ``NULL``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
