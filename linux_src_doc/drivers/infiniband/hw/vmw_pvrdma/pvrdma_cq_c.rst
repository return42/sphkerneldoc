.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_cq.c

.. _`pvrdma_req_notify_cq`:

pvrdma_req_notify_cq
====================

.. c:function:: int pvrdma_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    request notification for a completion queue

    :param ibcq:
        the completion queue
    :type ibcq: struct ib_cq \*

    :param notify_flags:
        notification flags
    :type notify_flags: enum ib_cq_notify_flags

.. _`pvrdma_create_cq`:

pvrdma_create_cq
================

.. c:function:: struct ib_cq *pvrdma_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    create completion queue

    :param ibdev:
        the device
    :type ibdev: struct ib_device \*

    :param attr:
        completion queue attributes
    :type attr: const struct ib_cq_init_attr \*

    :param context:
        user context
    :type context: struct ib_ucontext \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_destroy_cq`:

pvrdma_destroy_cq
=================

.. c:function:: int pvrdma_destroy_cq(struct ib_cq *cq)

    destroy completion queue

    :param cq:
        the completion queue to destroy.
    :type cq: struct ib_cq \*

.. _`pvrdma_poll_cq`:

pvrdma_poll_cq
==============

.. c:function:: int pvrdma_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *wc)

    poll for work completion queue entries

    :param ibcq:
        completion queue
    :type ibcq: struct ib_cq \*

    :param num_entries:
        the maximum number of entries
    :type num_entries: int

    :param wc:
        *undescribed*
    :type wc: struct ib_wc \*

.. This file was automatic generated / don't edit.

