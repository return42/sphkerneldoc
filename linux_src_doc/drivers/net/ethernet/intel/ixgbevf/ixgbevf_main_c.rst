.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbevf/ixgbevf_main.c

.. _`ixgbevf_set_ivar`:

ixgbevf_set_ivar
================

.. c:function:: void ixgbevf_set_ivar(struct ixgbevf_adapter *adapter, s8 direction, u8 queue, u8 msix_vector)

    set IVAR registers - maps interrupt causes to vectors

    :param adapter:
        pointer to adapter struct
    :type adapter: struct ixgbevf_adapter \*

    :param direction:
        0 for Rx, 1 for Tx, -1 for other causes
    :type direction: s8

    :param queue:
        queue to map the corresponding interrupt to
    :type queue: u8

    :param msix_vector:
        the vector to map to the corresponding queue
    :type msix_vector: u8

.. _`ixgbevf_tx_timeout`:

ixgbevf_tx_timeout
==================

.. c:function:: void ixgbevf_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ixgbevf_clean_tx_irq`:

ixgbevf_clean_tx_irq
====================

.. c:function:: bool ixgbevf_clean_tx_irq(struct ixgbevf_q_vector *q_vector, struct ixgbevf_ring *tx_ring, int napi_budget)

    Reclaim resources after transmit completes

    :param q_vector:
        board private structure
    :type q_vector: struct ixgbevf_q_vector \*

    :param tx_ring:
        tx ring to clean
    :type tx_ring: struct ixgbevf_ring \*

    :param napi_budget:
        Used to determine if we are in netpoll
    :type napi_budget: int

.. _`ixgbevf_rx_skb`:

ixgbevf_rx_skb
==============

.. c:function:: void ixgbevf_rx_skb(struct ixgbevf_q_vector *q_vector, struct sk_buff *skb)

    Helper function to determine proper Rx method

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct ixgbevf_q_vector \*

    :param skb:
        packet to send up
    :type skb: struct sk_buff \*

.. _`ixgbevf_rx_checksum`:

ixgbevf_rx_checksum
===================

.. c:function:: void ixgbevf_rx_checksum(struct ixgbevf_ring *ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    indicate in skb if hw indicated a good cksum

    :param ring:
        structure containig ring specific data
    :type ring: struct ixgbevf_ring \*

    :param rx_desc:
        current Rx descriptor being processed
    :type rx_desc: union ixgbe_adv_rx_desc \*

    :param skb:
        skb currently being received and modified
    :type skb: struct sk_buff \*

.. _`ixgbevf_process_skb_fields`:

ixgbevf_process_skb_fields
==========================

.. c:function:: void ixgbevf_process_skb_fields(struct ixgbevf_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Populate skb header fields from Rx descriptor

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct ixgbevf_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union ixgbe_adv_rx_desc \*

    :param skb:
        pointer to current skb being populated
    :type skb: struct sk_buff \*

.. _`ixgbevf_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the checksum, VLAN, protocol, and other fields within
the skb.

.. _`ixgbevf_is_non_eop`:

ixgbevf_is_non_eop
==================

.. c:function:: bool ixgbevf_is_non_eop(struct ixgbevf_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc)

    process handling of non-EOP buffers

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct ixgbevf_ring \*

    :param rx_desc:
        Rx descriptor for current buffer
    :type rx_desc: union ixgbe_adv_rx_desc \*

.. _`ixgbevf_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`ixgbevf_alloc_rx_buffers`:

ixgbevf_alloc_rx_buffers
========================

.. c:function:: void ixgbevf_alloc_rx_buffers(struct ixgbevf_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers; packet split

    :param rx_ring:
        rx descriptor ring (for a specific queue) to setup buffers on
    :type rx_ring: struct ixgbevf_ring \*

    :param cleaned_count:
        number of buffers to replace
    :type cleaned_count: u16

.. _`ixgbevf_cleanup_headers`:

ixgbevf_cleanup_headers
=======================

.. c:function:: bool ixgbevf_cleanup_headers(struct ixgbevf_ring *rx_ring, union ixgbe_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Correct corrupted or empty headers

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct ixgbevf_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union ixgbe_adv_rx_desc \*

    :param skb:
        pointer to current skb being fixed
    :type skb: struct sk_buff \*

.. _`ixgbevf_cleanup_headers.description`:

Description
-----------

Check for corrupted packet headers caused by senders on the local L2
embedded NIC switch not setting up their Tx Descriptors right.  These
should be very rare.

Also address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`ixgbevf_reuse_rx_page`:

ixgbevf_reuse_rx_page
=====================

.. c:function:: void ixgbevf_reuse_rx_page(struct ixgbevf_ring *rx_ring, struct ixgbevf_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param rx_ring:
        rx descriptor ring to store buffers on
    :type rx_ring: struct ixgbevf_ring \*

    :param old_buff:
        donor buffer to have page reused
    :type old_buff: struct ixgbevf_rx_buffer \*

.. _`ixgbevf_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`ixgbevf_add_rx_frag`:

ixgbevf_add_rx_frag
===================

.. c:function:: void ixgbevf_add_rx_frag(struct ixgbevf_ring *rx_ring, struct ixgbevf_rx_buffer *rx_buffer, struct sk_buff *skb, unsigned int size)

    Add contents of Rx buffer to sk_buff

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct ixgbevf_ring \*

    :param rx_buffer:
        buffer containing page to add
    :type rx_buffer: struct ixgbevf_rx_buffer \*

    :param skb:
        sk_buff to place the data into
    :type skb: struct sk_buff \*

    :param size:
        size of buffer to be added
    :type size: unsigned int

.. _`ixgbevf_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.

.. _`ixgbevf_poll`:

ixgbevf_poll
============

.. c:function:: int ixgbevf_poll(struct napi_struct *napi, int budget)

    NAPI polling calback

    :param napi:
        napi struct with our devices info in it
    :type napi: struct napi_struct \*

    :param budget:
        amount of work driver is allowed to do this pass, in packets
    :type budget: int

.. _`ixgbevf_poll.description`:

Description
-----------

This function will clean more than one or more rings associated with a
q_vector.

.. _`ixgbevf_write_eitr`:

ixgbevf_write_eitr
==================

.. c:function:: void ixgbevf_write_eitr(struct ixgbevf_q_vector *q_vector)

    write VTEITR register in hardware specific way

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct ixgbevf_q_vector \*

.. _`ixgbevf_configure_msix`:

ixgbevf_configure_msix
======================

.. c:function:: void ixgbevf_configure_msix(struct ixgbevf_adapter *adapter)

    Configure MSI-X hardware

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_configure_msix.description`:

Description
-----------

ixgbevf_configure_msix sets up the hardware to properly generate MSI-X
interrupts.

.. _`ixgbevf_update_itr`:

ixgbevf_update_itr
==================

.. c:function:: void ixgbevf_update_itr(struct ixgbevf_q_vector *q_vector, struct ixgbevf_ring_container *ring_container)

    update the dynamic ITR value based on statistics

    :param q_vector:
        structure containing interrupt and ring information
    :type q_vector: struct ixgbevf_q_vector \*

    :param ring_container:
        structure containing ring performance data
    :type ring_container: struct ixgbevf_ring_container \*

.. _`ixgbevf_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.

.. _`ixgbevf_msix_clean_rings`:

ixgbevf_msix_clean_rings
========================

.. c:function:: irqreturn_t ixgbevf_msix_clean_rings(int irq, void *data)

    single unshared vector rx clean (all queues)

    :param irq:
        unused
    :type irq: int

    :param data:
        pointer to our q_vector struct for this interrupt vector
    :type data: void \*

.. _`ixgbevf_request_msix_irqs`:

ixgbevf_request_msix_irqs
=========================

.. c:function:: int ixgbevf_request_msix_irqs(struct ixgbevf_adapter *adapter)

    Initialize MSI-X interrupts

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_request_msix_irqs.description`:

Description
-----------

ixgbevf_request_msix_irqs allocates MSI-X vectors and requests
interrupts from the kernel.

.. _`ixgbevf_request_irq`:

ixgbevf_request_irq
===================

.. c:function:: int ixgbevf_request_irq(struct ixgbevf_adapter *adapter)

    initialize interrupts

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`ixgbevf_irq_disable`:

ixgbevf_irq_disable
===================

.. c:function:: void ixgbevf_irq_disable(struct ixgbevf_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_irq_enable`:

ixgbevf_irq_enable
==================

.. c:function:: void ixgbevf_irq_enable(struct ixgbevf_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_configure_tx_ring`:

ixgbevf_configure_tx_ring
=========================

.. c:function:: void ixgbevf_configure_tx_ring(struct ixgbevf_adapter *adapter, struct ixgbevf_ring *ring)

    Configure 82599 VF Tx ring after Reset

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

    :param ring:
        structure containing ring specific data
    :type ring: struct ixgbevf_ring \*

.. _`ixgbevf_configure_tx_ring.description`:

Description
-----------

Configure the Tx descriptor ring after a reset.

.. _`ixgbevf_configure_tx`:

ixgbevf_configure_tx
====================

.. c:function:: void ixgbevf_configure_tx(struct ixgbevf_adapter *adapter)

    Configure 82599 VF Transmit Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`ixgbevf_init_rss_key`:

ixgbevf_init_rss_key
====================

.. c:function:: int ixgbevf_init_rss_key(struct ixgbevf_adapter *adapter)

    Initialize adapter RSS key

    :param adapter:
        device handle
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_init_rss_key.description`:

Description
-----------

Allocates and initializes the RSS key if it is not allocated.

.. _`ixgbevf_configure_rx`:

ixgbevf_configure_rx
====================

.. c:function:: void ixgbevf_configure_rx(struct ixgbevf_adapter *adapter)

    Configure 82599 VF Receive Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`ixgbevf_set_rx_mode`:

ixgbevf_set_rx_mode
===================

.. c:function:: void ixgbevf_set_rx_mode(struct net_device *netdev)

    Multicast and unicast set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ixgbevf_set_rx_mode.description`:

Description
-----------

The set_rx_method entry point is called whenever the multicast address
list, unicast address list or the network interface flags are updated.
This routine is responsible for configuring the hardware for proper
multicast mode and configuring requested unicast filters.

.. _`ixgbevf_clean_rx_ring`:

ixgbevf_clean_rx_ring
=====================

.. c:function:: void ixgbevf_clean_rx_ring(struct ixgbevf_ring *rx_ring)

    Free Rx Buffers per Queue

    :param rx_ring:
        ring to free buffers from
    :type rx_ring: struct ixgbevf_ring \*

.. _`ixgbevf_clean_tx_ring`:

ixgbevf_clean_tx_ring
=====================

.. c:function:: void ixgbevf_clean_tx_ring(struct ixgbevf_ring *tx_ring)

    Free Tx Buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct ixgbevf_ring \*

.. _`ixgbevf_clean_all_rx_rings`:

ixgbevf_clean_all_rx_rings
==========================

.. c:function:: void ixgbevf_clean_all_rx_rings(struct ixgbevf_adapter *adapter)

    Free Rx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_clean_all_tx_rings`:

ixgbevf_clean_all_tx_rings
==========================

.. c:function:: void ixgbevf_clean_all_tx_rings(struct ixgbevf_adapter *adapter)

    Free Tx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_set_num_queues`:

ixgbevf_set_num_queues
======================

.. c:function:: void ixgbevf_set_num_queues(struct ixgbevf_adapter *adapter)

    Allocate queues for device, feature dependent

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_set_num_queues.description`:

Description
-----------

This is the top level queue allocation routine.  The order here is very
important, starting with the "most" number of features turned on at once,
and ending with the smallest set of features.  This way large combinations
can be allocated if they're turned on, and smaller combinations are the
fallthrough conditions.

.. _`ixgbevf_set_interrupt_capability`:

ixgbevf_set_interrupt_capability
================================

.. c:function:: int ixgbevf_set_interrupt_capability(struct ixgbevf_adapter *adapter)

    set MSI-X or FAIL if not supported

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_set_interrupt_capability.description`:

Description
-----------

Attempt to configure the interrupts using the best available
capabilities of the hardware and the kernel.

.. _`ixgbevf_alloc_q_vector`:

ixgbevf_alloc_q_vector
======================

.. c:function:: int ixgbevf_alloc_q_vector(struct ixgbevf_adapter *adapter, int v_idx, int txr_count, int txr_idx, int xdp_count, int xdp_idx, int rxr_count, int rxr_idx)

    Allocate memory for a single interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

    :param v_idx:
        index of vector in adapter struct
    :type v_idx: int

    :param txr_count:
        number of Tx rings for q vector
    :type txr_count: int

    :param txr_idx:
        index of first Tx ring to assign
    :type txr_idx: int

    :param xdp_count:
        total number of XDP rings to allocate
    :type xdp_count: int

    :param xdp_idx:
        index of first XDP ring to allocate
    :type xdp_idx: int

    :param rxr_count:
        number of Rx rings for q vector
    :type rxr_count: int

    :param rxr_idx:
        index of first Rx ring to assign
    :type rxr_idx: int

.. _`ixgbevf_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`ixgbevf_free_q_vector`:

ixgbevf_free_q_vector
=====================

.. c:function:: void ixgbevf_free_q_vector(struct ixgbevf_adapter *adapter, int v_idx)

    Free memory allocated for specific interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

    :param v_idx:
        index of vector in adapter struct
    :type v_idx: int

.. _`ixgbevf_free_q_vector.description`:

Description
-----------

This function frees the memory allocated to the q_vector.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`ixgbevf_alloc_q_vectors`:

ixgbevf_alloc_q_vectors
=======================

.. c:function:: int ixgbevf_alloc_q_vectors(struct ixgbevf_adapter *adapter)

    Allocate memory for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`ixgbevf_free_q_vectors`:

ixgbevf_free_q_vectors
======================

.. c:function:: void ixgbevf_free_q_vectors(struct ixgbevf_adapter *adapter)

    Free memory allocated for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`ixgbevf_reset_interrupt_capability`:

ixgbevf_reset_interrupt_capability
==================================

.. c:function:: void ixgbevf_reset_interrupt_capability(struct ixgbevf_adapter *adapter)

    Reset MSIX setup

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_init_interrupt_scheme`:

ixgbevf_init_interrupt_scheme
=============================

.. c:function:: int ixgbevf_init_interrupt_scheme(struct ixgbevf_adapter *adapter)

    Determine if MSIX is supported and init

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_clear_interrupt_scheme`:

ixgbevf_clear_interrupt_scheme
==============================

.. c:function:: void ixgbevf_clear_interrupt_scheme(struct ixgbevf_adapter *adapter)

    Clear the current interrupt scheme settings

    :param adapter:
        board private structure to clear interrupt scheme on
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_clear_interrupt_scheme.description`:

Description
-----------

We go through and clear interrupt specific resources and reset the structure
to pre-load conditions

.. _`ixgbevf_sw_init`:

ixgbevf_sw_init
===============

.. c:function:: int ixgbevf_sw_init(struct ixgbevf_adapter *adapter)

    Initialize general software structures

    :param adapter:
        board private structure to initialize
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_sw_init.description`:

Description
-----------

ixgbevf_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`ixgbevf_update_stats`:

ixgbevf_update_stats
====================

.. c:function:: void ixgbevf_update_stats(struct ixgbevf_adapter *adapter)

    Update the board statistics counters.

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_service_timer`:

ixgbevf_service_timer
=====================

.. c:function:: void ixgbevf_service_timer(struct timer_list *t)

    Timer Call-back

    :param t:
        pointer to timer_list struct
    :type t: struct timer_list \*

.. _`ixgbevf_check_hang_subtask`:

ixgbevf_check_hang_subtask
==========================

.. c:function:: void ixgbevf_check_hang_subtask(struct ixgbevf_adapter *adapter)

    check for hung queues and dropped interrupts

    :param adapter:
        pointer to the device adapter structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_check_hang_subtask.description`:

Description
-----------

This function serves two purposes.  First it strobes the interrupt lines
in order to make certain interrupts are occurring.  Secondly it sets the
bits needed to check for TX hangs.  As a result we should immediately
determine if a hang has occurred.

.. _`ixgbevf_watchdog_update_link`:

ixgbevf_watchdog_update_link
============================

.. c:function:: void ixgbevf_watchdog_update_link(struct ixgbevf_adapter *adapter)

    update the link status

    :param adapter:
        pointer to the device adapter structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_watchdog_link_is_up`:

ixgbevf_watchdog_link_is_up
===========================

.. c:function:: void ixgbevf_watchdog_link_is_up(struct ixgbevf_adapter *adapter)

    update netif_carrier status and print link up message

    :param adapter:
        pointer to the device adapter structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_watchdog_link_is_down`:

ixgbevf_watchdog_link_is_down
=============================

.. c:function:: void ixgbevf_watchdog_link_is_down(struct ixgbevf_adapter *adapter)

    update netif_carrier status and print link down message

    :param adapter:
        pointer to the adapter structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_watchdog_subtask`:

ixgbevf_watchdog_subtask
========================

.. c:function:: void ixgbevf_watchdog_subtask(struct ixgbevf_adapter *adapter)

    worker thread to bring link up

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_service_task`:

ixgbevf_service_task
====================

.. c:function:: void ixgbevf_service_task(struct work_struct *work)

    manages and runs subtasks

    :param work:
        pointer to work_struct containing our data
    :type work: struct work_struct \*

.. _`ixgbevf_free_tx_resources`:

ixgbevf_free_tx_resources
=========================

.. c:function:: void ixgbevf_free_tx_resources(struct ixgbevf_ring *tx_ring)

    Free Tx Resources per Queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct ixgbevf_ring \*

.. _`ixgbevf_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`ixgbevf_free_all_tx_resources`:

ixgbevf_free_all_tx_resources
=============================

.. c:function:: void ixgbevf_free_all_tx_resources(struct ixgbevf_adapter *adapter)

    Free Tx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`ixgbevf_setup_tx_resources`:

ixgbevf_setup_tx_resources
==========================

.. c:function:: int ixgbevf_setup_tx_resources(struct ixgbevf_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param tx_ring:
        Tx descriptor ring (for a specific queue) to setup
    :type tx_ring: struct ixgbevf_ring \*

.. _`ixgbevf_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ixgbevf_setup_all_tx_resources`:

ixgbevf_setup_all_tx_resources
==============================

.. c:function:: int ixgbevf_setup_all_tx_resources(struct ixgbevf_adapter *adapter)

    allocate all queues Tx resources

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_setup_all_tx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`ixgbevf_setup_rx_resources`:

ixgbevf_setup_rx_resources
==========================

.. c:function:: int ixgbevf_setup_rx_resources(struct ixgbevf_adapter *adapter, struct ixgbevf_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

    :param rx_ring:
        Rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct ixgbevf_ring \*

.. _`ixgbevf_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbevf_setup_all_rx_resources`:

ixgbevf_setup_all_rx_resources
==============================

.. c:function:: int ixgbevf_setup_all_rx_resources(struct ixgbevf_adapter *adapter)

    allocate all queues Rx resources

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_setup_all_rx_resources.description`:

Description
-----------

If this function returns with an error, then it's possible one or
more of the rings is populated (while the rest are not).  It is the
callers duty to clean those orphaned rings.

Return 0 on success, negative on failure

.. _`ixgbevf_free_rx_resources`:

ixgbevf_free_rx_resources
=========================

.. c:function:: void ixgbevf_free_rx_resources(struct ixgbevf_ring *rx_ring)

    Free Rx Resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct ixgbevf_ring \*

.. _`ixgbevf_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`ixgbevf_free_all_rx_resources`:

ixgbevf_free_all_rx_resources
=============================

.. c:function:: void ixgbevf_free_all_rx_resources(struct ixgbevf_adapter *adapter)

    Free Rx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`ixgbevf_open`:

ixgbevf_open
============

.. c:function:: int ixgbevf_open(struct net_device *netdev)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ixgbevf_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`ixgbevf_close_suspend`:

ixgbevf_close_suspend
=====================

.. c:function:: void ixgbevf_close_suspend(struct ixgbevf_adapter *adapter)

    actions necessary to both suspend and close flows

    :param adapter:
        the private adapter struct
    :type adapter: struct ixgbevf_adapter \*

.. _`ixgbevf_close_suspend.description`:

Description
-----------

This function should contain the necessary work common to both suspending
and closing of the device.

.. _`ixgbevf_close`:

ixgbevf_close
=============

.. c:function:: int ixgbevf_close(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`ixgbevf_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`ixgbevf_set_mac`:

ixgbevf_set_mac
===============

.. c:function:: int ixgbevf_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`ixgbevf_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbevf_change_mtu`:

ixgbevf_change_mtu
==================

.. c:function:: int ixgbevf_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`ixgbevf_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgbevf_probe`:

ixgbevf_probe
=============

.. c:function:: int ixgbevf_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in ixgbevf_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`ixgbevf_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

ixgbevf_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`ixgbevf_remove`:

ixgbevf_remove
==============

.. c:function:: void ixgbevf_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`ixgbevf_remove.description`:

Description
-----------

ixgbevf_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`ixgbevf_io_error_detected`:

ixgbevf_io_error_detected
=========================

.. c:function:: pci_ers_result_t ixgbevf_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

.. _`ixgbevf_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`ixgbevf_io_slot_reset`:

ixgbevf_io_slot_reset
=====================

.. c:function:: pci_ers_result_t ixgbevf_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`ixgbevf_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot. Implementation
resembles the first-half of the ixgbevf_resume routine.

.. _`ixgbevf_io_resume`:

ixgbevf_io_resume
=================

.. c:function:: void ixgbevf_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`ixgbevf_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation. Implementation resembles the
second-half of the ixgbevf_resume routine.

.. _`ixgbevf_init_module`:

ixgbevf_init_module
===================

.. c:function:: int ixgbevf_init_module( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`ixgbevf_init_module.description`:

Description
-----------

ixgbevf_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`ixgbevf_exit_module`:

ixgbevf_exit_module
===================

.. c:function:: void __exit ixgbevf_exit_module( void)

    Driver Exit Cleanup Routine

    :param void:
        no arguments
    :type void: 

.. _`ixgbevf_exit_module.description`:

Description
-----------

ixgbevf_exit_module is called just before the driver is removed
from memory.

.. _`ixgbevf_get_hw_dev_name`:

ixgbevf_get_hw_dev_name
=======================

.. c:function:: char *ixgbevf_get_hw_dev_name(struct ixgbe_hw *hw)

    return device name string used by hardware layer to print debugging information

    :param hw:
        pointer to private hardware struct
    :type hw: struct ixgbe_hw \*

.. This file was automatic generated / don't edit.

