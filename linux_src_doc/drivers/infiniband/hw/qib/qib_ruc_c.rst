.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_ruc.c

.. _`qib_make_grh`:

qib_make_grh
============

.. c:function:: u32 qib_make_grh(struct qib_ibport *ibp, struct ib_grh *hdr, const struct ib_global_route *grh, u32 hwords, u32 nwords)

    construct a GRH header

    :param ibp:
        a pointer to the IB port
    :type ibp: struct qib_ibport \*

    :param hdr:
        a pointer to the GRH header being constructed
    :type hdr: struct ib_grh \*

    :param grh:
        the global route address to send to
    :type grh: const struct ib_global_route \*

    :param hwords:
        the number of 32 bit words of header being sent
    :type hwords: u32

    :param nwords:
        the number of 32 bit words of data being sent
    :type nwords: u32

.. _`qib_make_grh.description`:

Description
-----------

Return the size of the header in 32 bit words.

.. _`qib_do_send`:

qib_do_send
===========

.. c:function:: void qib_do_send(struct rvt_qp *qp)

    perform a send on a QP

    :param qp:
        pointer to the QP
    :type qp: struct rvt_qp \*

.. _`qib_do_send.description`:

Description
-----------

Process entries in the send work queue until credit or queue is
exhausted.  Only allow one CPU to send a packet per QP (tasklet).
Otherwise, two threads could send packets out of order.

.. This file was automatic generated / don't edit.

