
.. _API-usb-submit-urb:

==============
usb_submit_urb
==============

*man usb_submit_urb(9)*

*4.6.0-rc1*

issue an asynchronous transfer request for an endpoint


Synopsis
========

.. c:function:: int usb_submit_urb( struct urb * urb, gfp_t mem_flags )

Arguments
=========

``urb``
    pointer to the urb describing the request

``mem_flags``
    the type of memory to allocate, see ``kmalloc`` for a list of valid options for this.


Description
===========

This submits a transfer request, and transfers control of the URB describing that request to the USB subsystem. Request completion will be indicated later, asynchronously, by
calling the completion handler. The three types of completion are success, error, and unlink (a software-induced fault, also called “request cancellation”).

URBs may be submitted in interrupt context.

The caller must have correctly initialized the URB before submitting it. Functions such as ``usb_fill_bulk_urb`` and ``usb_fill_control_urb`` are available to ensure that most
fields are correctly initialized, for the particular kind of transfer, although they will not initialize any transfer flags.

If the submission is successful, the ``complete`` callback from the URB will be called exactly once, when the USB core and Host Controller Driver (HCD) are finished with the URB.
When the completion function is called, control of the URB is returned to the device driver which issued the request. The completion handler may then immediately free or reuse that
URB.

With few exceptions, USB device drivers should never access URB fields provided by usbcore or the HCD until its ``complete`` is called. The exceptions relate to periodic transfer
scheduling. For both interrupt and isochronous urbs, as part of successful URB submission urb->interval is modified to reflect the actual transfer period used (normally some power
of two units). And for isochronous urbs, urb->start_frame is modified to reflect when the URB's transfers were scheduled to start.

Not all isochronous transfer scheduling policies will work, but most host controller drivers should easily handle ISO queues going from now until 10-200 msec into the future.
Drivers should try to keep at least one or two msec of data in the queue; many controllers require that new transfers start at least 1 msec in the future when they are added. If
the driver is unable to keep up and the queue empties out, the behavior for new submissions is governed by the URB_ISO_ASAP flag. If the flag is set, or if the queue is idle,
then the URB is always assigned to the first available (and not yet expired) slot in the endpoint's schedule. If the flag is not set and the queue is active then the URB is always
assigned to the next slot in the schedule following the end of the endpoint's previous URB, even if that slot is in the past. When a packet is assigned in this way to a slot that
has already expired, the packet is not transmitted and the corresponding usb_iso_packet_descriptor's status field will return -EXDEV. If this would happen to all the packets in
the URB, submission fails with a -EXDEV error code.

For control endpoints, the synchronous ``usb_control_msg`` call is often used (in non-interrupt context) instead of this call. That is often used through convenience wrappers, for
the requests that are standardized in the USB 2.0 specification. For bulk endpoints, a synchronous ``usb_bulk_msg`` call is available.


Return
======

0 on successful submissions. A negative error number otherwise.


Request Queuing
===============

URBs may be submitted to endpoints before previous ones complete, to minimize the impact of interrupt latencies and system overhead on data throughput. With that queuing policy, an
endpoint's queue would never be empty. This is required for continuous isochronous data streams, and may also be required for some kinds of interrupt transfers. Such queuing also
maximizes bandwidth utilization by letting USB controllers start work on later requests before driver software has finished the completion processing for earlier (successful)
requests.

As of Linux 2.6, all USB endpoint transfer queues support depths greater than one. This was previously a HCD-specific behavior, except for ISO transfers. Non-isochronous endpoint
queues are inactive during cleanup after faults (transfer errors or cancellation).


Reserved Bandwidth Transfers
============================

Periodic transfers (interrupt or isochronous) are performed repeatedly, using the interval specified in the urb. Submitting the first urb to the endpoint reserves the bandwidth
necessary to make those transfers. If the USB subsystem can't allocate sufficient bandwidth to perform the periodic request, submitting such a periodic request should fail.

For devices under xHCI, the bandwidth is reserved at configuration time, or when the alt setting is selected. If there is not enough bus bandwidth, the configuration/alt setting
request will fail. Therefore, submissions to periodic endpoints on devices under xHCI should never fail due to bandwidth constraints.

Device drivers must explicitly request that repetition, by ensuring that some URB is always on the endpoint's queue (except possibly for short periods during completion callbacks).
When there is no longer an urb queued, the endpoint's bandwidth reservation is canceled. This means drivers can use their completion handlers to ensure they keep bandwidth they
need, by reinitializing and resubmitting the just-completed urb until the driver longer needs that periodic bandwidth.


Memory Flags
============

The general rules for how to decide which mem_flags to use are the same as for kmalloc. There are four different possible values; GFP_KERNEL, GFP_NOFS, GFP_NOIO and
GFP_ATOMIC.

GFP_NOFS is not ever used, as it has not been implemented yet.

GFP_ATOMIC is used when (a) you are inside a completion handler, an interrupt, bottom half, tasklet or timer, or (b) you are holding a spinlock or rwlock (does not apply to
semaphores), or (c) current->state != TASK_RUNNING, this is the case only after you've changed it.

GFP_NOIO is used in the block io path and error handling of storage devices.

All other situations use GFP_KERNEL.

Some more specific rules for mem_flags can be inferred, such as (1) start_xmit, timeout, and receive methods of network drivers must use GFP_ATOMIC (they are called with a
spinlock held); (2) queuecommand methods of scsi drivers must use GFP_ATOMIC (also called with a spinlock held); (3) If you use a kernel thread with a network driver you must use
GFP_NOIO, unless (b) or (c) apply; (4) after you have done a ``down`` you can use GFP_KERNEL, unless (b) or (c) apply or your are in a storage driver's block io path; (5) USB
probe and disconnect can use GFP_KERNEL unless (b) or (c) apply; and (6) changing firmware on a running storage or net device uses GFP_NOIO, unless b) or c) apply
