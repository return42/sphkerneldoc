.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/rc.c

.. _`hfi1_add_retry_timer`:

hfi1_add_retry_timer
====================

.. c:function:: void hfi1_add_retry_timer(struct rvt_qp *qp)

    add/start a retry timer \ ``qp``\  - the QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`hfi1_add_retry_timer.description`:

Description
-----------

add a retry timer on the QP

.. _`hfi1_add_rnr_timer`:

hfi1_add_rnr_timer
==================

.. c:function:: void hfi1_add_rnr_timer(struct rvt_qp *qp, u32 to)

    add/start an rnr timer \ ``qp``\  - the QP \ ``to``\  - timeout in usecs

    :param struct rvt_qp \*qp:
        *undescribed*

    :param u32 to:
        *undescribed*

.. _`hfi1_add_rnr_timer.description`:

Description
-----------

add an rnr timer on the QP

.. _`hfi1_mod_retry_timer`:

hfi1_mod_retry_timer
====================

.. c:function:: void hfi1_mod_retry_timer(struct rvt_qp *qp)

    mod a retry timer \ ``qp``\  - the QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`hfi1_mod_retry_timer.description`:

Description
-----------

Modify a potentially already running retry
timer

.. _`hfi1_stop_retry_timer`:

hfi1_stop_retry_timer
=====================

.. c:function:: int hfi1_stop_retry_timer(struct rvt_qp *qp)

    stop a retry timer \ ``qp``\  - the QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`hfi1_stop_retry_timer.description`:

Description
-----------

stop a retry timer and return if the timer
had been pending.

.. _`hfi1_stop_rc_timers`:

hfi1_stop_rc_timers
===================

.. c:function:: void hfi1_stop_rc_timers(struct rvt_qp *qp)

    stop all timers \ ``qp``\  - the QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`hfi1_stop_rc_timers.description`:

Description
-----------

stop any pending timers

.. _`hfi1_stop_rnr_timer`:

hfi1_stop_rnr_timer
===================

.. c:function:: int hfi1_stop_rnr_timer(struct rvt_qp *qp)

    stop an rnr timer \ ``qp``\  - the QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`hfi1_stop_rnr_timer.description`:

Description
-----------

stop an rnr timer and return if the timer
had been pending.

.. _`hfi1_del_timers_sync`:

hfi1_del_timers_sync
====================

.. c:function:: void hfi1_del_timers_sync(struct rvt_qp *qp)

    wait for any timeout routines to exit \ ``qp``\  - the QP

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`make_rc_ack`:

make_rc_ack
===========

.. c:function:: int make_rc_ack(struct hfi1_ibdev *dev, struct rvt_qp *qp, struct hfi1_other_headers *ohdr, struct hfi1_pkt_state *ps)

    construct a response packet (ACK, NAK, or RDMA read)

    :param struct hfi1_ibdev \*dev:
        the device for this QP

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param struct hfi1_other_headers \*ohdr:
        a pointer to the IB header being constructed

    :param struct hfi1_pkt_state \*ps:
        the xmit packet state

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

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param struct hfi1_pkt_state \*ps:
        *undescribed*

.. _`hfi1_make_rc_req.description`:

Description
-----------

Assumes s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`hfi1_send_rc_ack`:

hfi1_send_rc_ack
================

.. c:function:: void hfi1_send_rc_ack(struct hfi1_ctxtdata *rcd, struct rvt_qp *qp, int is_fecn)

    Construct an ACK packet and send it

    :param struct hfi1_ctxtdata \*rcd:
        *undescribed*

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param int is_fecn:
        *undescribed*

.. _`hfi1_send_rc_ack.description`:

Description
-----------

This is called from \ :c:func:`hfi1_rc_rcv`\  and \ :c:func:`handle_receive_interrupt`\ .
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

This is called from \ :c:func:`hfi1_rc_rcv`\  to process an incoming RC ACK
for the given QP.
Called at interrupt level with the QP s_lock held.

.. _`do_rc_ack`:

do_rc_ack
=========

.. c:function:: int do_rc_ack(struct rvt_qp *qp, u32 aeth, u32 psn, int opcode, u64 val, struct hfi1_ctxtdata *rcd)

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

    :param struct hfi1_ctxtdata \*rcd:
        *undescribed*

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

.. c:function:: void rc_rcv_resp(struct hfi1_ibport *ibp, struct hfi1_other_headers *ohdr, void *data, u32 tlen, struct rvt_qp *qp, u32 opcode, u32 psn, u32 hdrsize, u32 pmtu, struct hfi1_ctxtdata *rcd)

    process an incoming RC response packet

    :param struct hfi1_ibport \*ibp:
        the port this packet came in on

    :param struct hfi1_other_headers \*ohdr:
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

    :param struct hfi1_ctxtdata \*rcd:
        *undescribed*

.. _`rc_rcv_resp.description`:

Description
-----------

This is called from \ :c:func:`hfi1_rc_rcv`\  to process an incoming RC response
packet for the given QP.
Called at interrupt level.

.. _`rc_rcv_error`:

rc_rcv_error
============

.. c:function:: int rc_rcv_error(struct hfi1_other_headers *ohdr, void *data, struct rvt_qp *qp, u32 opcode, u32 psn, int diff, struct hfi1_ctxtdata *rcd)

    process an incoming duplicate or error RC packet

    :param struct hfi1_other_headers \*ohdr:
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

    :param struct hfi1_ctxtdata \*rcd:
        *undescribed*

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

    :param struct hfi1_packet \*packet:
        *undescribed*

.. _`hfi1_rc_rcv.description`:

Description
-----------

This is called from \ :c:func:`qp_rcv`\  to process an incoming RC packet
for the given QP.
May be called at interrupt level.

.. This file was automatic generated / don't edit.

