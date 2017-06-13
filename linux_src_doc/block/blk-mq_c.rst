.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq.c

.. _`blk_mq_quiesce_queue`:

blk_mq_quiesce_queue
====================

.. c:function:: void blk_mq_quiesce_queue(struct request_queue *q)

    wait until all ongoing queue_rq calls have finished

    :param struct request_queue \*q:
        request queue.

.. _`blk_mq_quiesce_queue.note`:

Note
----

this function does not prevent that the struct request \ :c:func:`end_io`\ 
callback function is invoked. Additionally, it is not prevented that
new \ :c:func:`queue_rq`\  calls occur unless the queue has been stopped first.

.. _`blk_mq_complete_request`:

blk_mq_complete_request
=======================

.. c:function:: void blk_mq_complete_request(struct request *rq)

    end I/O on a request

    :param struct request \*rq:
        the request being processed

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

    :param struct request_queue \*q:
        request queue.

.. _`blk_mq_queue_stopped.description`:

Description
-----------

The caller is responsible for serializing this function against
blk_mq_{start,stop}_hw_queue().

.. This file was automatic generated / don't edit.

