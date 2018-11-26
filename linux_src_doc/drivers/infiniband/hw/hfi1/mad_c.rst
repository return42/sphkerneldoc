.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/mad.c

.. _`get_pkeys`:

get_pkeys
=========

.. c:function:: int get_pkeys(struct hfi1_devdata *dd, u8 port, u16 *pkeys)

    return the PKEY table

    :param dd:
        the hfi1_ib device
    :type dd: struct hfi1_devdata \*

    :param port:
        the IB port number
    :type port: u8

    :param pkeys:
        the pkey table is placed here
    :type pkeys: u16 \*

.. _`__subn_set_opa_portinfo`:

\__subn_set_opa_portinfo
========================

.. c:function:: int __subn_set_opa_portinfo(struct opa_smp *smp, u32 am, u8 *data, struct ib_device *ibdev, u8 port, u32 *resp_len, u32 max_len, int local_mad)

    set port information

    :param smp:
        the incoming SM packet
    :type smp: struct opa_smp \*

    :param am:
        *undescribed*
    :type am: u32

    :param data:
        *undescribed*
    :type data: u8 \*

    :param ibdev:
        the infiniband device
    :type ibdev: struct ib_device \*

    :param port:
        the port on the device
    :type port: u8

    :param resp_len:
        *undescribed*
    :type resp_len: u32 \*

    :param max_len:
        *undescribed*
    :type max_len: u32

    :param local_mad:
        *undescribed*
    :type local_mad: int

.. _`set_pkeys`:

set_pkeys
=========

.. c:function:: int set_pkeys(struct hfi1_devdata *dd, u8 port, u16 *pkeys)

    set the PKEY table for ctxt 0

    :param dd:
        the hfi1_ib device
    :type dd: struct hfi1_devdata \*

    :param port:
        the IB port number
    :type port: u8

    :param pkeys:
        the PKEY table
    :type pkeys: u16 \*

.. _`tx_link_width`:

tx_link_width
=============

.. c:function:: u16 tx_link_width(u16 link_width)

    convert link width bitmask to integer value representing actual link width.

    :param link_width:
        width of active link
    :type link_width: u16

.. _`tx_link_width.description`:

Description
-----------

The function convert and return the index of bit set
that indicate the current link width.

.. _`get_xmit_wait_counters`:

get_xmit_wait_counters
======================

.. c:function:: u64 get_xmit_wait_counters(struct hfi1_pportdata *ppd, u16 link_width, u16 link_speed, int vl)

    Convert HFI 's SendWaitCnt/SendWaitVlCnt counter in unit of TXE cycle times to flit times.

    :param ppd:
        info of physical Hfi port
    :type ppd: struct hfi1_pportdata \*

    :param link_width:
        width of active link
    :type link_width: u16

    :param link_speed:
        speed of active link
    :type link_speed: u16

    :param vl:
        represent VL0-VL7, VL15 for PortVLXmitWait counters request
        and if vl value is C_VL_COUNT, it represent SendWaitCnt
        counter request
    :type vl: int

.. _`get_xmit_wait_counters.description`:

Description
-----------

Convert SendWaitCnt/SendWaitVlCnt counter from TXE cycle times to
flit times. Call this function to samples these counters. This
function will calculate for previous state transition and update
current state at end of function using ppd->prev_link_width and
ppd->port_vl_xmit_wait_last to port_vl_xmit_wait_curr and link_width.

.. _`hfi1_pkey_validation_pma`:

hfi1_pkey_validation_pma
========================

.. c:function:: int hfi1_pkey_validation_pma(struct hfi1_ibport *ibp, const struct opa_mad *in_mad, const struct ib_wc *in_wc)

    It validates PKEYs for incoming PMA MAD packets.

    :param ibp:
        IB port data
    :type ibp: struct hfi1_ibport \*

    :param in_mad:
        MAD packet with header and data
    :type in_mad: const struct opa_mad \*

    :param in_wc:
        Work completion data such as source LID, port number, etc.
    :type in_wc: const struct ib_wc \*

.. _`hfi1_pkey_validation_pma.these-are-all-the-possible-logic-rules-for-validating-a-pkey`:

These are all the possible logic rules for validating a pkey
------------------------------------------------------------


a) If pkey neither FULL_MGMT_P_KEY nor LIM_MGMT_P_KEY,
and NOT self-originated packet:
Drop MAD packet as it should always be part of the
management partition unless it's a self-originated packet.

b) If pkey_index -> FULL_MGMT_P_KEY, and LIM_MGMT_P_KEY in pkey table:
The packet is coming from a management node and the receiving node
is also a management node, so it is safe for the packet to go through.

c) If pkey_index -> FULL_MGMT_P_KEY, and LIM_MGMT_P_KEY is NOT in pkey table:
Drop the packet as LIM_MGMT_P_KEY should always be in the pkey table.
It could be an FM misconfiguration.

d) If pkey_index -> LIM_MGMT_P_KEY and FULL_MGMT_P_KEY is NOT in pkey table:
It is safe for the packet to go through since a non-management node is
talking to another non-management node.

e) If pkey_index -> LIM_MGMT_P_KEY and FULL_MGMT_P_KEY in pkey table:
Drop the packet because a non-management node is talking to a
management node, and it could be an attack.

For the implementation, these rules can be simplied to only checking
for (a) and (e). There's no need to check for rule (b) as
the packet doesn't need to be dropped. Rule (c) is not possible in
the driver as LIM_MGMT_P_KEY is always in the pkey table.

.. _`hfi1_pkey_validation_pma.return`:

Return
------

0 - pkey is okay, -EINVAL it's a bad pkey

.. _`hfi1_process_mad`:

hfi1_process_mad
================

.. c:function:: int hfi1_process_mad(struct ib_device *ibdev, int mad_flags, u8 port, const struct ib_wc *in_wc, const struct ib_grh *in_grh, const struct ib_mad_hdr *in_mad, size_t in_mad_size, struct ib_mad_hdr *out_mad, size_t *out_mad_size, u16 *out_mad_pkey_index)

    process an incoming MAD packet

    :param ibdev:
        the infiniband device this packet came in on
    :type ibdev: struct ib_device \*

    :param mad_flags:
        MAD flags
    :type mad_flags: int

    :param port:
        the port number this packet came in on
    :type port: u8

    :param in_wc:
        the work completion entry for this packet
    :type in_wc: const struct ib_wc \*

    :param in_grh:
        the global route header for this packet
    :type in_grh: const struct ib_grh \*

    :param in_mad:
        the incoming MAD
    :type in_mad: const struct ib_mad_hdr \*

    :param in_mad_size:
        *undescribed*
    :type in_mad_size: size_t

    :param out_mad:
        any outgoing MAD reply
    :type out_mad: struct ib_mad_hdr \*

    :param out_mad_size:
        *undescribed*
    :type out_mad_size: size_t \*

    :param out_mad_pkey_index:
        *undescribed*
    :type out_mad_pkey_index: u16 \*

.. _`hfi1_process_mad.description`:

Description
-----------

Returns IB_MAD_RESULT_SUCCESS if this is a MAD that we are not
interested in processing.

Note that the verbs framework has already done the MAD sanity checks,
and hop count/pointer updating for IB_MGMT_CLASS_SUBN_DIRECTED_ROUTE
MADs.

This is called by the ib_mad module.

.. This file was automatic generated / don't edit.

