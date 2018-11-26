.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-flush.c

.. _`blk_flush_complete_seq`:

blk_flush_complete_seq
======================

.. c:function:: bool blk_flush_complete_seq(struct request *rq, struct blk_flush_queue *fq, unsigned int seq, blk_status_t error)

    complete flush sequence

    :param rq:
        PREFLUSH/FUA request being sequenced
    :type rq: struct request \*

    :param fq:
        flush queue
    :type fq: struct blk_flush_queue \*

    :param seq:
        sequences to complete (mask of \ ``REQ_FSEQ_``\ *, can be zero)
    :type seq: unsigned int

    :param error:
        whether an error occurred
    :type error: blk_status_t

.. _`blk_flush_complete_seq.description`:

Description
-----------

\ ``rq``\  just completed \ ``seq``\  part of its flush sequence, record the
completion and trigger the next step.

.. _`blk_flush_complete_seq.context`:

Context
-------

spin_lock_irq(q->queue_lock or fq->mq_flush_lock)

.. _`blk_flush_complete_seq.return`:

Return
------

\ ``true``\  if requests were added to the dispatch queue, \ ``false``\  otherwise.

.. _`blk_kick_flush`:

blk_kick_flush
==============

.. c:function:: bool blk_kick_flush(struct request_queue *q, struct blk_flush_queue *fq, unsigned int flags)

    consider issuing flush request

    :param q:
        request_queue being kicked
    :type q: struct request_queue \*

    :param fq:
        flush queue
    :type fq: struct blk_flush_queue \*

    :param flags:
        cmd_flags of the original request
    :type flags: unsigned int

.. _`blk_kick_flush.description`:

Description
-----------

Flush related states of \ ``q``\  have changed, consider issuing flush request.
Please read the comment at the top of this file for more info.

.. _`blk_kick_flush.context`:

Context
-------

spin_lock_irq(q->queue_lock or fq->mq_flush_lock)

.. _`blk_kick_flush.return`:

Return
------

\ ``true``\  if flush was issued, \ ``false``\  otherwise.

.. _`blk_insert_flush`:

blk_insert_flush
================

.. c:function:: void blk_insert_flush(struct request *rq)

    insert a new PREFLUSH/FUA request

    :param rq:
        request to insert
    :type rq: struct request \*

.. _`blk_insert_flush.description`:

Description
-----------

To be called from \ :c:func:`__elv_add_request`\  for \ ``ELEVATOR_INSERT_FLUSH``\  insertions.
or \ :c:func:`__blk_mq_run_hw_queue`\  to dispatch request.
\ ``rq``\  is being submitted.  Analyze what needs to be done and put it on the
right queue.

.. _`blkdev_issue_flush`:

blkdev_issue_flush
==================

.. c:function:: int blkdev_issue_flush(struct block_device *bdev, gfp_t gfp_mask, sector_t *error_sector)

    queue a flush

    :param bdev:
        blockdev to issue flush for
    :type bdev: struct block_device \*

    :param gfp_mask:
        memory allocation flags (for bio_alloc)
    :type gfp_mask: gfp_t

    :param error_sector:
        error sector
    :type error_sector: sector_t \*

.. _`blkdev_issue_flush.description`:

Description
-----------

   Issue a flush for the block device in question. Caller can supply
   room for storing the error offset in case of a flush error, if they
   wish to.

.. This file was automatic generated / don't edit.

