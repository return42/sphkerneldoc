.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_cmn.c

.. _`bnx2x_move_fp`:

bnx2x_move_fp
=============

.. c:function:: void bnx2x_move_fp(struct bnx2x *bp, int from, int to)

    move content of the fastpath structure.

    :param struct bnx2x \*bp:
        driver handle

    :param int from:
        source FP index

    :param int to:
        destination FP index

.. _`bnx2x_move_fp.description`:

Description
-----------

Makes sure the contents of the bp->fp[to].napi is kept
intact. This is done by first copying the napi struct from
the target to the source, and then mem copying the entire
source onto the target. Update txdata pointers and related
content.

.. _`bnx2x_fill_fw_str`:

bnx2x_fill_fw_str
=================

.. c:function:: void bnx2x_fill_fw_str(struct bnx2x *bp, char *buf, size_t buf_len)

    Fill buffer with FW version string.

    :param struct bnx2x \*bp:
        driver handle

    :param char \*buf:
        character buffer to fill with the fw name

    :param size_t buf_len:
        length of the above buffer

.. _`bnx2x_shrink_eth_fp`:

bnx2x_shrink_eth_fp
===================

.. c:function:: void bnx2x_shrink_eth_fp(struct bnx2x *bp, int delta)

    guarantees fastpath structures stay intact

    :param struct bnx2x \*bp:
        driver handle

    :param int delta:
        number of eth queues which were not allocated

.. _`bnx2x_set_gro_params`:

bnx2x_set_gro_params
====================

.. c:function:: void bnx2x_set_gro_params(struct sk_buff *skb, u16 parsing_flags, u16 len_on_bd, unsigned int pkt_len, u16 num_of_coalesced_segs)

    compute GRO values

    :param struct sk_buff \*skb:
        packet skb

    :param u16 parsing_flags:
        parsing flags from the START CQE

    :param u16 len_on_bd:
        total length of the first packet for the
        aggregation.

    :param unsigned int pkt_len:
        length of all segments

    :param u16 num_of_coalesced_segs:
        *undescribed*

.. _`bnx2x_set_gro_params.description`:

Description
-----------

Approximate value of the MSS for this aggregation calculated using
the first packet of it.
Compute number of aggregated segments, and gso_type.

.. _`bnx2x_fill_report_data`:

bnx2x_fill_report_data
======================

.. c:function:: void bnx2x_fill_report_data(struct bnx2x *bp, struct bnx2x_link_report_data *data)

    fill link report data to report

    :param struct bnx2x \*bp:
        driver handle

    :param struct bnx2x_link_report_data \*data:
        link state to update

.. _`bnx2x_fill_report_data.description`:

Description
-----------

It uses a none-atomic bit operations because is called under the mutex.

.. _`bnx2x_link_report`:

bnx2x_link_report
=================

.. c:function:: void bnx2x_link_report(struct bnx2x *bp)

    report link status to OS.

    :param struct bnx2x \*bp:
        driver handle

.. _`bnx2x_link_report.description`:

Description
-----------

Calls the \\ :c:func:`__bnx2x_link_report`\  under the same locking scheme
as a link/PHY state managing code to ensure a consistent link
reporting.

.. _`__bnx2x_link_report`:

__bnx2x_link_report
===================

.. c:function:: void __bnx2x_link_report(struct bnx2x *bp)

    report link status to OS.

    :param struct bnx2x \*bp:
        driver handle

.. _`__bnx2x_link_report.description`:

Description
-----------

None atomic implementation.
Should be called under the phy_lock.

.. _`bnx2x_free_msix_irqs`:

bnx2x_free_msix_irqs
====================

.. c:function:: void bnx2x_free_msix_irqs(struct bnx2x *bp, int nvecs)

    free previously requested MSI-X IRQ vectors

    :param struct bnx2x \*bp:
        driver handle

    :param int nvecs:
        number of vectors to be released

.. _`bnx2x_set_real_num_queues`:

bnx2x_set_real_num_queues
=========================

.. c:function:: int bnx2x_set_real_num_queues(struct bnx2x *bp, int include_cnic)

    configure netdev->real_num_[tx,rx]_queues

    :param struct bnx2x \*bp:
        Driver handle

    :param int include_cnic:
        *undescribed*

.. _`bnx2x_set_real_num_queues.description`:

Description
-----------

We currently support for at most 16 Tx queues for each CoS thus we will
allocate a multiple of 16 for ETH L2 rings according to the value of the
bp->max_cos.

If there is an FCoE L2 queue the appropriate Tx queue will have the next
index after all ETH L2 indices.

If the actual number of Tx queues (for each CoS) is less than 16 then there
will be the holes at the end of each group of 16 ETh L2 indices (0..15,
16..31,...) with indices that are not coupled with any real Tx queue.

The proper configuration of skb->queue_mapping is handled by
\ :c:func:`bnx2x_select_queue`\  and \\ :c:func:`__skb_tx_hash`\ .

\ :c:func:`bnx2x_setup_tc`\  takes care of the proper TC mappings so that \\ :c:func:`__skb_tx_hash`\ 
will return a proper Tx index if TC is enabled (netdev->num_tc > 0).

.. _`bnx2x_bz_fp`:

bnx2x_bz_fp
===========

.. c:function:: void bnx2x_bz_fp(struct bnx2x *bp, int index)

    zero content of the fastpath structure.

    :param struct bnx2x \*bp:
        driver handle

    :param int index:
        fastpath index to be zeroed

.. _`bnx2x_bz_fp.description`:

Description
-----------

Makes sure the contents of the bp->fp[index].napi is kept
intact.

.. _`bnx2x_set_pbd_gso`:

bnx2x_set_pbd_gso
=================

.. c:function:: void bnx2x_set_pbd_gso(struct sk_buff *skb, struct eth_tx_parse_bd_e1x *pbd, u32 xmit_type)

    update PBD in GSO case.

    :param struct sk_buff \*skb:
        packet skb

    :param struct eth_tx_parse_bd_e1x \*pbd:
        parse BD

    :param u32 xmit_type:
        xmit flags

.. _`bnx2x_set_pbd_csum_enc`:

bnx2x_set_pbd_csum_enc
======================

.. c:function:: u8 bnx2x_set_pbd_csum_enc(struct bnx2x *bp, struct sk_buff *skb, u32 *parsing_data, u32 xmit_type)

    update PBD with checksum and return header length

    :param struct bnx2x \*bp:
        driver handle

    :param struct sk_buff \*skb:
        packet skb

    :param u32 \*parsing_data:
        data to be updated

    :param u32 xmit_type:
        xmit flags

.. _`bnx2x_set_pbd_csum_enc.description`:

Description
-----------

57712/578xx related, when skb has encapsulation

.. _`bnx2x_set_pbd_csum_e2`:

bnx2x_set_pbd_csum_e2
=====================

.. c:function:: u8 bnx2x_set_pbd_csum_e2(struct bnx2x *bp, struct sk_buff *skb, u32 *parsing_data, u32 xmit_type)

    update PBD with checksum and return header length

    :param struct bnx2x \*bp:
        driver handle

    :param struct sk_buff \*skb:
        packet skb

    :param u32 \*parsing_data:
        data to be updated

    :param u32 xmit_type:
        xmit flags

.. _`bnx2x_set_pbd_csum_e2.description`:

Description
-----------

57712/578xx related

.. _`bnx2x_set_pbd_csum`:

bnx2x_set_pbd_csum
==================

.. c:function:: u8 bnx2x_set_pbd_csum(struct bnx2x *bp, struct sk_buff *skb, struct eth_tx_parse_bd_e1x *pbd, u32 xmit_type)

    update PBD with checksum and return header length

    :param struct bnx2x \*bp:
        driver handle

    :param struct sk_buff \*skb:
        packet skb

    :param struct eth_tx_parse_bd_e1x \*pbd:
        parse BD to be updated

    :param u32 xmit_type:
        xmit flags

.. _`bnx2x_setup_tc`:

bnx2x_setup_tc
==============

.. c:function:: int bnx2x_setup_tc(struct net_device *dev, u8 num_tc)

    routine to configure net_device for multi tc

    :param struct net_device \*dev:
        *undescribed*

    :param u8 num_tc:
        *undescribed*

.. _`bnx2x_setup_tc.description`:

Description
-----------

callback connected to the ndo_setup_tc function pointer

.. This file was automatic generated / don't edit.

