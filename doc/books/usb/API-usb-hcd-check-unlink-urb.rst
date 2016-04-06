
.. _API-usb-hcd-check-unlink-urb:

========================
usb_hcd_check_unlink_urb
========================

*man usb_hcd_check_unlink_urb(9)*

*4.6.0-rc1*

check whether an URB may be unlinked


Synopsis
========

.. c:function:: int usb_hcd_check_unlink_urb( struct usb_hcd * hcd, struct urb * urb, int status )

Arguments
=========

``hcd``
    host controller to which ``urb`` was submitted

``urb``
    URB being checked for unlinkability

``status``
    error code to store in ``urb`` if the unlink succeeds


Description
===========

Host controller drivers should call this routine in their ``dequeue`` method. The HCD's private spinlock must be held and interrupts must be disabled. The actions carried out here
are required for making sure than an unlink is valid.


Return
======

0 for no error, otherwise a negative error code (in which case the ``dequeue`` method must fail). The possible error codes are:

-EIDRM: ``urb`` was not submitted or has already completed. The completion function may not have been called yet.

-EBUSY: ``urb`` has already been unlinked.
