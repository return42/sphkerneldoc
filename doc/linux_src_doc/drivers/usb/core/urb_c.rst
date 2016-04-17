.. -*- coding: utf-8; mode: rst -*-

=====
urb.c
=====


.. _`usb_init_urb`:

usb_init_urb
============

.. c:function:: void usb_init_urb (struct urb *urb)

    initializes a urb so that it can be used by a USB driver

    :param struct urb \*urb:
        pointer to the urb to initialize



.. _`usb_init_urb.description`:

Description
-----------

Initializes a urb so that the USB subsystem can use it properly.

If a urb is created with a call to :c:func:`usb_alloc_urb` it is not
necessary to call this function.  Only use this if you allocate the
space for a struct urb on your own.  If you call this function, be
careful when freeing the memory for your urb that it is no longer in
use by the USB core.

Only use this function if you _really_ understand what you are doing.



.. _`usb_alloc_urb`:

usb_alloc_urb
=============

.. c:function:: struct urb *usb_alloc_urb (int iso_packets, gfp_t mem_flags)

    creates a new urb for a USB driver to use

    :param int iso_packets:
        number of iso packets for this urb

    :param gfp_t mem_flags:
        the type of memory to allocate, see :c:func:`kmalloc` for a list of
        valid options for this.



.. _`usb_alloc_urb.description`:

Description
-----------

Creates an urb for the USB driver to use, initializes a few internal
structures, increments the usage counter, and returns a pointer to it.

If the driver want to use this urb for interrupt, control, or bulk
endpoints, pass '0' as the number of iso packets.

The driver must call :c:func:`usb_free_urb` when it is finished with the urb.



.. _`usb_alloc_urb.return`:

Return
------

A pointer to the new urb, or ``NULL`` if no memory is available.



.. _`usb_free_urb`:

usb_free_urb
============

.. c:function:: void usb_free_urb (struct urb *urb)

    frees the memory used by a urb when all users of it are finished

    :param struct urb \*urb:
        pointer to the urb to free, may be NULL



.. _`usb_free_urb.description`:

Description
-----------

Must be called when a user of a urb is finished with it.  When the last user
of the urb calls this function, the memory of the urb is freed.



.. _`usb_free_urb.note`:

Note
----

The transfer buffer associated with the urb is not freed unless the
URB_FREE_BUFFER transfer flag is set.



.. _`usb_get_urb`:

usb_get_urb
===========

.. c:function:: struct urb *usb_get_urb (struct urb *urb)

    increments the reference count of the urb

    :param struct urb \*urb:
        pointer to the urb to modify, may be NULL



.. _`usb_get_urb.description`:

Description
-----------

This must be  called whenever a urb is transferred from a device driver to a
host controller driver.  This allows proper reference counting to happen
for urbs.



.. _`usb_get_urb.return`:

Return
------

A pointer to the urb with the incremented reference counter.



.. _`usb_anchor_urb`:

usb_anchor_urb
==============

.. c:function:: void usb_anchor_urb (struct urb *urb, struct usb_anchor *anchor)

    anchors an URB while it is processed

    :param struct urb \*urb:
        pointer to the urb to anchor

    :param struct usb_anchor \*anchor:
        pointer to the anchor



.. _`usb_anchor_urb.description`:

Description
-----------

This can be called to have access to URBs which are to be executed
without bothering to track them



.. _`usb_unanchor_urb`:

usb_unanchor_urb
================

.. c:function:: void usb_unanchor_urb (struct urb *urb)

    unanchors an URB

    :param struct urb \*urb:
        pointer to the urb to anchor



.. _`usb_unanchor_urb.description`:

Description
-----------

Call this to stop the system keeping track of this URB



.. _`usb_submit_urb`:

usb_submit_urb
==============

.. c:function:: int usb_submit_urb (struct urb *urb, gfp_t mem_flags)

    issue an asynchronous transfer request for an endpoint

    :param struct urb \*urb:
        pointer to the urb describing the request

    :param gfp_t mem_flags:
        the type of memory to allocate, see :c:func:`kmalloc` for a list
        of valid options for this.



.. _`usb_submit_urb.description`:

Description
-----------

This submits a transfer request, and transfers control of the URB
describing that request to the USB subsystem.  Request completion will
be indicated later, asynchronously, by calling the completion handler.
The three types of completion are success, error, and unlink
(a software-induced fault, also called "request cancellation").

URBs may be submitted in interrupt context.

The caller must have correctly initialized the URB before submitting
it.  Functions such as :c:func:`usb_fill_bulk_urb` and :c:func:`usb_fill_control_urb` are
available to ensure that most fields are correctly initialized, for
the particular kind of transfer, although they will not initialize
any transfer flags.

If the submission is successful, the :c:func:`complete` callback from the URB
will be called exactly once, when the USB core and Host Controller Driver
(HCD) are finished with the URB.  When the completion function is called,
control of the URB is returned to the device driver which issued the
request.  The completion handler may then immediately free or reuse that
URB.

With few exceptions, USB device drivers should never access URB fields
provided by usbcore or the HCD until its :c:func:`complete` is called.
The exceptions relate to periodic transfer scheduling.  For both
interrupt and isochronous urbs, as part of successful URB submission
urb->interval is modified to reflect the actual transfer period used
(normally some power of two units).  And for isochronous urbs,
urb->start_frame is modified to reflect when the URB's transfers were
scheduled to start.

Not all isochronous transfer scheduling policies will work, but most
host controller drivers should easily handle ISO queues going from now
until 10-200 msec into the future.  Drivers should try to keep at
least one or two msec of data in the queue; many controllers require
that new transfers start at least 1 msec in the future when they are
added.  If the driver is unable to keep up and the queue empties out,
the behavior for new submissions is governed by the URB_ISO_ASAP flag.
If the flag is set, or if the queue is idle, then the URB is always
assigned to the first available (and not yet expired) slot in the
endpoint's schedule.  If the flag is not set and the queue is active
then the URB is always assigned to the next slot in the schedule
following the end of the endpoint's previous URB, even if that slot is
in the past.  When a packet is assigned in this way to a slot that has
already expired, the packet is not transmitted and the corresponding
usb_iso_packet_descriptor's status field will return -EXDEV.  If this
would happen to all the packets in the URB, submission fails with a
-EXDEV error code.

For control endpoints, the synchronous :c:func:`usb_control_msg` call is
often used (in non-interrupt context) instead of this call.
That is often used through convenience wrappers, for the requests
that are standardized in the USB 2.0 specification.  For bulk
endpoints, a synchronous :c:func:`usb_bulk_msg` call is available.



.. _`usb_submit_urb.return`:

Return
------

0 on successful submissions. A negative error number otherwise.



.. _`usb_submit_urb.request-queuing`:

Request Queuing
---------------


URBs may be submitted to endpoints before previous ones complete, to
minimize the impact of interrupt latencies and system overhead on data
throughput.  With that queuing policy, an endpoint's queue would never
be empty.  This is required for continuous isochronous data streams,
and may also be required for some kinds of interrupt transfers. Such
queuing also maximizes bandwidth utilization by letting USB controllers
start work on later requests before driver software has finished the
completion processing for earlier (successful) requests.

As of Linux 2.6, all USB endpoint transfer queues support depths greater
than one.  This was previously a HCD-specific behavior, except for ISO
transfers.  Non-isochronous endpoint queues are inactive during cleanup
after faults (transfer errors or cancellation).



.. _`usb_submit_urb.reserved-bandwidth-transfers`:

Reserved Bandwidth Transfers
----------------------------


Periodic transfers (interrupt or isochronous) are performed repeatedly,
using the interval specified in the urb.  Submitting the first urb to
the endpoint reserves the bandwidth necessary to make those transfers.
If the USB subsystem can't allocate sufficient bandwidth to perform
the periodic request, submitting such a periodic request should fail.

For devices under xHCI, the bandwidth is reserved at configuration time, or
when the alt setting is selected.  If there is not enough bus bandwidth, the
configuration/alt setting request will fail.  Therefore, submissions to
periodic endpoints on devices under xHCI should never fail due to bandwidth
constraints.

Device drivers must explicitly request that repetition, by ensuring that
some URB is always on the endpoint's queue (except possibly for short
periods during completion callbacks).  When there is no longer an urb
queued, the endpoint's bandwidth reservation is canceled.  This means
drivers can use their completion handlers to ensure they keep bandwidth
they need, by reinitializing and resubmitting the just-completed urb
until the driver longer needs that periodic bandwidth.



.. _`usb_submit_urb.memory-flags`:

Memory Flags
------------


The general rules for how to decide which mem_flags to use
are the same as for kmalloc.  There are four
different possible values; GFP_KERNEL, GFP_NOFS, GFP_NOIO and
GFP_ATOMIC.

GFP_NOFS is not ever used, as it has not been implemented yet.

GFP_ATOMIC is used when
(a) you are inside a completion handler, an interrupt, bottom half,
tasklet or timer, or
(b) you are holding a spinlock or rwlock (does not apply to
semaphores), or
(c) current->state != TASK_RUNNING, this is the case only after
you've changed it.

GFP_NOIO is used in the block io path and error handling of storage
devices.

All other situations use GFP_KERNEL.

Some more specific rules for mem_flags can be inferred, such as
(1) start_xmit, timeout, and receive methods of network drivers must
use GFP_ATOMIC (they are called with a spinlock held);
(2) queuecommand methods of scsi drivers must use GFP_ATOMIC (also
called with a spinlock held);
(3) If you use a kernel thread with a network driver you must use
GFP_NOIO, unless (b) or (c) apply;
(4) after you have done a :c:func:`down` you can use GFP_KERNEL, unless (b) or (c)
apply or your are in a storage driver's block io path;
(5) USB probe and disconnect can use GFP_KERNEL unless (b) or (c) apply; and
(6) changing firmware on a running storage or net device uses
GFP_NOIO, unless b) or c) apply



.. _`usb_unlink_urb`:

usb_unlink_urb
==============

.. c:function:: int usb_unlink_urb (struct urb *urb)

    abort/cancel a transfer request for an endpoint

    :param struct urb \*urb:
        pointer to urb describing a previously submitted request,
        may be NULL



.. _`usb_unlink_urb.description`:

Description
-----------

This routine cancels an in-progress request.  URBs complete only once
per submission, and may be canceled only once per submission.
Successful cancellation means termination of ``urb`` will be expedited
and the completion handler will be called with a status code
indicating that the request has been canceled (rather than any other
code).

Drivers should not call this routine or related routines, such as
:c:func:`usb_kill_urb` or :c:func:`usb_unlink_anchored_urbs`, after their disconnect
method has returned.  The disconnect function should synchronize with
a driver's I/O routines to insure that all URB-related activity has
completed before it returns.

This request is asynchronous, however the HCD might call the ->:c:func:`complete`
callback during unlink. Therefore when drivers call :c:func:`usb_unlink_urb`, they
must not hold any locks that may be taken by the completion function.
Success is indicated by returning -EINPROGRESS, at which time the URB will
probably not yet have been given back to the device driver. When it is
eventually called, the completion function will see ``urb``\ ->status ==
-ECONNRESET.
Failure is indicated by :c:func:`usb_unlink_urb` returning any other value.
Unlinking will fail when ``urb`` is not currently "linked" (i.e., it was
never submitted, or it was unlinked before, or the hardware is already
finished with it), even if the completion handler has not yet run.

The URB must not be deallocated while this routine is running.  In
particular, when a driver calls this routine, it must insure that the
completion handler cannot deallocate the URB.



.. _`usb_unlink_urb.return`:

Return
------

-EINPROGRESS on success. See description for other values on
failure.



.. _`usb_unlink_urb.unlinking-and-endpoint-queues`:

Unlinking and Endpoint Queues
-----------------------------


[The behaviors and guarantees described below do not apply to virtual
root hubs but only to endpoint queues for physical USB devices.]

Host Controller Drivers (HCDs) place all the URBs for a particular
endpoint in a queue.  Normally the queue advances as the controller
hardware processes each request.  But when an URB terminates with an
error its queue generally stops (see below), at least until that URB's
completion routine returns.  It is guaranteed that a stopped queue
will not restart until all its unlinked URBs have been fully retired,
with their completion routines run, even if that's not until some time
after the original completion handler returns.  The same behavior and
guarantee apply when an URB terminates because it was unlinked.

Bulk and interrupt endpoint queues are guaranteed to stop whenever an
URB terminates with any sort of error, including -ECONNRESET, -ENOENT,
and -EREMOTEIO.  Control endpoint queues behave the same way except
that they are not guaranteed to stop for -EREMOTEIO errors.  Queues
for isochronous endpoints are treated differently, because they must
advance at fixed rates.  Such queues do not stop when an URB
encounters an error or is unlinked.  An unlinked isochronous URB may
leave a gap in the stream of packets; it is undefined whether such
gaps can be filled in.

Note that early termination of an URB because a short packet was
received will generate a -EREMOTEIO error if and only if the
URB_SHORT_NOT_OK flag is set.  By setting this flag, USB device
drivers can build deep queues for large or complex bulk transfers
and clean them up reliably after any sort of aborted transfer by
unlinking all pending URBs at the first fault.

When a control URB terminates with an error other than -EREMOTEIO, it
is quite likely that the status stage of the transfer will not take
place.



.. _`usb_kill_urb`:

usb_kill_urb
============

.. c:function:: void usb_kill_urb (struct urb *urb)

    cancel a transfer request and wait for it to finish

    :param struct urb \*urb:
        pointer to URB describing a previously submitted request,
        may be NULL



.. _`usb_kill_urb.description`:

Description
-----------

This routine cancels an in-progress request.  It is guaranteed that
upon return all completion handlers will have finished and the URB
will be totally idle and available for reuse.  These features make
this an ideal way to stop I/O in a :c:func:`disconnect` callback or :c:func:`close`
function.  If the request has not already finished or been unlinked
the completion handler will see urb->status == -ENOENT.

While the routine is running, attempts to resubmit the URB will fail
with error -EPERM.  Thus even if the URB's completion handler always
tries to resubmit, it will not succeed and the URB will become idle.

The URB must not be deallocated while this routine is running.  In
particular, when a driver calls this routine, it must insure that the
completion handler cannot deallocate the URB.

This routine may not be used in an interrupt context (such as a bottom
half or a completion handler), or when holding a spinlock, or in other
situations where the caller can't :c:func:`schedule`.

This routine should not be called by a driver after its disconnect
method has returned.



.. _`usb_poison_urb`:

usb_poison_urb
==============

.. c:function:: void usb_poison_urb (struct urb *urb)

    reliably kill a transfer and prevent further use of an URB

    :param struct urb \*urb:
        pointer to URB describing a previously submitted request,
        may be NULL



.. _`usb_poison_urb.description`:

Description
-----------

This routine cancels an in-progress request.  It is guaranteed that
upon return all completion handlers will have finished and the URB
will be totally idle and cannot be reused.  These features make
this an ideal way to stop I/O in a :c:func:`disconnect` callback.
If the request has not already finished or been unlinked
the completion handler will see urb->status == -ENOENT.

After and while the routine runs, attempts to resubmit the URB will fail
with error -EPERM.  Thus even if the URB's completion handler always
tries to resubmit, it will not succeed and the URB will become idle.

The URB must not be deallocated while this routine is running.  In
particular, when a driver calls this routine, it must insure that the
completion handler cannot deallocate the URB.

This routine may not be used in an interrupt context (such as a bottom
half or a completion handler), or when holding a spinlock, or in other
situations where the caller can't :c:func:`schedule`.

This routine should not be called by a driver after its disconnect
method has returned.



.. _`usb_block_urb`:

usb_block_urb
=============

.. c:function:: void usb_block_urb (struct urb *urb)

    reliably prevent further use of an URB

    :param struct urb \*urb:
        pointer to URB to be blocked, may be NULL



.. _`usb_block_urb.description`:

Description
-----------

After the routine has run, attempts to resubmit the URB will fail
with error -EPERM.  Thus even if the URB's completion handler always
tries to resubmit, it will not succeed and the URB will become idle.

The URB must not be deallocated while this routine is running.  In
particular, when a driver calls this routine, it must insure that the
completion handler cannot deallocate the URB.



.. _`usb_kill_anchored_urbs`:

usb_kill_anchored_urbs
======================

.. c:function:: void usb_kill_anchored_urbs (struct usb_anchor *anchor)

    cancel transfer requests en masse

    :param struct usb_anchor \*anchor:
        anchor the requests are bound to



.. _`usb_kill_anchored_urbs.description`:

Description
-----------

this allows all outstanding URBs to be killed starting
from the back of the queue

This routine should not be called by a driver after its disconnect
method has returned.



.. _`usb_poison_anchored_urbs`:

usb_poison_anchored_urbs
========================

.. c:function:: void usb_poison_anchored_urbs (struct usb_anchor *anchor)

    cease all traffic from an anchor

    :param struct usb_anchor \*anchor:
        anchor the requests are bound to



.. _`usb_poison_anchored_urbs.description`:

Description
-----------

this allows all outstanding URBs to be poisoned starting
from the back of the queue. Newly added URBs will also be
poisoned

This routine should not be called by a driver after its disconnect
method has returned.



.. _`usb_unpoison_anchored_urbs`:

usb_unpoison_anchored_urbs
==========================

.. c:function:: void usb_unpoison_anchored_urbs (struct usb_anchor *anchor)

    let an anchor be used successfully again

    :param struct usb_anchor \*anchor:
        anchor the requests are bound to



.. _`usb_unpoison_anchored_urbs.description`:

Description
-----------

Reverses the effect of usb_poison_anchored_urbs
the anchor can be used normally after it returns



.. _`usb_unlink_anchored_urbs`:

usb_unlink_anchored_urbs
========================

.. c:function:: void usb_unlink_anchored_urbs (struct usb_anchor *anchor)

    asynchronously cancel transfer requests en masse

    :param struct usb_anchor \*anchor:
        anchor the requests are bound to



.. _`usb_unlink_anchored_urbs.description`:

Description
-----------

this allows all outstanding URBs to be unlinked starting
from the back of the queue. This function is asynchronous.
The unlinking is just triggered. It may happen after this
function has returned.

This routine should not be called by a driver after its disconnect
method has returned.



.. _`usb_anchor_suspend_wakeups`:

usb_anchor_suspend_wakeups
==========================

.. c:function:: void usb_anchor_suspend_wakeups (struct usb_anchor *anchor)

    :param struct usb_anchor \*anchor:
        the anchor you want to suspend wakeups on



.. _`usb_anchor_suspend_wakeups.description`:

Description
-----------

Call this to stop the last urb being unanchored from waking up any
usb_wait_anchor_empty_timeout waiters. This is used in the hcd urb give-
back path to delay waking up until after the completion handler has run.



.. _`usb_anchor_resume_wakeups`:

usb_anchor_resume_wakeups
=========================

.. c:function:: void usb_anchor_resume_wakeups (struct usb_anchor *anchor)

    :param struct usb_anchor \*anchor:
        the anchor you want to resume wakeups on



.. _`usb_anchor_resume_wakeups.description`:

Description
-----------

Allow usb_wait_anchor_empty_timeout waiters to be woken up again, and
wake up any current waiters if the anchor is empty.



.. _`usb_wait_anchor_empty_timeout`:

usb_wait_anchor_empty_timeout
=============================

.. c:function:: int usb_wait_anchor_empty_timeout (struct usb_anchor *anchor, unsigned int timeout)

    wait for an anchor to be unused

    :param struct usb_anchor \*anchor:
        the anchor you want to become unused

    :param unsigned int timeout:
        how long you are willing to wait in milliseconds



.. _`usb_wait_anchor_empty_timeout.description`:

Description
-----------

Call this is you want to be sure all an anchor's
URBs have finished



.. _`usb_wait_anchor_empty_timeout.return`:

Return
------

Non-zero if the anchor became unused. Zero on timeout.



.. _`usb_get_from_anchor`:

usb_get_from_anchor
===================

.. c:function:: struct urb *usb_get_from_anchor (struct usb_anchor *anchor)

    get an anchor's oldest urb

    :param struct usb_anchor \*anchor:
        the anchor whose urb you want



.. _`usb_get_from_anchor.description`:

Description
-----------

This will take the oldest urb from an anchor,
unanchor and return it



.. _`usb_get_from_anchor.return`:

Return
------

The oldest urb from ``anchor``\ , or ``NULL`` if ``anchor`` has no
urbs associated with it.



.. _`usb_scuttle_anchored_urbs`:

usb_scuttle_anchored_urbs
=========================

.. c:function:: void usb_scuttle_anchored_urbs (struct usb_anchor *anchor)

    unanchor all an anchor's urbs

    :param struct usb_anchor \*anchor:
        the anchor whose urbs you want to unanchor



.. _`usb_scuttle_anchored_urbs.description`:

Description
-----------

use this to get rid of all an anchor's urbs



.. _`usb_anchor_empty`:

usb_anchor_empty
================

.. c:function:: int usb_anchor_empty (struct usb_anchor *anchor)

    is an anchor empty

    :param struct usb_anchor \*anchor:
        the anchor you want to query



.. _`usb_anchor_empty.return`:

Return
------

1 if the anchor has no urbs associated with it.

