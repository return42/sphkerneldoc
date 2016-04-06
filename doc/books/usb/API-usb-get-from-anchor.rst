
.. _API-usb-get-from-anchor:

===================
usb_get_from_anchor
===================

*man usb_get_from_anchor(9)*

*4.6.0-rc1*

get an anchor's oldest urb


Synopsis
========

.. c:function:: struct urb ⋆ usb_get_from_anchor( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    the anchor whose urb you want


Description
===========

This will take the oldest urb from an anchor, unanchor and return it


Return
======

The oldest urb from ``anchor``, or ``NULL`` if ``anchor`` has no urbs associated with it.
