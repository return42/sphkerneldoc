.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/rc.c

.. _`make_rc_ack`:

make_rc_ack
===========

.. c:function:: int make_rc_ack(struct hfi1_ibdev *dev, struct rvt_qp *qp, struct ib_other_headers *ohdr, struct hfi1_pkt_state *ps)

    construct a response packet (ACK, NAK, or RDMA read)

    :param dev:
        the device for this QP
    :type dev: struct hfi1_ibdev \*

    :param qp:
        a pointer to the QP
    :type qp: struct rvt_qp \*

    :param ohdr:
        a pointer to the IB header being constructed
    :type ohdr: struct ib_other_headers \*

    :param ps:
        the xmit packet state
    :type ps: struct hfi1_pkt_state \*

.. _`make_rc_ack.description`:

Description
-----------

Return 1 if constructed; otherwise, return 0.
Note that we are in the responder's side of the QP context.
Note the QP s_lock must be held.

.. _`hfi1_make_rc_req`:

hfi1_make_rc_req
================

.. c:function:: int hfi1_make_rc_req(struct rvt_qp *qp, struct hfi1_pkt_state *ps)

    construct a request packet (SEND, RDMA r/w, ATOMIC)

    :param qp:
        a pointer to the QP
    :type qp: struct rvt_qp \*

    :param ps:
        *undescribed*
    :type ps: struct hfi1_pkt_state \*

.. _`hfi1_make_rc_req.description`:

Description
-----------

Assumes s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`hfi1_send_rc_ack`:

hfi1_send_rc_ack
================

.. c:function:: void hfi1_send_rc_ack(struct hfi1_packet *packet, bool is_fecn)

    Construct an ACK packet and send it

    :param packet:
        *undescribed*
    :type packet: struct hfi1_packet \*

    :param is_fecn:
        *undescribed*
    :type is_fecn: bool

.. _`hfi1_send_rc_ack.description`:

Description
-----------

This is called from \ :c:func:`hfi1_rc_rcv`\  and \ :c:func:`handle_receive_interrupt`\ .
Note that RDMA reads and atomics are handled in the
send side QP state and send engine.

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

This is called from \ :c:func:`hfi1_rc_rcv`\  to process an incoming RC ACK
for the given QP.
Called at interrupt level with the QP s_lock held.

.. _`do_rc_ack`:

do_rc_ack
=========

.. c:function:: int do_rc_ack(struct rvt_qp *qp, u32 aeth, u32 psn, int opcode, u64 val, struct hfi1_ctxtdata *rcd)

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
    :type rcd: struct hfi1_ctxtdata \*

.. _`do_rc_ack.description`:

Description
-----------

This is called from \ :c:func:`rc_rcv_resp`\  to process an incoming RC ACK
for the given QP.
May be called at interrupt level, with the QP s_lock held.
Returns 1 if OK, 0 if current operation should be aborted (NAK).

.. _`rc_rcv_resp`:

rc_rcv_resp
===========

.. c:function:: void rc_rcv_resp(struct hfi1_packet *packet)

    process an incoming RC response packet

    :param packet:
        data packet information
    :type packet: struct hfi1_packet \*

.. _`rc_rcv_resp.description`:

Description
-----------

This is called from \ :c:func:`hfi1_rc_rcv`\  to process an incoming RC response
packet for the given QP.
Called at interrupt level.

.. _`rc_rcv_error`:

rc_rcv_error
============

.. c:function:: int rc_rcv_error(struct ib_other_headers *ohdr, void *data, struct rvt_qp *qp, u32 opcode, u32 psn, int diff, struct hfi1_ctxtdata *rcd)

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
    :type rcd: struct hfi1_ctxtdata \*

.. _`rc_rcv_error.description`:

Description
-----------

This is called from \ :c:func:`hfi1_rc_rcv`\  to process an unexpected
incoming RC packet for the given QP.
Called at interrupt level.
Return 1 if no more processing is needed; otherwise return 0 to
schedule a response to be sent.

.. _`hfi1_rc_rcv`:

hfi1_rc_rcv
===========

.. c:function:: void hfi1_rc_rcv(struct hfi1_packet *packet)

    process an incoming RC packet

    :param packet:
        data packet information
    :type packet: struct hfi1_packet \*

.. _`hfi1_rc_rcv.description`:

Description
-----------

This is called from \ :c:func:`qp_rcv`\  to process an incoming RC packet
for the given QP.
May be called at interrupt level.

.. This file was automatic generated / don't edit.

