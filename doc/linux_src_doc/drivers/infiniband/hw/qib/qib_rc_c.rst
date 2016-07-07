.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_rc.c

.. _`qib_make_rc_ack`:

qib_make_rc_ack
===============

.. c:function:: int qib_make_rc_ack(struct qib_ibdev *dev, struct rvt_qp *qp, struct qib_other_headers *ohdr, u32 pmtu)

    construct a response packet (ACK, NAK, or RDMA read)

    :param struct qib_ibdev \*dev:
        the device for this QP

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param struct qib_other_headers \*ohdr:
        a pointer to the IB header being constructed

    :param u32 pmtu:
        the path MTU

.. _`qib_make_rc_ack.description`:

Description
-----------

Return 1 if constructed; otherwise, return 0.
Note that we are in the responder's side of the QP context.
Note the QP s_lock must be held.

.. _`qib_make_rc_req`:

qib_make_rc_req
===============

.. c:function:: int qib_make_rc_req(struct rvt_qp *qp, unsigned long *flags)

    construct a request packet (SEND, RDMA r/w, ATOMIC)

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param unsigned long \*flags:
        *undescribed*

.. _`qib_make_rc_req.description`:

Description
-----------

Assumes the s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`qib_send_rc_ack`:

qib_send_rc_ack
===============

.. c:function:: void qib_send_rc_ack(struct rvt_qp *qp)

    Construct an ACK packet and send it

    :param struct rvt_qp \*qp:
        a pointer to the QP

.. _`qib_send_rc_ack.description`:

Description
-----------

This is called from \ :c:func:`qib_rc_rcv`\  and \ :c:func:`qib_kreceive`\ .
Note that RDMA reads and atomics are handled in the
send side QP state and tasklet.

.. _`reset_psn`:

reset_psn
=========

.. c:function:: void reset_psn(struct rvt_qp *qp, u32 psn)

    reset the QP state to send starting from PSN

    :param struct rvt_qp \*qp:
        the QP

    :param u32 psn:
        the packet sequence number to restart at

.. _`reset_psn.description`:

Description
-----------

This is called from \ :c:func:`qib_rc_rcv`\  to process an incoming RC ACK
for the given QP.
Called at interrupt level with the QP s_lock held.

.. _`do_rc_ack`:

do_rc_ack
=========

.. c:function:: int do_rc_ack(struct rvt_qp *qp, u32 aeth, u32 psn, int opcode, u64 val, struct qib_ctxtdata *rcd)

    process an incoming RC ACK

    :param struct rvt_qp \*qp:
        the QP the ACK came in on

    :param u32 aeth:
        *undescribed*

    :param u32 psn:
        the packet sequence number of the ACK

    :param int opcode:
        the opcode of the request that resulted in the ACK

    :param u64 val:
        *undescribed*

    :param struct qib_ctxtdata \*rcd:
        *undescribed*

.. _`do_rc_ack.description`:

Description
-----------

This is called from \ :c:func:`qib_rc_rcv_resp`\  to process an incoming RC ACK
for the given QP.
Called at interrupt level with the QP s_lock held.
Returns 1 if OK, 0 if current operation should be aborted (NAK).

.. _`qib_rc_rcv_resp`:

qib_rc_rcv_resp
===============

.. c:function:: void qib_rc_rcv_resp(struct qib_ibport *ibp, struct qib_other_headers *ohdr, void *data, u32 tlen, struct rvt_qp *qp, u32 opcode, u32 psn, u32 hdrsize, u32 pmtu, struct qib_ctxtdata *rcd)

    process an incoming RC response packet

    :param struct qib_ibport \*ibp:
        the port this packet came in on

    :param struct qib_other_headers \*ohdr:
        the other headers for this packet

    :param void \*data:
        the packet data

    :param u32 tlen:
        the packet length

    :param struct rvt_qp \*qp:
        the QP for this packet

    :param u32 opcode:
        the opcode for this packet

    :param u32 psn:
        the packet sequence number for this packet

    :param u32 hdrsize:
        the header length

    :param u32 pmtu:
        the path MTU

    :param struct qib_ctxtdata \*rcd:
        *undescribed*

.. _`qib_rc_rcv_resp.description`:

Description
-----------

This is called from \ :c:func:`qib_rc_rcv`\  to process an incoming RC response
packet for the given QP.
Called at interrupt level.

.. _`qib_rc_rcv_error`:

qib_rc_rcv_error
================

.. c:function:: int qib_rc_rcv_error(struct qib_other_headers *ohdr, void *data, struct rvt_qp *qp, u32 opcode, u32 psn, int diff, struct qib_ctxtdata *rcd)

    process an incoming duplicate or error RC packet

    :param struct qib_other_headers \*ohdr:
        the other headers for this packet

    :param void \*data:
        the packet data

    :param struct rvt_qp \*qp:
        the QP for this packet

    :param u32 opcode:
        the opcode for this packet

    :param u32 psn:
        the packet sequence number for this packet

    :param int diff:
        the difference between the PSN and the expected PSN

    :param struct qib_ctxtdata \*rcd:
        *undescribed*

.. _`qib_rc_rcv_error.description`:

Description
-----------

This is called from \ :c:func:`qib_rc_rcv`\  to process an unexpected
incoming RC packet for the given QP.
Called at interrupt level.
Return 1 if no more processing is needed; otherwise return 0 to
schedule a response to be sent.

.. _`qib_rc_rcv`:

qib_rc_rcv
==========

.. c:function:: void qib_rc_rcv(struct qib_ctxtdata *rcd, struct qib_ib_header *hdr, int has_grh, void *data, u32 tlen, struct rvt_qp *qp)

    process an incoming RC packet

    :param struct qib_ctxtdata \*rcd:
        the context pointer

    :param struct qib_ib_header \*hdr:
        the header of this packet

    :param int has_grh:
        true if the header has a GRH

    :param void \*data:
        the packet data

    :param u32 tlen:
        the packet length

    :param struct rvt_qp \*qp:
        the QP for this packet

.. _`qib_rc_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_qp_rcv`\  to process an incoming RC packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

