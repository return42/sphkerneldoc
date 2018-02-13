.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bfq-iosched.c

.. _`icq_to_bic`:

icq_to_bic
==========

.. c:function:: struct bfq_io_cq *icq_to_bic(struct io_cq *icq)

    convert iocontext queue structure to bfq_io_cq.

    :param struct io_cq \*icq:
        the iocontext queue.

.. _`bfq_bic_lookup`:

bfq_bic_lookup
==============

.. c:function:: struct bfq_io_cq *bfq_bic_lookup(struct bfq_data *bfqd, struct io_context *ioc, struct request_queue *q)

    search into \ ``ioc``\  a bic associated to \ ``bfqd``\ .

    :param struct bfq_data \*bfqd:
        the lookup key.

    :param struct io_context \*ioc:
        the io_context of the process doing I/O.

    :param struct request_queue \*q:
        the request queue.

.. _`bfq_updated_next_req`:

bfq_updated_next_req
====================

.. c:function:: void bfq_updated_next_req(struct bfq_data *bfqd, struct bfq_queue *bfqq)

    update the queue after a new next_rq selection.

    :param struct bfq_data \*bfqd:
        the device data the queue belongs to.

    :param struct bfq_queue \*bfqq:
        the queue to update.

.. _`bfq_updated_next_req.description`:

Description
-----------

If the first request of a queue changes we make sure that the queue
has enough budget to serve at least its first request (if the
request has grown).  We do this because if the queue has not enough
budget for its first request, it has to go through two dispatch
rounds to actually get it dispatched.

.. _`__bfq_bfqq_recalc_budget`:

\__bfq_bfqq_recalc_budget
=========================

.. c:function:: void __bfq_bfqq_recalc_budget(struct bfq_data *bfqd, struct bfq_queue *bfqq, enum bfqq_expiration reason)

    try to adapt the budget to the \ ``bfqq``\  behavior.

    :param struct bfq_data \*bfqd:
        device data.

    :param struct bfq_queue \*bfqq:
        queue to update.

    :param enum bfqq_expiration reason:
        reason for expiration.

.. _`__bfq_bfqq_recalc_budget.description`:

Description
-----------

Handle the feedback on \ ``bfqq``\  budget at queue expiration.
See the body for detailed comments.

.. _`bfq_bfqq_expire`:

bfq_bfqq_expire
===============

.. c:function:: void bfq_bfqq_expire(struct bfq_data *bfqd, struct bfq_queue *bfqq, bool compensate, enum bfqq_expiration reason)

    expire a queue.

    :param struct bfq_data \*bfqd:
        device owning the queue.

    :param struct bfq_queue \*bfqq:
        the queue to expire.

    :param bool compensate:
        if true, compensate for the time spent idling.

    :param enum bfqq_expiration reason:
        the reason causing the expiration.

.. _`bfq_bfqq_expire.description`:

Description
-----------

If the process associated with bfqq does slow I/O (e.g., because it
issues random requests), we charge bfqq with the time it has been
in service instead of the service it has received (see
bfq_bfqq_charge_time for details on how this goal is achieved). As
a consequence, bfqq will typically get higher timestamps upon
reactivation, and hence it will be rescheduled as if it had
received more service than what it has actually received. In the
end, bfqq receives less service in proportion to how slowly its
associated process consumes its budgets (and hence how seriously it
tends to lower the throughput). In addition, this time-charging
strategy guarantees time fairness among slow processes. In
contrast, if the process associated with bfqq is not slow, we
charge bfqq exactly with the service it has received.

Charging time to the first type of queues and the exact service to
the other has the effect of using the WF2Q+ policy to schedule the
former on a timeslice basis, without violating service domain
guarantees among the latter.

.. This file was automatic generated / don't edit.

