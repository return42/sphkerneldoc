.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igbvf/netdev.c

.. _`igbvf_desc_unused`:

igbvf_desc_unused
=================

.. c:function:: int igbvf_desc_unused(struct igbvf_ring *ring)

    calculate if we have unused descriptors

    :param ring:
        *undescribed*
    :type ring: struct igbvf_ring \*

.. _`igbvf_receive_skb`:

igbvf_receive_skb
=================

.. c:function:: void igbvf_receive_skb(struct igbvf_adapter *adapter, struct net_device *netdev, struct sk_buff *skb, u32 status, u16 vlan)

    helper function to handle Rx indications

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param skb:
        pointer to sk_buff to be indicated to stack
    :type skb: struct sk_buff \*

    :param status:
        descriptor status field as written by hardware
    :type status: u32

    :param vlan:
        descriptor vlan field as written by hardware (no le/be conversion)
    :type vlan: u16

.. _`igbvf_alloc_rx_buffers`:

igbvf_alloc_rx_buffers
======================

.. c:function:: void igbvf_alloc_rx_buffers(struct igbvf_ring *rx_ring, int cleaned_count)

    Replace used receive buffers; packet split

    :param rx_ring:
        address of ring structure to repopulate
    :type rx_ring: struct igbvf_ring \*

    :param cleaned_count:
        number of buffers to repopulate
    :type cleaned_count: int

.. _`igbvf_clean_rx_irq`:

igbvf_clean_rx_irq
==================

.. c:function:: bool igbvf_clean_rx_irq(struct igbvf_adapter *adapter, int *work_done, int work_to_do)

    Send received data up the network stack; legacy

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

    :param work_done:
        *undescribed*
    :type work_done: int \*

    :param work_to_do:
        *undescribed*
    :type work_to_do: int

.. _`igbvf_clean_rx_irq.description`:

Description
-----------

the return value indicates whether actual cleaning was done, there
is no guarantee that everything was cleaned

.. _`igbvf_setup_tx_resources`:

igbvf_setup_tx_resources
========================

.. c:function:: int igbvf_setup_tx_resources(struct igbvf_adapter *adapter, struct igbvf_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

    :param tx_ring:
        *undescribed*
    :type tx_ring: struct igbvf_ring \*

.. _`igbvf_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igbvf_setup_rx_resources`:

igbvf_setup_rx_resources
========================

.. c:function:: int igbvf_setup_rx_resources(struct igbvf_adapter *adapter, struct igbvf_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

    :param rx_ring:
        *undescribed*
    :type rx_ring: struct igbvf_ring \*

.. _`igbvf_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igbvf_clean_tx_ring`:

igbvf_clean_tx_ring
===================

.. c:function:: void igbvf_clean_tx_ring(struct igbvf_ring *tx_ring)

    Free Tx Buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct igbvf_ring \*

.. _`igbvf_free_tx_resources`:

igbvf_free_tx_resources
=======================

.. c:function:: void igbvf_free_tx_resources(struct igbvf_ring *tx_ring)

    Free Tx Resources per Queue

    :param tx_ring:
        ring to free resources from
    :type tx_ring: struct igbvf_ring \*

.. _`igbvf_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`igbvf_clean_rx_ring`:

igbvf_clean_rx_ring
===================

.. c:function:: void igbvf_clean_rx_ring(struct igbvf_ring *rx_ring)

    Free Rx Buffers per Queue

    :param rx_ring:
        *undescribed*
    :type rx_ring: struct igbvf_ring \*

.. _`igbvf_free_rx_resources`:

igbvf_free_rx_resources
=======================

.. c:function:: void igbvf_free_rx_resources(struct igbvf_ring *rx_ring)

    Free Rx Resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct igbvf_ring \*

.. _`igbvf_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`igbvf_update_itr`:

igbvf_update_itr
================

.. c:function:: enum latency_range igbvf_update_itr(struct igbvf_adapter *adapter, enum latency_range itr_setting, int packets, int bytes)

    update the dynamic ITR value based on statistics

    :param adapter:
        pointer to adapter
    :type adapter: struct igbvf_adapter \*

    :param itr_setting:
        current adapter->itr
    :type itr_setting: enum latency_range

    :param packets:
        the number of packets during this measurement interval
    :type packets: int

    :param bytes:
        the number of bytes during this measurement interval
    :type bytes: int

.. _`igbvf_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte counts during the last
interrupt.  The advantage of per interrupt computation is faster updates
and more accurate ITR for the current traffic pattern.  Constants in this
function were computed based on theoretical maximum wire speed and thresholds
were set based on testing data as well as attempting to minimize response
time while increasing bulk throughput.

.. _`igbvf_clean_tx_irq`:

igbvf_clean_tx_irq
==================

.. c:function:: bool igbvf_clean_tx_irq(struct igbvf_ring *tx_ring)

    Reclaim resources after transmit completes

    :param tx_ring:
        *undescribed*
    :type tx_ring: struct igbvf_ring \*

.. _`igbvf_clean_tx_irq.description`:

Description
-----------

returns true if ring is completely cleaned

.. _`igbvf_configure_msix`:

igbvf_configure_msix
====================

.. c:function:: void igbvf_configure_msix(struct igbvf_adapter *adapter)

    Configure MSI-X hardware

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_configure_msix.description`:

Description
-----------

igbvf_configure_msix sets up the hardware to properly
generate MSI-X interrupts.

.. _`igbvf_set_interrupt_capability`:

igbvf_set_interrupt_capability
==============================

.. c:function:: void igbvf_set_interrupt_capability(struct igbvf_adapter *adapter)

    set MSI or MSI-X if supported

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_set_interrupt_capability.description`:

Description
-----------

Attempt to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`igbvf_request_msix`:

igbvf_request_msix
==================

.. c:function:: int igbvf_request_msix(struct igbvf_adapter *adapter)

    Initialize MSI-X interrupts

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_request_msix.description`:

Description
-----------

igbvf_request_msix allocates MSI-X vectors and requests interrupts from the
kernel.

.. _`igbvf_alloc_queues`:

igbvf_alloc_queues
==================

.. c:function:: int igbvf_alloc_queues(struct igbvf_adapter *adapter)

    Allocate memory for all rings

    :param adapter:
        board private structure to initialize
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_request_irq`:

igbvf_request_irq
=================

.. c:function:: int igbvf_request_irq(struct igbvf_adapter *adapter)

    initialize interrupts

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`igbvf_irq_disable`:

igbvf_irq_disable
=================

.. c:function:: void igbvf_irq_disable(struct igbvf_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_irq_enable`:

igbvf_irq_enable
================

.. c:function:: void igbvf_irq_enable(struct igbvf_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_poll`:

igbvf_poll
==========

.. c:function:: int igbvf_poll(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param napi:
        struct associated with this polling callback
    :type napi: struct napi_struct \*

    :param budget:
        amount of packets driver is allowed to process this poll
    :type budget: int

.. _`igbvf_set_rlpml`:

igbvf_set_rlpml
===============

.. c:function:: void igbvf_set_rlpml(struct igbvf_adapter *adapter)

    set receive large packet maximum length

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_set_rlpml.description`:

Description
-----------

Configure the maximum size of packets that will be received

.. _`igbvf_configure_tx`:

igbvf_configure_tx
==================

.. c:function:: void igbvf_configure_tx(struct igbvf_adapter *adapter)

    Configure Transmit Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`igbvf_setup_srrctl`:

igbvf_setup_srrctl
==================

.. c:function:: void igbvf_setup_srrctl(struct igbvf_adapter *adapter)

    configure the receive control registers

    :param adapter:
        Board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_configure_rx`:

igbvf_configure_rx
==================

.. c:function:: void igbvf_configure_rx(struct igbvf_adapter *adapter)

    Configure Receive Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`igbvf_set_multi`:

igbvf_set_multi
===============

.. c:function:: void igbvf_set_multi(struct net_device *netdev)

    Multicast and Promiscuous mode set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igbvf_set_multi.description`:

Description
-----------

The set_multi entry point is called whenever the multicast address
list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper multicast,
promiscuous mode, and all-multi behavior.

.. _`igbvf_set_uni`:

igbvf_set_uni
=============

.. c:function:: int igbvf_set_uni(struct net_device *netdev)

    Configure unicast MAC filters

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igbvf_set_uni.description`:

Description
-----------

This routine is responsible for configuring the hardware for proper
unicast filters.

.. _`igbvf_configure`:

igbvf_configure
===============

.. c:function:: void igbvf_configure(struct igbvf_adapter *adapter)

    configure the hardware for Rx and Tx

    :param adapter:
        private board structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_sw_init`:

igbvf_sw_init
=============

.. c:function:: int igbvf_sw_init(struct igbvf_adapter *adapter)

    Initialize general software structures (struct igbvf_adapter)

    :param adapter:
        board private structure to initialize
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_sw_init.description`:

Description
-----------

igbvf_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`igbvf_open`:

igbvf_open
==========

.. c:function:: int igbvf_open(struct net_device *netdev)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igbvf_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`igbvf_close`:

igbvf_close
===========

.. c:function:: int igbvf_close(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igbvf_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`igbvf_set_mac`:

igbvf_set_mac
=============

.. c:function:: int igbvf_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`igbvf_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igbvf_update_stats`:

igbvf_update_stats
==================

.. c:function:: void igbvf_update_stats(struct igbvf_adapter *adapter)

    Update the board statistics counters

    :param adapter:
        board private structure
    :type adapter: struct igbvf_adapter \*

.. _`igbvf_watchdog`:

igbvf_watchdog
==============

.. c:function:: void igbvf_watchdog(struct timer_list *t)

    Timer Call-back

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`igbvf_tx_timeout`:

igbvf_tx_timeout
================

.. c:function:: void igbvf_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igbvf_change_mtu`:

igbvf_change_mtu
================

.. c:function:: int igbvf_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`igbvf_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igbvf_io_error_detected`:

igbvf_io_error_detected
=======================

.. c:function:: pci_ers_result_t igbvf_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

.. _`igbvf_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`igbvf_io_slot_reset`:

igbvf_io_slot_reset
===================

.. c:function:: pci_ers_result_t igbvf_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`igbvf_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot. Implementation
resembles the first-half of the igbvf_resume routine.

.. _`igbvf_io_resume`:

igbvf_io_resume
===============

.. c:function:: void igbvf_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`igbvf_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation. Implementation resembles the
second-half of the igbvf_resume routine.

.. _`igbvf_probe`:

igbvf_probe
===========

.. c:function:: int igbvf_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in igbvf_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`igbvf_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

igbvf_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`igbvf_remove`:

igbvf_remove
============

.. c:function:: void igbvf_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`igbvf_remove.description`:

Description
-----------

igbvf_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`igbvf_init_module`:

igbvf_init_module
=================

.. c:function:: int igbvf_init_module( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`igbvf_init_module.description`:

Description
-----------

igbvf_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`igbvf_exit_module`:

igbvf_exit_module
=================

.. c:function:: void __exit igbvf_exit_module( void)

    Driver Exit Cleanup Routine

    :param void:
        no arguments
    :type void: 

.. _`igbvf_exit_module.description`:

Description
-----------

igbvf_exit_module is called just before the driver is removed
from memory.

.. This file was automatic generated / don't edit.

