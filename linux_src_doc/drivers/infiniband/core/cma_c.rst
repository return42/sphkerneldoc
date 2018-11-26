.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/cma.c

.. _`rdma_iw_cm_id`:

rdma_iw_cm_id
=============

.. c:function:: struct iw_cm_id *rdma_iw_cm_id(struct rdma_cm_id *id)

    return the iw_cm_id pointer for this cm_id.

    :param id:
        Communication Identifier
    :type id: struct rdma_cm_id \*

.. _`rdma_res_to_id`:

rdma_res_to_id
==============

.. c:function:: struct rdma_cm_id *rdma_res_to_id(struct rdma_restrack_entry *res)

    return the rdma_cm_id pointer for this restrack.

    :param res:
        rdma resource tracking entry pointer
    :type res: struct rdma_restrack_entry \*

.. _`cma_acquire_dev_by_src_ip`:

cma_acquire_dev_by_src_ip
=========================

.. c:function:: int cma_acquire_dev_by_src_ip(struct rdma_id_private *id_priv)

    Acquire cma device, port, gid attribute based on source ip address.

    :param id_priv:
        cm_id which should be bound to cma device
    :type id_priv: struct rdma_id_private \*

.. _`cma_acquire_dev_by_src_ip.description`:

Description
-----------

\ :c:func:`cma_acquire_dev_by_src_ip`\  binds cm id to cma device, port and GID attribute
based on source IP address. It returns 0 on success or error code otherwise.
It is applicable to active and passive side cm_id.

.. _`cma_ib_acquire_dev`:

cma_ib_acquire_dev
==================

.. c:function:: int cma_ib_acquire_dev(struct rdma_id_private *id_priv, const struct rdma_id_private *listen_id_priv, struct cma_req_info *req)

    Acquire cma device, port and SGID attribute

    :param id_priv:
        cm id to bind to cma device
    :type id_priv: struct rdma_id_private \*

    :param listen_id_priv:
        listener cm id to match against
    :type listen_id_priv: const struct rdma_id_private \*

    :param req:
        Pointer to req structure containaining incoming
        request information
        \ :c:func:`cma_ib_acquire_dev`\  acquires cma device, port and SGID attribute when
        rdma device matches for listen_id and incoming request. It also verifies
        that a GID table entry is present for the source address.
        Returns 0 on success, or returns error code otherwise.
    :type req: struct cma_req_info \*

.. This file was automatic generated / don't edit.

