.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_srq.c

.. _`pvrdma_query_srq`:

pvrdma_query_srq
================

.. c:function:: int pvrdma_query_srq(struct ib_srq *ibsrq, struct ib_srq_attr *srq_attr)

    query shared receive queue

    :param ibsrq:
        the shared receive queue to query
    :type ibsrq: struct ib_srq \*

    :param srq_attr:
        attributes to query and return to client
    :type srq_attr: struct ib_srq_attr \*

.. _`pvrdma_create_srq`:

pvrdma_create_srq
=================

.. c:function:: struct ib_srq *pvrdma_create_srq(struct ib_pd *pd, struct ib_srq_init_attr *init_attr, struct ib_udata *udata)

    create shared receive queue

    :param pd:
        protection domain
    :type pd: struct ib_pd \*

    :param init_attr:
        shared receive queue attributes
    :type init_attr: struct ib_srq_init_attr \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_destroy_srq`:

pvrdma_destroy_srq
==================

.. c:function:: int pvrdma_destroy_srq(struct ib_srq *srq)

    destroy shared receive queue

    :param srq:
        the shared receive queue to destroy
    :type srq: struct ib_srq \*

.. _`pvrdma_modify_srq`:

pvrdma_modify_srq
=================

.. c:function:: int pvrdma_modify_srq(struct ib_srq *ibsrq, struct ib_srq_attr *attr, enum ib_srq_attr_mask attr_mask, struct ib_udata *udata)

    modify shared receive queue attributes

    :param ibsrq:
        the shared receive queue to modify
    :type ibsrq: struct ib_srq \*

    :param attr:
        the shared receive queue's new attributes
    :type attr: struct ib_srq_attr \*

    :param attr_mask:
        attributes mask
    :type attr_mask: enum ib_srq_attr_mask

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_modify_srq.description`:

Description
-----------

\ ``returns``\  0 on success, otherwise returns an errno.

.. This file was automatic generated / don't edit.

