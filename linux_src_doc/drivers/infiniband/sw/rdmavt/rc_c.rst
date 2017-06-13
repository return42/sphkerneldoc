.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/sw/rdmavt/rc.c

.. _`rvt_compute_aeth`:

rvt_compute_aeth
================

.. c:function:: __be32 rvt_compute_aeth(struct rvt_qp *qp)

    compute the AETH (syndrome + MSN)

    :param struct rvt_qp \*qp:
        the queue pair to compute the AETH for

.. _`rvt_compute_aeth.description`:

Description
-----------

Returns the AETH.

.. _`rvt_get_credit`:

rvt_get_credit
==============

.. c:function:: void rvt_get_credit(struct rvt_qp *qp, u32 aeth)

    flush the send work queue of a QP

    :param struct rvt_qp \*qp:
        the qp who's send work queue to flush

    :param u32 aeth:
        the Acknowledge Extended Transport Header

.. _`rvt_get_credit.description`:

Description
-----------

The QP s_lock should be held.

.. This file was automatic generated / don't edit.

