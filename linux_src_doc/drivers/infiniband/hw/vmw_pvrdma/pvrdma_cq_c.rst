.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_cq.c

.. _`pvrdma_req_notify_cq`:

pvrdma_req_notify_cq
====================

.. c:function:: int pvrdma_req_notify_cq(struct ib_cq *ibcq, enum ib_cq_notify_flags notify_flags)

    request notification for a completion queue

    :param struct ib_cq \*ibcq:
        the completion queue

    :param enum ib_cq_notify_flags notify_flags:
        notification flags

.. _`pvrdma_create_cq`:

pvrdma_create_cq
================

.. c:function:: struct ib_cq *pvrdma_create_cq(struct ib_device *ibdev, const struct ib_cq_init_attr *attr, struct ib_ucontext *context, struct ib_udata *udata)

    create completion queue

    :param struct ib_device \*ibdev:
        the device

    :param const struct ib_cq_init_attr \*attr:
        completion queue attributes

    :param struct ib_ucontext \*context:
        user context

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_destroy_cq`:

pvrdma_destroy_cq
=================

.. c:function:: int pvrdma_destroy_cq(struct ib_cq *cq)

    destroy completion queue

    :param struct ib_cq \*cq:
        the completion queue to destroy.

.. _`pvrdma_modify_cq`:

pvrdma_modify_cq
================

.. c:function:: int pvrdma_modify_cq(struct ib_cq *cq, u16 cq_count, u16 cq_period)

    modify the CQ moderation parameters

    :param struct ib_cq \*cq:
        *undescribed*

    :param u16 cq_count:
        number of CQEs that will trigger an event

    :param u16 cq_period:
        max period of time in usec before triggering an event

.. _`pvrdma_poll_cq`:

pvrdma_poll_cq
==============

.. c:function:: int pvrdma_poll_cq(struct ib_cq *ibcq, int num_entries, struct ib_wc *wc)

    poll for work completion queue entries

    :param struct ib_cq \*ibcq:
        completion queue

    :param int num_entries:
        the maximum number of entries

    :param struct ib_wc \*wc:
        *undescribed*

.. _`pvrdma_resize_cq`:

pvrdma_resize_cq
================

.. c:function:: int pvrdma_resize_cq(struct ib_cq *ibcq, int entries, struct ib_udata *udata)

    resize CQ

    :param struct ib_cq \*ibcq:
        the completion queue

    :param int entries:
        CQ entries

    :param struct ib_udata \*udata:
        user data

.. This file was automatic generated / don't edit.

