
.. _API-usb-unlink-urb:

==============
usb_unlink_urb
==============

*man usb_unlink_urb(9)*

*4.6.0-rc1*

abort/cancel a transfer request for an endpoint


Synopsis
========

.. c:function:: int usb_unlink_urb( struct urb * urb )

Arguments
=========

``urb``
    pointer to urb describing a previously submitted request, may be NULL


Description
===========

This routine cancels an in-progress request. URBs complete only once per submission, and may be canceled only once per submission. Successful cancellation means termination of
``urb`` will be expedited and the completion handler will be called with a status code indicating that the request has been canceled (rather than any other code).

Drivers should not call this routine or related routines, such as ``usb_kill_urb`` or ``usb_unlink_anchored_urbs``, after their disconnect method has returned. The disconnect
function should synchronize with a driver's I/O routines to insure that all URB-related activity has completed before it returns.

This request is asynchronous, however the HCD might call the ->``complete`` callback during unlink. Therefore when drivers call ``usb_unlink_urb``, they must not hold any locks
that may be taken by the completion function. Success is indicated by returning -EINPROGRESS, at which time the URB will probably not yet have been given back to the device driver.
When it is eventually called, the completion function will see ``urb``->status == -ECONNRESET. Failure is indicated by ``usb_unlink_urb`` returning any other value. Unlinking will
fail when ``urb`` is not currently “linked” (i.e., it was never submitted, or it was unlinked before, or the hardware is already finished with it), even if the completion handler
has not yet run.

The URB must not be deallocated while this routine is running. In particular, when a driver calls this routine, it must insure that the completion handler cannot deallocate the
URB.


Return
======

-EINPROGRESS on success. See description for other values on failure.


Unlinking and Endpoint Queues
=============================

[The behaviors and guarantees described below do not apply to virtual root hubs but only to endpoint queues for physical USB devices.]

Host Controller Drivers (HCDs) place all the URBs for a particular endpoint in a queue. Normally the queue advances as the controller hardware processes each request. But when an
URB terminates with an error its queue generally stops (see below), at least until that URB's completion routine returns. It is guaranteed that a stopped queue will not restart
until all its unlinked URBs have been fully retired, with their completion routines run, even if that's not until some time after the original completion handler returns. The same
behavior and guarantee apply when an URB terminates because it was unlinked.

Bulk and interrupt endpoint queues are guaranteed to stop whenever an URB terminates with any sort of error, including -ECONNRESET, -ENOENT, and -EREMOTEIO. Control endpoint queues
behave the same way except that they are not guaranteed to stop for -EREMOTEIO errors. Queues for isochronous endpoints are treated differently, because they must advance at fixed
rates. Such queues do not stop when an URB encounters an error or is unlinked. An unlinked isochronous URB may leave a gap in the stream of packets; it is undefined whether such
gaps can be filled in.

Note that early termination of an URB because a short packet was received will generate a -EREMOTEIO error if and only if the URB_SHORT_NOT_OK flag is set. By setting this flag,
USB device drivers can build deep queues for large or complex bulk transfers and clean them up reliably after any sort of aborted transfer by unlinking all pending URBs at the
first fault.

When a control URB terminates with an error other than -EREMOTEIO, it is quite likely that the status stage of the transfer will not take place.
