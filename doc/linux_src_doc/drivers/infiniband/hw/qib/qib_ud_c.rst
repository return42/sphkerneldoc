.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_ud.c

.. _`qib_ud_loopback`:

qib_ud_loopback
===============

.. c:function:: void qib_ud_loopback(struct rvt_qp *sqp, struct rvt_swqe *swqe)

    handle send on loopback QPs

    :param struct rvt_qp \*sqp:
        the sending QP

    :param struct rvt_swqe \*swqe:
        the send work request

.. _`qib_ud_loopback.description`:

Description
-----------

This is called from \ :c:func:`qib_make_ud_req`\  to forward a WQE addressed
to the same HCA.
Note that the receive interrupt handler may be calling \ :c:func:`qib_ud_rcv`\ 
while this is being called.

.. _`qib_make_ud_req`:

qib_make_ud_req
===============

.. c:function:: int qib_make_ud_req(struct rvt_qp *qp, unsigned long *flags)

    construct a UD request packet

    :param struct rvt_qp \*qp:
        the QP

    :param unsigned long \*flags:
        *undescribed*

.. _`qib_make_ud_req.description`:

Description
-----------

Assumes the s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`qib_ud_rcv`:

qib_ud_rcv
==========

.. c:function:: void qib_ud_rcv(struct qib_ibport *ibp, struct qib_ib_header *hdr, int has_grh, void *data, u32 tlen, struct rvt_qp *qp)

    receive an incoming UD packet

    :param struct qib_ibport \*ibp:
        the port the packet came in on

    :param struct qib_ib_header \*hdr:
        the packet header

    :param int has_grh:
        true if the packet has a GRH

    :param void \*data:
        the packet data

    :param u32 tlen:
        the packet length

    :param struct rvt_qp \*qp:
        the QP the packet came on

.. _`qib_ud_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_qp_rcv`\  to process an incoming UD packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

