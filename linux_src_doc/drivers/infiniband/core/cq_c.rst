.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cq.c

.. _`ib_process_cq_direct`:

ib_process_cq_direct
====================

.. c:function:: int ib_process_cq_direct(struct ib_cq *cq, int budget)

    process a CQ in caller context

    :param struct ib_cq \*cq:
        CQ to process

    :param int budget:
        number of CQEs to poll for

.. _`ib_process_cq_direct.description`:

Description
-----------

This function is used to process all outstanding CQ entries on a
\ ``IB_POLL_DIRECT``\  CQ.  It does not offload CQ processing to a different
context and does not ask for completion interrupts from the HCA.

.. _`ib_process_cq_direct.note`:

Note
----

do not pass -1 as \ ``budget``\  unless it is guaranteed that the number
of completions that will be processed is small.

.. _`ib_alloc_cq`:

ib_alloc_cq
===========

.. c:function:: struct ib_cq *ib_alloc_cq(struct ib_device *dev, void *private, int nr_cqe, int comp_vector, enum ib_poll_context poll_ctx)

    allocate a completion queue

    :param struct ib_device \*dev:
        device to allocate the CQ for

    :param void \*private:
        driver private data, accessible from cq->cq_context

    :param int nr_cqe:
        number of CQEs to allocate

    :param int comp_vector:
        HCA completion vectors for this CQ

    :param enum ib_poll_context poll_ctx:
        context to poll the CQ from.

.. _`ib_alloc_cq.description`:

Description
-----------

This is the proper interface to allocate a CQ for in-kernel users. A
CQ allocated with this interface will automatically be polled from the
specified context. The ULP must use wr->wr_cqe instead of wr->wr_id
to use this CQ abstraction.

.. _`ib_free_cq`:

ib_free_cq
==========

.. c:function:: void ib_free_cq(struct ib_cq *cq)

    free a completion queue

    :param struct ib_cq \*cq:
        completion queue to free.

.. This file was automatic generated / don't edit.

