.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_srq.c

.. _`pvrdma_query_srq`:

pvrdma_query_srq
================

.. c:function:: int pvrdma_query_srq(struct ib_srq *ibsrq, struct ib_srq_attr *srq_attr)

    query shared receive queue

    :param struct ib_srq \*ibsrq:
        the shared receive queue to query

    :param struct ib_srq_attr \*srq_attr:
        attributes to query and return to client

.. _`pvrdma_create_srq`:

pvrdma_create_srq
=================

.. c:function:: struct ib_srq *pvrdma_create_srq(struct ib_pd *pd, struct ib_srq_init_attr *init_attr, struct ib_udata *udata)

    create shared receive queue

    :param struct ib_pd \*pd:
        protection domain

    :param struct ib_srq_init_attr \*init_attr:
        shared receive queue attributes

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_destroy_srq`:

pvrdma_destroy_srq
==================

.. c:function:: int pvrdma_destroy_srq(struct ib_srq *srq)

    destroy shared receive queue

    :param struct ib_srq \*srq:
        the shared receive queue to destroy

.. _`pvrdma_modify_srq`:

pvrdma_modify_srq
=================

.. c:function:: int pvrdma_modify_srq(struct ib_srq *ibsrq, struct ib_srq_attr *attr, enum ib_srq_attr_mask attr_mask, struct ib_udata *udata)

    modify shared receive queue attributes

    :param struct ib_srq \*ibsrq:
        the shared receive queue to modify

    :param struct ib_srq_attr \*attr:
        the shared receive queue's new attributes

    :param enum ib_srq_attr_mask attr_mask:
        attributes mask

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_modify_srq.description`:

Description
-----------

@returns 0 on success, otherwise returns an errno.

.. This file was automatic generated / don't edit.

