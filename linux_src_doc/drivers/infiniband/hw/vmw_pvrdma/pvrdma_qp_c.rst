.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/vmw_pvrdma/pvrdma_qp.c

.. _`pvrdma_create_qp`:

pvrdma_create_qp
================

.. c:function:: struct ib_qp *pvrdma_create_qp(struct ib_pd *pd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create queue pair

    :param struct ib_pd \*pd:
        protection domain

    :param struct ib_qp_init_attr \*init_attr:
        queue pair attributes

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_destroy_qp`:

pvrdma_destroy_qp
=================

.. c:function:: int pvrdma_destroy_qp(struct ib_qp *qp)

    destroy a queue pair

    :param struct ib_qp \*qp:
        the queue pair to destroy

.. _`pvrdma_modify_qp`:

pvrdma_modify_qp
================

.. c:function:: int pvrdma_modify_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_udata *udata)

    modify queue pair attributes

    :param struct ib_qp \*ibqp:
        the queue pair

    :param struct ib_qp_attr \*attr:
        the new queue pair's attributes

    :param int attr_mask:
        attributes mask

    :param struct ib_udata \*udata:
        user data

.. _`pvrdma_modify_qp.description`:

Description
-----------

@returns 0 on success, otherwise returns an errno.

.. _`pvrdma_post_send`:

pvrdma_post_send
================

.. c:function:: int pvrdma_post_send(struct ib_qp *ibqp, struct ib_send_wr *wr, struct ib_send_wr **bad_wr)

    post send work request entries on a QP

    :param struct ib_qp \*ibqp:
        the QP

    :param struct ib_send_wr \*wr:
        work request list to post

    :param struct ib_send_wr \*\*bad_wr:
        the first bad WR returned

.. _`pvrdma_post_recv`:

pvrdma_post_recv
================

.. c:function:: int pvrdma_post_recv(struct ib_qp *ibqp, struct ib_recv_wr *wr, struct ib_recv_wr **bad_wr)

    post receive work request entries on a QP

    :param struct ib_qp \*ibqp:
        the QP

    :param struct ib_recv_wr \*wr:
        the work request list to post

    :param struct ib_recv_wr \*\*bad_wr:
        the first bad WR returned

.. _`pvrdma_query_qp`:

pvrdma_query_qp
===============

.. c:function:: int pvrdma_query_qp(struct ib_qp *ibqp, struct ib_qp_attr *attr, int attr_mask, struct ib_qp_init_attr *init_attr)

    query a queue pair's attributes

    :param struct ib_qp \*ibqp:
        the queue pair to query

    :param struct ib_qp_attr \*attr:
        the queue pair's attributes

    :param int attr_mask:
        attributes mask

    :param struct ib_qp_init_attr \*init_attr:
        initial queue pair attributes

.. _`pvrdma_query_qp.description`:

Description
-----------

@returns 0 on success, otherwise returns an errno.

.. This file was automatic generated / don't edit.

