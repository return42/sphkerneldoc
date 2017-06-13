.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_ruc.c

.. _`qib_get_rwqe`:

qib_get_rwqe
============

.. c:function:: int qib_get_rwqe(struct rvt_qp *qp, int wr_id_only)

    copy the next RWQE into the QP's RWQE

    :param struct rvt_qp \*qp:
        the QP

    :param int wr_id_only:
        update qp->r_wr_id only, not qp->r_sge

.. _`qib_get_rwqe.description`:

Description
-----------

Return -1 if there is a local error, 0 if no RWQE is available,
otherwise return 1.

Can be called from interrupt level.

.. _`qib_ruc_loopback`:

qib_ruc_loopback
================

.. c:function:: void qib_ruc_loopback(struct rvt_qp *sqp)

    handle UC and RC lookback requests

    :param struct rvt_qp \*sqp:
        the sending QP

.. _`qib_ruc_loopback.description`:

Description
-----------

This is called from \ :c:func:`qib_do_send`\  to
forward a WQE addressed to the same HCA.
Note that although we are single threaded due to the tasklet, we still
have to protect against \ :c:func:`post_send`\ .  We don't have to worry about
receive interrupts since this is a connected protocol and all packets
will pass through here.

.. _`qib_make_grh`:

qib_make_grh
============

.. c:function:: u32 qib_make_grh(struct qib_ibport *ibp, struct ib_grh *hdr, const struct ib_global_route *grh, u32 hwords, u32 nwords)

    construct a GRH header

    :param struct qib_ibport \*ibp:
        a pointer to the IB port

    :param struct ib_grh \*hdr:
        a pointer to the GRH header being constructed

    :param const struct ib_global_route \*grh:
        the global route address to send to

    :param u32 hwords:
        the number of 32 bit words of header being sent

    :param u32 nwords:
        the number of 32 bit words of data being sent

.. _`qib_make_grh.description`:

Description
-----------

Return the size of the header in 32 bit words.

.. _`qib_do_send`:

qib_do_send
===========

.. c:function:: void qib_do_send(struct rvt_qp *qp)

    perform a send on a QP

    :param struct rvt_qp \*qp:
        pointer to the QP

.. _`qib_do_send.description`:

Description
-----------

Process entries in the send work queue until credit or queue is
exhausted.  Only allow one CPU to send a packet per QP (tasklet).
Otherwise, two threads could send packets out of order.

.. This file was automatic generated / don't edit.

