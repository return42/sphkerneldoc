
.. _API-usb-anchor-empty:

================
usb_anchor_empty
================

*man usb_anchor_empty(9)*

*4.6.0-rc1*

is an anchor empty


Synopsis
========

.. c:function:: int usb_anchor_empty( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    the anchor you want to query


Return
======

1 if the anchor has no urbs associated with it.
