
.. _API-usb-hcd-unlink-urb-from-ep:

==========================
usb_hcd_unlink_urb_from_ep
==========================

*man usb_hcd_unlink_urb_from_ep(9)*

*4.6.0-rc1*

remove an URB from its endpoint queue


Synopsis
========

.. c:function:: void usb_hcd_unlink_urb_from_ep( struct usb_hcd * hcd, struct urb * urb )

Arguments
=========

``hcd``
    host controller to which ``urb`` was submitted

``urb``
    URB being unlinked


Description
===========

Host controller drivers should call this routine before calling ``usb_hcd_giveback_urb``. The HCD's private spinlock must be held and interrupts must be disabled. The actions
carried out here are required for URB completion.
