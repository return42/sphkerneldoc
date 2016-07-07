.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_uc.c

.. _`qib_make_uc_req`:

qib_make_uc_req
===============

.. c:function:: int qib_make_uc_req(struct rvt_qp *qp, unsigned long *flags)

    construct a request packet (SEND, RDMA write)

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param unsigned long \*flags:
        *undescribed*

.. _`qib_make_uc_req.description`:

Description
-----------

Assumes the s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`qib_uc_rcv`:

qib_uc_rcv
==========

.. c:function:: void qib_uc_rcv(struct qib_ibport *ibp, struct qib_ib_header *hdr, int has_grh, void *data, u32 tlen, struct rvt_qp *qp)

    handle an incoming UC packet

    :param struct qib_ibport \*ibp:
        the port the packet came in on

    :param struct qib_ib_header \*hdr:
        the header of the packet

    :param int has_grh:
        true if the packet has a GRH

    :param void \*data:
        the packet data

    :param u32 tlen:
        the length of the packet

    :param struct rvt_qp \*qp:
        the QP for this packet.

.. _`qib_uc_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_qp_rcv`\  to process an incoming UC packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

