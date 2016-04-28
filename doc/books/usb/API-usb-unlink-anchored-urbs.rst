.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-unlink-anchored-urbs:

========================
usb_unlink_anchored_urbs
========================

*man usb_unlink_anchored_urbs(9)*

*4.6.0-rc5*

asynchronously cancel transfer requests en masse


Synopsis
========

.. c:function:: void usb_unlink_anchored_urbs( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    anchor the requests are bound to


Description
===========

this allows all outstanding URBs to be unlinked starting from the back
of the queue. This function is asynchronous. The unlinking is just
triggered. It may happen after this function has returned.

This routine should not be called by a driver after its disconnect
method has returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
