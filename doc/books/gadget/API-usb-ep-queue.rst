
.. _API-usb-ep-queue:

============
usb_ep_queue
============

*man usb_ep_queue(9)*

*4.6.0-rc1*

queues (submits) an I/O request to an endpoint.


Synopsis
========

.. c:function:: int usb_ep_queue( struct usb_ep * ep, struct usb_request * req, gfp_t gfp_flags )

Arguments
=========

``ep``
    the endpoint associated with the request

``req``
    the request being submitted

``gfp_flags``
    GFP_⋆ flags to use in case the lower level driver couldn't pre-allocate all necessary memory with the request.


Description
===========

This tells the device controller to perform the specified request through that endpoint (reading or writing a buffer). When the request completes, including being canceled by
``usb_ep_dequeue``, the request's completion routine is called to return the request to the driver. Any endpoint (except control endpoints like ep0) may have more than one transfer
request queued; they complete in FIFO order. Once a gadget driver submits a request, that request may not be examined or modified until it is given back to that driver through the
completion callback.

Each request is turned into one or more packets. The controller driver never merges adjacent requests into the same packet. OUT transfers will sometimes use data that's already
buffered in the hardware. Drivers can rely on the fact that the first byte of the request's buffer always corresponds to the first byte of some USB packet, for both IN and OUT
transfers.

Bulk endpoints can queue any amount of data; the transfer is packetized automatically. The last packet will be short if the request doesn't fill it out completely. Zero length
packets (ZLPs) should be avoided in portable protocols since not all usb hardware can successfully handle zero length packets. (ZLPs may be explicitly written, and may be
implicitly written if the request 'zero' flag is set.) Bulk endpoints may also be used for interrupt transfers; but the reverse is not true, and some endpoints won't support every
interrupt transfer. (Such as 768 byte packets.)

Interrupt-only endpoints are less functional than bulk endpoints, for example by not supporting queueing or not handling buffers that are larger than the endpoint's maxpacket size.
They may also treat data toggle differently.

Control endpoints ... after getting a ``setup`` callback, the driver queues one response (even if it would be zero length). That enables the status ack, after transferring data as
specified in the response. Setup functions may return negative error codes to generate protocol stalls. (Note that some USB device controllers disallow protocol stall responses in
some cases.) When control responses are deferred (the response is written after the setup callback returns), then ``usb_ep_set_halt`` may be used on ep0 to trigger protocol stalls.
Depending on the controller, it may not be possible to trigger a status-stage protocol stall when the data stage is over, that is, from within the response's completion routine.

For periodic endpoints, like interrupt or isochronous ones, the usb host arranges to poll once per interval, and the gadget driver usually will have queued some data to transfer at
that time.

Returns zero, or a negative error code. Endpoints that are not enabled report errors; errors will also be reported when the usb peripheral is disconnected.
