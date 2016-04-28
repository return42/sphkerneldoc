.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-hcd-link-urb-to-ep:

======================
usb_hcd_link_urb_to_ep
======================

*man usb_hcd_link_urb_to_ep(9)*

*4.6.0-rc5*

add an URB to its endpoint queue


Synopsis
========

.. c:function:: int usb_hcd_link_urb_to_ep( struct usb_hcd * hcd, struct urb * urb )

Arguments
=========

``hcd``
    host controller to which ``urb`` was submitted

``urb``
    URB being submitted


Description
===========

Host controller drivers should call this routine in their ``enqueue``
method. The HCD's private spinlock must be held and interrupts must be
disabled. The actions carried out here are required for URB submission,
as well as for endpoint shutdown and for usb_kill_urb.


Return
======

0 for no error, otherwise a negative error code (in which case the
``enqueue`` method must fail). If no error occurs but ``enqueue`` fails
anyway, it must call ``usb_hcd_unlink_urb_from_ep`` before releasing the
private spinlock and returning.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
