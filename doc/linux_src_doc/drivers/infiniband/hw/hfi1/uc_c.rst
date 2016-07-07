.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/uc.c

.. _`hfi1_make_uc_req`:

hfi1_make_uc_req
================

.. c:function:: int hfi1_make_uc_req(struct rvt_qp *qp, struct hfi1_pkt_state *ps)

    construct a request packet (SEND, RDMA write)

    :param struct rvt_qp \*qp:
        a pointer to the QP

    :param struct hfi1_pkt_state \*ps:
        *undescribed*

.. _`hfi1_make_uc_req.description`:

Description
-----------

Assume s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`hfi1_uc_rcv`:

hfi1_uc_rcv
===========

.. c:function:: void hfi1_uc_rcv(struct hfi1_packet *packet)

    handle an incoming UC packet

    :param struct hfi1_packet \*packet:
        *undescribed*

.. _`hfi1_uc_rcv.description`:

Description
-----------

This is called from \ :c:func:`qp_rcv`\  to process an incoming UC packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

