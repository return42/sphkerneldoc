.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-init-queue:

==============
blk_init_queue
==============

*man blk_init_queue(9)*

*4.6.0-rc5*

prepare a request queue for use with a block device


Synopsis
========

.. c:function:: struct request_queue * blk_init_queue( request_fn_proc * rfn, spinlock_t * lock )

Arguments
=========

``rfn``
    The function to be called to process requests that have been placed
    on the queue.

``lock``
    Request queue spin lock


Description
===========

If a block device wishes to use the standard request handling
procedures, which sorts requests and coalesces adjacent requests, then
it must call ``blk_init_queue``. The function ``rfn`` will be called
when there are requests on the queue that need to be processed. If the
device supports plugging, then ``rfn`` may not be called immediately
when requests are available on the queue, but may be called at some time
later instead. Plugged queues are generally unplugged when a buffer
belonging to one of the requests on the queue is needed, or due to
memory pressure.

``rfn`` is not required, or even expected, to remove all requests off
the queue, but only as many as it can handle at a time. If it does leave
requests on the queue, it is responsible for arranging that the requests
get dealt with eventually.

The queue spin lock must be held while manipulating the requests on the
request queue; this lock will be taken also from interrupt context, so
irq disabling is needed for it.

Function returns a pointer to the initialized request queue, or ``NULL``
if it didn't succeed.


Note
====

``blk_init_queue`` must be paired with a ``blk_cleanup_queue`` call when
the block device is deactivated (such as at module unload).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
