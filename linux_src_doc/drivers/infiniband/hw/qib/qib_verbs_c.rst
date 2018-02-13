.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_verbs.c

.. _`qib_copy_sge`:

qib_copy_sge
============

.. c:function:: void qib_copy_sge(struct rvt_sge_state *ss, void *data, u32 length, int release)

    copy data to SGE memory

    :param struct rvt_sge_state \*ss:
        the SGE state

    :param void \*data:
        the data to copy

    :param u32 length:
        the length of the data

    :param int release:
        *undescribed*

.. _`qib_qp_rcv`:

qib_qp_rcv
==========

.. c:function:: void qib_qp_rcv(struct qib_ctxtdata *rcd, struct ib_header *hdr, int has_grh, void *data, u32 tlen, struct rvt_qp *qp)

    processing an incoming packet on a QP

    :param struct qib_ctxtdata \*rcd:
        the context pointer

    :param struct ib_header \*hdr:
        the packet header

    :param int has_grh:
        true if the packet has a GRH

    :param void \*data:
        the packet data

    :param u32 tlen:
        the packet length

    :param struct rvt_qp \*qp:
        the QP the packet came on

.. _`qib_qp_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_ib_rcv`\  to process an incoming packet
for the given QP.
Called at interrupt level.

.. _`qib_ib_rcv`:

qib_ib_rcv
==========

.. c:function:: void qib_ib_rcv(struct qib_ctxtdata *rcd, void *rhdr, void *data, u32 tlen)

    process an incoming packet

    :param struct qib_ctxtdata \*rcd:
        the context pointer

    :param void \*rhdr:
        the header of the packet

    :param void \*data:
        the packet payload

    :param u32 tlen:
        the packet length

.. _`qib_ib_rcv.description`:

Description
-----------

This is called from \ :c:func:`qib_kreceive`\  to process an incoming packet at
interrupt level. Tlen is the length of the header + data + CRC in bytes.

.. _`qib_verbs_send`:

qib_verbs_send
==============

.. c:function:: int qib_verbs_send(struct rvt_qp *qp, struct ib_header *hdr, u32 hdrwords, struct rvt_sge_state *ss, u32 len)

    send a packet

    :param struct rvt_qp \*qp:
        the QP to send on

    :param struct ib_header \*hdr:
        the packet header

    :param u32 hdrwords:
        the number of 32-bit words in the header

    :param struct rvt_sge_state \*ss:
        the SGE to send

    :param u32 len:
        the length of the packet in bytes

.. _`qib_verbs_send.description`:

Description
-----------

Return zero if packet is sent or queued OK.
Return non-zero and clear qp->s_flags RVT_S_BUSY otherwise.

.. _`qib_get_counters`:

qib_get_counters
================

.. c:function:: int qib_get_counters(struct qib_pportdata *ppd, struct qib_verbs_counters *cntrs)

    get various chip counters

    :param struct qib_pportdata \*ppd:
        *undescribed*

    :param struct qib_verbs_counters \*cntrs:
        counters are placed here

.. _`qib_get_counters.description`:

Description
-----------

Return the counters needed by \ :c:func:`recv_pma_get_portcounters`\ .

.. _`qib_ib_piobufavail`:

qib_ib_piobufavail
==================

.. c:function:: void qib_ib_piobufavail(struct qib_devdata *dd)

    callback when a PIO buffer is available

    :param struct qib_devdata \*dd:
        the device pointer

.. _`qib_ib_piobufavail.description`:

Description
-----------

This is called from \ :c:func:`qib_intr`\  at interrupt level when a PIO buffer is
available after \ :c:func:`qib_verbs_send`\  returned an error that no buffers were
available. Disable the interrupt if there are no more QPs waiting.

.. _`qib_get_npkeys`:

qib_get_npkeys
==============

.. c:function:: unsigned qib_get_npkeys(struct qib_devdata *dd)

    return the size of the PKEY table for context 0

    :param struct qib_devdata \*dd:
        the qlogic_ib device

.. _`qib_fill_device_attr`:

qib_fill_device_attr
====================

.. c:function:: void qib_fill_device_attr(struct qib_devdata *dd)

    Fill in rvt dev info device attributes.

    :param struct qib_devdata \*dd:
        the device data structure

.. _`qib_register_ib_device`:

qib_register_ib_device
======================

.. c:function:: int qib_register_ib_device(struct qib_devdata *dd)

    register our device with the infiniband core

    :param struct qib_devdata \*dd:
        the device data structure
        Return the allocated qib_ibdev pointer or NULL on error.

.. _`_qib_schedule_send`:

\_qib_schedule_send
===================

.. c:function:: void _qib_schedule_send(struct rvt_qp *qp)

    schedule progress \ ``qp``\  - the qp

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`_qib_schedule_send.description`:

Description
-----------

This schedules progress w/o regard to the s_flags.

It is only used in post send, which doesn't hold
the s_lock.

.. _`qib_schedule_send`:

qib_schedule_send
=================

.. c:function:: void qib_schedule_send(struct rvt_qp *qp)

    schedule progress \ ``qp``\  - the qp

    :param struct rvt_qp \*qp:
        *undescribed*

.. _`qib_schedule_send.description`:

Description
-----------

This schedules qp progress.  The s_lock
should be held.

.. This file was automatic generated / don't edit.

