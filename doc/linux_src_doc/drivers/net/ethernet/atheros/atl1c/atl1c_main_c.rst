.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/atheros/atl1c/atl1c_main.c

.. _`atl1c_irq_enable`:

atl1c_irq_enable
================

.. c:function:: void atl1c_irq_enable(struct atl1c_adapter *adapter)

    Enable default interrupt generation settings

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_irq_disable`:

atl1c_irq_disable
=================

.. c:function:: void atl1c_irq_disable(struct atl1c_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_irq_reset`:

atl1c_irq_reset
===============

.. c:function:: void atl1c_irq_reset(struct atl1c_adapter *adapter)

    reset interrupt confiure on the NIC

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_phy_config`:

atl1c_phy_config
================

.. c:function:: void atl1c_phy_config(unsigned long data)

    Timer Call-back

    :param unsigned long data:
        pointer to netdev cast into an unsigned long

.. _`atl1c_tx_timeout`:

atl1c_tx_timeout
================

.. c:function:: void atl1c_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1c_set_multi`:

atl1c_set_multi
===============

.. c:function:: void atl1c_set_multi(struct net_device *netdev)

    Multicast and Promiscuous mode set

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1c_set_multi.description`:

Description
-----------

The set_multi entry point is called whenever the multicast address
list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper multicast,
promiscuous mode, and all-multi behavior.

.. _`atl1c_set_mac_addr`:

atl1c_set_mac_addr
==================

.. c:function:: int atl1c_set_mac_addr(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`atl1c_set_mac_addr.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`atl1c_change_mtu`:

atl1c_change_mtu
================

.. c:function:: int atl1c_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`atl1c_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`atl1c_alloc_queues`:

atl1c_alloc_queues
==================

.. c:function:: int atl1c_alloc_queues(struct atl1c_adapter *adapter)

    Allocate memory for all rings

    :param struct atl1c_adapter \*adapter:
        board private structure to initialize

.. _`atl1c_sw_init`:

atl1c_sw_init
=============

.. c:function:: int atl1c_sw_init(struct atl1c_adapter *adapter)

    Initialize general software structures (struct atl1c_adapter)

    :param struct atl1c_adapter \*adapter:
        board private structure to initialize

.. _`atl1c_sw_init.description`:

Description
-----------

atl1c_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`atl1c_clean_tx_ring`:

atl1c_clean_tx_ring
===================

.. c:function:: void atl1c_clean_tx_ring(struct atl1c_adapter *adapter, enum atl1c_trans_queue type)

    Free Tx-skb

    :param struct atl1c_adapter \*adapter:
        board private structure

    :param enum atl1c_trans_queue type:
        *undescribed*

.. _`atl1c_clean_rx_ring`:

atl1c_clean_rx_ring
===================

.. c:function:: void atl1c_clean_rx_ring(struct atl1c_adapter *adapter)

    Free rx-reservation skbs

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_free_ring_resources`:

atl1c_free_ring_resources
=========================

.. c:function:: void atl1c_free_ring_resources(struct atl1c_adapter *adapter)

    Free Tx / RX descriptor Resources

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_free_ring_resources.description`:

Description
-----------

Free all transmit software resources

.. _`atl1c_setup_ring_resources`:

atl1c_setup_ring_resources
==========================

.. c:function:: int atl1c_setup_ring_resources(struct atl1c_adapter *adapter)

    allocate Tx / RX descriptor resources

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_setup_ring_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`atl1c_configure_mac`:

atl1c_configure_mac
===================

.. c:function:: int atl1c_configure_mac(struct atl1c_adapter *adapter)

    Configure Transmit\ :c:type:`struct Receive <Receive>` Unit after Reset

    :param struct atl1c_adapter \*adapter:
        board private structure

.. _`atl1c_configure_mac.description`:

Description
-----------

Configure the Tx /Rx unit of the MAC after a reset.

.. _`atl1c_get_stats`:

atl1c_get_stats
===============

.. c:function:: struct net_device_stats *atl1c_get_stats(struct net_device *netdev)

    Get System Network Statistics

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1c_get_stats.description`:

Description
-----------

Returns the address of the device statistics structure.
The statistics are actually updated from the timer callback.

.. _`atl1c_intr`:

atl1c_intr
==========

.. c:function:: irqreturn_t atl1c_intr(int irq, void *data)

    Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`atl1c_clean`:

atl1c_clean
===========

.. c:function:: int atl1c_clean(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param struct napi_struct \*napi:
        *undescribed*

    :param int budget:
        *undescribed*

.. _`atl1c_open`:

atl1c_open
==========

.. c:function:: int atl1c_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1c_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`atl1c_close`:

atl1c_close
===========

.. c:function:: int atl1c_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1c_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`atl1c_probe`:

atl1c_probe
===========

.. c:function:: int atl1c_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in atl1c_pci_tbl

.. _`atl1c_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

atl1c_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`atl1c_remove`:

atl1c_remove
============

.. c:function:: void atl1c_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`atl1c_remove.description`:

Description
-----------

atl1c_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`atl1c_io_error_detected`:

atl1c_io_error_detected
=======================

.. c:function:: pci_ers_result_t atl1c_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`atl1c_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`atl1c_io_slot_reset`:

atl1c_io_slot_reset
===================

.. c:function:: pci_ers_result_t atl1c_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`atl1c_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot. Implementation
resembles the first-half of the e1000_resume routine.

.. _`atl1c_io_resume`:

atl1c_io_resume
===============

.. c:function:: void atl1c_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`atl1c_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation. Implementation resembles the
second-half of the atl1c_resume routine.

.. This file was automatic generated / don't edit.

