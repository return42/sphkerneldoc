.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-exec.c

.. _`blk_end_sync_rq`:

blk_end_sync_rq
===============

.. c:function:: void blk_end_sync_rq(struct request *rq, blk_status_t error)

    executes a completion event on a request

    :param rq:
        request to complete
    :type rq: struct request \*

    :param error:
        end I/O status of the request
    :type error: blk_status_t

.. _`blk_execute_rq_nowait`:

blk_execute_rq_nowait
=====================

.. c:function:: void blk_execute_rq_nowait(struct request_queue *q, struct gendisk *bd_disk, struct request *rq, int at_head, rq_end_io_fn *done)

    insert a request into queue for execution

    :param q:
        queue to insert the request in
    :type q: struct request_queue \*

    :param bd_disk:
        matching gendisk
    :type bd_disk: struct gendisk \*

    :param rq:
        request to insert
    :type rq: struct request \*

    :param at_head:
        insert request at head or tail of queue
    :type at_head: int

    :param done:
        I/O completion handler
    :type done: rq_end_io_fn \*

.. _`blk_execute_rq_nowait.description`:

Description
-----------

   Insert a fully prepared request at the back of the I/O scheduler queue
   for execution.  Don't wait for completion.

.. _`blk_execute_rq_nowait.note`:

Note
----

   This function will invoke \ ``done``\  directly if the queue is dead.

.. _`blk_execute_rq`:

blk_execute_rq
==============

.. c:function:: void blk_execute_rq(struct request_queue *q, struct gendisk *bd_disk, struct request *rq, int at_head)

    insert a request into queue for execution

    :param q:
        queue to insert the request in
    :type q: struct request_queue \*

    :param bd_disk:
        matching gendisk
    :type bd_disk: struct gendisk \*

    :param rq:
        request to insert
    :type rq: struct request \*

    :param at_head:
        insert request at head or tail of queue
    :type at_head: int

.. _`blk_execute_rq.description`:

Description
-----------

   Insert a fully prepared request at the back of the I/O scheduler queue
   for execution and wait for completion.

.. This file was automatic generated / don't edit.

