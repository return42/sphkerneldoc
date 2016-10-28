.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/qp.h

.. _`hfi1_compute_aeth`:

hfi1_compute_aeth
=================

.. c:function:: __be32 hfi1_compute_aeth(struct rvt_qp *qp)

    compute the AETH (syndrome + MSN)

    :param struct rvt_qp \*qp:
        the queue pair to compute the AETH for

.. _`hfi1_compute_aeth.description`:

Description
-----------

Returns the AETH.

.. _`hfi1_create_qp`:

hfi1_create_qp
==============

.. c:function:: struct ib_qp *hfi1_create_qp(struct ib_pd *ibpd, struct ib_qp_init_attr *init_attr, struct ib_udata *udata)

    create a queue pair for a device

    :param struct ib_pd \*ibpd:
        the protection domain who's device we create the queue pair for

    :param struct ib_qp_init_attr \*init_attr:
        the attributes of the queue pair

    :param struct ib_udata \*udata:
        user data for libibverbs.so

.. _`hfi1_create_qp.description`:

Description
-----------

Returns the queue pair on success, otherwise returns an errno.

Called by the \ :c:func:`ib_create_qp`\  core verbs function.

.. _`hfi1_get_credit`:

hfi1_get_credit
===============

.. c:function:: void hfi1_get_credit(struct rvt_qp *qp, u32 aeth)

    flush the send work queue of a QP

    :param struct rvt_qp \*qp:
        the qp who's send work queue to flush

    :param u32 aeth:
        the Acknowledge Extended Transport Header

.. _`hfi1_get_credit.description`:

Description
-----------

The QP s_lock should be held.

.. _`hfi1_qp_wakeup`:

hfi1_qp_wakeup
==============

.. c:function:: void hfi1_qp_wakeup(struct rvt_qp *qp, u32 flag)

    wake up on the indicated event

    :param struct rvt_qp \*qp:
        the QP

    :param u32 flag:
        flag the qp on which the qp is stalled

.. _`qp_iter_init`:

qp_iter_init
============

.. c:function:: struct qp_iter *qp_iter_init(struct hfi1_ibdev *dev)

    initialize the iterator for the qp hash list

    :param struct hfi1_ibdev \*dev:
        the hfi1_ibdev

.. _`qp_iter_next`:

qp_iter_next
============

.. c:function:: int qp_iter_next(struct qp_iter *iter)

    Find the next qp in the hash list

    :param struct qp_iter \*iter:
        the iterator for the qp hash list

.. _`qp_iter_print`:

qp_iter_print
=============

.. c:function:: void qp_iter_print(struct seq_file *s, struct qp_iter *iter)

    print the qp information to seq_file

    :param struct seq_file \*s:
        the seq_file to emit the qp information on

    :param struct qp_iter \*iter:
        the iterator for the qp hash list

.. _`qp_comm_est`:

qp_comm_est
===========

.. c:function:: void qp_comm_est(struct rvt_qp *qp)

    handle trap with QP established

    :param struct rvt_qp \*qp:
        the QP

.. This file was automatic generated / don't edit.

