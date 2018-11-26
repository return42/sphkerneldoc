.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_rc.c

.. _`qib_make_rc_ack`:

qib_make_rc_ack
===============

.. c:function:: int qib_make_rc_ack(struct qib_ibdev *dev, struct rvt_qp *qp, struct ib_other_headers *ohdr, u32 pmtu)

    construct a response packet (ACK, NAK, or RDMA read)

    :param dev:
        the device for this QP
    :type dev: struct qib_ibdev \*

    :param qp:
        a pointer to the QP
    :type qp: struct rvt_qp \*

    :param ohdr:
        a pointer to the IB header being constructed
    :type ohdr: struct ib_other_headers \*

    :param pmtu:
        the path MTU
    :type pmtu: u32

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

    :param qp:
        a pointer to the QP
    :type qp: struct rvt_qp \*

    :param flags:
        *undescribed*
    :type flags: unsigned long \*

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

    :param qp:
        a pointer to the QP
    :type qp: struct rvt_qp \*

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

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

    :param psn:
        the packet sequence number to restart at
    :type psn: u32

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

    :param qp:
        the QP the ACK came in on
    :type qp: struct rvt_qp \*

    :param aeth:
        *undescribed*
    :type aeth: u32

    :param psn:
        the packet sequence number of the ACK
    :type psn: u32

    :param opcode:
        the opcode of the request that resulted in the ACK
    :type opcode: int

    :param val:
        *undescribed*
    :type val: u64

    :param rcd:
        *undescribed*
    :type rcd: struct qib_ctxtdata \*

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

.. c:function:: void qib_rc_rcv_resp(struct qib_ibport *ibp, struct ib_other_headers *ohdr, void *data, u32 tlen, struct rvt_qp *qp, u32 opcode, u32 psn, u32 hdrsize, u32 pmtu, struct qib_ctxtdata *rcd)

    process an incoming RC response packet

    :param ibp:
        the port this packet came in on
    :type ibp: struct qib_ibport \*

    :param ohdr:
        the other headers for this packet
    :type ohdr: struct ib_other_headers \*

    :param data:
        the packet data
    :type data: void \*

    :param tlen:
        the packet length
    :type tlen: u32

    :param qp:
        the QP for this packet
    :type qp: struct rvt_qp \*

    :param opcode:
        the opcode for this packet
    :type opcode: u32

    :param psn:
        the packet sequence number for this packet
    :type psn: u32

    :param hdrsize:
        the header length
    :type hdrsize: u32

    :param pmtu:
        the path MTU
    :type pmtu: u32

    :param rcd:
        *undescribed*
    :type rcd: struct qib_ctxtdata \*

.. _`qib_rc_rcv_resp.description`:

Description
-----------

This is called from \ :c:func:`qib_rc_rcv`\  to process an incoming RC response
packet for the given QP.
Called at interrupt level.

.. _`qib_rc_rcv_error`:

qib_rc_rcv_error
================

.. c:function:: int qib_rc_rcv_error(struct ib_other_headers *ohdr, void *data, struct rvt_qp *qp, u32 opcode, u32 psn, int diff, struct qib_ctxtdata *rcd)

    process an incoming duplicate or error RC packet

    :param ohdr:
        the other headers for this packet
    :type ohdr: struct ib_other_headers \*

    :param data:
        the packet data
    :type data: void \*

    :param qp:
        the QP for this packet
    :type qp: struct rvt_qp \*

    :param opcode:
        the opcode for this packet
    :type opcode: u32

    :param psn:
        the packet sequence number for this packet
    :type psn: u32

    :param diff:
        the difference between the PSN and the expected PSN
    :type diff: int

    :param rcd:
        *undescribed*
    :type rcd: struct qib_ctxtdata \*

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

.. c:function:: void qib_rc_rcv(struct qib_ctxtdata *rcd, struct ib_header *hdr, int has_grh, void *data, u32 tlen, struct rvt_qp *qp)

    process an incoming RC packet

    :param rcd:
        the context pointer
    :type rcd: struct qib_ctxtdata \*

    :param hdr:
        the header of this packet
    :type hdr: struct ib_header \*

    :param has_grh:
        true if the header has a GRH
    :type has_grh: int

    :param data:
        the packet data
    :type data: void \*

    :param tlen:
        the packet length
    :type tlen: u32

    :param qp:
        the QP for this packet
    :type qp: struct rvt_qp \*

.. _`qib_rc_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_qp_rcv`\  to process an incoming RC packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

