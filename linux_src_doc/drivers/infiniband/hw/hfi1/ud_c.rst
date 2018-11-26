.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/ud.c

.. _`ud_loopback`:

ud_loopback
===========

.. c:function:: void ud_loopback(struct rvt_qp *sqp, struct rvt_swqe *swqe)

    handle send on loopback QPs

    :param sqp:
        the sending QP
    :type sqp: struct rvt_qp \*

    :param swqe:
        the send work request
    :type swqe: struct rvt_swqe \*

.. _`ud_loopback.description`:

Description
-----------

This is called from \ :c:func:`hfi1_make_ud_req`\  to forward a WQE addressed
to the same HFI.
Note that the receive interrupt handler may be calling \ :c:func:`hfi1_ud_rcv`\ 
while this is being called.

.. _`hfi1_make_ud_req`:

hfi1_make_ud_req
================

.. c:function:: int hfi1_make_ud_req(struct rvt_qp *qp, struct hfi1_pkt_state *ps)

    construct a UD request packet

    :param qp:
        the QP
    :type qp: struct rvt_qp \*

    :param ps:
        *undescribed*
    :type ps: struct hfi1_pkt_state \*

.. _`hfi1_make_ud_req.description`:

Description
-----------

Assume s_lock is held.

Return 1 if constructed; otherwise, return 0.

.. _`hfi1_ud_rcv`:

hfi1_ud_rcv
===========

.. c:function:: void hfi1_ud_rcv(struct hfi1_packet *packet)

    receive an incoming UD packet

    :param packet:
        *undescribed*
    :type packet: struct hfi1_packet \*

.. _`hfi1_ud_rcv.description`:

Description
-----------

This is called from \ :c:func:`qp_rcv`\  to process an incoming UD packet
for the given QP.
Called at interrupt level.

.. This file was automatic generated / don't edit.

