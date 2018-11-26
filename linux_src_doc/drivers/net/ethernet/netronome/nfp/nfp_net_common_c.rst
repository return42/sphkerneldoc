.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_common.c

.. _`nfp_net_get_fw_version`:

nfp_net_get_fw_version
======================

.. c:function:: void nfp_net_get_fw_version(struct nfp_net_fw_version *fw_ver, void __iomem *ctrl_bar)

    Read and parse the FW version

    :param fw_ver:
        Output fw_version structure to read to
    :type fw_ver: struct nfp_net_fw_version \*

    :param ctrl_bar:
        Mapped address of the control BAR
    :type ctrl_bar: void __iomem \*

.. _`nfp_net_reconfig_post`:

nfp_net_reconfig_post
=====================

.. c:function:: void nfp_net_reconfig_post(struct nfp_net *nn, u32 update)

    Post async reconfig request

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

    :param update:
        The value for the update field in the BAR config
    :type update: u32

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

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

    :param update:
        The value for the update field in the BAR config
    :type update: u32

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

.. _`nfp_net_reconfig_mbox`:

nfp_net_reconfig_mbox
=====================

.. c:function:: int nfp_net_reconfig_mbox(struct nfp_net *nn, u32 mbox_cmd)

    Reconfigure the firmware via the mailbox

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

    :param mbox_cmd:
        The value for the mailbox command
    :type mbox_cmd: u32

.. _`nfp_net_reconfig_mbox.description`:

Description
-----------

Helper function for mailbox updates

.. _`nfp_net_reconfig_mbox.return`:

Return
------

Negative errno on error, 0 on success

.. _`nfp_net_irq_unmask`:

nfp_net_irq_unmask
==================

.. c:function:: void nfp_net_irq_unmask(struct nfp_net *nn, unsigned int entry_nr)

    Unmask automasked interrupt

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

    :param entry_nr:
        MSI-X table entry
    :type entry_nr: unsigned int

.. _`nfp_net_irq_unmask.description`:

Description
-----------

Clear the ICR for the IRQ entry.

.. _`nfp_net_irqs_alloc`:

nfp_net_irqs_alloc
==================

.. c:function:: unsigned int nfp_net_irqs_alloc(struct pci_dev *pdev, struct msix_entry *irq_entries, unsigned int min_irqs, unsigned int wanted_irqs)

    allocates MSI-X irqs

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

    :param irq_entries:
        Array to be initialized and used to hold the irq entries
    :type irq_entries: struct msix_entry \*

    :param min_irqs:
        Minimal acceptable number of interrupts
    :type min_irqs: unsigned int

    :param wanted_irqs:
        Target number of interrupts to allocate
    :type wanted_irqs: unsigned int

.. _`nfp_net_irqs_alloc.return`:

Return
------

Number of irqs obtained or 0 on error.

.. _`nfp_net_irqs_assign`:

nfp_net_irqs_assign
===================

.. c:function:: void nfp_net_irqs_assign(struct nfp_net *nn, struct msix_entry *irq_entries, unsigned int n)

    Assign interrupts allocated externally to netdev

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

    :param irq_entries:
        Table of allocated interrupts
    :type irq_entries: struct msix_entry \*

    :param n:
        Size of \ ``irq_entries``\  (number of entries to grab)
    :type n: unsigned int

.. _`nfp_net_irqs_assign.description`:

Description
-----------

After interrupts are allocated with \ :c:func:`nfp_net_irqs_alloc`\  this function
should be called to assign them to a specific netdev (port).

.. _`nfp_net_irqs_disable`:

nfp_net_irqs_disable
====================

.. c:function:: void nfp_net_irqs_disable(struct pci_dev *pdev)

    Disable interrupts

    :param pdev:
        PCI device structure
    :type pdev: struct pci_dev \*

.. _`nfp_net_irqs_disable.description`:

Description
-----------

Undoes what \ ``nfp_net_irqs_alloc``\ () does.

.. _`nfp_net_irq_rxtx`:

nfp_net_irq_rxtx
================

.. c:function:: irqreturn_t nfp_net_irq_rxtx(int irq, void *data)

    Interrupt service routine for RX/TX rings.

    :param irq:
        Interrupt
    :type irq: int

    :param data:
        Opaque data structure
    :type data: void \*

.. _`nfp_net_irq_rxtx.return`:

Return
------

Indicate if the interrupt has been handled.

.. _`nfp_net_read_link_status`:

nfp_net_read_link_status
========================

.. c:function:: void nfp_net_read_link_status(struct nfp_net *nn)

    Reread link status from control BAR

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

.. _`nfp_net_irq_lsc`:

nfp_net_irq_lsc
===============

.. c:function:: irqreturn_t nfp_net_irq_lsc(int irq, void *data)

    Interrupt service routine for link state changes

    :param irq:
        Interrupt
    :type irq: int

    :param data:
        Opaque data structure
    :type data: void \*

.. _`nfp_net_irq_lsc.return`:

Return
------

Indicate if the interrupt has been handled.

.. _`nfp_net_irq_exn`:

nfp_net_irq_exn
===============

.. c:function:: irqreturn_t nfp_net_irq_exn(int irq, void *data)

    Interrupt service routine for exceptions

    :param irq:
        Interrupt
    :type irq: int

    :param data:
        Opaque data structure
    :type data: void \*

.. _`nfp_net_irq_exn.return`:

Return
------

Indicate if the interrupt has been handled.

.. _`nfp_net_tx_ring_init`:

nfp_net_tx_ring_init
====================

.. c:function:: void nfp_net_tx_ring_init(struct nfp_net_tx_ring *tx_ring, struct nfp_net_r_vector *r_vec, unsigned int idx, bool is_xdp)

    Fill in the boilerplate for a TX ring

    :param tx_ring:
        TX ring structure
    :type tx_ring: struct nfp_net_tx_ring \*

    :param r_vec:
        IRQ vector servicing this ring
    :type r_vec: struct nfp_net_r_vector \*

    :param idx:
        Ring index
    :type idx: unsigned int

    :param is_xdp:
        Is this an XDP TX ring?
    :type is_xdp: bool

.. _`nfp_net_rx_ring_init`:

nfp_net_rx_ring_init
====================

.. c:function:: void nfp_net_rx_ring_init(struct nfp_net_rx_ring *rx_ring, struct nfp_net_r_vector *r_vec, unsigned int idx)

    Fill in the boilerplate for a RX ring

    :param rx_ring:
        RX ring structure
    :type rx_ring: struct nfp_net_rx_ring \*

    :param r_vec:
        IRQ vector servicing this ring
    :type r_vec: struct nfp_net_r_vector \*

    :param idx:
        Ring index
    :type idx: unsigned int

.. _`nfp_net_aux_irq_request`:

nfp_net_aux_irq_request
=======================

.. c:function:: int nfp_net_aux_irq_request(struct nfp_net *nn, u32 ctrl_offset, const char *format, char *name, size_t name_sz, unsigned int vector_idx, irq_handler_t handler)

    Request an auxiliary interrupt (LSC or EXN)

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

    :param ctrl_offset:
        Control BAR offset where IRQ configuration should be written
    :type ctrl_offset: u32

    :param format:
        printf-style format to construct the interrupt name
    :type format: const char \*

    :param name:
        Pointer to allocated space for interrupt name
    :type name: char \*

    :param name_sz:
        Size of space for interrupt name
    :type name_sz: size_t

    :param vector_idx:
        Index of MSI-X vector used for this interrupt
    :type vector_idx: unsigned int

    :param handler:
        IRQ handler to register for this interrupt
    :type handler: irq_handler_t

.. _`nfp_net_aux_irq_free`:

nfp_net_aux_irq_free
====================

.. c:function:: void nfp_net_aux_irq_free(struct nfp_net *nn, u32 ctrl_offset, unsigned int vector_idx)

    Free an auxiliary interrupt (LSC or EXN)

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

    :param ctrl_offset:
        Control BAR offset where IRQ configuration should be written
    :type ctrl_offset: u32

    :param vector_idx:
        Index of MSI-X vector used for this interrupt
    :type vector_idx: unsigned int

.. _`nfp_net_tx_full`:

nfp_net_tx_full
===============

.. c:function:: int nfp_net_tx_full(struct nfp_net_tx_ring *tx_ring, int dcnt)

    Check if the TX ring is full

    :param tx_ring:
        TX ring to check
    :type tx_ring: struct nfp_net_tx_ring \*

    :param dcnt:
        Number of descriptors that need to be enqueued (must be >= 1)
    :type dcnt: int

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

    :param nd_q:
        netdev queue
    :type nd_q: struct netdev_queue \*

    :param tx_ring:
        driver tx queue structure
    :type tx_ring: struct nfp_net_tx_ring \*

.. _`nfp_net_tx_ring_stop.description`:

Description
-----------

Safely stop TX ring.  Remember that while we are running .start_xmit()
someone else may be cleaning the TX ring completions so we need to be
extra careful here.

.. _`nfp_net_tx_tso`:

nfp_net_tx_tso
==============

.. c:function:: void nfp_net_tx_tso(struct nfp_net_r_vector *r_vec, struct nfp_net_tx_buf *txbuf, struct nfp_net_tx_desc *txd, struct sk_buff *skb)

    Set up Tx descriptor for LSO

    :param r_vec:
        per-ring structure
    :type r_vec: struct nfp_net_r_vector \*

    :param txbuf:
        Pointer to driver soft TX descriptor
    :type txbuf: struct nfp_net_tx_buf \*

    :param txd:
        Pointer to HW TX descriptor
    :type txd: struct nfp_net_tx_desc \*

    :param skb:
        Pointer to SKB
    :type skb: struct sk_buff \*

.. _`nfp_net_tx_tso.description`:

Description
-----------

Set up Tx descriptor for LSO, do nothing for non-LSO skbs.
Return error on packet header greater than maximum supported LSO header size.

.. _`nfp_net_tx_csum`:

nfp_net_tx_csum
===============

.. c:function:: void nfp_net_tx_csum(struct nfp_net_dp *dp, struct nfp_net_r_vector *r_vec, struct nfp_net_tx_buf *txbuf, struct nfp_net_tx_desc *txd, struct sk_buff *skb)

    Set TX CSUM offload flags in TX descriptor

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param r_vec:
        per-ring structure
    :type r_vec: struct nfp_net_r_vector \*

    :param txbuf:
        Pointer to driver soft TX descriptor
    :type txbuf: struct nfp_net_tx_buf \*

    :param txd:
        Pointer to TX descriptor
    :type txd: struct nfp_net_tx_desc \*

    :param skb:
        Pointer to SKB
    :type skb: struct sk_buff \*

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

    :param skb:
        SKB to transmit
    :type skb: struct sk_buff \*

    :param netdev:
        netdev structure
    :type netdev: struct net_device \*

.. _`nfp_net_tx.return`:

Return
------

NETDEV_TX_OK on success.

.. _`nfp_net_tx_complete`:

nfp_net_tx_complete
===================

.. c:function:: void nfp_net_tx_complete(struct nfp_net_tx_ring *tx_ring, int budget)

    Handled completed TX packets

    :param tx_ring:
        TX ring structure
    :type tx_ring: struct nfp_net_tx_ring \*

    :param budget:
        NAPI budget (only used as bool to determine if in NAPI context)
    :type budget: int

.. _`nfp_net_tx_ring_reset`:

nfp_net_tx_ring_reset
=====================

.. c:function:: void nfp_net_tx_ring_reset(struct nfp_net_dp *dp, struct nfp_net_tx_ring *tx_ring)

    Free any untransmitted buffers and reset pointers

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param tx_ring:
        TX ring structure
    :type tx_ring: struct nfp_net_tx_ring \*

.. _`nfp_net_tx_ring_reset.description`:

Description
-----------

Assumes that the device is stopped, must be idempotent.

.. _`nfp_net_rx_alloc_one`:

nfp_net_rx_alloc_one
====================

.. c:function:: void *nfp_net_rx_alloc_one(struct nfp_net_dp *dp, dma_addr_t *dma_addr)

    Allocate and map page frag for RX

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param dma_addr:
        Pointer to storage for DMA address (output param)
    :type dma_addr: dma_addr_t \*

.. _`nfp_net_rx_alloc_one.description`:

Description
-----------

This function will allcate a new page frag, map it for DMA.

.. _`nfp_net_rx_alloc_one.return`:

Return
------

allocated page frag or NULL on failure.

.. _`nfp_net_rx_give_one`:

nfp_net_rx_give_one
===================

.. c:function:: void nfp_net_rx_give_one(const struct nfp_net_dp *dp, struct nfp_net_rx_ring *rx_ring, void *frag, dma_addr_t dma_addr)

    Put mapped skb on the software and hardware rings

    :param dp:
        NFP Net data path struct
    :type dp: const struct nfp_net_dp \*

    :param rx_ring:
        RX ring structure
    :type rx_ring: struct nfp_net_rx_ring \*

    :param frag:
        page fragment buffer
    :type frag: void \*

    :param dma_addr:
        DMA address of skb mapping
    :type dma_addr: dma_addr_t

.. _`nfp_net_rx_ring_reset`:

nfp_net_rx_ring_reset
=====================

.. c:function:: void nfp_net_rx_ring_reset(struct nfp_net_rx_ring *rx_ring)

    Reflect in SW state of freelist after disable

    :param rx_ring:
        RX ring structure
    :type rx_ring: struct nfp_net_rx_ring \*

.. _`nfp_net_rx_ring_reset.description`:

Description
-----------

Assumes that the device is stopped, must be idempotent.

.. _`nfp_net_rx_ring_bufs_free`:

nfp_net_rx_ring_bufs_free
=========================

.. c:function:: void nfp_net_rx_ring_bufs_free(struct nfp_net_dp *dp, struct nfp_net_rx_ring *rx_ring)

    Free any buffers currently on the RX ring

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param rx_ring:
        RX ring to remove buffers from
    :type rx_ring: struct nfp_net_rx_ring \*

.. _`nfp_net_rx_ring_bufs_free.description`:

Description
-----------

Assumes that the device is stopped and buffers are in [0, ring->cnt - 1)
entries.  After device is disabled \ :c:func:`nfp_net_rx_ring_reset`\  must be called
to restore required ring geometry.

.. _`nfp_net_rx_ring_bufs_alloc`:

nfp_net_rx_ring_bufs_alloc
==========================

.. c:function:: int nfp_net_rx_ring_bufs_alloc(struct nfp_net_dp *dp, struct nfp_net_rx_ring *rx_ring)

    Fill RX ring with buffers (don't give to FW)

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param rx_ring:
        RX ring to remove buffers from
    :type rx_ring: struct nfp_net_rx_ring \*

.. _`nfp_net_rx_ring_fill_freelist`:

nfp_net_rx_ring_fill_freelist
=============================

.. c:function:: void nfp_net_rx_ring_fill_freelist(struct nfp_net_dp *dp, struct nfp_net_rx_ring *rx_ring)

    Give buffers from the ring to FW

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param rx_ring:
        RX ring to fill
    :type rx_ring: struct nfp_net_rx_ring \*

.. _`nfp_net_rx_csum_has_errors`:

nfp_net_rx_csum_has_errors
==========================

.. c:function:: int nfp_net_rx_csum_has_errors(u16 flags)

    group check if rxd has any csum errors

    :param flags:
        RX descriptor flags field in CPU byte order
    :type flags: u16

.. _`nfp_net_rx_csum`:

nfp_net_rx_csum
===============

.. c:function:: void nfp_net_rx_csum(struct nfp_net_dp *dp, struct nfp_net_r_vector *r_vec, struct nfp_net_rx_desc *rxd, struct nfp_meta_parsed *meta, struct sk_buff *skb)

    set SKB checksum field based on RX descriptor flags

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param r_vec:
        per-ring structure
    :type r_vec: struct nfp_net_r_vector \*

    :param rxd:
        Pointer to RX descriptor
    :type rxd: struct nfp_net_rx_desc \*

    :param meta:
        Parsed metadata prepend
    :type meta: struct nfp_meta_parsed \*

    :param skb:
        Pointer to SKB
    :type skb: struct sk_buff \*

.. _`nfp_net_rx`:

nfp_net_rx
==========

.. c:function:: int nfp_net_rx(struct nfp_net_rx_ring *rx_ring, int budget)

    receive up to \ ``budget``\  packets on \ ``rx_ring``\ 

    :param rx_ring:
        RX ring to receive from
    :type rx_ring: struct nfp_net_rx_ring \*

    :param budget:
        NAPI budget
    :type budget: int

.. _`nfp_net_rx.description`:

Description
-----------

Note, this function is separated out from the napi poll function to
more cleanly separate packet receive code from other bookkeeping
functions performed in the napi poll function.

.. _`nfp_net_rx.return`:

Return
------

Number of packets received.

.. _`nfp_net_poll`:

nfp_net_poll
============

.. c:function:: int nfp_net_poll(struct napi_struct *napi, int budget)

    napi poll function

    :param napi:
        NAPI structure
    :type napi: struct napi_struct \*

    :param budget:
        NAPI budget
    :type budget: int

.. _`nfp_net_poll.return`:

Return
------

number of packets polled.

.. _`nfp_net_vecs_init`:

nfp_net_vecs_init
=================

.. c:function:: void nfp_net_vecs_init(struct nfp_net *nn)

    Assign IRQs and setup rvecs.

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

.. _`nfp_net_tx_ring_free`:

nfp_net_tx_ring_free
====================

.. c:function:: void nfp_net_tx_ring_free(struct nfp_net_tx_ring *tx_ring)

    Free resources allocated to a TX ring

    :param tx_ring:
        TX ring to free
    :type tx_ring: struct nfp_net_tx_ring \*

.. _`nfp_net_tx_ring_alloc`:

nfp_net_tx_ring_alloc
=====================

.. c:function:: int nfp_net_tx_ring_alloc(struct nfp_net_dp *dp, struct nfp_net_tx_ring *tx_ring)

    Allocate resource for a TX ring

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param tx_ring:
        TX Ring structure to allocate
    :type tx_ring: struct nfp_net_tx_ring \*

.. _`nfp_net_tx_ring_alloc.return`:

Return
------

0 on success, negative errno otherwise.

.. _`nfp_net_rx_ring_free`:

nfp_net_rx_ring_free
====================

.. c:function:: void nfp_net_rx_ring_free(struct nfp_net_rx_ring *rx_ring)

    Free resources allocated to a RX ring

    :param rx_ring:
        RX ring to free
    :type rx_ring: struct nfp_net_rx_ring \*

.. _`nfp_net_rx_ring_alloc`:

nfp_net_rx_ring_alloc
=====================

.. c:function:: int nfp_net_rx_ring_alloc(struct nfp_net_dp *dp, struct nfp_net_rx_ring *rx_ring)

    Allocate resource for a RX ring

    :param dp:
        NFP Net data path struct
    :type dp: struct nfp_net_dp \*

    :param rx_ring:
        RX ring to allocate
    :type rx_ring: struct nfp_net_rx_ring \*

.. _`nfp_net_rx_ring_alloc.return`:

Return
------

0 on success, negative errno otherwise.

.. _`nfp_net_rss_write_itbl`:

nfp_net_rss_write_itbl
======================

.. c:function:: void nfp_net_rss_write_itbl(struct nfp_net *nn)

    Write RSS indirection table to device

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_rss_write_key`:

nfp_net_rss_write_key
=====================

.. c:function:: void nfp_net_rss_write_key(struct nfp_net *nn)

    Write RSS hash key to device

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_coalesce_write_cfg`:

nfp_net_coalesce_write_cfg
==========================

.. c:function:: void nfp_net_coalesce_write_cfg(struct nfp_net *nn)

    Write irq coalescence configuration to HW

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_write_mac_addr`:

nfp_net_write_mac_addr
======================

.. c:function:: void nfp_net_write_mac_addr(struct nfp_net *nn, const u8 *addr)

    Write mac address to the device control BAR

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

    :param addr:
        MAC address to write
    :type addr: const u8 \*

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

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_clear_config_and_disable.warning`:

Warning
-------

must be fully idempotent.

.. _`nfp_net_set_config_and_enable`:

nfp_net_set_config_and_enable
=============================

.. c:function:: int nfp_net_set_config_and_enable(struct nfp_net *nn)

    Write control BAR and enable NFP

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_close_stack`:

nfp_net_close_stack
===================

.. c:function:: void nfp_net_close_stack(struct nfp_net *nn)

    Quiesce the stack (part of close)

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_close_free_all`:

nfp_net_close_free_all
======================

.. c:function:: void nfp_net_close_free_all(struct nfp_net *nn)

    Free all runtime resources

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_netdev_close`:

nfp_net_netdev_close
====================

.. c:function:: int nfp_net_netdev_close(struct net_device *netdev)

    Called when the device is downed

    :param netdev:
        netdev structure
    :type netdev: struct net_device \*

.. _`nfp_net_open_stack`:

nfp_net_open_stack
==================

.. c:function:: void nfp_net_open_stack(struct nfp_net *nn)

    Start the device from stack's perspective

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_set_vxlan_port`:

nfp_net_set_vxlan_port
======================

.. c:function:: void nfp_net_set_vxlan_port(struct nfp_net *nn, int idx, __be16 port)

    set vxlan port in SW and reconfigure HW

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

    :param idx:
        Index into the port table where new port should be written
    :type idx: int

    :param port:
        UDP port to configure (pass zero to remove VXLAN port)
    :type port: __be16

.. _`nfp_net_find_vxlan_idx`:

nfp_net_find_vxlan_idx
======================

.. c:function:: int nfp_net_find_vxlan_idx(struct nfp_net *nn, __be16 port)

    find table entry of the port or a free one

    :param nn:
        NFP Network structure
    :type nn: struct nfp_net \*

    :param port:
        UDP port to look for
    :type port: __be16

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

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_alloc`:

nfp_net_alloc
=============

.. c:function:: struct nfp_net *nfp_net_alloc(struct pci_dev *pdev, bool needs_netdev, unsigned int max_tx_rings, unsigned int max_rx_rings)

    Allocate netdev and related structure

    :param pdev:
        PCI device
    :type pdev: struct pci_dev \*

    :param needs_netdev:
        Whether to allocate a netdev for this vNIC
    :type needs_netdev: bool

    :param max_tx_rings:
        Maximum number of TX rings supported by device
    :type max_tx_rings: unsigned int

    :param max_rx_rings:
        Maximum number of RX rings supported by device
    :type max_rx_rings: unsigned int

.. _`nfp_net_alloc.description`:

Description
-----------

This function allocates a netdev device and fills in the initial
part of the \ ``struct``\  nfp_net structure.  In case of control device
nfp_net structure is allocated without the netdev.

.. _`nfp_net_alloc.return`:

Return
------

NFP Net device structure, or ERR_PTR on error.

.. _`nfp_net_free`:

nfp_net_free
============

.. c:function:: void nfp_net_free(struct nfp_net *nn)

    Undo what \ ``nfp_net_alloc``\ () did

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_rss_key_sz`:

nfp_net_rss_key_sz
==================

.. c:function:: unsigned int nfp_net_rss_key_sz(struct nfp_net *nn)

    Get current size of the RSS key

    :param nn:
        NFP Net device instance
    :type nn: struct nfp_net \*

.. _`nfp_net_rss_key_sz.return`:

Return
------

size of the RSS key for currently selected hash function.

.. _`nfp_net_rss_init`:

nfp_net_rss_init
================

.. c:function:: void nfp_net_rss_init(struct nfp_net *nn)

    Set the initial RSS parameters

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_irqmod_init`:

nfp_net_irqmod_init
===================

.. c:function:: void nfp_net_irqmod_init(struct nfp_net *nn)

    Set the initial IRQ moderation parameters

    :param nn:
        NFP Net device to reconfigure
    :type nn: struct nfp_net \*

.. _`nfp_net_init`:

nfp_net_init
============

.. c:function:: int nfp_net_init(struct nfp_net *nn)

    Initialise/finalise the nfp_net structure

    :param nn:
        NFP Net device structure
    :type nn: struct nfp_net \*

.. _`nfp_net_init.return`:

Return
------

0 on success or negative errno on error.

.. _`nfp_net_clean`:

nfp_net_clean
=============

.. c:function:: void nfp_net_clean(struct nfp_net *nn)

    Undo what \ :c:func:`nfp_net_init`\  did.

    :param nn:
        NFP Net device structure
    :type nn: struct nfp_net \*

.. This file was automatic generated / don't edit.

