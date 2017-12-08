.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgb/ixgb_main.c

.. _`ixgb_init_module`:

ixgb_init_module
================

.. c:function:: int ixgb_init_module( void)

    Driver Registration Routine

    :param  void:
        no arguments

.. _`ixgb_init_module.description`:

Description
-----------

ixgb_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`ixgb_exit_module`:

ixgb_exit_module
================

.. c:function:: void __exit ixgb_exit_module( void)

    Driver Exit Cleanup Routine

    :param  void:
        no arguments

.. _`ixgb_exit_module.description`:

Description
-----------

ixgb_exit_module is called just before the driver is removed
from memory.

.. _`ixgb_irq_disable`:

ixgb_irq_disable
================

.. c:function:: void ixgb_irq_disable(struct ixgb_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_irq_enable`:

ixgb_irq_enable
===============

.. c:function:: void ixgb_irq_enable(struct ixgb_adapter *adapter)

    Enable default interrupt generation settings

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_probe`:

ixgb_probe
==========

.. c:function:: int ixgb_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in ixgb_pci_tbl

.. _`ixgb_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

ixgb_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`ixgb_remove`:

ixgb_remove
===========

.. c:function:: void ixgb_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`ixgb_remove.description`:

Description
-----------

ixgb_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`ixgb_sw_init`:

ixgb_sw_init
============

.. c:function:: int ixgb_sw_init(struct ixgb_adapter *adapter)

    Initialize general software structures (struct ixgb_adapter)

    :param struct ixgb_adapter \*adapter:
        board private structure to initialize

.. _`ixgb_sw_init.description`:

Description
-----------

ixgb_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`ixgb_open`:

ixgb_open
=========

.. c:function:: int ixgb_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgb_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`ixgb_close`:

ixgb_close
==========

.. c:function:: int ixgb_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgb_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`ixgb_setup_tx_resources`:

ixgb_setup_tx_resources
=======================

.. c:function:: int ixgb_setup_tx_resources(struct ixgb_adapter *adapter)

    allocate Tx resources (Descriptors)

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`ixgb_configure_tx`:

ixgb_configure_tx
=================

.. c:function:: void ixgb_configure_tx(struct ixgb_adapter *adapter)

    Configure 82597 Transmit Unit after Reset.

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`ixgb_setup_rx_resources`:

ixgb_setup_rx_resources
=======================

.. c:function:: int ixgb_setup_rx_resources(struct ixgb_adapter *adapter)

    allocate Rx resources (Descriptors)

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgb_setup_rctl`:

ixgb_setup_rctl
===============

.. c:function:: void ixgb_setup_rctl(struct ixgb_adapter *adapter)

    configure the receive control register

    :param struct ixgb_adapter \*adapter:
        Board private structure

.. _`ixgb_configure_rx`:

ixgb_configure_rx
=================

.. c:function:: void ixgb_configure_rx(struct ixgb_adapter *adapter)

    Configure 82597 Receive Unit after Reset.

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`ixgb_free_tx_resources`:

ixgb_free_tx_resources
======================

.. c:function:: void ixgb_free_tx_resources(struct ixgb_adapter *adapter)

    Free Tx Resources

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`ixgb_clean_tx_ring`:

ixgb_clean_tx_ring
==================

.. c:function:: void ixgb_clean_tx_ring(struct ixgb_adapter *adapter)

    Free Tx Buffers

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_free_rx_resources`:

ixgb_free_rx_resources
======================

.. c:function:: void ixgb_free_rx_resources(struct ixgb_adapter *adapter)

    Free Rx Resources

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`ixgb_clean_rx_ring`:

ixgb_clean_rx_ring
==================

.. c:function:: void ixgb_clean_rx_ring(struct ixgb_adapter *adapter)

    Free Rx Buffers

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_set_mac`:

ixgb_set_mac
============

.. c:function:: int ixgb_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`ixgb_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgb_set_multi`:

ixgb_set_multi
==============

.. c:function:: void ixgb_set_multi(struct net_device *netdev)

    Multicast and Promiscuous mode set

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgb_set_multi.description`:

Description
-----------

The set_multi entry point is called whenever the multicast address
list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper multicast,
promiscuous mode, and all-multi behavior.

.. _`ixgb_watchdog`:

ixgb_watchdog
=============

.. c:function:: void ixgb_watchdog(struct timer_list *t)

    Timer Call-back

    :param struct timer_list \*t:
        *undescribed*

.. _`ixgb_tx_timeout`:

ixgb_tx_timeout
===============

.. c:function:: void ixgb_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`ixgb_change_mtu`:

ixgb_change_mtu
===============

.. c:function:: int ixgb_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`ixgb_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`ixgb_update_stats`:

ixgb_update_stats
=================

.. c:function:: void ixgb_update_stats(struct ixgb_adapter *adapter)

    Update the board statistics counters.

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_intr`:

ixgb_intr
=========

.. c:function:: irqreturn_t ixgb_intr(int irq, void *data)

    Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`ixgb_clean`:

ixgb_clean
==========

.. c:function:: int ixgb_clean(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param struct napi_struct \*napi:
        *undescribed*

    :param int budget:
        *undescribed*

.. _`ixgb_clean_tx_irq`:

ixgb_clean_tx_irq
=================

.. c:function:: bool ixgb_clean_tx_irq(struct ixgb_adapter *adapter)

    Reclaim resources after transmit completes

    :param struct ixgb_adapter \*adapter:
        board private structure

.. _`ixgb_rx_checksum`:

ixgb_rx_checksum
================

.. c:function:: void ixgb_rx_checksum(struct ixgb_adapter *adapter, struct ixgb_rx_desc *rx_desc, struct sk_buff *skb)

    Receive Checksum Offload for 82597.

    :param struct ixgb_adapter \*adapter:
        board private structure

    :param struct ixgb_rx_desc \*rx_desc:
        receive descriptor

    :param struct sk_buff \*skb:
        *undescribed*

.. _`ixgb_clean_rx_irq`:

ixgb_clean_rx_irq
=================

.. c:function:: bool ixgb_clean_rx_irq(struct ixgb_adapter *adapter, int *work_done, int work_to_do)

    Send received data up the network stack,

    :param struct ixgb_adapter \*adapter:
        board private structure

    :param int \*work_done:
        *undescribed*

    :param int work_to_do:
        *undescribed*

.. _`ixgb_alloc_rx_buffers`:

ixgb_alloc_rx_buffers
=====================

.. c:function:: void ixgb_alloc_rx_buffers(struct ixgb_adapter *adapter, int cleaned_count)

    Replace used receive buffers

    :param struct ixgb_adapter \*adapter:
        address of board private structure

    :param int cleaned_count:
        *undescribed*

.. _`ixgb_io_error_detected`:

ixgb_io_error_detected
======================

.. c:function:: pci_ers_result_t ixgb_io_error_detected(struct pci_dev *pdev, enum pci_channel_state state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        pointer to pci device with error

    :param enum pci_channel_state state:
        pci channel state after error

.. _`ixgb_io_error_detected.description`:

Description
-----------

This callback is called by the PCI subsystem whenever
a PCI bus error is detected.

.. _`ixgb_io_slot_reset`:

ixgb_io_slot_reset
==================

.. c:function:: pci_ers_result_t ixgb_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset. \ ``pdev``\     pointer to pci device with error

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`ixgb_io_slot_reset.description`:

Description
-----------

This callback is called after the PCI bus has been reset.
Basically, this tries to restart the card from scratch.
This is a shortened version of the device probe/discovery code,
it resembles the first-half of the \ :c:func:`ixgb_probe`\  routine.

.. _`ixgb_io_resume`:

ixgb_io_resume
==============

.. c:function:: void ixgb_io_resume(struct pci_dev *pdev)

    called when its OK to resume normal operations \ ``pdev``\     pointer to pci device with error

    :param struct pci_dev \*pdev:
        *undescribed*

.. _`ixgb_io_resume.description`:

Description
-----------

The error recovery driver tells us that its OK to resume
normal operation. Implementation resembles the second-half
of the \ :c:func:`ixgb_probe`\  routine.

.. This file was automatic generated / don't edit.

