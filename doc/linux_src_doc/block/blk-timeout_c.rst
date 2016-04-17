.. -*- coding: utf-8; mode: rst -*-

=============
blk-timeout.c
=============


.. _`blk_abort_request`:

blk_abort_request
=================

.. c:function:: void blk_abort_request (struct request *req)

    - Request request recovery for the specified command

    :param struct request \*req:
        pointer to the request of interest



.. _`blk_abort_request.description`:

Description
-----------

This function requests that the block layer start recovery for the
request by deleting the timer and calling the q's timeout function.
LLDDs who implement their own error recovery MAY ignore the timeout
event if they generated blk_abort_req. Must hold queue lock.



.. _`blk_add_timer`:

blk_add_timer
=============

.. c:function:: void blk_add_timer (struct request *req)

    Start timeout timer for a single request

    :param struct request \*req:
        request that is about to start running.



.. _`blk_add_timer.notes`:

Notes
-----

Each request has its own timer, and as it is added to the queue, we
set up the timer. When the request completes, we cancel the timer.
Queue lock must be held for the non-mq case, mq case doesn't care.

