.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_common.c

.. _`nfp_net_get_fw_version`:

nfp_net_get_fw_version
======================

.. c:function:: void nfp_net_get_fw_version(struct nfp_net_fw_version *fw_ver, void __iomem *ctrl_bar)

    Read and parse the FW version

    :param struct nfp_net_fw_version \*fw_ver:
        Output fw_version structure to read to

    :param void __iomem \*ctrl_bar:
        Mapped address of the control BAR

.. _`nfp_net_reconfig_post`:

nfp_net_reconfig_post
=====================

.. c:function:: void nfp_net_reconfig_post(struct nfp_net *nn, u32 update)

    Post async reconfig request

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

    :param u32 update:
        The value for the update field in the BAR config

.. _`nfp_net_reconfig_post.description`:

Description
-----------

Record FW reconfiguration request.  Reconfiguration will be kicked off
whenever reconfiguration machinery is idle.  Multiple requests can be
merged together!

.. _`nfp_net_reconfig`:

nfp_net_reconfig
================

.. c:function:: int nfp_net_reconfig(struct nfp_net *nn, u32 update)

    Reconfigure the firmware

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

    :param u32 update:
        The value for the update field in the BAR config

.. _`nfp_net_reconfig.description`:

Description
-----------

Write the update word to the BAR and ping the reconfig queue.  The
poll until the firmware has acknowledged the update by zeroing the
update word.

.. _`nfp_net_reconfig.return`:

Return
------

Negative errno on error, 0 on success

.. _`nfp_net_irq_unmask_msix`:

nfp_net_irq_unmask_msix
=======================

.. c:function:: void nfp_net_irq_unmask_msix(struct nfp_net *nn, unsigned int entry_nr)

    Unmask MSI-X after automasking

    :param struct nfp_net \*nn:
        NFP Network structure

    :param unsigned int entry_nr:
        MSI-X table entry

.. _`nfp_net_irq_unmask_msix.description`:

Description
-----------

Clear the MSI-X table mask bit for the given entry bypassing Linux irq
handling subsystem.  Use \*only\* to reenable automasked vectors.

.. _`nfp_net_irq_unmask`:

nfp_net_irq_unmask
==================

.. c:function:: void nfp_net_irq_unmask(struct nfp_net *nn, unsigned int entry_nr)

    Unmask automasked interrupt

    :param struct nfp_net \*nn:
        NFP Network structure

    :param unsigned int entry_nr:
        MSI-X table entry

.. _`nfp_net_irq_unmask.description`:

Description
-----------

If MSI-X auto-masking is enabled clear the mask bit, otherwise
clear the ICR for the entry.

.. _`nfp_net_msix_alloc`:

nfp_net_msix_alloc
==================

.. c:function:: int nfp_net_msix_alloc(struct nfp_net *nn, int nr_vecs)

    Try to allocate MSI-X irqs

    :param struct nfp_net \*nn:
        NFP Network structure

    :param int nr_vecs:
        Number of MSI-X vectors to allocate

.. _`nfp_net_msix_alloc.description`:

Description
-----------

For MSI-X we want at least NFP_NET_NON_Q_VECTORS + 1 vectors.

.. _`nfp_net_msix_alloc.return`:

Return
------

Number of MSI-X vectors obtained or 0 on error.

.. _`nfp_net_irqs_wanted`:

nfp_net_irqs_wanted
===================

.. c:function:: int nfp_net_irqs_wanted(struct nfp_net *nn)

    Work out how many interrupt vectors we want

    :param struct nfp_net \*nn:
        NFP Network structure

.. _`nfp_net_irqs_wanted.description`:

Description
-----------

We want a vector per CPU (or ring), whatever is smaller plus
NFP_NET_NON_Q_VECTORS for LSC etc.

.. _`nfp_net_irqs_wanted.return`:

Return
------

Number of interrupts wanted

.. _`nfp_net_irqs_alloc`:

nfp_net_irqs_alloc
==================

.. c:function:: int nfp_net_irqs_alloc(struct nfp_net *nn)

    allocates MSI-X irqs

    :param struct nfp_net \*nn:
        NFP Network structure

.. _`nfp_net_irqs_alloc.return`:

Return
------

Number of irqs obtained or 0 on error.

.. _`nfp_net_irqs_disable`:

nfp_net_irqs_disable
====================

.. c:function:: void nfp_net_irqs_disable(struct nfp_net *nn)

    Disable interrupts

    :param struct nfp_net \*nn:
        NFP Network structure

.. _`nfp_net_irqs_disable.description`:

Description
-----------

Undoes what \ ``nfp_net_irqs_alloc``\ () does.

.. _`nfp_net_irq_rxtx`:

nfp_net_irq_rxtx
================

.. c:function:: irqreturn_t nfp_net_irq_rxtx(int irq, void *data)

    Interrupt service routine for RX/TX rings.

    :param int irq:
        Interrupt

    :param void \*data:
        Opaque data structure

.. _`nfp_net_irq_rxtx.return`:

Return
------

Indicate if the interrupt has been handled.

.. _`nfp_net_read_link_status`:

nfp_net_read_link_status
========================

.. c:function:: void nfp_net_read_link_status(struct nfp_net *nn)

    Reread link status from control BAR

    :param struct nfp_net \*nn:
        NFP Network structure

.. _`nfp_net_irq_lsc`:

nfp_net_irq_lsc
===============

.. c:function:: irqreturn_t nfp_net_irq_lsc(int irq, void *data)

    Interrupt service routine for link state changes

    :param int irq:
        Interrupt

    :param void \*data:
        Opaque data structure

.. _`nfp_net_irq_lsc.return`:

Return
------

Indicate if the interrupt has been handled.

.. _`nfp_net_irq_exn`:

nfp_net_irq_exn
===============

.. c:function:: irqreturn_t nfp_net_irq_exn(int irq, void *data)

    Interrupt service routine for exceptions

    :param int irq:
        Interrupt

    :param void \*data:
        Opaque data structure

.. _`nfp_net_irq_exn.return`:

Return
------

Indicate if the interrupt has been handled.

.. _`nfp_net_tx_ring_init`:

nfp_net_tx_ring_init
====================

.. c:function:: void nfp_net_tx_ring_init(struct nfp_net_tx_ring *tx_ring, struct nfp_net_r_vector *r_vec, unsigned int idx)

    Fill in the boilerplate for a TX ring

    :param struct nfp_net_tx_ring \*tx_ring:
        TX ring structure

    :param struct nfp_net_r_vector \*r_vec:
        IRQ vector servicing this ring

    :param unsigned int idx:
        Ring index

.. _`nfp_net_rx_ring_init`:

nfp_net_rx_ring_init
====================

.. c:function:: void nfp_net_rx_ring_init(struct nfp_net_rx_ring *rx_ring, struct nfp_net_r_vector *r_vec, unsigned int idx)

    Fill in the boilerplate for a RX ring

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring structure

    :param struct nfp_net_r_vector \*r_vec:
        IRQ vector servicing this ring

    :param unsigned int idx:
        Ring index

.. _`nfp_net_irqs_assign`:

nfp_net_irqs_assign
===================

.. c:function:: void nfp_net_irqs_assign(struct net_device *netdev)

    Assign IRQs and setup rvecs.

    :param struct net_device \*netdev:
        netdev structure

.. _`nfp_net_aux_irq_request`:

nfp_net_aux_irq_request
=======================

.. c:function:: int nfp_net_aux_irq_request(struct nfp_net *nn, u32 ctrl_offset, const char *format, char *name, size_t name_sz, unsigned int vector_idx, irq_handler_t handler)

    Request an auxiliary interrupt (LSC or EXN)

    :param struct nfp_net \*nn:
        NFP Network structure

    :param u32 ctrl_offset:
        Control BAR offset where IRQ configuration should be written

    :param const char \*format:
        printf-style format to construct the interrupt name

    :param char \*name:
        Pointer to allocated space for interrupt name

    :param size_t name_sz:
        Size of space for interrupt name

    :param unsigned int vector_idx:
        Index of MSI-X vector used for this interrupt

    :param irq_handler_t handler:
        IRQ handler to register for this interrupt

.. _`nfp_net_aux_irq_free`:

nfp_net_aux_irq_free
====================

.. c:function:: void nfp_net_aux_irq_free(struct nfp_net *nn, u32 ctrl_offset, unsigned int vector_idx)

    Free an auxiliary interrupt (LSC or EXN)

    :param struct nfp_net \*nn:
        NFP Network structure

    :param u32 ctrl_offset:
        Control BAR offset where IRQ configuration should be written

    :param unsigned int vector_idx:
        Index of MSI-X vector used for this interrupt

.. _`nfp_net_tx_full`:

nfp_net_tx_full
===============

.. c:function:: int nfp_net_tx_full(struct nfp_net_tx_ring *tx_ring, int dcnt)

    Check if the TX ring is full

    :param struct nfp_net_tx_ring \*tx_ring:
        TX ring to check

    :param int dcnt:
        Number of descriptors that need to be enqueued (must be >= 1)

.. _`nfp_net_tx_full.description`:

Description
-----------

This function checks, based on the \*host copy\* of read/write
pointer if a given TX ring is full.  The real TX queue may have
some newly made available slots.

.. _`nfp_net_tx_full.return`:

Return
------

True if the ring is full.

.. _`nfp_net_tx_ring_stop`:

nfp_net_tx_ring_stop
====================

.. c:function:: void nfp_net_tx_ring_stop(struct netdev_queue *nd_q, struct nfp_net_tx_ring *tx_ring)

    stop tx ring

    :param struct netdev_queue \*nd_q:
        netdev queue

    :param struct nfp_net_tx_ring \*tx_ring:
        driver tx queue structure

.. _`nfp_net_tx_ring_stop.description`:

Description
-----------

Safely stop TX ring.  Remember that while we are running .start_xmit()
someone else may be cleaning the TX ring completions so we need to be
extra careful here.

.. _`nfp_net_tx_tso`:

nfp_net_tx_tso
==============

.. c:function:: void nfp_net_tx_tso(struct nfp_net *nn, struct nfp_net_r_vector *r_vec, struct nfp_net_tx_buf *txbuf, struct nfp_net_tx_desc *txd, struct sk_buff *skb)

    Set up Tx descriptor for LSO

    :param struct nfp_net \*nn:
        NFP Net device

    :param struct nfp_net_r_vector \*r_vec:
        per-ring structure

    :param struct nfp_net_tx_buf \*txbuf:
        Pointer to driver soft TX descriptor

    :param struct nfp_net_tx_desc \*txd:
        Pointer to HW TX descriptor

    :param struct sk_buff \*skb:
        Pointer to SKB

.. _`nfp_net_tx_tso.description`:

Description
-----------

Set up Tx descriptor for LSO, do nothing for non-LSO skbs.
Return error on packet header greater than maximum supported LSO header size.

.. _`nfp_net_tx_csum`:

nfp_net_tx_csum
===============

.. c:function:: void nfp_net_tx_csum(struct nfp_net *nn, struct nfp_net_r_vector *r_vec, struct nfp_net_tx_buf *txbuf, struct nfp_net_tx_desc *txd, struct sk_buff *skb)

    Set TX CSUM offload flags in TX descriptor

    :param struct nfp_net \*nn:
        NFP Net device

    :param struct nfp_net_r_vector \*r_vec:
        per-ring structure

    :param struct nfp_net_tx_buf \*txbuf:
        Pointer to driver soft TX descriptor

    :param struct nfp_net_tx_desc \*txd:
        Pointer to TX descriptor

    :param struct sk_buff \*skb:
        Pointer to SKB

.. _`nfp_net_tx_csum.description`:

Description
-----------

This function sets the TX checksum flags in the TX descriptor based
on the configuration and the protocol of the packet to be transmitted.

.. _`nfp_net_tx`:

nfp_net_tx
==========

.. c:function:: int nfp_net_tx(struct sk_buff *skb, struct net_device *netdev)

    Main transmit entry point

    :param struct sk_buff \*skb:
        SKB to transmit

    :param struct net_device \*netdev:
        netdev structure

.. _`nfp_net_tx.return`:

Return
------

NETDEV_TX_OK on success.

.. _`nfp_net_tx_complete`:

nfp_net_tx_complete
===================

.. c:function:: void nfp_net_tx_complete(struct nfp_net_tx_ring *tx_ring)

    Handled completed TX packets

    :param struct nfp_net_tx_ring \*tx_ring:
        TX ring structure

.. _`nfp_net_tx_complete.return`:

Return
------

Number of completed TX descriptors

.. _`nfp_net_tx_ring_reset`:

nfp_net_tx_ring_reset
=====================

.. c:function:: void nfp_net_tx_ring_reset(struct nfp_net *nn, struct nfp_net_tx_ring *tx_ring)

    Free any untransmitted buffers and reset pointers

    :param struct nfp_net \*nn:
        NFP Net device

    :param struct nfp_net_tx_ring \*tx_ring:
        TX ring structure

.. _`nfp_net_tx_ring_reset.description`:

Description
-----------

Assumes that the device is stopped

.. _`nfp_net_rx_space`:

nfp_net_rx_space
================

.. c:function:: int nfp_net_rx_space(struct nfp_net_rx_ring *rx_ring)

    return the number of free slots on the RX ring

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring structure

.. _`nfp_net_rx_space.description`:

Description
-----------

Make sure we leave at least one slot free.

.. _`nfp_net_rx_space.return`:

Return
------

True if there is space on the RX ring

.. _`nfp_net_rx_alloc_one`:

nfp_net_rx_alloc_one
====================

.. c:function:: struct sk_buff *nfp_net_rx_alloc_one(struct nfp_net_rx_ring *rx_ring, dma_addr_t *dma_addr, unsigned int fl_bufsz)

    Allocate and map skb for RX

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring structure of the skb

    :param dma_addr_t \*dma_addr:
        Pointer to storage for DMA address (output param)

    :param unsigned int fl_bufsz:
        size of freelist buffers

.. _`nfp_net_rx_alloc_one.description`:

Description
-----------

This function will allcate a new skb, map it for DMA.

.. _`nfp_net_rx_alloc_one.return`:

Return
------

allocated skb or NULL on failure.

.. _`nfp_net_rx_give_one`:

nfp_net_rx_give_one
===================

.. c:function:: void nfp_net_rx_give_one(struct nfp_net_rx_ring *rx_ring, struct sk_buff *skb, dma_addr_t dma_addr)

    Put mapped skb on the software and hardware rings

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring structure

    :param struct sk_buff \*skb:
        Skb to put on rings

    :param dma_addr_t dma_addr:
        DMA address of skb mapping

.. _`nfp_net_rx_ring_reset`:

nfp_net_rx_ring_reset
=====================

.. c:function:: void nfp_net_rx_ring_reset(struct nfp_net_rx_ring *rx_ring)

    Reflect in SW state of freelist after disable

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring structure

.. _`nfp_net_rx_ring_reset.warning`:

Warning
-------

Do \*not\* call if ring buffers were never put on the FW freelist
(i.e. device was not enabled)!

.. _`nfp_net_rx_ring_bufs_free`:

nfp_net_rx_ring_bufs_free
=========================

.. c:function:: void nfp_net_rx_ring_bufs_free(struct nfp_net *nn, struct nfp_net_rx_ring *rx_ring)

    Free any buffers currently on the RX ring

    :param struct nfp_net \*nn:
        NFP Net device

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring to remove buffers from

.. _`nfp_net_rx_ring_bufs_free.description`:

Description
-----------

Assumes that the device is stopped and buffers are in [0, ring->cnt - 1)
entries.  After device is disabled \ :c:func:`nfp_net_rx_ring_reset`\  must be called
to restore required ring geometry.

.. _`nfp_net_rx_ring_bufs_alloc`:

nfp_net_rx_ring_bufs_alloc
==========================

.. c:function:: int nfp_net_rx_ring_bufs_alloc(struct nfp_net *nn, struct nfp_net_rx_ring *rx_ring)

    Fill RX ring with buffers (don't give to FW)

    :param struct nfp_net \*nn:
        NFP Net device

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring to remove buffers from

.. _`nfp_net_rx_ring_fill_freelist`:

nfp_net_rx_ring_fill_freelist
=============================

.. c:function:: void nfp_net_rx_ring_fill_freelist(struct nfp_net_rx_ring *rx_ring)

    Give buffers from the ring to FW

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring to fill

.. _`nfp_net_rx_csum_has_errors`:

nfp_net_rx_csum_has_errors
==========================

.. c:function:: int nfp_net_rx_csum_has_errors(u16 flags)

    group check if rxd has any csum errors

    :param u16 flags:
        RX descriptor flags field in CPU byte order

.. _`nfp_net_rx_csum`:

nfp_net_rx_csum
===============

.. c:function:: void nfp_net_rx_csum(struct nfp_net *nn, struct nfp_net_r_vector *r_vec, struct nfp_net_rx_desc *rxd, struct sk_buff *skb)

    set SKB checksum field based on RX descriptor flags

    :param struct nfp_net \*nn:
        NFP Net device

    :param struct nfp_net_r_vector \*r_vec:
        per-ring structure

    :param struct nfp_net_rx_desc \*rxd:
        Pointer to RX descriptor

    :param struct sk_buff \*skb:
        Pointer to SKB

.. _`nfp_net_rx`:

nfp_net_rx
==========

.. c:function:: int nfp_net_rx(struct nfp_net_rx_ring *rx_ring, int budget)

    receive up to \ ``budget``\  packets on \ ``rx_ring``\ 

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring to receive from

    :param int budget:
        NAPI budget

.. _`nfp_net_rx.description`:

Description
-----------

Note, this function is separated out from the napi poll function to
more cleanly separate packet receive code from other bookkeeping
functions performed in the napi poll function.

There are differences between the NFP-3200 firmware and the
NFP-6000 firmware.  The NFP-3200 firmware uses a dedicated RX queue
to indicate that new packets have arrived.  The NFP-6000 does not
have this queue and uses the DD bit in the RX descriptor. This
method cannot be used on the NFP-3200 as it causes a race

.. _`nfp_net_rx.condition`:

condition
---------

The RX ring write pointer on the NFP-3200 is updated
after packets (and descriptors) have been DMAed.  If the DD bit is
used and subsequently the read pointer is updated this may lead to
the RX queue to underflow (if the firmware has not yet update the
write pointer).  Therefore we use slightly ugly conditional code
below to handle the differences.  We may, in the future update the
NFP-3200 firmware to behave the same as the firmware on the
NFP-6000.

.. _`nfp_net_rx.return`:

Return
------

Number of packets received.

.. _`nfp_net_poll`:

nfp_net_poll
============

.. c:function:: int nfp_net_poll(struct napi_struct *napi, int budget)

    napi poll function

    :param struct napi_struct \*napi:
        NAPI structure

    :param int budget:
        NAPI budget

.. _`nfp_net_poll.return`:

Return
------

number of packets polled.

.. _`nfp_net_tx_ring_free`:

nfp_net_tx_ring_free
====================

.. c:function:: void nfp_net_tx_ring_free(struct nfp_net_tx_ring *tx_ring)

    Free resources allocated to a TX ring

    :param struct nfp_net_tx_ring \*tx_ring:
        TX ring to free

.. _`nfp_net_tx_ring_alloc`:

nfp_net_tx_ring_alloc
=====================

.. c:function:: int nfp_net_tx_ring_alloc(struct nfp_net_tx_ring *tx_ring, u32 cnt)

    Allocate resource for a TX ring

    :param struct nfp_net_tx_ring \*tx_ring:
        TX Ring structure to allocate

    :param u32 cnt:
        Ring buffer count

.. _`nfp_net_tx_ring_alloc.return`:

Return
------

0 on success, negative errno otherwise.

.. _`nfp_net_rx_ring_free`:

nfp_net_rx_ring_free
====================

.. c:function:: void nfp_net_rx_ring_free(struct nfp_net_rx_ring *rx_ring)

    Free resources allocated to a RX ring

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring to free

.. _`nfp_net_rx_ring_alloc`:

nfp_net_rx_ring_alloc
=====================

.. c:function:: int nfp_net_rx_ring_alloc(struct nfp_net_rx_ring *rx_ring, unsigned int fl_bufsz, u32 cnt)

    Allocate resource for a RX ring

    :param struct nfp_net_rx_ring \*rx_ring:
        RX ring to allocate

    :param unsigned int fl_bufsz:
        Size of buffers to allocate

    :param u32 cnt:
        Ring buffer count

.. _`nfp_net_rx_ring_alloc.return`:

Return
------

0 on success, negative errno otherwise.

.. _`nfp_net_rss_write_itbl`:

nfp_net_rss_write_itbl
======================

.. c:function:: void nfp_net_rss_write_itbl(struct nfp_net *nn)

    Write RSS indirection table to device

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_rss_write_key`:

nfp_net_rss_write_key
=====================

.. c:function:: void nfp_net_rss_write_key(struct nfp_net *nn)

    Write RSS hash key to device

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_coalesce_write_cfg`:

nfp_net_coalesce_write_cfg
==========================

.. c:function:: void nfp_net_coalesce_write_cfg(struct nfp_net *nn)

    Write irq coalescence configuration to HW

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_write_mac_addr`:

nfp_net_write_mac_addr
======================

.. c:function:: void nfp_net_write_mac_addr(struct nfp_net *nn)

    Write mac address to the device control BAR

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_write_mac_addr.description`:

Description
-----------

Writes the MAC address from the netdev to the device control BAR.  Does not
perform the required reconfig.  We do a bit of byte swapping dance because
firmware is LE.

.. _`nfp_net_clear_config_and_disable`:

nfp_net_clear_config_and_disable
================================

.. c:function:: void nfp_net_clear_config_and_disable(struct nfp_net *nn)

    Clear control BAR and disable NFP

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_set_config_and_enable`:

nfp_net_set_config_and_enable
=============================

.. c:function:: int nfp_net_set_config_and_enable(struct nfp_net *nn)

    Write control BAR and enable NFP

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_open_stack`:

nfp_net_open_stack
==================

.. c:function:: void nfp_net_open_stack(struct nfp_net *nn)

    Start the device from stack's perspective

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_close_stack`:

nfp_net_close_stack
===================

.. c:function:: void nfp_net_close_stack(struct nfp_net *nn)

    Quiescent the stack (part of close)

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_close_free_all`:

nfp_net_close_free_all
======================

.. c:function:: void nfp_net_close_free_all(struct nfp_net *nn)

    Free all runtime resources

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_netdev_close`:

nfp_net_netdev_close
====================

.. c:function:: int nfp_net_netdev_close(struct net_device *netdev)

    Called when the device is downed

    :param struct net_device \*netdev:
        netdev structure

.. _`nfp_net_set_vxlan_port`:

nfp_net_set_vxlan_port
======================

.. c:function:: void nfp_net_set_vxlan_port(struct nfp_net *nn, int idx, __be16 port)

    set vxlan port in SW and reconfigure HW

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

    :param int idx:
        Index into the port table where new port should be written

    :param __be16 port:
        UDP port to configure (pass zero to remove VXLAN port)

.. _`nfp_net_find_vxlan_idx`:

nfp_net_find_vxlan_idx
======================

.. c:function:: int nfp_net_find_vxlan_idx(struct nfp_net *nn, __be16 port)

    find table entry of the port or a free one

    :param struct nfp_net \*nn:
        NFP Network structure

    :param __be16 port:
        UDP port to look for

.. _`nfp_net_find_vxlan_idx.return`:

Return
------

if the port is already in the table -- it's position;
if the port is not in the table -- free position to use;
if the table is full -- -ENOSPC.

.. _`nfp_net_info`:

nfp_net_info
============

.. c:function:: void nfp_net_info(struct nfp_net *nn)

    Print general info about the NIC

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_netdev_alloc`:

nfp_net_netdev_alloc
====================

.. c:function:: struct nfp_net *nfp_net_netdev_alloc(struct pci_dev *pdev, int max_tx_rings, int max_rx_rings)

    Allocate netdev and related structure

    :param struct pci_dev \*pdev:
        PCI device

    :param int max_tx_rings:
        Maximum number of TX rings supported by device

    :param int max_rx_rings:
        Maximum number of RX rings supported by device

.. _`nfp_net_netdev_alloc.description`:

Description
-----------

This function allocates a netdev device and fills in the initial
part of the \ ``struct``\  nfp_net structure.

.. _`nfp_net_netdev_alloc.return`:

Return
------

NFP Net device structure, or ERR_PTR on error.

.. _`nfp_net_netdev_free`:

nfp_net_netdev_free
===================

.. c:function:: void nfp_net_netdev_free(struct nfp_net *nn)

    Undo what \ ``nfp_net_netdev_alloc``\ () did

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_rss_init`:

nfp_net_rss_init
================

.. c:function:: void nfp_net_rss_init(struct nfp_net *nn)

    Set the initial RSS parameters

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_irqmod_init`:

nfp_net_irqmod_init
===================

.. c:function:: void nfp_net_irqmod_init(struct nfp_net *nn)

    Set the initial IRQ moderation parameters

    :param struct nfp_net \*nn:
        NFP Net device to reconfigure

.. _`nfp_net_netdev_init`:

nfp_net_netdev_init
===================

.. c:function:: int nfp_net_netdev_init(struct net_device *netdev)

    Initialise/finalise the netdev structure

    :param struct net_device \*netdev:
        netdev structure

.. _`nfp_net_netdev_init.return`:

Return
------

0 on success or negative errno on error.

.. _`nfp_net_netdev_clean`:

nfp_net_netdev_clean
====================

.. c:function:: void nfp_net_netdev_clean(struct net_device *netdev)

    Undo what \ :c:func:`nfp_net_netdev_init`\  did.

    :param struct net_device \*netdev:
        netdev structure

.. This file was automatic generated / don't edit.

