.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-core.c

.. _`blk_queue_flag_set`:

blk_queue_flag_set
==================

.. c:function:: void blk_queue_flag_set(unsigned int flag, struct request_queue *q)

    atomically set a queue flag

    :param flag:
        flag to be set
    :type flag: unsigned int

    :param q:
        request queue
    :type q: struct request_queue \*

.. _`blk_queue_flag_clear`:

blk_queue_flag_clear
====================

.. c:function:: void blk_queue_flag_clear(unsigned int flag, struct request_queue *q)

    atomically clear a queue flag

    :param flag:
        flag to be cleared
    :type flag: unsigned int

    :param q:
        request queue
    :type q: struct request_queue \*

.. _`blk_queue_flag_test_and_set`:

blk_queue_flag_test_and_set
===========================

.. c:function:: bool blk_queue_flag_test_and_set(unsigned int flag, struct request_queue *q)

    atomically test and set a queue flag

    :param flag:
        flag to be set
    :type flag: unsigned int

    :param q:
        request queue
    :type q: struct request_queue \*

.. _`blk_queue_flag_test_and_set.description`:

Description
-----------

Returns the previous value of \ ``flag``\  - 0 if the flag was not set and 1 if
the flag was already set.

.. _`blk_queue_flag_test_and_clear`:

blk_queue_flag_test_and_clear
=============================

.. c:function:: bool blk_queue_flag_test_and_clear(unsigned int flag, struct request_queue *q)

    atomically test and clear a queue flag

    :param flag:
        flag to be cleared
    :type flag: unsigned int

    :param q:
        request queue
    :type q: struct request_queue \*

.. _`blk_queue_flag_test_and_clear.description`:

Description
-----------

Returns the previous value of \ ``flag``\  - 0 if the flag was not set and 1 if
the flag was set.

.. _`blk_delay_queue`:

blk_delay_queue
===============

.. c:function:: void blk_delay_queue(struct request_queue *q, unsigned long msecs)

    restart queueing after defined interval

    :param q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question
    :type q: struct request_queue \*

    :param msecs:
        Delay in msecs
    :type msecs: unsigned long

.. _`blk_delay_queue.description`:

Description
-----------

  Sometimes queueing needs to be postponed for a little while, to allow
  resources to come back. This function will make sure that queueing is
  restarted around the specified time.

.. _`blk_start_queue_async`:

blk_start_queue_async
=====================

.. c:function:: void blk_start_queue_async(struct request_queue *q)

    asynchronously restart a previously stopped queue

    :param q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question
    :type q: struct request_queue \*

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

    :param q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question
    :type q: struct request_queue \*

.. _`blk_start_queue.description`:

Description
-----------

  \ :c:func:`blk_start_queue`\  will clear the stop flag on the queue, and call
  the request_fn for the queue if it was in a stopped state when
  entered. Also see \ :c:func:`blk_stop_queue`\ .

.. _`blk_stop_queue`:

blk_stop_queue
==============

.. c:function:: void blk_stop_queue(struct request_queue *q)

    stop a queue

    :param q:
        The \ :c:type:`struct request_queue <request_queue>`\  in question
    :type q: struct request_queue \*

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
  \ :c:func:`blk_start_queue`\  to restart queue operations.

.. _`blk_sync_queue`:

blk_sync_queue
==============

.. c:function:: void blk_sync_queue(struct request_queue *q)

    cancel any pending callbacks on a queue

    :param q:
        the queue
    :type q: struct request_queue \*

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

.. _`blk_set_pm_only`:

blk_set_pm_only
===============

.. c:function:: void blk_set_pm_only(struct request_queue *q)

    increment pm_only counter

    :param q:
        request queue pointer
    :type q: struct request_queue \*

.. _`__blk_run_queue_uncond`:

__blk_run_queue_uncond
======================

.. c:function:: void __blk_run_queue_uncond(struct request_queue *q)

    run a queue whether or not it has been stopped

    :param q:
        The queue to run
    :type q: struct request_queue \*

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

    :param q:
        The queue to run
    :type q: struct request_queue \*

.. _`__blk_run_queue.description`:

Description
-----------

   See \ ``blk_run_queue``\ .

.. _`blk_run_queue_async`:

blk_run_queue_async
===================

.. c:function:: void blk_run_queue_async(struct request_queue *q)

    run a single device queue in workqueue context

    :param q:
        The queue to run
    :type q: struct request_queue \*

.. _`blk_run_queue_async.description`:

Description
-----------

   Tells kblockd to perform the equivalent of \ ``blk_run_queue``\  on behalf
   of us.

.. _`blk_run_queue_async.note`:

Note
----

   Since it is not allowed to run q->delay_work after \ :c:func:`blk_cleanup_queue`\ 
   has canceled q->delay_work, callers must hold the queue lock to avoid
   race conditions between \ :c:func:`blk_cleanup_queue`\  and \ :c:func:`blk_run_queue_async`\ .

.. _`blk_run_queue`:

blk_run_queue
=============

.. c:function:: void blk_run_queue(struct request_queue *q)

    run a single device queue

    :param q:
        The queue to run
    :type q: struct request_queue \*

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

    :param q:
        queue to drain
    :type q: struct request_queue \*

    :param drain_all:
        whether to drain all requests or only the ones w/ ELVPRIV
    :type drain_all: bool

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

    :param q:
        queue of interest
    :type q: struct request_queue \*

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

    :param q:
        queue of interest
    :type q: struct request_queue \*

.. _`blk_queue_bypass_end.description`:

Description
-----------

Leave bypass mode and restore the normal queueing behavior.

.. _`blk_queue_bypass_end.note`:

Note
----

although \ :c:func:`blk_queue_bypass_start`\  is only called for blk-sq queues,
this function is called for both blk-sq and blk-mq queues.

.. _`blk_cleanup_queue`:

blk_cleanup_queue
=================

.. c:function:: void blk_cleanup_queue(struct request_queue *q)

    shutdown a request queue

    :param q:
        request queue to shutdown
    :type q: struct request_queue \*

.. _`blk_cleanup_queue.description`:

Description
-----------

Mark \ ``q``\  DYING, drain all pending requests, mark \ ``q``\  DEAD, destroy and
put it.  All future requests will be failed immediately with -ENODEV.

.. _`blk_queue_enter`:

blk_queue_enter
===============

.. c:function:: int blk_queue_enter(struct request_queue *q, blk_mq_req_flags_t flags)

    try to increase q->q_usage_counter

    :param q:
        request queue pointer
    :type q: struct request_queue \*

    :param flags:
        BLK_MQ_REQ_NOWAIT and/or BLK_MQ_REQ_PREEMPT
    :type flags: blk_mq_req_flags_t

.. _`blk_alloc_queue_node`:

blk_alloc_queue_node
====================

.. c:function:: struct request_queue *blk_alloc_queue_node(gfp_t gfp_mask, int node_id, spinlock_t *lock)

    allocate a request queue

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

    :param node_id:
        NUMA node to allocate memory from
    :type node_id: int

    :param lock:
        For legacy queues, pointer to a spinlock that will be used to e.g.
        serialize calls to the legacy .request_fn() callback. Ignored for
        blk-mq request queues.
    :type lock: spinlock_t \*

.. _`blk_alloc_queue_node.note`:

Note
----

pass the queue lock as the third argument to this function instead of
setting the queue lock pointer explicitly to avoid triggering a sporadic
crash in the blkcg code. This function namely calls \ :c:func:`blkcg_init_queue`\  and
the queue lock pointer must be set before \ :c:func:`blkcg_init_queue`\  is called.

.. _`blk_init_queue`:

blk_init_queue
==============

.. c:function:: struct request_queue *blk_init_queue(request_fn_proc *rfn, spinlock_t *lock)

    prepare a request queue for use with a block device

    :param rfn:
        The function to be called to process requests that have been
        placed on the queue.
    :type rfn: request_fn_proc \*

    :param lock:
        Request queue spin lock
    :type lock: spinlock_t \*

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

.. c:function:: struct request *__get_request(struct request_list *rl, unsigned int op, struct bio *bio, blk_mq_req_flags_t flags, gfp_t gfp_mask)

    get a free request

    :param rl:
        request list to allocate from
    :type rl: struct request_list \*

    :param op:
        operation and flags
    :type op: unsigned int

    :param bio:
        bio to allocate request for (can be \ ``NULL``\ )
    :type bio: struct bio \*

    :param flags:
        BLQ_MQ_REQ_* flags
    :type flags: blk_mq_req_flags_t

    :param gfp_mask:
        allocator flags
    :type gfp_mask: gfp_t

.. _`__get_request.description`:

Description
-----------

Get a free request from \ ``q``\ .  This function may fail under memory
pressure or if \ ``q``\  is dead.

Must be called with \ ``q->queue_lock``\  held and,
Returns ERR_PTR on failure, with \ ``q->queue_lock``\  held.
Returns request pointer on success, with \ ``q->queue_lock``\  *not held*.

.. _`get_request`:

get_request
===========

.. c:function:: struct request *get_request(struct request_queue *q, unsigned int op, struct bio *bio, blk_mq_req_flags_t flags, gfp_t gfp)

    get a free request

    :param q:
        request_queue to allocate request from
    :type q: struct request_queue \*

    :param op:
        operation and flags
    :type op: unsigned int

    :param bio:
        bio to allocate request for (can be \ ``NULL``\ )
    :type bio: struct bio \*

    :param flags:
        BLK_MQ_REQ_* flags.
    :type flags: blk_mq_req_flags_t

    :param gfp:
        allocator flags
    :type gfp: gfp_t

.. _`get_request.description`:

Description
-----------

Get a free request from \ ``q``\ .  If \ ``BLK_MQ_REQ_NOWAIT``\  is set in \ ``flags``\ ,
this function keeps retrying under memory pressure and fails iff \ ``q``\  is dead.

Must be called with \ ``q->queue_lock``\  held and,
Returns ERR_PTR on failure, with \ ``q->queue_lock``\  held.
Returns request pointer on success, with \ ``q->queue_lock``\  *not held*.

.. _`blk_get_request`:

blk_get_request
===============

.. c:function:: struct request *blk_get_request(struct request_queue *q, unsigned int op, blk_mq_req_flags_t flags)

    allocate a request

    :param q:
        request queue to allocate a request for
    :type q: struct request_queue \*

    :param op:
        operation (REQ_OP_*) and REQ_* flags, e.g. REQ_SYNC.
    :type op: unsigned int

    :param flags:
        BLK_MQ_REQ_* flags, e.g. BLK_MQ_REQ_NOWAIT.
    :type flags: blk_mq_req_flags_t

.. _`blk_requeue_request`:

blk_requeue_request
===================

.. c:function:: void blk_requeue_request(struct request_queue *q, struct request *rq)

    put a request back on queue

    :param q:
        request queue where request should be inserted
    :type q: struct request_queue \*

    :param rq:
        request to be inserted
    :type rq: struct request \*

.. _`blk_requeue_request.description`:

Description
-----------

   Drivers often keep queueing requests until the hardware cannot accept
   more, when that condition happens we need to put the request back
   on the queue. Must be called with queue lock held.

.. _`part_round_stats`:

part_round_stats
================

.. c:function:: void part_round_stats(struct request_queue *q, int cpu, struct hd_struct *part)

    Round off the performance stats on a struct disk_stats.

    :param q:
        target block queue
    :type q: struct request_queue \*

    :param cpu:
        cpu number for stats access
    :type cpu: int

    :param part:
        target partition
    :type part: struct hd_struct \*

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

    :param q:
        request_queue new bio is being queued at
    :type q: struct request_queue \*

    :param bio:
        new bio being queued
    :type bio: struct bio \*

    :param request_count:
        out parameter for number of traversed plugged requests
    :type request_count: unsigned int \*

    :param same_queue_rq:
        pointer to \ :c:type:`struct request <request>`\  that gets filled in when
        another request associated with \ ``q``\  is found on the plug list
        (optional, may be \ ``NULL``\ )
    :type same_queue_rq: struct request \*\*

.. _`blk_attempt_plug_merge.description`:

Description
-----------

Determine whether \ ``bio``\  being queued on \ ``q``\  can be merged with a request
on \ ``current``\ 's plugged list.  Returns \ ``true``\  if merge was successful,
otherwise \ ``false``\ .

Plugging coalesces IOs from the same issuer for the same purpose without
going through \ ``q->queue_lock``\ .  As such it's more of an issuing mechanism
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

    :param bio:
        The bio describing the location in memory and on the device.
    :type bio: struct bio \*

.. _`generic_make_request.description`:

Description
-----------

\ :c:func:`generic_make_request`\  is used to make I/O requests of block
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

.. _`direct_make_request`:

direct_make_request
===================

.. c:function:: blk_qc_t direct_make_request(struct bio *bio)

    hand a buffer directly to its device driver for I/O

    :param bio:
        The bio describing the location in memory and on the device.
    :type bio: struct bio \*

.. _`direct_make_request.description`:

Description
-----------

This function behaves like \ :c:func:`generic_make_request`\ , but does not protect
against recursion.  Must only be used if the called driver is known
to not call generic_make_request (or direct_make_request) again from
its make_request function.  (Calling direct_make_request again from
a workqueue is perfectly fine as that doesn't recurse).

.. _`submit_bio`:

submit_bio
==========

.. c:function:: blk_qc_t submit_bio(struct bio *bio)

    submit a bio to the block device layer for I/O

    :param bio:
        The \ :c:type:`struct bio <bio>`\  which describes the I/O
    :type bio: struct bio \*

.. _`submit_bio.description`:

Description
-----------

\ :c:func:`submit_bio`\  is very similar in purpose to \ :c:func:`generic_make_request`\ , and
uses that function to do most of the work. Both are fairly rough
interfaces; \ ``bio``\  must be presetup and ready for I/O.

.. _`blk_cloned_rq_check_limits`:

blk_cloned_rq_check_limits
==========================

.. c:function:: int blk_cloned_rq_check_limits(struct request_queue *q, struct request *rq)

    Helper function to check a cloned request for new the queue limits

    :param q:
        the queue
    :type q: struct request_queue \*

    :param rq:
        the request being checked
    :type rq: struct request \*

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

.. c:function:: blk_status_t blk_insert_cloned_request(struct request_queue *q, struct request *rq)

    Helper for stacking drivers to submit a request

    :param q:
        the queue to submit the request
    :type q: struct request_queue \*

    :param rq:
        the request being queued
    :type rq: struct request \*

.. _`blk_rq_err_bytes`:

blk_rq_err_bytes
================

.. c:function:: unsigned int blk_rq_err_bytes(const struct request *rq)

    determine number of bytes till the next failure boundary

    :param rq:
        request to examine
    :type rq: const struct request \*

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

.. _`blk_peek_request`:

blk_peek_request
================

.. c:function:: struct request *blk_peek_request(struct request_queue *q)

    peek at the top of a request queue

    :param q:
        request queue to peek at
    :type q: struct request_queue \*

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

.. _`blk_start_request`:

blk_start_request
=================

.. c:function:: void blk_start_request(struct request *req)

    start request processing on the driver

    :param req:
        request to dequeue
    :type req: struct request \*

.. _`blk_start_request.description`:

Description
-----------

    Dequeue \ ``req``\  and start timeout timer on it.  This hands off the
    request to the driver.

.. _`blk_fetch_request`:

blk_fetch_request
=================

.. c:function:: struct request *blk_fetch_request(struct request_queue *q)

    fetch a request from a request queue

    :param q:
        request queue to fetch a request from
    :type q: struct request_queue \*

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

.. _`blk_update_request`:

blk_update_request
==================

.. c:function:: bool blk_update_request(struct request *req, blk_status_t error, unsigned int nr_bytes)

    Special helper function for request stacking drivers

    :param req:
        the request being processed
    :type req: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

    :param nr_bytes:
        number of bytes to complete \ ``req``\ 
    :type nr_bytes: unsigned int

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

.. _`blk_update_request.note`:

Note
----

     The RQF_SPECIAL_PAYLOAD flag is ignored on purpose in both
     \ :c:func:`blk_rq_bytes`\  and in \ :c:func:`blk_update_request`\ .

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

    :param req:
        the request
    :type req: struct request \*

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

.. c:function:: bool blk_end_bidi_request(struct request *rq, blk_status_t error, unsigned int nr_bytes, unsigned int bidi_bytes)

    Complete a bidi request

    :param rq:
        the request to complete
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

    :param nr_bytes:
        number of bytes to complete \ ``rq``\ 
    :type nr_bytes: unsigned int

    :param bidi_bytes:
        number of bytes to complete \ ``rq->next_rq``\ 
    :type bidi_bytes: unsigned int

.. _`blk_end_bidi_request.description`:

Description
-----------

    Ends I/O on a number of bytes attached to \ ``rq``\  and \ ``rq->next_rq``\ .
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

.. c:function:: bool __blk_end_bidi_request(struct request *rq, blk_status_t error, unsigned int nr_bytes, unsigned int bidi_bytes)

    Complete a bidi request with queue lock held

    :param rq:
        the request to complete
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

    :param nr_bytes:
        number of bytes to complete \ ``rq``\ 
    :type nr_bytes: unsigned int

    :param bidi_bytes:
        number of bytes to complete \ ``rq->next_rq``\ 
    :type bidi_bytes: unsigned int

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

.. c:function:: bool blk_end_request(struct request *rq, blk_status_t error, unsigned int nr_bytes)

    Helper function for drivers to complete the request.

    :param rq:
        the request being processed
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

    :param nr_bytes:
        number of bytes to complete
    :type nr_bytes: unsigned int

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

.. c:function:: void blk_end_request_all(struct request *rq, blk_status_t error)

    Helper function for drives to finish the request.

    :param rq:
        the request to finish
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

.. _`blk_end_request_all.description`:

Description
-----------

    Completely finish \ ``rq``\ .

.. _`__blk_end_request`:

__blk_end_request
=================

.. c:function:: bool __blk_end_request(struct request *rq, blk_status_t error, unsigned int nr_bytes)

    Helper function for drivers to complete the request.

    :param rq:
        the request being processed
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

    :param nr_bytes:
        number of bytes to complete
    :type nr_bytes: unsigned int

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

.. c:function:: void __blk_end_request_all(struct request *rq, blk_status_t error)

    Helper function for drives to finish the request.

    :param rq:
        the request to finish
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

.. _`__blk_end_request_all.description`:

Description
-----------

    Completely finish \ ``rq``\ .  Must be called with queue lock held.

.. _`__blk_end_request_cur`:

__blk_end_request_cur
=====================

.. c:function:: bool __blk_end_request_cur(struct request *rq, blk_status_t error)

    Helper function to finish the current request chunk.

    :param rq:
        the request to finish the current chunk for
    :type rq: struct request \*

    :param error:
        block status code
    :type error: blk_status_t

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

    :param rq:
        the request to be flushed
    :type rq: struct request \*

.. _`rq_flush_dcache_pages.description`:

Description
-----------

    Flush all pages in \ ``rq``\ .

.. _`blk_lld_busy`:

blk_lld_busy
============

.. c:function:: int blk_lld_busy(struct request_queue *q)

    Check if underlying low-level drivers of a device are busy

    :param q:
        the queue of the device being checked
    :type q: struct request_queue \*

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

    :param rq:
        the clone request to be cleaned up
    :type rq: struct request \*

.. _`blk_rq_unprep_clone.description`:

Description
-----------

    Free all bios in \ ``rq``\  for a cloned request.

.. _`blk_rq_prep_clone`:

blk_rq_prep_clone
=================

.. c:function:: int blk_rq_prep_clone(struct request *rq, struct request *rq_src, struct bio_set *bs, gfp_t gfp_mask, int (*bio_ctr)(struct bio *, struct bio *, void *), void *data)

    Helper function to setup clone request

    :param rq:
        the request to be setup
    :type rq: struct request \*

    :param rq_src:
        original request to be cloned
    :type rq_src: struct request \*

    :param bs:
        bio_set that bios for clone are allocated from
    :type bs: struct bio_set \*

    :param gfp_mask:
        memory allocation mask for bio
    :type gfp_mask: gfp_t

    :param int (\*bio_ctr)(struct bio \*, struct bio \*, void \*):
        setup function to be called for each clone bio.
        Returns \ ``0``\  for success, non \ ``0``\  for failure.

    :param data:
        private data to be passed to \ ``bio_ctr``\ 
    :type data: void \*

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

    :param plug:
        The \ :c:type:`struct blk_plug <blk_plug>`\  that needs to be initialized
    :type plug: struct blk_plug \*

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

.. This file was automatic generated / don't edit.

