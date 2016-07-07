.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/verbs.c

.. _`hfi1_copy_sge`:

hfi1_copy_sge
=============

.. c:function:: void hfi1_copy_sge(struct rvt_sge_state *ss, void *data, u32 length, int release, int copy_last)

    copy data to SGE memory

    :param struct rvt_sge_state \*ss:
        the SGE state

    :param void \*data:
        the data to copy

    :param u32 length:
        the length of the data

    :param int release:
        *undescribed*

    :param int copy_last:
        do a separate copy of the last 8 bytes

.. _`hfi1_skip_sge`:

hfi1_skip_sge
=============

.. c:function:: void hfi1_skip_sge(struct rvt_sge_state *ss, u32 length, int release)

    skip over SGE memory

    :param struct rvt_sge_state \*ss:
        the SGE state

    :param u32 length:
        the number of bytes to skip

    :param int release:
        *undescribed*

.. _`hfi1_ib_rcv`:

hfi1_ib_rcv
===========

.. c:function:: void hfi1_ib_rcv(struct hfi1_packet *packet)

    process an incoming packet

    :param struct hfi1_packet \*packet:
        data packet information

.. _`hfi1_ib_rcv.description`:

Description
-----------

This is called to process an incoming packet at interrupt level.

Tlen is the length of the header + data + CRC in bytes.

.. _`egress_pkey_check`:

egress_pkey_check
=================

.. c:function:: int egress_pkey_check(struct hfi1_pportdata *ppd, __be16 *lrh, __be32 *bth, u8 sc5, int8_t s_pkey_index)

    check P_KEY of a packet

    :param struct hfi1_pportdata \*ppd:
        Physical IB port data

    :param __be16 \*lrh:
        Local route header

    :param __be32 \*bth:
        Base transport header

    :param u8 sc5:
        SC for packet

    :param int8_t s_pkey_index:
        It will be used for look up optimization for kernel contexts
        only. If it is negative value, then it means user contexts is calling this
        function.

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

.. c:function:: send_routine get_send_routine(struct rvt_qp *qp, struct verbs_txreq *tx)

    choose an egress routine

    :param struct rvt_qp \*qp:
        *undescribed*

    :param struct verbs_txreq \*tx:
        *undescribed*

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

    :param struct rvt_qp \*qp:
        the QP to send on

    :param struct hfi1_pkt_state \*ps:
        the state of the packet to send

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

    :param struct hfi1_devdata \*dd:
        the device data structure

.. _`hfi1_get_npkeys`:

hfi1_get_npkeys
===============

.. c:function:: unsigned hfi1_get_npkeys(struct hfi1_devdata *dd)

    return the size of the PKEY table for context 0

    :param struct hfi1_devdata \*dd:
        the hfi1_ib device

.. _`hfi1_register_ib_device`:

hfi1_register_ib_device
=======================

.. c:function:: int hfi1_register_ib_device(struct hfi1_devdata *dd)

    register our device with the infiniband core

    :param struct hfi1_devdata \*dd:
        the device data structure
        Return 0 if successful, errno if unsuccessful.

.. This file was automatic generated / don't edit.

