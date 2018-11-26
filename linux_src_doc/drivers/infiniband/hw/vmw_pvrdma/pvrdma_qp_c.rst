.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_qp.c

.. _`pvrdma_create_qp`:

pvrdma_create_qp
================

.. c:function:: struct ib_qp *pvrdma_create_qp(struct ib_pd *pd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create queue pair

    :param pd:
        protection domain
    :type pd: struct ib_pd \*

    :param init_attr:
        queue pair attributes
    :type init_attr: struct ib_qp_init_attr \*

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_destroy_qp`:

pvrdma_destroy_qp
=================

.. c:function:: int pvrdma_destroy_qp(struct ib_qp *qp)

    destroy a queue pair

    :param qp:
        the queue pair to destroy
    :type qp: struct ib_qp \*

.. _`pvrdma_modify_qp`:

pvrdma_modify_qp
================

.. c:function:: int pvrdma_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    modify queue pair attributes

    :param ibqp:
        the queue pair
    :type ibqp: struct ib_qp \*

    :param attr:
        the new queue pair's attributes
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        attributes mask
    :type attr_mask: int

    :param udata:
        user data
    :type udata: struct ib_udata \*

.. _`pvrdma_modify_qp.description`:

Description
-----------

\ ``returns``\  0 on success, otherwise returns an errno.

.. _`pvrdma_post_send`:

pvrdma_post_send
================

.. c:function:: int pvrdma_post_send(struct ib_qp *ibqp, const struct ib_send_wr *wr, const struct ib_send_wr **bad_wr)

    post send work request entries on a QP

    :param ibqp:
        the QP
    :type ibqp: struct ib_qp \*

    :param wr:
        work request list to post
    :type wr: const struct ib_send_wr \*

    :param bad_wr:
        the first bad WR returned
    :type bad_wr: const struct ib_send_wr \*\*

.. _`pvrdma_post_recv`:

pvrdma_post_recv
================

.. c:function:: int pvrdma_post_recv(struct ib_qp *ibqp, const struct ib_recv_wr *wr, const struct ib_recv_wr **bad_wr)

    post receive work request entries on a QP

    :param ibqp:
        the QP
    :type ibqp: struct ib_qp \*

    :param wr:
        the work request list to post
    :type wr: const struct ib_recv_wr \*

    :param bad_wr:
        the first bad WR returned
    :type bad_wr: const struct ib_recv_wr \*\*

.. _`pvrdma_query_qp`:

pvrdma_query_qp
===============

.. c:function:: int pvrdma_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    query a queue pair's attributes

    :param ibqp:
        the queue pair to query
    :type ibqp: struct ib_qp \*

    :param attr:
        the queue pair's attributes
    :type attr: struct ib_qp_attr \*

    :param attr_mask:
        attributes mask
    :type attr_mask: int

    :param init_attr:
        initial queue pair attributes
    :type init_attr: struct ib_qp_init_attr \*

.. _`pvrdma_query_qp.description`:

Description
-----------

\ ``returns``\  0 on success, otherwise returns an errno.

.. This file was automatic generated / don't edit.

