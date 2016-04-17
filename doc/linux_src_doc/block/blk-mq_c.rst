.. -*- coding: utf-8; mode: rst -*-

========
blk-mq.c
========


.. _`blk_mq_complete_request`:

blk_mq_complete_request
=======================

.. c:function:: void blk_mq_complete_request (struct request *rq, int error)

    end I/O on a request

    :param struct request \*rq:
        the request being processed

    :param int error:

        *undescribed*



.. _`blk_mq_complete_request.description`:

Description
-----------

Ends all I/O on a request. It does not handle partial completions.
The actual completion happens out-of-order, through a IPI handler.

