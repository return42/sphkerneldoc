.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_main.c

.. _`ixgbe_pcie_from_parent`:

ixgbe_pcie_from_parent
======================

.. c:function:: bool ixgbe_pcie_from_parent(struct ixgbe_hw *hw)

    Determine whether PCIe info should come from parent

    :param struct ixgbe_hw \*hw:
        hw specific details

.. _`ixgbe_pcie_from_parent.description`:

Description
-----------

This function is used by probe to determine whether a device's PCI-Express
bandwidth details should be gathered from the parent bus instead of from the
device. Used to ensure that various locations all have the correct device ID
checks.

.. _`ixgbe_read_reg`:

ixgbe_read_reg
==============

.. c:function:: u32 ixgbe_read_reg(struct ixgbe_hw *hw, u32 reg)

    Read from device register

    :param struct ixgbe_hw \*hw:
        hw specific details

    :param u32 reg:
        offset of register to read

.. _`ixgbe_read_reg.description`:

Description
-----------

Returns : value read or IXGBE_FAILED_READ_REG if removed

This function is used to read device registers. It checks for device
removal by confirming any read that returns all ones by checking the
status register value for all ones. This function avoids reading from
the hardware if a removal was previously detected in which case it
returns IXGBE_FAILED_READ_REG (all ones).

.. _`ixgbe_set_ivar`:

ixgbe_set_ivar
==============

.. c:function:: void ixgbe_set_ivar(struct ixgbe_adapter *adapter, s8 direction, u8 queue, u8 msix_vector)

    set the IVAR registers, mapping interrupt causes to vectors

    :param struct ixgbe_adapter \*adapter:
        pointer to adapter struct

    :param s8 direction:
        0 for Rx, 1 for Tx, -1 for other causes

    :param u8 queue:
        queue to map the corresponding interrupt to

    :param u8 msix_vector:
        the vector to map to the corresponding queue

.. _`ixgbe_tx_timeout_reset`:

ixgbe_tx_timeout_reset
======================

.. c:function:: void ixgbe_tx_timeout_reset(struct ixgbe_adapter *adapter)

    initiate reset due to Tx timeout

    :param struct ixgbe_adapter \*adapter:
        driver private struct

.. _`ixgbe_tx_maxrate`:

ixgbe_tx_maxrate
================

.. c:function:: int ixgbe_tx_maxrate(struct net_device *netdev, int queue_index, u32 maxrate)

    callback to set the maximum per-queue bitrate

    :param struct net_device \*netdev:
        *undescribed*

    :param int queue_index:
        *undescribed*

    :param u32 maxrate:
        *undescribed*

.. _`ixgbe_clean_tx_irq`:

ixgbe_clean_tx_irq
==================

.. c:function:: bool ixgbe_clean_tx_irq(struct ixgbe_q_vector *q_vector, struct ixgbe_ring *tx_ring, int napi_budget)

    Reclaim resources after transmit completes

    :param struct ixgbe_q_vector \*q_vector:
        structure containing interrupt and ring information

    :param struct ixgbe_ring \*tx_ring:
        tx ring to clean

    :param int napi_budget:
        Used to determine if we are in netpoll

.. _`ixgbe_rx_is_fcoe`:

ixgbe_rx_is_fcoe
================

.. c:function:: bool ixgbe_rx_is_fcoe(struct ixgbe_ring *ring, union ixgbe_adv_rx_desc *rx_desc)

    check the rx desc for incoming pkt type

    :param struct ixgbe_ring \*ring:
        structure containing ring specific data

    :param union ixgbe_adv_rx_desc \*rx_desc:
        advanced rx descriptor

.. _`ixgbe_rx_is_fcoe.description`:

Description
-----------

Returns : true if it is FCoE pkt

.. _`ixgbe_rx_checksum`:

ixgbe_rx_checksum
=================

.. c:function:: void ixgbe_rx_checksum(struct ixgbe_ring *ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    indicate in skb if hw indicated a good cksum

    :param struct ixgbe_ring \*ring:
        structure containing ring specific data

    :param union ixgbe_adv_rx_desc \*rx_desc:
        current Rx descriptor being processed

    :param struct sk_buff \*skb:
        skb currently being received and modified

.. _`ixgbe_alloc_rx_buffers`:

ixgbe_alloc_rx_buffers
======================

.. c:function:: void ixgbe_alloc_rx_buffers(struct ixgbe_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers

    :param struct ixgbe_ring \*rx_ring:
        ring to place buffers on

    :param u16 cleaned_count:
        number of buffers to replace

.. _`ixgbe_process_skb_fields`:

ixgbe_process_skb_fields
========================

.. c:function:: void ixgbe_process_skb_fields(struct ixgbe_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Populate skb header fields from Rx descriptor

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring packet is being transacted on

    :param union ixgbe_adv_rx_desc \*rx_desc:
        pointer to the EOP Rx descriptor

    :param struct sk_buff \*skb:
        pointer to current skb being populated

.. _`ixgbe_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, timestamp, protocol, and
other fields within the skb.

.. _`ixgbe_is_non_eop`:

ixgbe_is_non_eop
================

.. c:function:: bool ixgbe_is_non_eop(struct ixgbe_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    process handling of non-EOP buffers

    :param struct ixgbe_ring \*rx_ring:
        Rx ring being processed

    :param union ixgbe_adv_rx_desc \*rx_desc:
        Rx descriptor for current buffer

    :param struct sk_buff \*skb:
        Current socket buffer containing buffer in progress

.. _`ixgbe_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`ixgbe_pull_tail`:

ixgbe_pull_tail
===============

.. c:function:: void ixgbe_pull_tail(struct ixgbe_ring *rx_ring, struct sk_buff *skb)

    ixgbe specific version of skb_pull_tail

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring packet is being transacted on

    :param struct sk_buff \*skb:
        pointer to current skb being adjusted

.. _`ixgbe_pull_tail.description`:

Description
-----------

This function is an ixgbe specific version of \__pskb_pull_tail.  The
main difference between this version and the original function is that
this function can make several assumptions about the state of things
that allow for significant optimizations versus the standard function.
As a result we can do things like drop a frag and maintain an accurate
truesize for the skb.

.. _`ixgbe_dma_sync_frag`:

ixgbe_dma_sync_frag
===================

.. c:function:: void ixgbe_dma_sync_frag(struct ixgbe_ring *rx_ring, struct sk_buff *skb)

    perform DMA sync for first frag of SKB

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring packet is being transacted on

    :param struct sk_buff \*skb:
        pointer to current skb being updated

.. _`ixgbe_dma_sync_frag.description`:

Description
-----------

This function provides a basic DMA sync up for the first fragment of an
skb.  The reason for doing this is that the first fragment cannot be
unmapped until we have reached the end of packet descriptor for a buffer
chain.

.. _`ixgbe_cleanup_headers`:

ixgbe_cleanup_headers
=====================

.. c:function:: bool ixgbe_cleanup_headers(struct ixgbe_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Correct corrupted or empty headers

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring packet is being transacted on

    :param union ixgbe_adv_rx_desc \*rx_desc:
        pointer to the EOP Rx descriptor

    :param struct sk_buff \*skb:
        pointer to current skb being fixed

.. _`ixgbe_cleanup_headers.description`:

Description
-----------

Check if the skb is valid in the XDP case it will be an error pointer.
Return true in this case to abort processing and advance to next
descriptor.

Check for corrupted packet headers caused by senders on the local L2
embedded NIC switch not setting up their Tx Descriptors right.  These
should be very rare.

Also address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`ixgbe_reuse_rx_page`:

ixgbe_reuse_rx_page
===================

.. c:function:: void ixgbe_reuse_rx_page(struct ixgbe_ring *rx_ring, struct ixgbe_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring to store buffers on

    :param struct ixgbe_rx_buffer \*old_buff:
        donor buffer to have page reused

.. _`ixgbe_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`ixgbe_add_rx_frag`:

ixgbe_add_rx_frag
=================

.. c:function:: void ixgbe_add_rx_frag(struct ixgbe_ring *rx_ring, struct ixgbe_rx_buffer *rx_buffer, struct sk_buff *skb, unsigned int size)

    Add contents of Rx buffer to sk_buff

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring to transact packets on

    :param struct ixgbe_rx_buffer \*rx_buffer:
        buffer containing page to add

    :param struct sk_buff \*skb:
        sk_buff to place the data into

    :param unsigned int size:
        *undescribed*

.. _`ixgbe_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.
This is done either through a direct copy if the data in the buffer is
less than the skb header size, otherwise it will just attach the page as
a frag to the skb.

The function will then update the page offset if necessary and return
true if the buffer can be reused by the adapter.

.. _`ixgbe_clean_rx_irq`:

ixgbe_clean_rx_irq
==================

.. c:function:: int ixgbe_clean_rx_irq(struct ixgbe_q_vector *q_vector, struct ixgbe_ring *rx_ring, const int budget)

    Clean completed descriptors from Rx ring - bounce buf

    :param struct ixgbe_q_vector \*q_vector:
        structure containing interrupt and ring information

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring to transact packets on

    :param const int budget:
        Total limit on number of packets to process

.. _`ixgbe_clean_rx_irq.description`:

Description
-----------

This function provides a "bounce buffer" approach to Rx interrupt
processing.  The advantage to this is that on systems that have
expensive overhead for IOMMU access this provides a means of avoiding
it by maintaining the mapping of the page to the syste.

Returns amount of work completed

.. _`ixgbe_configure_msix`:

ixgbe_configure_msix
====================

.. c:function:: void ixgbe_configure_msix(struct ixgbe_adapter *adapter)

    Configure MSI-X hardware

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_configure_msix.description`:

Description
-----------

ixgbe_configure_msix sets up the hardware to properly generate MSI-X
interrupts.

.. _`ixgbe_update_itr`:

ixgbe_update_itr
================

.. c:function:: void ixgbe_update_itr(struct ixgbe_q_vector *q_vector, struct ixgbe_ring_container *ring_container)

    update the dynamic ITR value based on statistics

    :param struct ixgbe_q_vector \*q_vector:
        structure containing interrupt and ring information

    :param struct ixgbe_ring_container \*ring_container:
        structure containing ring performance data

.. _`ixgbe_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.
this functionality is controlled by the InterruptThrottleRate module
parameter (see ixgbe_param.c)

.. _`ixgbe_write_eitr`:

ixgbe_write_eitr
================

.. c:function:: void ixgbe_write_eitr(struct ixgbe_q_vector *q_vector)

    write EITR register in hardware specific way

    :param struct ixgbe_q_vector \*q_vector:
        structure containing interrupt and ring information

.. _`ixgbe_write_eitr.description`:

Description
-----------

This function is made to be called by ethtool and by the driver
when it needs to update EITR registers at runtime.  Hardware
specific quirks/differences are taken care of here.

.. _`ixgbe_check_overtemp_subtask`:

ixgbe_check_overtemp_subtask
============================

.. c:function:: void ixgbe_check_overtemp_subtask(struct ixgbe_adapter *adapter)

    check for over temperature

    :param struct ixgbe_adapter \*adapter:
        pointer to adapter

.. _`ixgbe_irq_enable`:

ixgbe_irq_enable
================

.. c:function:: void ixgbe_irq_enable(struct ixgbe_adapter *adapter, bool queues, bool flush)

    Enable default interrupt generation settings

    :param struct ixgbe_adapter \*adapter:
        board private structure

    :param bool queues:
        *undescribed*

    :param bool flush:
        *undescribed*

.. _`ixgbe_poll`:

ixgbe_poll
==========

.. c:function:: int ixgbe_poll(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param struct napi_struct \*napi:
        structure for representing this polling device

    :param int budget:
        how many packets driver is allowed to clean

.. _`ixgbe_poll.description`:

Description
-----------

This function is used for legacy and MSI, NAPI mode

.. _`ixgbe_request_msix_irqs`:

ixgbe_request_msix_irqs
=======================

.. c:function:: int ixgbe_request_msix_irqs(struct ixgbe_adapter *adapter)

    Initialize MSI-X interrupts

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_request_msix_irqs.description`:

Description
-----------

ixgbe_request_msix_irqs allocates MSI-X vectors and requests
interrupts from the kernel.

.. _`ixgbe_intr`:

ixgbe_intr
==========

.. c:function:: irqreturn_t ixgbe_intr(int irq, void *data)

    legacy mode Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`ixgbe_request_irq`:

ixgbe_request_irq
=================

.. c:function:: int ixgbe_request_irq(struct ixgbe_adapter *adapter)

    initialize interrupts

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`ixgbe_irq_disable`:

ixgbe_irq_disable
=================

.. c:function:: void ixgbe_irq_disable(struct ixgbe_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_configure_msi_and_legacy`:

ixgbe_configure_msi_and_legacy
==============================

.. c:function:: void ixgbe_configure_msi_and_legacy(struct ixgbe_adapter *adapter)

    Initialize PIN (INTA...) and MSI interrupts

    :param struct ixgbe_adapter \*adapter:
        *undescribed*

.. _`ixgbe_configure_tx_ring`:

ixgbe_configure_tx_ring
=======================

.. c:function:: void ixgbe_configure_tx_ring(struct ixgbe_adapter *adapter, struct ixgbe_ring *ring)

    Configure 8259x Tx ring after Reset

    :param struct ixgbe_adapter \*adapter:
        board private structure

    :param struct ixgbe_ring \*ring:
        structure containing ring specific data

.. _`ixgbe_configure_tx_ring.description`:

Description
-----------

Configure the Tx descriptor ring after a reset.

.. _`ixgbe_configure_tx`:

ixgbe_configure_tx
==================

.. c:function:: void ixgbe_configure_tx(struct ixgbe_adapter *adapter)

    Configure 8259x Transmit Unit after Reset

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`ixgbe_rss_indir_tbl_entries`:

ixgbe_rss_indir_tbl_entries
===========================

.. c:function:: u32 ixgbe_rss_indir_tbl_entries(struct ixgbe_adapter *adapter)

    Return RSS indirection table entries

    :param struct ixgbe_adapter \*adapter:
        device handle

.. _`ixgbe_rss_indir_tbl_entries.description`:

Description
-----------

- 82598/82599/X540:     128
- X550(non-SRIOV mode): 512
- X550(SRIOV mode):     64

.. _`ixgbe_store_key`:

ixgbe_store_key
===============

.. c:function:: void ixgbe_store_key(struct ixgbe_adapter *adapter)

    Write the RSS key to HW

    :param struct ixgbe_adapter \*adapter:
        device handle

.. _`ixgbe_store_key.description`:

Description
-----------

Write the RSS key stored in adapter.rss_key to HW.

.. _`ixgbe_init_rss_key`:

ixgbe_init_rss_key
==================

.. c:function:: int ixgbe_init_rss_key(struct ixgbe_adapter *adapter)

    Initialize adapter RSS key

    :param struct ixgbe_adapter \*adapter:
        device handle

.. _`ixgbe_init_rss_key.description`:

Description
-----------

Allocates and initializes the RSS key if it is not allocated.

.. _`ixgbe_store_reta`:

ixgbe_store_reta
================

.. c:function:: void ixgbe_store_reta(struct ixgbe_adapter *adapter)

    Write the RETA table to HW

    :param struct ixgbe_adapter \*adapter:
        device handle

.. _`ixgbe_store_reta.description`:

Description
-----------

Write the RSS redirection table stored in adapter.rss_indir_tbl[] to HW.

.. _`ixgbe_store_vfreta`:

ixgbe_store_vfreta
==================

.. c:function:: void ixgbe_store_vfreta(struct ixgbe_adapter *adapter)

    Write the RETA table to HW (x550 devices in SRIOV mode)

    :param struct ixgbe_adapter \*adapter:
        device handle

.. _`ixgbe_store_vfreta.description`:

Description
-----------

Write the RSS redirection table stored in adapter.rss_indir_tbl[] to HW.

.. _`ixgbe_configure_rscctl`:

ixgbe_configure_rscctl
======================

.. c:function:: void ixgbe_configure_rscctl(struct ixgbe_adapter *adapter, struct ixgbe_ring *ring)

    enable RSC for the indicated ring

    :param struct ixgbe_adapter \*adapter:
        address of board private structure

    :param struct ixgbe_ring \*ring:
        *undescribed*

.. _`ixgbe_configure_rx`:

ixgbe_configure_rx
==================

.. c:function:: void ixgbe_configure_rx(struct ixgbe_adapter *adapter)

    Configure 8259x Receive Unit after Reset

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`ixgbe_vlan_strip_disable`:

ixgbe_vlan_strip_disable
========================

.. c:function:: void ixgbe_vlan_strip_disable(struct ixgbe_adapter *adapter)

    helper to disable hw vlan stripping

    :param struct ixgbe_adapter \*adapter:
        driver data

.. _`ixgbe_vlan_strip_enable`:

ixgbe_vlan_strip_enable
=======================

.. c:function:: void ixgbe_vlan_strip_enable(struct ixgbe_adapter *adapter)

    helper to enable hw vlan stripping

    :param struct ixgbe_adapter \*adapter:
        driver data

.. _`ixgbe_write_mc_addr_list`:

ixgbe_write_mc_addr_list
========================

.. c:function:: int ixgbe_write_mc_addr_list(struct net_device *netdev)

    write multicast addresses to MTA

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgbe_write_mc_addr_list.description`:

Description
-----------

Writes multicast address list to the MTA hash table.

.. _`ixgbe_write_mc_addr_list.return`:

Return
------

-ENOMEM on failure
0 on no addresses written
X on writing X addresses to MTA

.. _`ixgbe_write_uc_addr_list`:

ixgbe_write_uc_addr_list
========================

.. c:function:: int ixgbe_write_uc_addr_list(struct net_device *netdev, int vfn)

    write unicast addresses to RAR table

    :param struct net_device \*netdev:
        network interface device structure

    :param int vfn:
        *undescribed*

.. _`ixgbe_write_uc_addr_list.description`:

Description
-----------

Writes unicast address list to the RAR table.

.. _`ixgbe_write_uc_addr_list.return`:

Return
------

-ENOMEM on failure/insufficient address space
0 on no addresses written
X on writing X addresses to the RAR table

.. _`ixgbe_set_rx_mode`:

ixgbe_set_rx_mode
=================

.. c:function:: void ixgbe_set_rx_mode(struct net_device *netdev)

    Unicast, Multicast and Promiscuous mode set

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgbe_set_rx_mode.description`:

Description
-----------

The set_rx_method entry point is called whenever the unicast/multicast
address list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper unicast, multicast and
promiscuous mode.

.. _`ixgbe_configure_dcb`:

ixgbe_configure_dcb
===================

.. c:function:: void ixgbe_configure_dcb(struct ixgbe_adapter *adapter)

    Configure DCB hardware

    :param struct ixgbe_adapter \*adapter:
        ixgbe adapter struct

.. _`ixgbe_configure_dcb.description`:

Description
-----------

This is called by the driver on open to configure the DCB hardware.
This is also called by the gennetlink interface when reconfiguring
the DCB state.

.. _`ixgbe_hpbthresh`:

ixgbe_hpbthresh
===============

.. c:function:: int ixgbe_hpbthresh(struct ixgbe_adapter *adapter, int pb)

    calculate high water mark for flow control

    :param struct ixgbe_adapter \*adapter:
        board private structure to calculate for

    :param int pb:
        packet buffer to calculate

.. _`ixgbe_lpbthresh`:

ixgbe_lpbthresh
===============

.. c:function:: int ixgbe_lpbthresh(struct ixgbe_adapter *adapter, int pb)

    calculate low water mark for for flow control

    :param struct ixgbe_adapter \*adapter:
        board private structure to calculate for

    :param int pb:
        packet buffer to calculate

.. _`ixgbe_clean_rx_ring`:

ixgbe_clean_rx_ring
===================

.. c:function:: void ixgbe_clean_rx_ring(struct ixgbe_ring *rx_ring)

    Free Rx Buffers per Queue

    :param struct ixgbe_ring \*rx_ring:
        ring to free buffers from

.. _`ixgbe_sfp_link_config`:

ixgbe_sfp_link_config
=====================

.. c:function:: void ixgbe_sfp_link_config(struct ixgbe_adapter *adapter)

    set up SFP+ link

    :param struct ixgbe_adapter \*adapter:
        pointer to private adapter struct

.. _`ixgbe_non_sfp_link_config`:

ixgbe_non_sfp_link_config
=========================

.. c:function:: int ixgbe_non_sfp_link_config(struct ixgbe_hw *hw)

    set up non-SFP+ link

    :param struct ixgbe_hw \*hw:
        pointer to private hardware struct

.. _`ixgbe_non_sfp_link_config.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbe_clean_tx_ring`:

ixgbe_clean_tx_ring
===================

.. c:function:: void ixgbe_clean_tx_ring(struct ixgbe_ring *tx_ring)

    Free Tx Buffers

    :param struct ixgbe_ring \*tx_ring:
        ring to be cleaned

.. _`ixgbe_clean_all_rx_rings`:

ixgbe_clean_all_rx_rings
========================

.. c:function:: void ixgbe_clean_all_rx_rings(struct ixgbe_adapter *adapter)

    Free Rx Buffers for all queues

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_clean_all_tx_rings`:

ixgbe_clean_all_tx_rings
========================

.. c:function:: void ixgbe_clean_all_tx_rings(struct ixgbe_adapter *adapter)

    Free Tx Buffers for all queues

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_set_eee_capable`:

ixgbe_set_eee_capable
=====================

.. c:function:: void ixgbe_set_eee_capable(struct ixgbe_adapter *adapter)

    helper function to determine EEE support on X550

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_tx_timeout`:

ixgbe_tx_timeout
================

.. c:function:: void ixgbe_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgbe_sw_init`:

ixgbe_sw_init
=============

.. c:function:: int ixgbe_sw_init(struct ixgbe_adapter *adapter, const struct ixgbe_info *ii)

    Initialize general software structures (struct ixgbe_adapter)

    :param struct ixgbe_adapter \*adapter:
        board private structure to initialize

    :param const struct ixgbe_info \*ii:
        *undescribed*

.. _`ixgbe_sw_init.description`:

Description
-----------

ixgbe_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`ixgbe_setup_tx_resources`:

ixgbe_setup_tx_resources
========================

.. c:function:: int ixgbe_setup_tx_resources(struct ixgbe_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param struct ixgbe_ring \*tx_ring:
        tx descriptor ring (for a specific queue) to setup

.. _`ixgbe_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ixgbe_setup_all_tx_resources`:

ixgbe_setup_all_tx_resources
============================

.. c:function:: int ixgbe_setup_all_tx_resources(struct ixgbe_adapter *adapter)

    allocate all queues Tx resources

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_setup_all_tx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`ixgbe_setup_rx_resources`:

ixgbe_setup_rx_resources
========================

.. c:function:: int ixgbe_setup_rx_resources(struct ixgbe_adapter *adapter, struct ixgbe_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param struct ixgbe_adapter \*adapter:
        *undescribed*

    :param struct ixgbe_ring \*rx_ring:
        rx descriptor ring (for a specific queue) to setup

.. _`ixgbe_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbe_setup_all_rx_resources`:

ixgbe_setup_all_rx_resources
============================

.. c:function:: int ixgbe_setup_all_rx_resources(struct ixgbe_adapter *adapter)

    allocate all queues Rx resources

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_setup_all_rx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`ixgbe_free_tx_resources`:

ixgbe_free_tx_resources
=======================

.. c:function:: void ixgbe_free_tx_resources(struct ixgbe_ring *tx_ring)

    Free Tx Resources per Queue

    :param struct ixgbe_ring \*tx_ring:
        Tx descriptor ring for a specific queue

.. _`ixgbe_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`ixgbe_free_all_tx_resources`:

ixgbe_free_all_tx_resources
===========================

.. c:function:: void ixgbe_free_all_tx_resources(struct ixgbe_adapter *adapter)

    Free Tx Resources for All Queues

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`ixgbe_free_rx_resources`:

ixgbe_free_rx_resources
=======================

.. c:function:: void ixgbe_free_rx_resources(struct ixgbe_ring *rx_ring)

    Free Rx Resources

    :param struct ixgbe_ring \*rx_ring:
        ring to clean the resources from

.. _`ixgbe_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`ixgbe_free_all_rx_resources`:

ixgbe_free_all_rx_resources
===========================

.. c:function:: void ixgbe_free_all_rx_resources(struct ixgbe_adapter *adapter)

    Free Rx Resources for All Queues

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`ixgbe_change_mtu`:

ixgbe_change_mtu
================

.. c:function:: int ixgbe_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`ixgbe_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbe_open`:

ixgbe_open
==========

.. c:function:: int ixgbe_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgbe_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`ixgbe_close`:

ixgbe_close
===========

.. c:function:: int ixgbe_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgbe_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`ixgbe_update_stats`:

ixgbe_update_stats
==================

.. c:function:: void ixgbe_update_stats(struct ixgbe_adapter *adapter)

    Update the board statistics counters.

    :param struct ixgbe_adapter \*adapter:
        board private structure

.. _`ixgbe_fdir_reinit_subtask`:

ixgbe_fdir_reinit_subtask
=========================

.. c:function:: void ixgbe_fdir_reinit_subtask(struct ixgbe_adapter *adapter)

    worker thread to reinit FDIR filter table

    :param struct ixgbe_adapter \*adapter:
        pointer to the device adapter structure

.. _`ixgbe_check_hang_subtask`:

ixgbe_check_hang_subtask
========================

.. c:function:: void ixgbe_check_hang_subtask(struct ixgbe_adapter *adapter)

    check for hung queues and dropped interrupts

    :param struct ixgbe_adapter \*adapter:
        pointer to the device adapter structure

.. _`ixgbe_check_hang_subtask.description`:

Description
-----------

This function serves two purposes.  First it strobes the interrupt lines
in order to make certain interrupts are occurring.  Secondly it sets the
bits needed to check for TX hangs.  As a result we should immediately
determine if a hang has occurred.

.. _`ixgbe_watchdog_update_link`:

ixgbe_watchdog_update_link
==========================

.. c:function:: void ixgbe_watchdog_update_link(struct ixgbe_adapter *adapter)

    update the link status

    :param struct ixgbe_adapter \*adapter:
        pointer to the device adapter structure

.. _`ixgbe_watchdog_link_is_up`:

ixgbe_watchdog_link_is_up
=========================

.. c:function:: void ixgbe_watchdog_link_is_up(struct ixgbe_adapter *adapter)

    update netif_carrier status and print link up message

    :param struct ixgbe_adapter \*adapter:
        pointer to the device adapter structure

.. _`ixgbe_watchdog_link_is_down`:

ixgbe_watchdog_link_is_down
===========================

.. c:function:: void ixgbe_watchdog_link_is_down(struct ixgbe_adapter *adapter)

    update netif_carrier status and print link down message

    :param struct ixgbe_adapter \*adapter:
        pointer to the adapter structure

.. _`ixgbe_watchdog_flush_tx`:

ixgbe_watchdog_flush_tx
=======================

.. c:function:: void ixgbe_watchdog_flush_tx(struct ixgbe_adapter *adapter)

    flush queues on link down

    :param struct ixgbe_adapter \*adapter:
        pointer to the device adapter structure

.. _`ixgbe_watchdog_subtask`:

ixgbe_watchdog_subtask
======================

.. c:function:: void ixgbe_watchdog_subtask(struct ixgbe_adapter *adapter)

    check and bring link up

    :param struct ixgbe_adapter \*adapter:
        pointer to the device adapter structure

.. _`ixgbe_sfp_detection_subtask`:

ixgbe_sfp_detection_subtask
===========================

.. c:function:: void ixgbe_sfp_detection_subtask(struct ixgbe_adapter *adapter)

    poll for SFP+ cable

    :param struct ixgbe_adapter \*adapter:
        the ixgbe adapter structure

.. _`ixgbe_sfp_link_config_subtask`:

ixgbe_sfp_link_config_subtask
=============================

.. c:function:: void ixgbe_sfp_link_config_subtask(struct ixgbe_adapter *adapter)

    set up link SFP after module install

    :param struct ixgbe_adapter \*adapter:
        the ixgbe adapter structure

.. _`ixgbe_service_timer`:

ixgbe_service_timer
===================

.. c:function:: void ixgbe_service_timer(unsigned long data)

    Timer Call-back

    :param unsigned long data:
        pointer to adapter cast into an unsigned long

.. _`ixgbe_service_task`:

ixgbe_service_task
==================

.. c:function:: void ixgbe_service_task(struct work_struct *work)

    manages and runs subtasks

    :param struct work_struct \*work:
        pointer to work_struct containing our data

.. _`ixgbe_set_mac`:

ixgbe_set_mac
=============

.. c:function:: int ixgbe_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`ixgbe_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbe_add_sanmac_netdev`:

ixgbe_add_sanmac_netdev
=======================

.. c:function:: int ixgbe_add_sanmac_netdev(struct net_device *dev)

    Add the SAN MAC address to the corresponding netdev->dev_addrs

    :param struct net_device \*dev:
        *undescribed*

.. _`ixgbe_add_sanmac_netdev.description`:

Description
-----------

Returns non-zero on failure

.. _`ixgbe_del_sanmac_netdev`:

ixgbe_del_sanmac_netdev
=======================

.. c:function:: int ixgbe_del_sanmac_netdev(struct net_device *dev)

    Removes the SAN MAC address to the corresponding netdev->dev_addrs

    :param struct net_device \*dev:
        *undescribed*

.. _`ixgbe_del_sanmac_netdev.description`:

Description
-----------

Returns non-zero on failure

.. _`ixgbe_validate_rtr`:

ixgbe_validate_rtr
==================

.. c:function:: void ixgbe_validate_rtr(struct ixgbe_adapter *adapter, u8 tc)

    verify 802.1Qp to Rx packet buffer mapping is valid.

    :param struct ixgbe_adapter \*adapter:
        pointer to ixgbe_adapter

    :param u8 tc:
        number of traffic classes currently enabled

.. _`ixgbe_validate_rtr.description`:

Description
-----------

Configure a valid 802.1Qp to Rx packet buffer mapping ie confirm
802.1Q priority maps to a packet buffer that exists.

.. _`ixgbe_set_prio_tc_map`:

ixgbe_set_prio_tc_map
=====================

.. c:function:: void ixgbe_set_prio_tc_map(struct ixgbe_adapter *adapter)

    Configure netdev prio tc map

    :param struct ixgbe_adapter \*adapter:
        Pointer to adapter struct

.. _`ixgbe_set_prio_tc_map.description`:

Description
-----------

Populate the netdev user priority to tc map

.. _`ixgbe_setup_tc`:

ixgbe_setup_tc
==============

.. c:function:: int ixgbe_setup_tc(struct net_device *dev, u8 tc)

    configure net_device for multiple traffic classes

    :param struct net_device \*dev:
        *undescribed*

    :param u8 tc:
        number of traffic classes to enable

.. _`ixgbe_add_udp_tunnel_port`:

ixgbe_add_udp_tunnel_port
=========================

.. c:function:: void ixgbe_add_udp_tunnel_port(struct net_device *dev, struct udp_tunnel_info *ti)

    Get notifications about adding UDP tunnel ports

    :param struct net_device \*dev:
        The port's netdev

    :param struct udp_tunnel_info \*ti:
        Tunnel endpoint information

.. _`ixgbe_del_udp_tunnel_port`:

ixgbe_del_udp_tunnel_port
=========================

.. c:function:: void ixgbe_del_udp_tunnel_port(struct net_device *dev, struct udp_tunnel_info *ti)

    Get notifications about removing UDP tunnel ports

    :param struct net_device \*dev:
        The port's netdev

    :param struct udp_tunnel_info \*ti:
        Tunnel endpoint information

.. _`ixgbe_configure_bridge_mode`:

ixgbe_configure_bridge_mode
===========================

.. c:function:: int ixgbe_configure_bridge_mode(struct ixgbe_adapter *adapter, __u16 mode)

    set various bridge modes \ ``adapter``\  - the private structure \ ``mode``\  - requested bridge mode

    :param struct ixgbe_adapter \*adapter:
        *undescribed*

    :param __u16 mode:
        *undescribed*

.. _`ixgbe_configure_bridge_mode.description`:

Description
-----------

Configure some settings require for various bridge modes.

.. _`ixgbe_enumerate_functions`:

ixgbe_enumerate_functions
=========================

.. c:function:: int ixgbe_enumerate_functions(struct ixgbe_adapter *adapter)

    Get the number of ports this device has

    :param struct ixgbe_adapter \*adapter:
        adapter structure

.. _`ixgbe_enumerate_functions.description`:

Description
-----------

This function enumerates the phsyical functions co-located on a single slot,
in order to determine how many ports a device has. This is most useful in
determining the required GT/s of PCIe bandwidth necessary for optimal
performance.

.. _`ixgbe_wol_supported`:

ixgbe_wol_supported
===================

.. c:function:: bool ixgbe_wol_supported(struct ixgbe_adapter *adapter, u16 device_id, u16 subdevice_id)

    Check whether device supports WoL

    :param struct ixgbe_adapter \*adapter:
        the adapter private structure

    :param u16 device_id:
        the device ID

    :param u16 subdevice_id:
        *undescribed*

.. _`ixgbe_wol_supported.description`:

Description
-----------

This function is used by probe and ethtool to determine
which devices have WoL support

.. _`ixgbe_probe`:

ixgbe_probe
===========

.. c:function:: int ixgbe_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in ixgbe_pci_tbl

.. _`ixgbe_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

ixgbe_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`ixgbe_remove`:

ixgbe_remove
============

.. c:function:: void ixgbe_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`ixgbe_remove.description`:

Description
-----------

ixgbe_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`ixgbe_io_error_detected`:

ixgbe_io_error_detected
=======================

.. c:function:: pci_ers_result_t ixgbe_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`ixgbe_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`ixgbe_io_slot_reset`:

ixgbe_io_slot_reset
===================

.. c:function:: pci_ers_result_t ixgbe_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`ixgbe_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.

.. _`ixgbe_io_resume`:

ixgbe_io_resume
===============

.. c:function:: void ixgbe_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`ixgbe_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation.

.. _`ixgbe_init_module`:

ixgbe_init_module
=================

.. c:function:: int ixgbe_init_module( void)

    Driver Registration Routine

    :param  void:
        no arguments

.. _`ixgbe_init_module.description`:

Description
-----------

ixgbe_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`ixgbe_exit_module`:

ixgbe_exit_module
=================

.. c:function:: void __exit ixgbe_exit_module( void)

    Driver Exit Cleanup Routine

    :param  void:
        no arguments

.. _`ixgbe_exit_module.description`:

Description
-----------

ixgbe_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.

