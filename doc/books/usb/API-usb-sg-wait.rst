
.. _API-usb-sg-wait:

===========
usb_sg_wait
===========

*man usb_sg_wait(9)*

*4.6.0-rc1*

synchronously execute scatter/gather request


Synopsis
========

.. c:function:: void usb_sg_wait( struct usb_sg_request * io )

Arguments
=========

``io``
    request block handle, as initialized with ``usb_sg_init``. some fields become accessible when this call returns.


Context
=======

!in_interrupt ()


Description
===========

This function blocks until the specified I/O operation completes. It leverages the grouping of the related I/O requests to get good transfer rates, by queueing the requests. At
higher speeds, such queuing can significantly improve USB throughput.

There are three kinds of completion for this function. (1) success, where io->status is zero. The number of io->bytes transferred is as requested. (2) error, where io->status is a
negative errno value. The number of io->bytes transferred before the error is usually less than requested, and can be nonzero. (3) cancellation, a type of error with status
-ECONNRESET that is initiated by ``usb_sg_cancel``.

When this function returns, all memory allocated through ``usb_sg_init`` or this call will have been freed. The request block parameter may still be passed to ``usb_sg_cancel``, or
it may be freed. It could also be reinitialized and then reused.


Data Transfer Rates
===================

Bulk transfers are valid for full or high speed endpoints. The best full speed data rate is 19 packets of 64 bytes each per frame, or 1216 bytes per millisecond. The best high
speed data rate is 13 packets of 512 bytes each per microframe, or 52 KBytes per millisecond.

The reason to use interrupt transfers through this API would most likely be to reserve high speed bandwidth, where up to 24 KBytes per millisecond could be transferred. That
capability is less useful for low or full speed interrupt endpoints, which allow at most one packet per millisecond, of at most 8 or 64 bytes (respectively).

It is not necessary to call this function to reserve bandwidth for devices under an xHCI host controller, as the bandwidth is reserved when the configuration or interface alt
setting is selected.
