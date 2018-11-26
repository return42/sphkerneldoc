.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq.c

.. _`blk_mq_quiesce_queue`:

blk_mq_quiesce_queue
====================

.. c:function:: void blk_mq_quiesce_queue(struct request_queue *q)

    wait until all ongoing dispatches have finished

    :param q:
        request queue.
    :type q: struct request_queue \*

.. _`blk_mq_quiesce_queue.note`:

Note
----

this function does not prevent that the struct request \ :c:func:`end_io`\ 
callback function is invoked. Once this function is returned, we make
sure no dispatch can happen until the queue is unquiesced via
\ :c:func:`blk_mq_unquiesce_queue`\ .

.. _`blk_mq_complete_request`:

blk_mq_complete_request
=======================

.. c:function:: void blk_mq_complete_request(struct request *rq)

    end I/O on a request

    :param rq:
        the request being processed
    :type rq: struct request \*

.. _`blk_mq_complete_request.description`:

Description
-----------

Ends all I/O on a request. It does not handle partial completions.
The actual completion happens out-of-order, through a IPI handler.

.. _`blk_mq_queue_stopped`:

blk_mq_queue_stopped
====================

.. c:function:: bool blk_mq_queue_stopped(struct request_queue *q)

    check whether one or more hctxs have been stopped

    :param q:
        request queue.
    :type q: struct request_queue \*

.. _`blk_mq_queue_stopped.description`:

Description
-----------

The caller is responsible for serializing this function against
blk_mq_{start,stop}_hw_queue().

.. This file was automatic generated / don't edit.

