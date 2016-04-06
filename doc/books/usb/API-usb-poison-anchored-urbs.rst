
.. _API-usb-poison-anchored-urbs:

========================
usb_poison_anchored_urbs
========================

*man usb_poison_anchored_urbs(9)*

*4.6.0-rc1*

cease all traffic from an anchor


Synopsis
========

.. c:function:: void usb_poison_anchored_urbs( struct usb_anchor * anchor )

Arguments
=========

``anchor``
    anchor the requests are bound to


Description
===========

this allows all outstanding URBs to be poisoned starting from the back of the queue. Newly added URBs will also be poisoned

This routine should not be called by a driver after its disconnect method has returned.
