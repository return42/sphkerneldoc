.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000/e1000_main.c

.. _`e1000_get_hw_dev`:

e1000_get_hw_dev
================

.. c:function:: struct net_device *e1000_get_hw_dev(struct e1000_hw *hw)

    return device used by hardware layer to print debugging information

    :param hw:
        *undescribed*
    :type hw: struct e1000_hw \*

.. _`e1000_init_module`:

e1000_init_module
=================

.. c:function:: int e1000_init_module( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`e1000_init_module.description`:

Description
-----------

e1000_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`e1000_exit_module`:

e1000_exit_module
=================

.. c:function:: void __exit e1000_exit_module( void)

    Driver Exit Cleanup Routine

    :param void:
        no arguments
    :type void: 

.. _`e1000_exit_module.description`:

Description
-----------

e1000_exit_module is called just before the driver is removed
from memory.

.. _`e1000_irq_disable`:

e1000_irq_disable
=================

.. c:function:: void e1000_irq_disable(struct e1000_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_irq_enable`:

e1000_irq_enable
================

.. c:function:: void e1000_irq_enable(struct e1000_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_configure`:

e1000_configure
===============

.. c:function:: void e1000_configure(struct e1000_adapter *adapter)

    configure the hardware for RX and TX \ ``adapter``\  = private board structure

    :param adapter:
        *undescribed*
    :type adapter: struct e1000_adapter \*

.. _`e1000_power_up_phy`:

e1000_power_up_phy
==================

.. c:function:: void e1000_power_up_phy(struct e1000_adapter *adapter)

    restore link in case the phy was powered down

    :param adapter:
        address of board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_power_up_phy.description`:

Description
-----------

The phy may be powered down to save power and turn off link when the
driver is unloaded and wake on lan is not enabled (among others)
\*\*\* this routine MUST be followed by a call to e1000_reset \*\*\*

.. _`e1000_is_need_ioport`:

e1000_is_need_ioport
====================

.. c:function:: int e1000_is_need_ioport(struct pci_dev *pdev)

    determine if an adapter needs ioport resources or not

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`e1000_is_need_ioport.description`:

Description
-----------

Return true if an adapter needs ioport resources

.. _`e1000_init_hw_struct`:

e1000_init_hw_struct
====================

.. c:function:: int e1000_init_hw_struct(struct e1000_adapter *adapter, struct e1000_hw *hw)

    initialize members of hw struct

    :param adapter:
        board private struct
    :type adapter: struct e1000_adapter \*

    :param hw:
        structure used by e1000_hw.c
    :type hw: struct e1000_hw \*

.. _`e1000_init_hw_struct.description`:

Description
-----------

Factors out initialization of the e1000_hw struct to its own function
that can be called very early at init (just after struct allocation).
Fields are initialized based on PCI device information and
OS network device settings (MTU size).
Returns negative error codes if MAC type setup fails.

.. _`e1000_probe`:

e1000_probe
===========

.. c:function:: int e1000_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in e1000_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`e1000_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

e1000_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`e1000_remove`:

e1000_remove
============

.. c:function:: void e1000_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`e1000_remove.description`:

Description
-----------

e1000_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device. That could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`e1000_sw_init`:

e1000_sw_init
=============

.. c:function:: int e1000_sw_init(struct e1000_adapter *adapter)

    Initialize general software structures (struct e1000_adapter)

    :param adapter:
        board private structure to initialize
    :type adapter: struct e1000_adapter \*

.. _`e1000_sw_init.description`:

Description
-----------

e1000_sw_init initializes the Adapter private data structure.
e1000_init_hw_struct MUST be called before this function

.. _`e1000_alloc_queues`:

e1000_alloc_queues
==================

.. c:function:: int e1000_alloc_queues(struct e1000_adapter *adapter)

    Allocate memory for all rings

    :param adapter:
        board private structure to initialize
    :type adapter: struct e1000_adapter \*

.. _`e1000_alloc_queues.description`:

Description
-----------

We allocate one ring per queue at run-time since we don't know the
number of queues at compile-time.

.. _`e1000_open`:

e1000_open
==========

.. c:function:: int e1000_open(struct net_device *netdev)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`e1000_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog task is started,
and the stack is notified that the interface is ready.

.. _`e1000_close`:

e1000_close
===========

.. c:function:: int e1000_close(struct net_device *netdev)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`e1000_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`e1000_check_64k_bound`:

e1000_check_64k_bound
=====================

.. c:function:: bool e1000_check_64k_bound(struct e1000_adapter *adapter, void *start, unsigned long len)

    check that memory doesn't cross 64kB boundary

    :param adapter:
        address of board private structure
    :type adapter: struct e1000_adapter \*

    :param start:
        address of beginning of memory
    :type start: void \*

    :param len:
        length of memory
    :type len: unsigned long

.. _`e1000_setup_tx_resources`:

e1000_setup_tx_resources
========================

.. c:function:: int e1000_setup_tx_resources(struct e1000_adapter *adapter, struct e1000_tx_ring *txdr)

    allocate Tx resources (Descriptors)

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param txdr:
        tx descriptor ring (for a specific queue) to setup
    :type txdr: struct e1000_tx_ring \*

.. _`e1000_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`e1000_setup_all_tx_resources`:

e1000_setup_all_tx_resources
============================

.. c:function:: int e1000_setup_all_tx_resources(struct e1000_adapter *adapter)

    wrapper to allocate Tx resources (Descriptors) for all queues

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_setup_all_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`e1000_configure_tx`:

e1000_configure_tx
==================

.. c:function:: void e1000_configure_tx(struct e1000_adapter *adapter)

    Configure 8254x Transmit Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`e1000_setup_rx_resources`:

e1000_setup_rx_resources
========================

.. c:function:: int e1000_setup_rx_resources(struct e1000_adapter *adapter, struct e1000_rx_ring *rxdr)

    allocate Rx resources (Descriptors)

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param rxdr:
        rx descriptor ring (for a specific queue) to setup
    :type rxdr: struct e1000_rx_ring \*

.. _`e1000_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`e1000_setup_all_rx_resources`:

e1000_setup_all_rx_resources
============================

.. c:function:: int e1000_setup_all_rx_resources(struct e1000_adapter *adapter)

    wrapper to allocate Rx resources (Descriptors) for all queues

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_setup_all_rx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`e1000_setup_rctl`:

e1000_setup_rctl
================

.. c:function:: void e1000_setup_rctl(struct e1000_adapter *adapter)

    configure the receive control registers

    :param adapter:
        Board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_configure_rx`:

e1000_configure_rx
==================

.. c:function:: void e1000_configure_rx(struct e1000_adapter *adapter)

    Configure 8254x Receive Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`e1000_free_tx_resources`:

e1000_free_tx_resources
=======================

.. c:function:: void e1000_free_tx_resources(struct e1000_adapter *adapter, struct e1000_tx_ring *tx_ring)

    Free Tx Resources per Queue

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct e1000_tx_ring \*

.. _`e1000_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`e1000_free_all_tx_resources`:

e1000_free_all_tx_resources
===========================

.. c:function:: void e1000_free_all_tx_resources(struct e1000_adapter *adapter)

    Free Tx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`e1000_clean_tx_ring`:

e1000_clean_tx_ring
===================

.. c:function:: void e1000_clean_tx_ring(struct e1000_adapter *adapter, struct e1000_tx_ring *tx_ring)

    Free Tx Buffers

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct e1000_tx_ring \*

.. _`e1000_clean_all_tx_rings`:

e1000_clean_all_tx_rings
========================

.. c:function:: void e1000_clean_all_tx_rings(struct e1000_adapter *adapter)

    Free Tx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_free_rx_resources`:

e1000_free_rx_resources
=======================

.. c:function:: void e1000_free_rx_resources(struct e1000_adapter *adapter, struct e1000_rx_ring *rx_ring)

    Free Rx Resources

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct e1000_rx_ring \*

.. _`e1000_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`e1000_free_all_rx_resources`:

e1000_free_all_rx_resources
===========================

.. c:function:: void e1000_free_all_rx_resources(struct e1000_adapter *adapter)

    Free Rx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`e1000_clean_rx_ring`:

e1000_clean_rx_ring
===================

.. c:function:: void e1000_clean_rx_ring(struct e1000_adapter *adapter, struct e1000_rx_ring *rx_ring)

    Free Rx Buffers per Queue

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param rx_ring:
        ring to free buffers from
    :type rx_ring: struct e1000_rx_ring \*

.. _`e1000_clean_all_rx_rings`:

e1000_clean_all_rx_rings
========================

.. c:function:: void e1000_clean_all_rx_rings(struct e1000_adapter *adapter)

    Free Rx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_set_mac`:

e1000_set_mac
=============

.. c:function:: int e1000_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`e1000_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`e1000_set_rx_mode`:

e1000_set_rx_mode
=================

.. c:function:: void e1000_set_rx_mode(struct net_device *netdev)

    Secondary Unicast, Multicast and Promiscuous mode set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`e1000_set_rx_mode.description`:

Description
-----------

The set_rx_mode entry point is called whenever the unicast or multicast
address lists or the network interface flags are updated. This routine is
responsible for configuring the hardware for proper unicast, multicast,
promiscuous mode, and all-multi behavior.

.. _`e1000_update_phy_info_task`:

e1000_update_phy_info_task
==========================

.. c:function:: void e1000_update_phy_info_task(struct work_struct *work)

    get phy info

    :param work:
        work struct contained inside adapter struct
    :type work: struct work_struct \*

.. _`e1000_update_phy_info_task.description`:

Description
-----------

Need to wait a few seconds after link up to get diagnostic information from
the phy

.. _`e1000_82547_tx_fifo_stall_task`:

e1000_82547_tx_fifo_stall_task
==============================

.. c:function:: void e1000_82547_tx_fifo_stall_task(struct work_struct *work)

    task to complete work

    :param work:
        work struct contained inside adapter struct
    :type work: struct work_struct \*

.. _`e1000_watchdog`:

e1000_watchdog
==============

.. c:function:: void e1000_watchdog(struct work_struct *work)

    work function

    :param work:
        work struct contained inside adapter struct
    :type work: struct work_struct \*

.. _`e1000_update_itr`:

e1000_update_itr
================

.. c:function:: unsigned int e1000_update_itr(struct e1000_adapter *adapter, u16 itr_setting, int packets, int bytes)

    update the dynamic ITR value based on statistics

    :param adapter:
        pointer to adapter
    :type adapter: struct e1000_adapter \*

    :param itr_setting:
        current adapter->itr
    :type itr_setting: u16

    :param packets:
        the number of packets during this measurement interval
    :type packets: int

    :param bytes:
        the number of bytes during this measurement interval
    :type bytes: int

.. _`e1000_update_itr.description`:

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
parameter (see e1000_param.c)

.. _`e1000_tx_timeout`:

e1000_tx_timeout
================

.. c:function:: void e1000_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`e1000_change_mtu`:

e1000_change_mtu
================

.. c:function:: int e1000_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`e1000_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`e1000_update_stats`:

e1000_update_stats
==================

.. c:function:: void e1000_update_stats(struct e1000_adapter *adapter)

    Update the board statistics counters

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

.. _`e1000_intr`:

e1000_intr
==========

.. c:function:: irqreturn_t e1000_intr(int irq, void *data)

    Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a network interface device structure
    :type data: void \*

.. _`e1000_clean`:

e1000_clean
===========

.. c:function:: int e1000_clean(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param napi:
        *undescribed*
    :type napi: struct napi_struct \*

    :param budget:
        *undescribed*
    :type budget: int

.. _`e1000_clean_tx_irq`:

e1000_clean_tx_irq
==================

.. c:function:: bool e1000_clean_tx_irq(struct e1000_adapter *adapter, struct e1000_tx_ring *tx_ring)

    Reclaim resources after transmit completes

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param tx_ring:
        *undescribed*
    :type tx_ring: struct e1000_tx_ring \*

.. _`e1000_rx_checksum`:

e1000_rx_checksum
=================

.. c:function:: void e1000_rx_checksum(struct e1000_adapter *adapter, u32 status_err, u32 csum, struct sk_buff *skb)

    Receive Checksum Offload for 82543

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param status_err:
        receive descriptor status and error fields
    :type status_err: u32

    :param csum:
        receive descriptor csum field
    :type csum: u32

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

.. _`e1000_consume_page`:

e1000_consume_page
==================

.. c:function:: void e1000_consume_page(struct e1000_rx_buffer *bi, struct sk_buff *skb, u16 length)

    helper function for jumbo Rx path

    :param bi:
        *undescribed*
    :type bi: struct e1000_rx_buffer \*

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param length:
        *undescribed*
    :type length: u16

.. _`e1000_receive_skb`:

e1000_receive_skb
=================

.. c:function:: void e1000_receive_skb(struct e1000_adapter *adapter, u8 status, __le16 vlan, struct sk_buff *skb)

    helper function to handle rx indications

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param status:
        descriptor status field as written by hardware
    :type status: u8

    :param vlan:
        descriptor vlan field as written by hardware (no le/be conversion)
    :type vlan: __le16

    :param skb:
        pointer to sk_buff to be indicated to stack
    :type skb: struct sk_buff \*

.. _`e1000_tbi_adjust_stats`:

e1000_tbi_adjust_stats
======================

.. c:function:: void e1000_tbi_adjust_stats(struct e1000_hw *hw, struct e1000_hw_stats *stats, u32 frame_len, const u8 *mac_addr)

    :param hw:
        Struct containing variables accessed by shared code
    :type hw: struct e1000_hw \*

    :param stats:
        *undescribed*
    :type stats: struct e1000_hw_stats \*

    :param frame_len:
        The length of the frame in question
    :type frame_len: u32

    :param mac_addr:
        The Ethernet destination address of the frame in question
    :type mac_addr: const u8 \*

.. _`e1000_tbi_adjust_stats.description`:

Description
-----------

Adjusts the statistic counters when a frame is accepted by TBI_ACCEPT

.. _`e1000_clean_jumbo_rx_irq`:

e1000_clean_jumbo_rx_irq
========================

.. c:function:: bool e1000_clean_jumbo_rx_irq(struct e1000_adapter *adapter, struct e1000_rx_ring *rx_ring, int *work_done, int work_to_do)

    Send received data up the network stack; legacy

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param rx_ring:
        ring to clean
    :type rx_ring: struct e1000_rx_ring \*

    :param work_done:
        amount of napi work completed this call
    :type work_done: int \*

    :param work_to_do:
        max amount of work allowed for this call to do
    :type work_to_do: int

.. _`e1000_clean_jumbo_rx_irq.description`:

Description
-----------

the return value indicates whether actual cleaning was done, there
is no guarantee that everything was cleaned

.. _`e1000_clean_rx_irq`:

e1000_clean_rx_irq
==================

.. c:function:: bool e1000_clean_rx_irq(struct e1000_adapter *adapter, struct e1000_rx_ring *rx_ring, int *work_done, int work_to_do)

    Send received data up the network stack; legacy

    :param adapter:
        board private structure
    :type adapter: struct e1000_adapter \*

    :param rx_ring:
        ring to clean
    :type rx_ring: struct e1000_rx_ring \*

    :param work_done:
        amount of napi work completed this call
    :type work_done: int \*

    :param work_to_do:
        max amount of work allowed for this call to do
    :type work_to_do: int

.. _`e1000_alloc_jumbo_rx_buffers`:

e1000_alloc_jumbo_rx_buffers
============================

.. c:function:: void e1000_alloc_jumbo_rx_buffers(struct e1000_adapter *adapter, struct e1000_rx_ring *rx_ring, int cleaned_count)

    Replace used jumbo receive buffers

    :param adapter:
        address of board private structure
    :type adapter: struct e1000_adapter \*

    :param rx_ring:
        pointer to receive ring structure
    :type rx_ring: struct e1000_rx_ring \*

    :param cleaned_count:
        number of buffers to allocate this pass
    :type cleaned_count: int

.. _`e1000_alloc_rx_buffers`:

e1000_alloc_rx_buffers
======================

.. c:function:: void e1000_alloc_rx_buffers(struct e1000_adapter *adapter, struct e1000_rx_ring *rx_ring, int cleaned_count)

    Replace used receive buffers; legacy & extended

    :param adapter:
        address of board private structure
    :type adapter: struct e1000_adapter \*

    :param rx_ring:
        *undescribed*
    :type rx_ring: struct e1000_rx_ring \*

    :param cleaned_count:
        *undescribed*
    :type cleaned_count: int

.. _`e1000_smartspeed`:

e1000_smartspeed
================

.. c:function:: void e1000_smartspeed(struct e1000_adapter *adapter)

    Workaround for SmartSpeed on 82541 and 82547 controllers.

    :param adapter:
        *undescribed*
    :type adapter: struct e1000_adapter \*

.. _`e1000_ioctl`:

e1000_ioctl
===========

.. c:function:: int e1000_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`e1000_mii_ioctl`:

e1000_mii_ioctl
===============

.. c:function:: int e1000_mii_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`e1000_io_error_detected`:

e1000_io_error_detected
=======================

.. c:function:: pci_ers_result_t e1000_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

.. _`e1000_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`e1000_io_slot_reset`:

e1000_io_slot_reset
===================

.. c:function:: pci_ers_result_t e1000_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`e1000_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot. Implementation
resembles the first-half of the e1000_resume routine.

.. _`e1000_io_resume`:

e1000_io_resume
===============

.. c:function:: void e1000_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`e1000_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation. Implementation resembles the
second-half of the e1000_resume routine.

.. This file was automatic generated / don't edit.

