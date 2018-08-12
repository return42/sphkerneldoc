.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/ruc.c

.. _`ruc_loopback`:

ruc_loopback
============

.. c:function:: void ruc_loopback(struct rvt_qp *sqp)

    handle UC and RC loopback requests

    :param struct rvt_qp \*sqp:
        the sending QP

.. _`ruc_loopback.description`:

Description
-----------

This is called from \ :c:func:`hfi1_do_send`\  to
forward a WQE addressed to the same HFI.
Note that although we are single threaded due to the send engine, we still
have to protect against \ :c:func:`post_send`\ .  We don't have to worry about
receive interrupts since this is a connected protocol and all packets
will pass through here.

.. _`hfi1_make_grh`:

hfi1_make_grh
=============

.. c:function:: u32 hfi1_make_grh(struct hfi1_ibport *ibp, struct ib_grh *hdr, const struct ib_global_route *grh, u32 hwords, u32 nwords)

    construct a GRH header

    :param struct hfi1_ibport \*ibp:
        a pointer to the IB port

    :param struct ib_grh \*hdr:
        a pointer to the GRH header being constructed

    :param const struct ib_global_route \*grh:
        the global route address to send to

    :param u32 hwords:
        size of header after grh being sent in dwords

    :param u32 nwords:
        the number of 32 bit words of data being sent

.. _`hfi1_make_grh.description`:

Description
-----------

Return the size of the header in 32 bit words.

.. _`build_ahg`:

build_ahg
=========

.. c:function:: void build_ahg(struct rvt_qp *qp, u32 npsn)

    create ahg in s_ahg

    :param struct rvt_qp \*qp:
        a pointer to QP

    :param u32 npsn:
        the next PSN for the request/response

.. _`build_ahg.description`:

Description
-----------

This routine handles the AHG by allocating an ahg entry and causing the
copy of the first middle.

Subsequent middles use the copied entry, editing the
PSN with 1 or 2 edits.

.. _`hfi1_make_ruc_header_16b`:

hfi1_make_ruc_header_16B
========================

.. c:function:: void hfi1_make_ruc_header_16B(struct rvt_qp *qp, struct ib_other_headers *ohdr, u32 bth0, u32 bth2, int middle, struct hfi1_pkt_state *ps)

    build a 16B header

    :param struct rvt_qp \*qp:
        the queue pair

    :param struct ib_other_headers \*ohdr:
        a pointer to the destination header memory

    :param u32 bth0:
        bth0 passed in from the RC/UC builder

    :param u32 bth2:
        bth2 passed in from the RC/UC builder

    :param int middle:
        non zero implies indicates ahg "could" be used

    :param struct hfi1_pkt_state \*ps:
        the current packet state

.. _`hfi1_make_ruc_header_16b.this-routine-may-disarm-ahg-under-these-situations`:

This routine may disarm ahg under these situations
--------------------------------------------------

- packet needs a GRH
- BECN needed
- migration state not IB_MIG_MIGRATED

.. _`hfi1_make_ruc_header_9b`:

hfi1_make_ruc_header_9B
=======================

.. c:function:: void hfi1_make_ruc_header_9B(struct rvt_qp *qp, struct ib_other_headers *ohdr, u32 bth0, u32 bth2, int middle, struct hfi1_pkt_state *ps)

    build a 9B header

    :param struct rvt_qp \*qp:
        the queue pair

    :param struct ib_other_headers \*ohdr:
        a pointer to the destination header memory

    :param u32 bth0:
        bth0 passed in from the RC/UC builder

    :param u32 bth2:
        bth2 passed in from the RC/UC builder

    :param int middle:
        non zero implies indicates ahg "could" be used

    :param struct hfi1_pkt_state \*ps:
        the current packet state

.. _`hfi1_make_ruc_header_9b.this-routine-may-disarm-ahg-under-these-situations`:

This routine may disarm ahg under these situations
--------------------------------------------------

- packet needs a GRH
- BECN needed
- migration state not IB_MIG_MIGRATED

.. _`schedule_send_yield`:

schedule_send_yield
===================

.. c:function:: bool schedule_send_yield(struct rvt_qp *qp, struct hfi1_pkt_state *ps)

    test for a yield required for QP send engine

    :param struct rvt_qp \*qp:
        a pointer to QP

    :param struct hfi1_pkt_state \*ps:
        a pointer to a structure with commonly lookup values for
        the the send engine progress

.. _`schedule_send_yield.description`:

Description
-----------

This routine checks if the time slice for the QP has expired
for RC QPs, if so an additional work entry is queued. At this
point, other QPs have an opportunity to be scheduled. It
returns true if a yield is required, otherwise, false
is returned.

.. _`hfi1_do_send`:

hfi1_do_send
============

.. c:function:: void hfi1_do_send(struct rvt_qp *qp, bool in_thread)

    perform a send on a QP

    :param struct rvt_qp \*qp:
        *undescribed*

    :param bool in_thread:
        true if in a workqueue thread

.. _`hfi1_do_send.description`:

Description
-----------

Process entries in the send work queue until credit or queue is
exhausted.  Only allow one CPU to send a packet per QP.
Otherwise, two threads could send packets out of order.

.. This file was automatic generated / don't edit.

