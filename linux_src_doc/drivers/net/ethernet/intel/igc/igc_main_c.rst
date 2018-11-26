.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igc/igc_main.c

.. _`igc_power_up_link`:

igc_power_up_link
=================

.. c:function:: void igc_power_up_link(struct igc_adapter *adapter)

    Power up the phy/serdes link

    :param adapter:
        address of board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_power_down_link`:

igc_power_down_link
===================

.. c:function:: void igc_power_down_link(struct igc_adapter *adapter)

    Power down the phy/serdes link

    :param adapter:
        address of board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_release_hw_control`:

igc_release_hw_control
======================

.. c:function:: void igc_release_hw_control(struct igc_adapter *adapter)

    release control of the h/w to f/w

    :param adapter:
        address of board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_release_hw_control.description`:

Description
-----------

igc_release_hw_control resets CTRL_EXT:DRV_LOAD bit.
For ASF and Pass Through versions of f/w this means that the
driver is no longer loaded.

.. _`igc_get_hw_control`:

igc_get_hw_control
==================

.. c:function:: void igc_get_hw_control(struct igc_adapter *adapter)

    get control of the h/w from f/w

    :param adapter:
        address of board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_get_hw_control.description`:

Description
-----------

igc_get_hw_control sets CTRL_EXT:DRV_LOAD bit.
For ASF and Pass Through versions of f/w this means that
the driver is loaded.

.. _`igc_free_tx_resources`:

igc_free_tx_resources
=====================

.. c:function:: void igc_free_tx_resources(struct igc_ring *tx_ring)

    Free Tx Resources per Queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct igc_ring \*

.. _`igc_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`igc_free_all_tx_resources`:

igc_free_all_tx_resources
=========================

.. c:function:: void igc_free_all_tx_resources(struct igc_adapter *adapter)

    Free Tx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`igc_clean_tx_ring`:

igc_clean_tx_ring
=================

.. c:function:: void igc_clean_tx_ring(struct igc_ring *tx_ring)

    Free Tx Buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct igc_ring \*

.. _`igc_clean_all_tx_rings`:

igc_clean_all_tx_rings
======================

.. c:function:: void igc_clean_all_tx_rings(struct igc_adapter *adapter)

    Free Tx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_setup_tx_resources`:

igc_setup_tx_resources
======================

.. c:function:: int igc_setup_tx_resources(struct igc_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param tx_ring:
        tx descriptor ring (for a specific queue) to setup
    :type tx_ring: struct igc_ring \*

.. _`igc_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igc_setup_all_tx_resources`:

igc_setup_all_tx_resources
==========================

.. c:function:: int igc_setup_all_tx_resources(struct igc_adapter *adapter)

    wrapper to allocate Tx resources for all queues

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_setup_all_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igc_clean_rx_ring`:

igc_clean_rx_ring
=================

.. c:function:: void igc_clean_rx_ring(struct igc_ring *rx_ring)

    Free Rx Buffers per Queue

    :param rx_ring:
        ring to free buffers from
    :type rx_ring: struct igc_ring \*

.. _`igc_clean_all_rx_rings`:

igc_clean_all_rx_rings
======================

.. c:function:: void igc_clean_all_rx_rings(struct igc_adapter *adapter)

    Free Rx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_free_rx_resources`:

igc_free_rx_resources
=====================

.. c:function:: void igc_free_rx_resources(struct igc_ring *rx_ring)

    Free Rx Resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct igc_ring \*

.. _`igc_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`igc_free_all_rx_resources`:

igc_free_all_rx_resources
=========================

.. c:function:: void igc_free_all_rx_resources(struct igc_adapter *adapter)

    Free Rx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`igc_setup_rx_resources`:

igc_setup_rx_resources
======================

.. c:function:: int igc_setup_rx_resources(struct igc_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param rx_ring:
        rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct igc_ring \*

.. _`igc_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igc_setup_all_rx_resources`:

igc_setup_all_rx_resources
==========================

.. c:function:: int igc_setup_all_rx_resources(struct igc_adapter *adapter)

    wrapper to allocate Rx resources (Descriptors) for all queues

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_setup_all_rx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igc_configure_rx_ring`:

igc_configure_rx_ring
=====================

.. c:function:: void igc_configure_rx_ring(struct igc_adapter *adapter, struct igc_ring *ring)

    Configure a receive ring after Reset

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

    :param ring:
        receive ring to be configured
    :type ring: struct igc_ring \*

.. _`igc_configure_rx_ring.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`igc_configure_rx`:

igc_configure_rx
================

.. c:function:: void igc_configure_rx(struct igc_adapter *adapter)

    Configure receive Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`igc_configure_tx_ring`:

igc_configure_tx_ring
=====================

.. c:function:: void igc_configure_tx_ring(struct igc_adapter *adapter, struct igc_ring *ring)

    Configure transmit ring after Reset

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

    :param ring:
        tx ring to configure
    :type ring: struct igc_ring \*

.. _`igc_configure_tx_ring.description`:

Description
-----------

Configure a transmit ring after a reset.

.. _`igc_configure_tx`:

igc_configure_tx
================

.. c:function:: void igc_configure_tx(struct igc_adapter *adapter)

    Configure transmit Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`igc_setup_mrqc`:

igc_setup_mrqc
==============

.. c:function:: void igc_setup_mrqc(struct igc_adapter *adapter)

    configure the multiple receive queue control registers

    :param adapter:
        Board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_setup_rctl`:

igc_setup_rctl
==============

.. c:function:: void igc_setup_rctl(struct igc_adapter *adapter)

    configure the receive control registers

    :param adapter:
        Board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_setup_tctl`:

igc_setup_tctl
==============

.. c:function:: void igc_setup_tctl(struct igc_adapter *adapter)

    configure the transmit control registers

    :param adapter:
        Board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_set_mac`:

igc_set_mac
===========

.. c:function:: int igc_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`igc_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igc_process_skb_fields`:

igc_process_skb_fields
======================

.. c:function:: void igc_process_skb_fields(struct igc_ring *rx_ring, union igc_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Populate skb header fields from Rx descriptor

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct igc_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union igc_adv_rx_desc \*

    :param skb:
        pointer to current skb being populated
    :type skb: struct sk_buff \*

.. _`igc_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, timestamp, protocol, and
other fields within the skb.

.. _`igc_add_rx_frag`:

igc_add_rx_frag
===============

.. c:function:: void igc_add_rx_frag(struct igc_ring *rx_ring, struct igc_rx_buffer *rx_buffer, struct sk_buff *skb, unsigned int size)

    Add contents of Rx buffer to sk_buff

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct igc_ring \*

    :param rx_buffer:
        buffer containing page to add
    :type rx_buffer: struct igc_rx_buffer \*

    :param skb:
        sk_buff to place the data into
    :type skb: struct sk_buff \*

    :param size:
        size of buffer to be added
    :type size: unsigned int

.. _`igc_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.

.. _`igc_reuse_rx_page`:

igc_reuse_rx_page
=================

.. c:function:: void igc_reuse_rx_page(struct igc_ring *rx_ring, struct igc_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param rx_ring:
        rx descriptor ring to store buffers on
    :type rx_ring: struct igc_ring \*

    :param old_buff:
        donor buffer to have page reused
    :type old_buff: struct igc_rx_buffer \*

.. _`igc_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`igc_is_non_eop`:

igc_is_non_eop
==============

.. c:function:: bool igc_is_non_eop(struct igc_ring *rx_ring, union igc_adv_rx_desc *rx_desc)

    process handling of non-EOP buffers

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct igc_ring \*

    :param rx_desc:
        Rx descriptor for current buffer
    :type rx_desc: union igc_adv_rx_desc \*

.. _`igc_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`igc_cleanup_headers`:

igc_cleanup_headers
===================

.. c:function:: bool igc_cleanup_headers(struct igc_ring *rx_ring, union igc_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Correct corrupted or empty headers

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct igc_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union igc_adv_rx_desc \*

    :param skb:
        pointer to current skb being fixed
    :type skb: struct sk_buff \*

.. _`igc_cleanup_headers.description`:

Description
-----------

Address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`igc_alloc_rx_buffers`:

igc_alloc_rx_buffers
====================

.. c:function:: void igc_alloc_rx_buffers(struct igc_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers; packet split

    :param rx_ring:
        *undescribed*
    :type rx_ring: struct igc_ring \*

    :param cleaned_count:
        *undescribed*
    :type cleaned_count: u16

.. _`igc_clean_tx_irq`:

igc_clean_tx_irq
================

.. c:function:: bool igc_clean_tx_irq(struct igc_q_vector *q_vector, int napi_budget)

    Reclaim resources after transmit completes

    :param q_vector:
        pointer to q_vector containing needed info
    :type q_vector: struct igc_q_vector \*

    :param napi_budget:
        Used to determine if we are in netpoll
    :type napi_budget: int

.. _`igc_clean_tx_irq.description`:

Description
-----------

returns true if ring is completely cleaned

.. _`igc_ioctl`:

igc_ioctl
=========

.. c:function:: int igc_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    I/O control method

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param cmd:
        command
    :type cmd: int

.. _`igc_up`:

igc_up
======

.. c:function:: void igc_up(struct igc_adapter *adapter)

    Open the interface and prepare it to handle traffic

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_update_stats`:

igc_update_stats
================

.. c:function:: void igc_update_stats(struct igc_adapter *adapter)

    Update the board statistics counters

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_down`:

igc_down
========

.. c:function:: void igc_down(struct igc_adapter *adapter)

    Close the interface

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_change_mtu`:

igc_change_mtu
==============

.. c:function:: int igc_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`igc_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igc_get_stats`:

igc_get_stats
=============

.. c:function:: struct net_device_stats *igc_get_stats(struct net_device *netdev)

    Get System Network Statistics

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igc_get_stats.description`:

Description
-----------

Returns the address of the device statistics structure.
The statistics are updated here and also from the timer callback.

.. _`igc_configure`:

igc_configure
=============

.. c:function:: void igc_configure(struct igc_adapter *adapter)

    configure the hardware for RX and TX

    :param adapter:
        private board structure
    :type adapter: struct igc_adapter \*

.. _`igc_rar_set_index`:

igc_rar_set_index
=================

.. c:function:: void igc_rar_set_index(struct igc_adapter *adapter, u32 index)

    Sync RAL[index] and RAH[index] registers with MAC table

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

    :param index:
        Index of the RAR entry which need to be synced with MAC table
    :type index: u32

.. _`igc_set_rx_mode`:

igc_set_rx_mode
===============

.. c:function:: void igc_set_rx_mode(struct net_device *netdev)

    Secondary Unicast, Multicast and Promiscuous mode set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igc_set_rx_mode.description`:

Description
-----------

The set_rx_mode entry point is called whenever the unicast or multicast
address lists or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper unicast, multicast,
promiscuous mode, and all-multi behavior.

.. _`igc_msix_other`:

igc_msix_other
==============

.. c:function:: irqreturn_t igc_msix_other(int irq, void *data)

    msix other interrupt handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a q_vector
    :type data: void \*

.. _`igc_write_ivar`:

igc_write_ivar
==============

.. c:function:: void igc_write_ivar(struct igc_hw *hw, int msix_vector, int index, int offset)

    configure ivar for given MSI-X vector

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param msix_vector:
        vector number we are allocating to a given ring
    :type msix_vector: int

    :param index:
        row index of IVAR register to write within IVAR table
    :type index: int

    :param offset:
        column offset of in IVAR, should be multiple of 8
    :type offset: int

.. _`igc_write_ivar.description`:

Description
-----------

The IVAR table consists of 2 columns,
each containing an cause allocation for an Rx and Tx ring, and a
variable number of rows depending on the number of queues supported.

.. _`igc_configure_msix`:

igc_configure_msix
==================

.. c:function:: void igc_configure_msix(struct igc_adapter *adapter)

    Configure MSI-X hardware

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

.. _`igc_configure_msix.description`:

Description
-----------

igc_configure_msix sets up the hardware to properly
generate MSI-X interrupts.

.. _`igc_request_msix`:

igc_request_msix
================

.. c:function:: int igc_request_msix(struct igc_adapter *adapter)

    Initialize MSI-X interrupts

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

.. _`igc_request_msix.description`:

Description
-----------

igc_request_msix allocates MSI-X vectors and requests interrupts from the
kernel.

.. _`igc_reset_q_vector`:

igc_reset_q_vector
==================

.. c:function:: void igc_reset_q_vector(struct igc_adapter *adapter, int v_idx)

    Reset config for interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

    :param v_idx:
        Index of vector to be reset
    :type v_idx: int

.. _`igc_reset_q_vector.description`:

Description
-----------

If NAPI is enabled it will delete any references to the
NAPI struct. This is preparation for igc_free_q_vector.

.. _`igc_clear_interrupt_scheme`:

igc_clear_interrupt_scheme
==========================

.. c:function:: void igc_clear_interrupt_scheme(struct igc_adapter *adapter)

    reset the device to a state of no interrupts

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

.. _`igc_clear_interrupt_scheme.description`:

Description
-----------

This function resets the device so that it has 0 rx queues, tx queues, and
MSI-X interrupts allocated.

.. _`igc_free_q_vectors`:

igc_free_q_vectors
==================

.. c:function:: void igc_free_q_vectors(struct igc_adapter *adapter)

    Free memory allocated for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

.. _`igc_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`igc_free_q_vector`:

igc_free_q_vector
=================

.. c:function:: void igc_free_q_vector(struct igc_adapter *adapter, int v_idx)

    Free memory allocated for specific interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

    :param v_idx:
        Index of vector to be freed
    :type v_idx: int

.. _`igc_free_q_vector.description`:

Description
-----------

This function frees the memory allocated to the q_vector.

.. _`igc_has_link`:

igc_has_link
============

.. c:function:: bool igc_has_link(struct igc_adapter *adapter)

    check shared code for link and determine up/down

    :param adapter:
        pointer to driver private info
    :type adapter: struct igc_adapter \*

.. _`igc_watchdog`:

igc_watchdog
============

.. c:function:: void igc_watchdog(struct timer_list *t)

    Timer Call-back

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`igc_update_ring_itr`:

igc_update_ring_itr
===================

.. c:function:: void igc_update_ring_itr(struct igc_q_vector *q_vector)

    update the dynamic ITR value based on packet size

    :param q_vector:
        pointer to q_vector
    :type q_vector: struct igc_q_vector \*

.. _`igc_update_ring_itr.description`:

Description
-----------

Stores a new ITR value based on strictly on packet size.  This
algorithm is less sophisticated than that used in igc_update_itr,
due to the difficulty of synchronizing statistics across multiple
receive rings.  The divisors and thresholds used by this function
were determined based on theoretical maximum wire speed and testing
data, in order to minimize response time while increasing bulk
throughput.

.. _`igc_update_ring_itr.note`:

NOTE
----

This function is called only when operating in a multiqueue
receive environment.

.. _`igc_update_itr`:

igc_update_itr
==============

.. c:function:: void igc_update_itr(struct igc_q_vector *q_vector, struct igc_ring_container *ring_container)

    update the dynamic ITR value based on statistics

    :param q_vector:
        pointer to q_vector
    :type q_vector: struct igc_q_vector \*

    :param ring_container:
        ring info to update the itr for
    :type ring_container: struct igc_ring_container \*

.. _`igc_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.

.. _`igc_update_itr.note`:

NOTE
----

These calculations are only valid when operating in a single-
queue environment.

.. _`igc_intr_msi`:

igc_intr_msi
============

.. c:function:: irqreturn_t igc_intr_msi(int irq, void *data)

    Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a network interface device structure
    :type data: void \*

.. _`igc_intr`:

igc_intr
========

.. c:function:: irqreturn_t igc_intr(int irq, void *data)

    Legacy Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a network interface device structure
    :type data: void \*

.. _`igc_poll`:

igc_poll
========

.. c:function:: int igc_poll(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param napi:
        napi polling structure
    :type napi: struct napi_struct \*

    :param budget:
        count of how many packets we should handle
    :type budget: int

.. _`igc_set_interrupt_capability`:

igc_set_interrupt_capability
============================

.. c:function:: void igc_set_interrupt_capability(struct igc_adapter *adapter, bool msix)

    set MSI or MSI-X if supported

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

    :param msix:
        *undescribed*
    :type msix: bool

.. _`igc_set_interrupt_capability.description`:

Description
-----------

Attempt to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`igc_alloc_q_vector`:

igc_alloc_q_vector
==================

.. c:function:: int igc_alloc_q_vector(struct igc_adapter *adapter, unsigned int v_count, unsigned int v_idx, unsigned int txr_count, unsigned int txr_idx, unsigned int rxr_count, unsigned int rxr_idx)

    Allocate memory for a single interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

    :param v_count:
        q_vectors allocated on adapter, used for ring interleaving
    :type v_count: unsigned int

    :param v_idx:
        index of vector in adapter struct
    :type v_idx: unsigned int

    :param txr_count:
        total number of Tx rings to allocate
    :type txr_count: unsigned int

    :param txr_idx:
        index of first Tx ring to allocate
    :type txr_idx: unsigned int

    :param rxr_count:
        total number of Rx rings to allocate
    :type rxr_count: unsigned int

    :param rxr_idx:
        index of first Rx ring to allocate
    :type rxr_idx: unsigned int

.. _`igc_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`igc_alloc_q_vectors`:

igc_alloc_q_vectors
===================

.. c:function:: int igc_alloc_q_vectors(struct igc_adapter *adapter)

    Allocate memory for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

.. _`igc_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`igc_cache_ring_register`:

igc_cache_ring_register
=======================

.. c:function:: void igc_cache_ring_register(struct igc_adapter *adapter)

    Descriptor ring to register mapping

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

.. _`igc_cache_ring_register.description`:

Description
-----------

Once we know the feature-set enabled for the device, we'll cache
the register offset the descriptor ring is assigned to.

.. _`igc_init_interrupt_scheme`:

igc_init_interrupt_scheme
=========================

.. c:function:: int igc_init_interrupt_scheme(struct igc_adapter *adapter, bool msix)

    initialize interrupts, allocate queues/vectors

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

    :param msix:
        *undescribed*
    :type msix: bool

.. _`igc_init_interrupt_scheme.description`:

Description
-----------

This function initializes the interrupts and allocates all of the queues.

.. _`igc_irq_disable`:

igc_irq_disable
===============

.. c:function:: void igc_irq_disable(struct igc_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_irq_enable`:

igc_irq_enable
==============

.. c:function:: void igc_irq_enable(struct igc_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct igc_adapter \*

.. _`igc_request_irq`:

igc_request_irq
===============

.. c:function:: int igc_request_irq(struct igc_adapter *adapter)

    initialize interrupts

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igc_adapter \*

.. _`igc_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`__igc_open`:

\__igc_open
===========

.. c:function:: int __igc_open(struct net_device *netdev, bool resuming)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param resuming:
        *undescribed*
    :type resuming: bool

.. _`__igc_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`__igc_close`:

\__igc_close
============

.. c:function:: int __igc_close(struct net_device *netdev, bool suspending)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param suspending:
        *undescribed*
    :type suspending: bool

.. _`__igc_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the driver's control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`igc_probe`:

igc_probe
=========

.. c:function:: int igc_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in igc_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`igc_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

igc_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring the adapter private structure,
and a hardware reset occur.

.. _`igc_remove`:

igc_remove
==========

.. c:function:: void igc_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`igc_remove.description`:

Description
-----------

igc_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  This could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`igc_sw_init`:

igc_sw_init
===========

.. c:function:: int igc_sw_init(struct igc_adapter *adapter)

    Initialize general software structures (struct igc_adapter)

    :param adapter:
        board private structure to initialize
    :type adapter: struct igc_adapter \*

.. _`igc_sw_init.description`:

Description
-----------

igc_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`igc_get_hw_dev`:

igc_get_hw_dev
==============

.. c:function:: struct net_device *igc_get_hw_dev(struct igc_hw *hw)

    return device

    :param hw:
        pointer to hardware structure
    :type hw: struct igc_hw \*

.. _`igc_get_hw_dev.description`:

Description
-----------

used by hardware layer to print debugging information

.. _`igc_init_module`:

igc_init_module
===============

.. c:function:: int igc_init_module( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`igc_init_module.description`:

Description
-----------

igc_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`igc_exit_module`:

igc_exit_module
===============

.. c:function:: void __exit igc_exit_module( void)

    Driver Exit Cleanup Routine

    :param void:
        no arguments
    :type void: 

.. _`igc_exit_module.description`:

Description
-----------

igc_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.

