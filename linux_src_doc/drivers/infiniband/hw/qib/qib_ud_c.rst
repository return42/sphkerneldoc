.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_ud.c

.. _`qib_ud_loopback`:

qib_ud_loopback
===============

.. c:function:: void qib_ud_loopback(struct rvt_qp *sqp, struct rvt_swqe *swqe)

    handle send on loopback QPs

    :param sqp:
        the sending QP
    :type sqp: struct rvt_qp \*

    :param swqe:
        the send work request
    :type swqe: struct rvt_swqe \*

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

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

    :param flags:
        *undescribed*
    :type flags: unsigned long \*

.. _`qib_make_ud_req.description`:

Description
-----------

Assumes the s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`qib_ud_rcv`:

qib_ud_rcv
==========

.. c:function:: void qib_ud_rcv(struct qib_ibport *ibp, struct ib_header *hdr, int has_grh, void *data, u32 tlen, struct rvt_qp *qp)

    receive an incoming UD packet

    :param ibp:
        the port the packet came in on
    :type ibp: struct qib_ibport \*

    :param hdr:
        the packet header
    :type hdr: struct ib_header \*

    :param has_grh:
        true if the packet has a GRH
    :type has_grh: int

    :param data:
        the packet data
    :type data: void \*

    :param tlen:
        the packet length
    :type tlen: u32

    :param qp:
        the QP the packet came on
    :type qp: struct rvt_qp \*

.. _`qib_ud_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_qp_rcv`\  to process an incoming UD packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

