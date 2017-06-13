.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-core.c

.. _`blk_delay_queue`:

blk_delay_queue
===============

.. c:function:: void blk_delay_queue(struct request_queue *q, unsigned long msecs)

    restart queueing after defined interval

    :param struct request_queue \*q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question

    :param unsigned long msecs:
        Delay in msecs

.. _`blk_delay_queue.description`:

Description
-----------

  Sometimes queueing needs to be postponed for a little while, to allow
  resources to come back. This function will make sure that queueing is
  restarted around the specified time. Queue lock must be held.

.. _`blk_start_queue_async`:

blk_start_queue_async
=====================

.. c:function:: void blk_start_queue_async(struct request_queue *q)

    asynchronously restart a previously stopped queue

    :param struct request_queue \*q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question

.. _`blk_start_queue_async.description`:

Description
-----------

  \ :c:func:`blk_start_queue_async`\  will clear the stop flag on the queue, and
  ensure that the request_fn for the queue is run from an async
  context.

.. _`blk_start_queue`:

blk_start_queue
===============

.. c:function:: void blk_start_queue(struct request_queue *q)

    restart a previously stopped queue

    :param struct request_queue \*q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question

.. _`blk_start_queue.description`:

Description
-----------

  \ :c:func:`blk_start_queue`\  will clear the stop flag on the queue, and call
  the request_fn for the queue if it was in a stopped state when
  entered. Also see \ :c:func:`blk_stop_queue`\ . Queue lock must be held.

.. _`blk_stop_queue`:

blk_stop_queue
==============

.. c:function:: void blk_stop_queue(struct request_queue *q)

    stop a queue

    :param struct request_queue \*q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question

.. _`blk_stop_queue.description`:

Description
-----------

  The Linux block layer assumes that a block driver will consume all
  entries on the request queue when the request_fn strategy is called.
  Often this will not happen, because of hardware limitations (queue
  depth settings). If a device driver gets a 'queue full' response,
  or if it simply chooses not to queue more I/O at one point, it can
  call this function to prevent the request_fn from being called until
  the driver has signalled it's ready to go again. This happens by calling
  \ :c:func:`blk_start_queue`\  to restart queue operations. Queue lock must be held.

.. _`blk_sync_queue`:

blk_sync_queue
==============

.. c:function:: void blk_sync_queue(struct request_queue *q)

    cancel any pending callbacks on a queue

    :param struct request_queue \*q:
        the queue

.. _`blk_sync_queue.description`:

Description
-----------

    The block layer may perform asynchronous callback activity
    on a queue, such as calling the unplug function after a timeout.
    A block device may call blk_sync_queue to ensure that any
    such activity is cancelled, thus allowing it to release resources
    that the callbacks might use. The caller must already have made sure
    that its ->make_request_fn will not re-add plugging prior to calling
    this function.

    This function does not cancel any asynchronous activity arising
    out of elevator or throttling code. That would require \ :c:func:`elevator_exit`\ 
    and \ :c:func:`blkcg_exit_queue`\  to be called with queue lock initialized.

.. _`__blk_run_queue_uncond`:

__blk_run_queue_uncond
======================

.. c:function:: void __blk_run_queue_uncond(struct request_queue *q)

    run a queue whether or not it has been stopped

    :param struct request_queue \*q:
        The queue to run

.. _`__blk_run_queue_uncond.description`:

Description
-----------

   Invoke request handling on a queue if there are any pending requests.
   May be used to restart request handling after a request has completed.
   This variant runs the queue whether or not the queue has been
   stopped. Must be called with the queue lock held and interrupts
   disabled. See also \ ``blk_run_queue``\ .

.. _`__blk_run_queue`:

__blk_run_queue
===============

.. c:function:: void __blk_run_queue(struct request_queue *q)

    run a single device queue

    :param struct request_queue \*q:
        The queue to run

.. _`__blk_run_queue.description`:

Description
-----------

   See \ ``blk_run_queue``\ . This variant must be called with the queue lock
   held and interrupts disabled.

.. _`blk_run_queue_async`:

blk_run_queue_async
===================

.. c:function:: void blk_run_queue_async(struct request_queue *q)

    run a single device queue in workqueue context

    :param struct request_queue \*q:
        The queue to run

.. _`blk_run_queue_async.description`:

Description
-----------

   Tells kblockd to perform the equivalent of \ ``blk_run_queue``\  on behalf
   of us. The caller must hold the queue lock.

.. _`blk_run_queue`:

blk_run_queue
=============

.. c:function:: void blk_run_queue(struct request_queue *q)

    run a single device queue

    :param struct request_queue \*q:
        The queue to run

.. _`blk_run_queue.description`:

Description
-----------

   Invoke request handling on this queue, if it has pending work to do.
   May be used to restart queueing when a request has completed.

.. _`__blk_drain_queue`:

__blk_drain_queue
=================

.. c:function:: void __blk_drain_queue(struct request_queue *q, bool drain_all)

    drain requests from request_queue

    :param struct request_queue \*q:
        queue to drain

    :param bool drain_all:
        whether to drain all requests or only the ones w/ ELVPRIV

.. _`__blk_drain_queue.description`:

Description
-----------

Drain requests from \ ``q``\ .  If \ ``drain_all``\  is set, all requests are drained.
If not, only ELVPRIV requests are drained.  The caller is responsible
for ensuring that no new requests which need to be drained are queued.

.. _`blk_queue_bypass_start`:

blk_queue_bypass_start
======================

.. c:function:: void blk_queue_bypass_start(struct request_queue *q)

    enter queue bypass mode

    :param struct request_queue \*q:
        queue of interest

.. _`blk_queue_bypass_start.description`:

Description
-----------

In bypass mode, only the dispatch FIFO queue of \ ``q``\  is used.  This
function makes \ ``q``\  enter bypass mode and drains all requests which were
throttled or issued before.  On return, it's guaranteed that no request
is being throttled or has ELVPRIV set and \ :c:func:`blk_queue_bypass`\  \ ``true``\ 
inside queue or RCU read lock.

.. _`blk_queue_bypass_end`:

blk_queue_bypass_end
====================

.. c:function:: void blk_queue_bypass_end(struct request_queue *q)

    leave queue bypass mode

    :param struct request_queue \*q:
        queue of interest

.. _`blk_queue_bypass_end.description`:

Description
-----------

Leave bypass mode and restore the normal queueing behavior.

.. _`blk_cleanup_queue`:

blk_cleanup_queue
=================

.. c:function:: void blk_cleanup_queue(struct request_queue *q)

    shutdown a request queue

    :param struct request_queue \*q:
        request queue to shutdown

.. _`blk_cleanup_queue.description`:

Description
-----------

Mark \ ``q``\  DYING, drain all pending requests, mark \ ``q``\  DEAD, destroy and
put it.  All future requests will be failed immediately with -ENODEV.

.. _`blk_init_queue`:

blk_init_queue
==============

.. c:function:: struct request_queue *blk_init_queue(request_fn_proc *rfn, spinlock_t *lock)

    prepare a request queue for use with a block device

    :param request_fn_proc \*rfn:
        The function to be called to process requests that have been
        placed on the queue.

    :param spinlock_t \*lock:
        Request queue spin lock

.. _`blk_init_queue.description`:

Description
-----------

   If a block device wishes to use the standard request handling procedures,
   which sorts requests and coalesces adjacent requests, then it must
   call \ :c:func:`blk_init_queue`\ .  The function \ ``rfn``\  will be called when there
   are requests on the queue that need to be processed.  If the device
   supports plugging, then \ ``rfn``\  may not be called immediately when requests
   are available on the queue, but may be called at some time later instead.
   Plugged queues are generally unplugged when a buffer belonging to one
   of the requests on the queue is needed, or due to memory pressure.

   \ ``rfn``\  is not required, or even expected, to remove all requests off the
   queue, but only as many as it can handle at a time.  If it does leave
   requests on the queue, it is responsible for arranging that the requests
   get dealt with eventually.

   The queue spin lock must be held while manipulating the requests on the
   request queue; this lock will be taken also from interrupt context, so irq
   disabling is needed for it.

   Function returns a pointer to the initialized request queue, or \ ``NULL``\  if
   it didn't succeed.

.. _`blk_init_queue.note`:

Note
----

   \ :c:func:`blk_init_queue`\  must be paired with a \ :c:func:`blk_cleanup_queue`\  call
   when the block device is deactivated (such as at module unload).

.. _`__get_request`:

__get_request
=============

.. c:function:: struct request *__get_request(struct request_list *rl, unsigned int op, struct bio *bio, gfp_t gfp_mask)

    get a free request

    :param struct request_list \*rl:
        request list to allocate from

    :param unsigned int op:
        operation and flags

    :param struct bio \*bio:
        bio to allocate request for (can be \ ``NULL``\ )

    :param gfp_t gfp_mask:
        allocation mask

.. _`__get_request.description`:

Description
-----------

Get a free request from \ ``q``\ .  This function may fail under memory
pressure or if \ ``q``\  is dead.

Must be called with \ ``q``\ ->queue_lock held and,
Returns ERR_PTR on failure, with \ ``q``\ ->queue_lock held.
Returns request pointer on success, with \ ``q``\ ->queue_lock *not held*.

.. _`get_request`:

get_request
===========

.. c:function:: struct request *get_request(struct request_queue *q, unsigned int op, struct bio *bio, gfp_t gfp_mask)

    get a free request

    :param struct request_queue \*q:
        request_queue to allocate request from

    :param unsigned int op:
        operation and flags

    :param struct bio \*bio:
        bio to allocate request for (can be \ ``NULL``\ )

    :param gfp_t gfp_mask:
        allocation mask

.. _`get_request.description`:

Description
-----------

Get a free request from \ ``q``\ .  If \ ``__GFP_DIRECT_RECLAIM``\  is set in \ ``gfp_mask``\ ,
this function keeps retrying under memory pressure and fails iff \ ``q``\  is dead.

Must be called with \ ``q``\ ->queue_lock held and,
Returns ERR_PTR on failure, with \ ``q``\ ->queue_lock held.
Returns request pointer on success, with \ ``q``\ ->queue_lock *not held*.

.. _`blk_requeue_request`:

blk_requeue_request
===================

.. c:function:: void blk_requeue_request(struct request_queue *q, struct request *rq)

    put a request back on queue

    :param struct request_queue \*q:
        request queue where request should be inserted

    :param struct request \*rq:
        request to be inserted

.. _`blk_requeue_request.description`:

Description
-----------

   Drivers often keep queueing requests until the hardware cannot accept
   more, when that condition happens we need to put the request back
   on the queue. Must be called with queue lock held.

.. _`part_round_stats`:

part_round_stats
================

.. c:function:: void part_round_stats(int cpu, struct hd_struct *part)

    Round off the performance stats on a struct disk_stats.

    :param int cpu:
        cpu number for stats access

    :param struct hd_struct \*part:
        target partition

.. _`part_round_stats.description`:

Description
-----------

The average IO queue length and utilisation statistics are maintained
by observing the current state of the queue length and the amount of
time it has been in this state for.

Normally, that accounting is done on IO completion, but that can result
in more than a second's worth of IO being accounted for within any one
second, leading to >100% utilisation.  To deal with that, we call this
function to do a round-off before returning the results when reading
/proc/diskstats.  This accounts immediately for all queue usage up to
the current jiffies and restarts the counters again.

.. _`blk_attempt_plug_merge`:

blk_attempt_plug_merge
======================

.. c:function:: bool blk_attempt_plug_merge(struct request_queue *q, struct bio *bio, unsigned int *request_count, struct request **same_queue_rq)

    try to merge with \ ``current``\ 's plugged list

    :param struct request_queue \*q:
        request_queue new bio is being queued at

    :param struct bio \*bio:
        new bio being queued

    :param unsigned int \*request_count:
        out parameter for number of traversed plugged requests

    :param struct request \*\*same_queue_rq:
        pointer to \ :c:type:`struct request <request>`\  that gets filled in when
        another request associated with \ ``q``\  is found on the plug list
        (optional, may be \ ``NULL``\ )

.. _`blk_attempt_plug_merge.description`:

Description
-----------

Determine whether \ ``bio``\  being queued on \ ``q``\  can be merged with a request
on \ ``current``\ 's plugged list.  Returns \ ``true``\  if merge was successful,
otherwise \ ``false``\ .

Plugging coalesces IOs from the same issuer for the same purpose without
going through \ ``q``\ ->queue_lock.  As such it's more of an issuing mechanism
than scheduling, and the request, while may have elvpriv data, is not
added on the elevator at this point.  In addition, we don't have
reliable access to the elevator outside queue lock.  Only check basic
merging parameters without querying the elevator.

Caller must ensure !blk_queue_nomerges(q) beforehand.

.. _`generic_make_request`:

generic_make_request
====================

.. c:function:: blk_qc_t generic_make_request(struct bio *bio)

    hand a buffer to its device driver for I/O

    :param struct bio \*bio:
        The bio describing the location in memory and on the device.

.. _`generic_make_request.description`:

Description
-----------

generic_make_request() is used to make I/O requests of block
devices. It is passed a \ :c:type:`struct bio <bio>`\ , which describes the I/O that needs
to be done.

\ :c:func:`generic_make_request`\  does not return any status.  The
success/failure status of the request, along with notification of
completion, is delivered asynchronously through the bio->bi_end_io
function described (one day) else where.

The caller of generic_make_request must make sure that bi_io_vec
are set to describe the memory buffer, and that bi_dev and bi_sector are
set to describe the device address, and the
bi_end_io and optionally bi_private are set to describe how
completion notification should be signaled.

generic_make_request and the drivers it calls may use bi_next if this
bio happens to be merged with someone else, and may resubmit the bio to
a lower device by calling into generic_make_request recursively, which
means the bio should NOT be touched after the call to ->make_request_fn.

.. _`submit_bio`:

submit_bio
==========

.. c:function:: blk_qc_t submit_bio(struct bio *bio)

    submit a bio to the block device layer for I/O

    :param struct bio \*bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O

.. _`submit_bio.description`:

Description
-----------

submit_bio() is very similar in purpose to \ :c:func:`generic_make_request`\ , and
uses that function to do most of the work. Both are fairly rough
interfaces; \ ``bio``\  must be presetup and ready for I/O.

.. _`blk_cloned_rq_check_limits`:

blk_cloned_rq_check_limits
==========================

.. c:function:: int blk_cloned_rq_check_limits(struct request_queue *q, struct request *rq)

    Helper function to check a cloned request for new the queue limits

    :param struct request_queue \*q:
        the queue

    :param struct request \*rq:
        the request being checked

.. _`blk_cloned_rq_check_limits.description`:

Description
-----------

   \ ``rq``\  may have been made based on weaker limitations of upper-level queues
   in request stacking drivers, and it may violate the limitation of \ ``q``\ .
   Since the block layer and the underlying device driver trust \ ``rq``\ 
   after it is inserted to \ ``q``\ , it should be checked against \ ``q``\  before
   the insertion using this generic function.

   Request stacking drivers like request-based dm may change the queue
   limits when retrying requests on other queues. Those requests need
   to be checked against the new queue limits again during dispatch.

.. _`blk_insert_cloned_request`:

blk_insert_cloned_request
=========================

.. c:function:: int blk_insert_cloned_request(struct request_queue *q, struct request *rq)

    Helper for stacking drivers to submit a request

    :param struct request_queue \*q:
        the queue to submit the request

    :param struct request \*rq:
        the request being queued

.. _`blk_rq_err_bytes`:

blk_rq_err_bytes
================

.. c:function:: unsigned int blk_rq_err_bytes(const struct request *rq)

    determine number of bytes till the next failure boundary

    :param const struct request \*rq:
        request to examine

.. _`blk_rq_err_bytes.description`:

Description
-----------

    A request could be merge of IOs which require different failure
    handling.  This function determines the number of bytes which
    can be failed from the beginning of the request without
    crossing into area which need to be retried further.

.. _`blk_rq_err_bytes.return`:

Return
------

    The number of bytes to fail.

.. _`blk_rq_err_bytes.context`:

Context
-------

    queue_lock must be held.

.. _`blk_peek_request`:

blk_peek_request
================

.. c:function:: struct request *blk_peek_request(struct request_queue *q)

    peek at the top of a request queue

    :param struct request_queue \*q:
        request queue to peek at

.. _`blk_peek_request.description`:

Description
-----------

    Return the request at the top of \ ``q``\ .  The returned request
    should be started using \ :c:func:`blk_start_request`\  before LLD starts
    processing it.

.. _`blk_peek_request.return`:

Return
------

    Pointer to the request at the top of \ ``q``\  if available.  Null
    otherwise.

.. _`blk_peek_request.context`:

Context
-------

    queue_lock must be held.

.. _`blk_start_request`:

blk_start_request
=================

.. c:function:: void blk_start_request(struct request *req)

    start request processing on the driver

    :param struct request \*req:
        request to dequeue

.. _`blk_start_request.description`:

Description
-----------

    Dequeue \ ``req``\  and start timeout timer on it.  This hands off the
    request to the driver.

    Block internal functions which don't want to start timer should
    call \ :c:func:`blk_dequeue_request`\ .

.. _`blk_start_request.context`:

Context
-------

    queue_lock must be held.

.. _`blk_fetch_request`:

blk_fetch_request
=================

.. c:function:: struct request *blk_fetch_request(struct request_queue *q)

    fetch a request from a request queue

    :param struct request_queue \*q:
        request queue to fetch a request from

.. _`blk_fetch_request.description`:

Description
-----------

    Return the request at the top of \ ``q``\ .  The request is started on
    return and LLD can start processing it immediately.

.. _`blk_fetch_request.return`:

Return
------

    Pointer to the request at the top of \ ``q``\  if available.  Null
    otherwise.

.. _`blk_fetch_request.context`:

Context
-------

    queue_lock must be held.

.. _`blk_update_request`:

blk_update_request
==================

.. c:function:: bool blk_update_request(struct request *req, int error, unsigned int nr_bytes)

    Special helper function for request stacking drivers

    :param struct request \*req:
        the request being processed

    :param int error:
        %0 for success, < \ ``0``\  for error

    :param unsigned int nr_bytes:
        number of bytes to complete \ ``req``\ 

.. _`blk_update_request.description`:

Description
-----------

    Ends I/O on a number of bytes attached to \ ``req``\ , but doesn't complete
    the request structure even if \ ``req``\  doesn't have leftover.
    If \ ``req``\  has leftover, sets it up for the next range of segments.

    This special helper function is only for request stacking drivers
    (e.g. request-based dm) so that they can handle partial completion.
    Actual device drivers should use blk_end_request instead.

    Passing the result of \ :c:func:`blk_rq_bytes`\  as \ ``nr_bytes``\  guarantees
    \ ``false``\  return from this function.

.. _`blk_update_request.return`:

Return
------

    \ ``false``\  - this request doesn't have any more data
    \ ``true``\   - this request has more data

.. _`blk_unprep_request`:

blk_unprep_request
==================

.. c:function:: void blk_unprep_request(struct request *req)

    unprepare a request

    :param struct request \*req:
        the request

.. _`blk_unprep_request.description`:

Description
-----------

This function makes a request ready for complete resubmission (or
completion).  It happens only after all error handling is complete,
so represents the appropriate moment to deallocate any resources
that were allocated to the request in the prep_rq_fn.  The queue
lock is held when calling this.

.. _`blk_end_bidi_request`:

blk_end_bidi_request
====================

.. c:function:: bool blk_end_bidi_request(struct request *rq, int error, unsigned int nr_bytes, unsigned int bidi_bytes)

    Complete a bidi request

    :param struct request \*rq:
        the request to complete

    :param int error:
        %0 for success, < \ ``0``\  for error

    :param unsigned int nr_bytes:
        number of bytes to complete \ ``rq``\ 

    :param unsigned int bidi_bytes:
        number of bytes to complete \ ``rq``\ ->next_rq

.. _`blk_end_bidi_request.description`:

Description
-----------

    Ends I/O on a number of bytes attached to \ ``rq``\  and \ ``rq``\ ->next_rq.
    Drivers that supports bidi can safely call this member for any
    type of request, bidi or uni.  In the later case \ ``bidi_bytes``\  is
    just ignored.

.. _`blk_end_bidi_request.return`:

Return
------

    \ ``false``\  - we are done with this request
    \ ``true``\   - still buffers pending for this request

.. _`__blk_end_bidi_request`:

__blk_end_bidi_request
======================

.. c:function:: bool __blk_end_bidi_request(struct request *rq, int error, unsigned int nr_bytes, unsigned int bidi_bytes)

    Complete a bidi request with queue lock held

    :param struct request \*rq:
        the request to complete

    :param int error:
        %0 for success, < \ ``0``\  for error

    :param unsigned int nr_bytes:
        number of bytes to complete \ ``rq``\ 

    :param unsigned int bidi_bytes:
        number of bytes to complete \ ``rq``\ ->next_rq

.. _`__blk_end_bidi_request.description`:

Description
-----------

    Identical to \ :c:func:`blk_end_bidi_request`\  except that queue lock is
    assumed to be locked on entry and remains so on return.

.. _`__blk_end_bidi_request.return`:

Return
------

    \ ``false``\  - we are done with this request
    \ ``true``\   - still buffers pending for this request

.. _`blk_end_request`:

blk_end_request
===============

.. c:function:: bool blk_end_request(struct request *rq, int error, unsigned int nr_bytes)

    Helper function for drivers to complete the request.

    :param struct request \*rq:
        the request being processed

    :param int error:
        %0 for success, < \ ``0``\  for error

    :param unsigned int nr_bytes:
        number of bytes to complete

.. _`blk_end_request.description`:

Description
-----------

    Ends I/O on a number of bytes attached to \ ``rq``\ .
    If \ ``rq``\  has leftover, sets it up for the next range of segments.

.. _`blk_end_request.return`:

Return
------

    \ ``false``\  - we are done with this request
    \ ``true``\   - still buffers pending for this request

.. _`blk_end_request_all`:

blk_end_request_all
===================

.. c:function:: void blk_end_request_all(struct request *rq, int error)

    Helper function for drives to finish the request.

    :param struct request \*rq:
        the request to finish

    :param int error:
        %0 for success, < \ ``0``\  for error

.. _`blk_end_request_all.description`:

Description
-----------

    Completely finish \ ``rq``\ .

.. _`__blk_end_request`:

__blk_end_request
=================

.. c:function:: bool __blk_end_request(struct request *rq, int error, unsigned int nr_bytes)

    Helper function for drivers to complete the request.

    :param struct request \*rq:
        the request being processed

    :param int error:
        %0 for success, < \ ``0``\  for error

    :param unsigned int nr_bytes:
        number of bytes to complete

.. _`__blk_end_request.description`:

Description
-----------

    Must be called with queue lock held unlike \ :c:func:`blk_end_request`\ .

.. _`__blk_end_request.return`:

Return
------

    \ ``false``\  - we are done with this request
    \ ``true``\   - still buffers pending for this request

.. _`__blk_end_request_all`:

__blk_end_request_all
=====================

.. c:function:: void __blk_end_request_all(struct request *rq, int error)

    Helper function for drives to finish the request.

    :param struct request \*rq:
        the request to finish

    :param int error:
        %0 for success, < \ ``0``\  for error

.. _`__blk_end_request_all.description`:

Description
-----------

    Completely finish \ ``rq``\ .  Must be called with queue lock held.

.. _`__blk_end_request_cur`:

__blk_end_request_cur
=====================

.. c:function:: bool __blk_end_request_cur(struct request *rq, int error)

    Helper function to finish the current request chunk.

    :param struct request \*rq:
        the request to finish the current chunk for

    :param int error:
        %0 for success, < \ ``0``\  for error

.. _`__blk_end_request_cur.description`:

Description
-----------

    Complete the current consecutively mapped chunk from \ ``rq``\ .  Must
    be called with queue lock held.

.. _`__blk_end_request_cur.return`:

Return
------

    \ ``false``\  - we are done with this request
    \ ``true``\   - still buffers pending for this request

.. _`rq_flush_dcache_pages`:

rq_flush_dcache_pages
=====================

.. c:function:: void rq_flush_dcache_pages(struct request *rq)

    Helper function to flush all pages in a request

    :param struct request \*rq:
        the request to be flushed

.. _`rq_flush_dcache_pages.description`:

Description
-----------

    Flush all pages in \ ``rq``\ .

.. _`blk_lld_busy`:

blk_lld_busy
============

.. c:function:: int blk_lld_busy(struct request_queue *q)

    Check if underlying low-level drivers of a device are busy

    :param struct request_queue \*q:
        the queue of the device being checked

.. _`blk_lld_busy.description`:

Description
-----------

   Check if underlying low-level drivers of a device are busy.
   If the drivers want to export their busy state, they must set own
   exporting function using \ :c:func:`blk_queue_lld_busy`\  first.

   Basically, this function is used only by request stacking drivers
   to stop dispatching requests to underlying devices when underlying
   devices are busy.  This behavior helps more I/O merging on the queue
   of the request stacking driver and prevents I/O throughput regression
   on burst I/O load.

.. _`blk_lld_busy.return`:

Return
------

   0 - Not busy (The request stacking driver should dispatch request)
   1 - Busy (The request stacking driver should stop dispatching request)

.. _`blk_rq_unprep_clone`:

blk_rq_unprep_clone
===================

.. c:function:: void blk_rq_unprep_clone(struct request *rq)

    Helper function to free all bios in a cloned request

    :param struct request \*rq:
        the clone request to be cleaned up

.. _`blk_rq_unprep_clone.description`:

Description
-----------

    Free all bios in \ ``rq``\  for a cloned request.

.. _`blk_rq_prep_clone`:

blk_rq_prep_clone
=================

.. c:function:: int blk_rq_prep_clone(struct request *rq, struct request *rq_src, struct bio_set *bs, gfp_t gfp_mask, int (*bio_ctr)(struct bio *, struct bio *, void *), void *data)

    Helper function to setup clone request

    :param struct request \*rq:
        the request to be setup

    :param struct request \*rq_src:
        original request to be cloned

    :param struct bio_set \*bs:
        bio_set that bios for clone are allocated from

    :param gfp_t gfp_mask:
        memory allocation mask for bio

    :param int (\*bio_ctr)(struct bio \*, struct bio \*, void \*):
        setup function to be called for each clone bio.
        Returns \ ``0``\  for success, non \ ``0``\  for failure.

    :param void \*data:
        private data to be passed to \ ``bio_ctr``\ 

.. _`blk_rq_prep_clone.description`:

Description
-----------

    Clones bios in \ ``rq_src``\  to \ ``rq``\ , and copies attributes of \ ``rq_src``\  to \ ``rq``\ .
    The actual data parts of \ ``rq_src``\  (e.g. ->cmd, ->sense)
    are not copied, and copying such parts is the caller's responsibility.
    Also, pages which the original bios are pointing to are not copied
    and the cloned bios just point same pages.
    So cloned bios must be completed before original bios, which means
    the caller must complete \ ``rq``\  before \ ``rq_src``\ .

.. _`blk_start_plug`:

blk_start_plug
==============

.. c:function:: void blk_start_plug(struct blk_plug *plug)

    initialize blk_plug and track it inside the task_struct

    :param struct blk_plug \*plug:
        The \ :c:type:`struct blk_plug <blk_plug>`\  that needs to be initialized

.. _`blk_start_plug.description`:

Description
-----------

  Tracking blk_plug inside the task_struct will help with auto-flushing the
  pending I/O should the task end up blocking between \ :c:func:`blk_start_plug`\  and
  \ :c:func:`blk_finish_plug`\ . This is important from a performance perspective, but
  also ensures that we don't deadlock. For instance, if the task is blocking
  for a memory allocation, memory reclaim could end up wanting to free a
  page belonging to that request that is currently residing in our private
  plug. By flushing the pending I/O when the process goes to sleep, we avoid
  this kind of deadlock.

.. _`blk_pm_runtime_init`:

blk_pm_runtime_init
===================

.. c:function:: void blk_pm_runtime_init(struct request_queue *q, struct device *dev)

    Block layer runtime PM initialization routine

    :param struct request_queue \*q:
        the queue of the device

    :param struct device \*dev:
        the device the queue belongs to

.. _`blk_pm_runtime_init.description`:

Description
-----------

   Initialize runtime-PM-related fields for \ ``q``\  and start auto suspend for
   \ ``dev``\ . Drivers that want to take advantage of request-based runtime PM
   should call this function after \ ``dev``\  has been initialized, and its
   request queue \ ``q``\  has been allocated, and runtime PM for it can not happen
   yet(either due to disabled/forbidden or its usage_count > 0). In most
   cases, driver should call this function before any I/O has taken place.

   This function takes care of setting up using auto suspend for the device,
   the autosuspend delay is set to -1 to make runtime suspend impossible
   until an updated value is either set by user or by driver. Drivers do
   not need to touch other autosuspend settings.

   The block layer runtime PM is request based, so only works for drivers
   that use request as their IO unit instead of those directly use bio's.

.. _`blk_pre_runtime_suspend`:

blk_pre_runtime_suspend
=======================

.. c:function:: int blk_pre_runtime_suspend(struct request_queue *q)

    Pre runtime suspend check

    :param struct request_queue \*q:
        the queue of the device

.. _`blk_pre_runtime_suspend.description`:

Description
-----------

   This function will check if runtime suspend is allowed for the device
   by examining if there are any requests pending in the queue. If there
   are requests pending, the device can not be runtime suspended; otherwise,
   the queue's status will be updated to SUSPENDING and the driver can
   proceed to suspend the device.

   For the not allowed case, we mark last busy for the device so that
   runtime PM core will try to autosuspend it some time later.

   This function should be called near the start of the device's
   runtime_suspend callback.

.. _`blk_pre_runtime_suspend.return`:

Return
------

   0         - OK to runtime suspend the device
   -EBUSY    - Device should not be runtime suspended

.. _`blk_post_runtime_suspend`:

blk_post_runtime_suspend
========================

.. c:function:: void blk_post_runtime_suspend(struct request_queue *q, int err)

    Post runtime suspend processing

    :param struct request_queue \*q:
        the queue of the device

    :param int err:
        return value of the device's runtime_suspend function

.. _`blk_post_runtime_suspend.description`:

Description
-----------

   Update the queue's runtime status according to the return value of the
   device's runtime suspend function and mark last busy for the device so
   that PM core will try to auto suspend the device at a later time.

   This function should be called near the end of the device's
   runtime_suspend callback.

.. _`blk_pre_runtime_resume`:

blk_pre_runtime_resume
======================

.. c:function:: void blk_pre_runtime_resume(struct request_queue *q)

    Pre runtime resume processing

    :param struct request_queue \*q:
        the queue of the device

.. _`blk_pre_runtime_resume.description`:

Description
-----------

   Update the queue's runtime status to RESUMING in preparation for the
   runtime resume of the device.

   This function should be called near the start of the device's
   runtime_resume callback.

.. _`blk_post_runtime_resume`:

blk_post_runtime_resume
=======================

.. c:function:: void blk_post_runtime_resume(struct request_queue *q, int err)

    Post runtime resume processing

    :param struct request_queue \*q:
        the queue of the device

    :param int err:
        return value of the device's runtime_resume function

.. _`blk_post_runtime_resume.description`:

Description
-----------

   Update the queue's runtime status according to the return value of the
   device's runtime_resume function. If it is successfully resumed, process
   the requests that are queued into the device's queue when it is resuming
   and then mark last busy and initiate autosuspend for it.

   This function should be called near the end of the device's
   runtime_resume callback.

.. _`blk_set_runtime_active`:

blk_set_runtime_active
======================

.. c:function:: void blk_set_runtime_active(struct request_queue *q)

    Force runtime status of the queue to be active

    :param struct request_queue \*q:
        the queue of the device

.. _`blk_set_runtime_active.description`:

Description
-----------

If the device is left runtime suspended during system suspend the resume
hook typically resumes the device and corrects runtime status
accordingly. However, that does not affect the queue runtime PM status
which is still "suspended". This prevents processing requests from the
queue.

This function can be used in driver's resume hook to correct queue
runtime PM status and re-enable peeking requests from the queue. It
should be called before first request is added to the queue.

.. This file was automatic generated / don't edit.

