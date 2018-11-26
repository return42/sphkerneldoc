.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-softirq.c

.. _`blk_complete_request`:

blk_complete_request
====================

.. c:function:: void blk_complete_request(struct request *req)

    end I/O on a request

    :param req:
        the request being processed
    :type req: struct request \*

.. _`blk_complete_request.description`:

Description
-----------

Ends all I/O on a request. It does not handle partial completions,
unless the driver actually implements this in its completion callback
through requeueing. The actual completion happens out-of-order,
through a softirq handler. The user must have registered a completion
callback through \ :c:func:`blk_queue_softirq_done`\ .

.. This file was automatic generated / don't edit.

