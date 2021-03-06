.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/ruc.c

.. _`hfi1_make_grh`:

hfi1_make_grh
=============

.. c:function:: u32 hfi1_make_grh(struct hfi1_ibport *ibp, struct ib_grh *hdr, const struct ib_global_route *grh, u32 hwords, u32 nwords)

    construct a GRH header

    :param ibp:
        a pointer to the IB port
    :type ibp: struct hfi1_ibport \*

    :param hdr:
        a pointer to the GRH header being constructed
    :type hdr: struct ib_grh \*

    :param grh:
        the global route address to send to
    :type grh: const struct ib_global_route \*

    :param hwords:
        size of header after grh being sent in dwords
    :type hwords: u32

    :param nwords:
        the number of 32 bit words of data being sent
    :type nwords: u32

.. _`hfi1_make_grh.description`:

Description
-----------

Return the size of the header in 32 bit words.

.. _`build_ahg`:

build_ahg
=========

.. c:function:: void build_ahg(struct rvt_qp *qp, u32 npsn)

    create ahg in s_ahg

    :param qp:
        a pointer to QP
    :type qp: struct rvt_qp \*

    :param npsn:
        the next PSN for the request/response
    :type npsn: u32

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

    :param qp:
        the queue pair
    :type qp: struct rvt_qp \*

    :param ohdr:
        a pointer to the destination header memory
    :type ohdr: struct ib_other_headers \*

    :param bth0:
        bth0 passed in from the RC/UC builder
    :type bth0: u32

    :param bth2:
        bth2 passed in from the RC/UC builder
    :type bth2: u32

    :param middle:
        non zero implies indicates ahg "could" be used
    :type middle: int

    :param ps:
        the current packet state
    :type ps: struct hfi1_pkt_state \*

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

    :param qp:
        the queue pair
    :type qp: struct rvt_qp \*

    :param ohdr:
        a pointer to the destination header memory
    :type ohdr: struct ib_other_headers \*

    :param bth0:
        bth0 passed in from the RC/UC builder
    :type bth0: u32

    :param bth2:
        bth2 passed in from the RC/UC builder
    :type bth2: u32

    :param middle:
        non zero implies indicates ahg "could" be used
    :type middle: int

    :param ps:
        the current packet state
    :type ps: struct hfi1_pkt_state \*

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

    :param qp:
        a pointer to QP
    :type qp: struct rvt_qp \*

    :param ps:
        a pointer to a structure with commonly lookup values for
        the the send engine progress
    :type ps: struct hfi1_pkt_state \*

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

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param in_thread:
        true if in a workqueue thread
    :type in_thread: bool

.. _`hfi1_do_send.description`:

Description
-----------

Process entries in the send work queue until credit or queue is
exhausted.  Only allow one CPU to send a packet per QP.
Otherwise, two threads could send packets out of order.

.. This file was automatic generated / don't edit.

