.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/qp.h

.. _`hfi1_create_qp`:

hfi1_create_qp
==============

.. c:function:: struct ib_qp *hfi1_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create a queue pair for a device

    :param ibpd:
        the protection domain who's device we create the queue pair for
    :type ibpd: struct ib_pd \*

    :param init_attr:
        the attributes of the queue pair
    :type init_attr: struct ib_qp_init_attr \*

    :param udata:
        user data for libibverbs.so
    :type udata: struct ib_udata \*

.. _`hfi1_create_qp.description`:

Description
-----------

Returns the queue pair on success, otherwise returns an errno.

Called by the \ :c:func:`ib_create_qp`\  core verbs function.

.. _`hfi1_qp_wakeup`:

hfi1_qp_wakeup
==============

.. c:function:: void hfi1_qp_wakeup(struct rvt_qp *qp, u32 flag)

    wake up on the indicated event

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

    :param flag:
        flag the qp on which the qp is stalled
    :type flag: u32

.. This file was automatic generated / don't edit.

