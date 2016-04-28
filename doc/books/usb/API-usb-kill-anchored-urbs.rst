.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-kill-anchored-urbs:

======================
usb_kill_anchored_urbs
======================

*man usb_kill_anchored_urbs(9)*

*4.6.0-rc5*

cancel transfer requests en masse


Synopsis
========

.. c:function:: void usb_kill_anchored_urbs( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    anchor the requests are bound to


Description
===========

this allows all outstanding URBs to be killed starting from the back of
the queue

This routine should not be called by a driver after its disconnect
method has returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
