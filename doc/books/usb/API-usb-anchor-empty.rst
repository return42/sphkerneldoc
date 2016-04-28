.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-anchor-empty:

================
usb_anchor_empty
================

*man usb_anchor_empty(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
