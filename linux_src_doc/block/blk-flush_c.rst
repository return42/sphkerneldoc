.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-flush.c

.. _`blk_flush_complete_seq`:

blk_flush_complete_seq
======================

.. c:function:: bool blk_flush_complete_seq(struct request *rq, struct blk_flush_queue *fq, unsigned int seq, blk_status_t error)

    complete flush sequence

    :param struct request \*rq:
        PREFLUSH/FUA request being sequenced

    :param struct blk_flush_queue \*fq:
        flush queue

    :param unsigned int seq:
        sequences to complete (mask of \ ``REQ_FSEQ_``\ *, can be zero)

    :param blk_status_t error:
        whether an error occurred

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

.. c:function:: bool blk_kick_flush(struct request_queue *q, struct blk_flush_queue *fq)

    consider issuing flush request

    :param struct request_queue \*q:
        request_queue being kicked

    :param struct blk_flush_queue \*fq:
        flush queue

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

    :param struct request \*rq:
        request to insert

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

    :param struct block_device \*bdev:
        blockdev to issue flush for

    :param gfp_t gfp_mask:
        memory allocation flags (for bio_alloc)

    :param sector_t \*error_sector:
        error sector

.. _`blkdev_issue_flush.description`:

Description
-----------

   Issue a flush for the block device in question. Caller can supply
   room for storing the error offset in case of a flush error, if they
   wish to.

.. This file was automatic generated / don't edit.

