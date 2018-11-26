.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/verbs.c

.. _`hfi1_ib_rcv`:

hfi1_ib_rcv
===========

.. c:function:: void hfi1_ib_rcv(struct hfi1_packet *packet)

    process an incoming packet

    :param packet:
        data packet information
    :type packet: struct hfi1_packet \*

.. _`hfi1_ib_rcv.description`:

Description
-----------

This is called to process an incoming packet at interrupt level.

.. _`update_tx_opstats`:

update_tx_opstats
=================

.. c:function:: void update_tx_opstats(struct rvt_qp *qp, struct hfi1_pkt_state *ps, u32 plen)

    record stats by opcode \ ``qp``\ ; the qp

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param ps:
        transmit packet state
    :type ps: struct hfi1_pkt_state \*

    :param plen:
        the plen in dwords
    :type plen: u32

.. _`update_tx_opstats.description`:

Description
-----------

This is a routine to record the tx opstats after a
packet has been presented to the egress mechanism.

.. _`egress_pkey_check`:

egress_pkey_check
=================

.. c:function:: int egress_pkey_check(struct hfi1_pportdata *ppd, u32 slid, u16 pkey, u8 sc5, int8_t s_pkey_index)

    check P_KEY of a packet

    :param ppd:
        Physical IB port data
    :type ppd: struct hfi1_pportdata \*

    :param slid:
        SLID for packet
    :type slid: u32

    :param pkey:
        *undescribed*
    :type pkey: u16

    :param sc5:
        SC for packet
    :type sc5: u8

    :param s_pkey_index:
        It will be used for look up optimization for kernel contexts
        only. If it is negative value, then it means user contexts is calling this
        function.
    :type s_pkey_index: int8_t

.. _`egress_pkey_check.description`:

Description
-----------

It checks if hdr's pkey is valid.

.. _`egress_pkey_check.return`:

Return
------

0 on success, otherwise, 1

.. _`get_send_routine`:

get_send_routine
================

.. c:function:: send_routine get_send_routine(struct rvt_qp *qp, struct hfi1_pkt_state *ps)

    choose an egress routine

    :param qp:
        *undescribed*
    :type qp: struct rvt_qp \*

    :param ps:
        *undescribed*
    :type ps: struct hfi1_pkt_state \*

.. _`get_send_routine.description`:

Description
-----------

Choose an egress routine based on QP type
and size

.. _`hfi1_verbs_send`:

hfi1_verbs_send
===============

.. c:function:: int hfi1_verbs_send(struct rvt_qp *qp, struct hfi1_pkt_state *ps)

    send a packet

    :param qp:
        the QP to send on
    :type qp: struct rvt_qp \*

    :param ps:
        the state of the packet to send
    :type ps: struct hfi1_pkt_state \*

.. _`hfi1_verbs_send.description`:

Description
-----------

Return zero if packet is sent or queued OK.
Return non-zero and clear qp->s_flags RVT_S_BUSY otherwise.

.. _`hfi1_fill_device_attr`:

hfi1_fill_device_attr
=====================

.. c:function:: void hfi1_fill_device_attr(struct hfi1_devdata *dd)

    Fill in rvt dev info device attributes.

    :param dd:
        the device data structure
    :type dd: struct hfi1_devdata \*

.. _`hfi1_get_npkeys`:

hfi1_get_npkeys
===============

.. c:function:: unsigned hfi1_get_npkeys(struct hfi1_devdata *dd)

    return the size of the PKEY table for context 0

    :param dd:
        the hfi1_ib device
    :type dd: struct hfi1_devdata \*

.. _`hfi1_register_ib_device`:

hfi1_register_ib_device
=======================

.. c:function:: int hfi1_register_ib_device(struct hfi1_devdata *dd)

    register our device with the infiniband core

    :param dd:
        the device data structure
        Return 0 if successful, errno if unsuccessful.
    :type dd: struct hfi1_devdata \*

.. This file was automatic generated / don't edit.

