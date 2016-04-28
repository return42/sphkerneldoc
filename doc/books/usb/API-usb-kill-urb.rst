.. -*- coding: utf-8; mode: rst -*-

.. _API-usb-kill-urb:

============
usb_kill_urb
============

*man usb_kill_urb(9)*

*4.6.0-rc5*

cancel a transfer request and wait for it to finish


Synopsis
========

.. c:function:: void usb_kill_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to URB describing a previously submitted request, may be
    NULL


Description
===========

This routine cancels an in-progress request. It is guaranteed that upon
return all completion handlers will have finished and the URB will be
totally idle and available for reuse. These features make this an ideal
way to stop I/O in a ``disconnect`` callback or ``close`` function. If
the request has not already finished or been unlinked the completion
handler will see urb->status == -ENOENT.

While the routine is running, attempts to resubmit the URB will fail
with error -EPERM. Thus even if the URB's completion handler always
tries to resubmit, it will not succeed and the URB will become idle.

The URB must not be deallocated while this routine is running. In
particular, when a driver calls this routine, it must insure that the
completion handler cannot deallocate the URB.

This routine may not be used in an interrupt context (such as a bottom
half or a completion handler), or when holding a spinlock, or in other
situations where the caller can't ``schedule``.

This routine should not be called by a driver after its disconnect
method has returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
