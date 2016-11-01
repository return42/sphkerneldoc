.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/trace/events/block.h

.. _`trace_block_touch_buffer`:

trace_block_touch_buffer
========================

.. c:function:: void trace_block_touch_buffer(struct buffer_head *bh)

    mark a buffer accessed

    :param struct buffer_head \*bh:
        buffer_head being touched

.. _`trace_block_touch_buffer.description`:

Description
-----------

Called from \ :c:func:`touch_buffer`\ .

.. _`trace_block_dirty_buffer`:

trace_block_dirty_buffer
========================

.. c:function:: void trace_block_dirty_buffer(struct buffer_head *bh)

    mark a buffer dirty

    :param struct buffer_head \*bh:
        buffer_head being dirtied

.. _`trace_block_dirty_buffer.description`:

Description
-----------

Called from \ :c:func:`mark_buffer_dirty`\ .

.. _`trace_block_rq_abort`:

trace_block_rq_abort
====================

.. c:function:: void trace_block_rq_abort(struct request_queue *q, struct request *rq)

    abort block operation request

    :param struct request_queue \*q:
        queue containing the block operation request

    :param struct request \*rq:
        block IO operation request

.. _`trace_block_rq_abort.description`:

Description
-----------

Called immediately after pending block IO operation request \ ``rq``\  in
queue \ ``q``\  is aborted. The fields in the operation request \ ``rq``\ 
can be examined to determine which device and sectors the pending
operation would access.

.. _`trace_block_rq_requeue`:

trace_block_rq_requeue
======================

.. c:function:: void trace_block_rq_requeue(struct request_queue *q, struct request *rq)

    place block IO request back on a queue

    :param struct request_queue \*q:
        queue holding operation

    :param struct request \*rq:
        block IO operation request

.. _`trace_block_rq_requeue.description`:

Description
-----------

The block operation request \ ``rq``\  is being placed back into queue
\ ``q``\ .  For some reason the request was not completed and needs to be
put back in the queue.

.. _`trace_block_rq_complete`:

trace_block_rq_complete
=======================

.. c:function:: void trace_block_rq_complete(struct request_queue *q, struct request *rq, unsigned int nr_bytes)

    block IO operation completed by device driver

    :param struct request_queue \*q:
        queue containing the block operation request

    :param struct request \*rq:
        block operations request

    :param unsigned int nr_bytes:
        number of completed bytes

.. _`trace_block_rq_complete.description`:

Description
-----------

The block_rq_complete tracepoint event indicates that some portion
of operation request has been completed by the device driver.  If
the \ ``rq``\ ->bio is \ ``NULL``\ , then there is absolutely no additional work to
do for the request. If \ ``rq``\ ->bio is non-NULL then there is
additional work required to complete the request.

.. _`trace_block_rq_insert`:

trace_block_rq_insert
=====================

.. c:function:: void trace_block_rq_insert(struct request_queue *q, struct request *rq)

    insert block operation request into queue

    :param struct request_queue \*q:
        target queue

    :param struct request \*rq:
        block IO operation request

.. _`trace_block_rq_insert.description`:

Description
-----------

Called immediately before block operation request \ ``rq``\  is inserted
into queue \ ``q``\ .  The fields in the operation request \ ``rq``\  struct can
be examined to determine which device and sectors the pending
operation would access.

.. _`trace_block_rq_issue`:

trace_block_rq_issue
====================

.. c:function:: void trace_block_rq_issue(struct request_queue *q, struct request *rq)

    issue pending block IO request operation to device driver

    :param struct request_queue \*q:
        queue holding operation

    :param struct request \*rq:
        block IO operation operation request

.. _`trace_block_rq_issue.description`:

Description
-----------

Called when block operation request \ ``rq``\  from queue \ ``q``\  is sent to a
device driver for processing.

.. _`trace_block_bio_bounce`:

trace_block_bio_bounce
======================

.. c:function:: void trace_block_bio_bounce(struct request_queue *q, struct bio *bio)

    used bounce buffer when processing block operation

    :param struct request_queue \*q:
        queue holding the block operation

    :param struct bio \*bio:
        block operation

.. _`trace_block_bio_bounce.description`:

Description
-----------

A bounce buffer was used to handle the block operation \ ``bio``\  in \ ``q``\ .
This occurs when hardware limitations prevent a direct transfer of
data between the \ ``bio``\  data memory area and the IO device.  Use of a
bounce buffer requires extra copying of data and decreases
performance.

.. _`trace_block_bio_complete`:

trace_block_bio_complete
========================

.. c:function:: void trace_block_bio_complete(struct request_queue *q, struct bio *bio, int error)

    completed all work on the block operation

    :param struct request_queue \*q:
        queue holding the block operation

    :param struct bio \*bio:
        block operation completed

    :param int error:
        io error value

.. _`trace_block_bio_complete.description`:

Description
-----------

This tracepoint indicates there is no further work to do on this
block IO operation \ ``bio``\ .

.. _`trace_block_bio_backmerge`:

trace_block_bio_backmerge
=========================

.. c:function:: void trace_block_bio_backmerge(struct request_queue *q, struct request *rq, struct bio *bio)

    merging block operation to the end of an existing operation

    :param struct request_queue \*q:
        queue holding operation

    :param struct request \*rq:
        request bio is being merged into

    :param struct bio \*bio:
        new block operation to merge

.. _`trace_block_bio_backmerge.description`:

Description
-----------

Merging block request \ ``bio``\  to the end of an existing block request
in queue \ ``q``\ .

.. _`trace_block_bio_frontmerge`:

trace_block_bio_frontmerge
==========================

.. c:function:: void trace_block_bio_frontmerge(struct request_queue *q, struct request *rq, struct bio *bio)

    merging block operation to the beginning of an existing operation

    :param struct request_queue \*q:
        queue holding operation

    :param struct request \*rq:
        request bio is being merged into

    :param struct bio \*bio:
        new block operation to merge

.. _`trace_block_bio_frontmerge.description`:

Description
-----------

Merging block IO operation \ ``bio``\  to the beginning of an existing block
operation in queue \ ``q``\ .

.. _`trace_block_bio_queue`:

trace_block_bio_queue
=====================

.. c:function:: void trace_block_bio_queue(struct request_queue *q, struct bio *bio)

    putting new block IO operation in queue

    :param struct request_queue \*q:
        queue holding operation

    :param struct bio \*bio:
        new block operation

.. _`trace_block_bio_queue.description`:

Description
-----------

About to place the block IO operation \ ``bio``\  into queue \ ``q``\ .

.. _`trace_block_getrq`:

trace_block_getrq
=================

.. c:function:: void trace_block_getrq(struct request_queue *q, struct bio *bio, int rw)

    get a free request entry in queue for block IO operations

    :param struct request_queue \*q:
        queue for operations

    :param struct bio \*bio:
        pending block IO operation

    :param int rw:
        low bit indicates a read (%0) or a write (%1)

.. _`trace_block_getrq.description`:

Description
-----------

A request struct for queue \ ``q``\  has been allocated to handle the
block IO operation \ ``bio``\ .

.. _`trace_block_sleeprq`:

trace_block_sleeprq
===================

.. c:function:: void trace_block_sleeprq(struct request_queue *q, struct bio *bio, int rw)

    waiting to get a free request entry in queue for block IO operation

    :param struct request_queue \*q:
        queue for operation

    :param struct bio \*bio:
        pending block IO operation

    :param int rw:
        low bit indicates a read (%0) or a write (%1)

.. _`trace_block_sleeprq.description`:

Description
-----------

In the case where a request struct cannot be provided for queue \ ``q``\ 
the process needs to wait for an request struct to become
available.  This tracepoint event is generated each time the
process goes to sleep waiting for request struct become available.

.. _`trace_block_plug`:

trace_block_plug
================

.. c:function:: void trace_block_plug(struct request_queue *q)

    keep operations requests in request queue

    :param struct request_queue \*q:
        request queue to plug

.. _`trace_block_plug.description`:

Description
-----------

Plug the request queue \ ``q``\ .  Do not allow block operation requests
to be sent to the device driver. Instead, accumulate requests in
the queue to improve throughput performance of the block device.

.. _`trace_block_unplug`:

trace_block_unplug
==================

.. c:function:: void trace_block_unplug(struct request_queue *q, unsigned int depth, bool explicit)

    release of operations requests in request queue

    :param struct request_queue \*q:
        request queue to unplug

    :param unsigned int depth:
        number of requests just added to the queue

    :param bool explicit:
        whether this was an explicit unplug, or one from \ :c:func:`schedule`\ 

.. _`trace_block_unplug.description`:

Description
-----------

Unplug request queue \ ``q``\  because device driver is scheduled to work
on elements in the request queue.

.. _`trace_block_split`:

trace_block_split
=================

.. c:function:: void trace_block_split(struct request_queue *q, struct bio *bio, unsigned int new_sector)

    split a single bio struct into two bio structs

    :param struct request_queue \*q:
        queue containing the bio

    :param struct bio \*bio:
        block operation being split

    :param unsigned int new_sector:
        The starting sector for the new bio

.. _`trace_block_split.description`:

Description
-----------

The bio request \ ``bio``\  in request queue \ ``q``\  needs to be split into two
bio requests. The newly created \ ``bio``\  request starts at
\ ``new_sector``\ . This split may be required due to hardware limitation
such as operation crossing device boundaries in a RAID system.

.. _`trace_block_bio_remap`:

trace_block_bio_remap
=====================

.. c:function:: void trace_block_bio_remap(struct request_queue *q, struct bio *bio, dev_t dev, sector_t from)

    map request for a logical device to the raw device

    :param struct request_queue \*q:
        queue holding the operation

    :param struct bio \*bio:
        revised operation

    :param dev_t dev:
        device for the operation

    :param sector_t from:
        original sector for the operation

.. _`trace_block_bio_remap.description`:

Description
-----------

An operation for a logical device has been mapped to the
raw block device.

.. _`trace_block_rq_remap`:

trace_block_rq_remap
====================

.. c:function:: void trace_block_rq_remap(struct request_queue *q, struct request *rq, dev_t dev, sector_t from)

    map request for a block operation request

    :param struct request_queue \*q:
        queue holding the operation

    :param struct request \*rq:
        block IO operation request

    :param dev_t dev:
        device for the operation

    :param sector_t from:
        original sector for the operation

.. _`trace_block_rq_remap.description`:

Description
-----------

The block operation request \ ``rq``\  in \ ``q``\  has been remapped.  The block
operation request \ ``rq``\  holds the current information and \ ``from``\  hold
the original sector.

.. This file was automatic generated / don't edit.

