.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cma.c

.. _`rdma_iw_cm_id`:

rdma_iw_cm_id
=============

.. c:function:: struct iw_cm_id *rdma_iw_cm_id(struct rdma_cm_id *id)

    return the iw_cm_id pointer for this cm_id.

    :param struct rdma_cm_id \*id:
        Communication Identifier

.. _`rdma_res_to_id`:

rdma_res_to_id
==============

.. c:function:: struct rdma_cm_id *rdma_res_to_id(struct rdma_restrack_entry *res)

    return the rdma_cm_id pointer for this restrack.

    :param struct rdma_restrack_entry \*res:
        rdma resource tracking entry pointer

.. This file was automatic generated / don't edit.

