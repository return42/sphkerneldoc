.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_pci.c

.. _`fm10k_service_timer`:

fm10k_service_timer
===================

.. c:function:: void fm10k_service_timer(unsigned long data)

    Timer Call-back

    :param unsigned long data:
        pointer to interface cast into an unsigned long

.. _`fm10k_configure_swpri_map`:

fm10k_configure_swpri_map
=========================

.. c:function:: void fm10k_configure_swpri_map(struct fm10k_intfc *interface)

    Configure Receive SWPRI to PC mapping

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_configure_swpri_map.description`:

Description
-----------

Configure the SWPRI to PC mapping for the port.

.. _`fm10k_watchdog_update_host_state`:

fm10k_watchdog_update_host_state
================================

.. c:function:: void fm10k_watchdog_update_host_state(struct fm10k_intfc *interface)

    Update the link status based on host.

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_mbx_subtask`:

fm10k_mbx_subtask
=================

.. c:function:: void fm10k_mbx_subtask(struct fm10k_intfc *interface)

    Process upstream and downstream mailboxes

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_mbx_subtask.description`:

Description
-----------

This function will process both the upstream and downstream mailboxes.

.. _`fm10k_watchdog_host_is_ready`:

fm10k_watchdog_host_is_ready
============================

.. c:function:: void fm10k_watchdog_host_is_ready(struct fm10k_intfc *interface)

    Update netdev status based on host ready

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_watchdog_host_not_ready`:

fm10k_watchdog_host_not_ready
=============================

.. c:function:: void fm10k_watchdog_host_not_ready(struct fm10k_intfc *interface)

    Update netdev status based on host not ready

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_update_stats`:

fm10k_update_stats
==================

.. c:function:: void fm10k_update_stats(struct fm10k_intfc *interface)

    Update the board statistics counters.

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_watchdog_flush_tx`:

fm10k_watchdog_flush_tx
=======================

.. c:function:: void fm10k_watchdog_flush_tx(struct fm10k_intfc *interface)

    flush queues on host not ready \ ``interface``\  - pointer to the device interface structure

    :param struct fm10k_intfc \*interface:
        *undescribed*

.. _`fm10k_watchdog_subtask`:

fm10k_watchdog_subtask
======================

.. c:function:: void fm10k_watchdog_subtask(struct fm10k_intfc *interface)

    check and bring link up \ ``interface``\  - pointer to the device interface structure

    :param struct fm10k_intfc \*interface:
        *undescribed*

.. _`fm10k_check_hang_subtask`:

fm10k_check_hang_subtask
========================

.. c:function:: void fm10k_check_hang_subtask(struct fm10k_intfc *interface)

    check for hung queues and dropped interrupts \ ``interface``\  - pointer to the device interface structure

    :param struct fm10k_intfc \*interface:
        *undescribed*

.. _`fm10k_check_hang_subtask.description`:

Description
-----------

This function serves two purposes.  First it strobes the interrupt lines
in order to make certain interrupts are occurring.  Secondly it sets the
bits needed to check for TX hangs.  As a result we should immediately
determine if a hang has occurred.

.. _`fm10k_service_task`:

fm10k_service_task
==================

.. c:function:: void fm10k_service_task(struct work_struct *work)

    manages and runs subtasks

    :param struct work_struct \*work:
        pointer to work_struct containing our data

.. _`fm10k_configure_tx_ring`:

fm10k_configure_tx_ring
=======================

.. c:function:: void fm10k_configure_tx_ring(struct fm10k_intfc *interface, struct fm10k_ring *ring)

    Configure Tx ring after Reset

    :param struct fm10k_intfc \*interface:
        board private structure

    :param struct fm10k_ring \*ring:
        structure containing ring specific data

.. _`fm10k_configure_tx_ring.description`:

Description
-----------

Configure the Tx descriptor ring after a reset.

.. _`fm10k_enable_tx_ring`:

fm10k_enable_tx_ring
====================

.. c:function:: void fm10k_enable_tx_ring(struct fm10k_intfc *interface, struct fm10k_ring *ring)

    Verify Tx ring is enabled after configuration

    :param struct fm10k_intfc \*interface:
        board private structure

    :param struct fm10k_ring \*ring:
        structure containing ring specific data

.. _`fm10k_enable_tx_ring.description`:

Description
-----------

Verify the Tx descriptor ring is ready for transmit.

.. _`fm10k_configure_tx`:

fm10k_configure_tx
==================

.. c:function:: void fm10k_configure_tx(struct fm10k_intfc *interface)

    Configure Transmit Unit after Reset

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`fm10k_configure_rx_ring`:

fm10k_configure_rx_ring
=======================

.. c:function:: void fm10k_configure_rx_ring(struct fm10k_intfc *interface, struct fm10k_ring *ring)

    Configure Rx ring after Reset

    :param struct fm10k_intfc \*interface:
        board private structure

    :param struct fm10k_ring \*ring:
        structure containing ring specific data

.. _`fm10k_configure_rx_ring.description`:

Description
-----------

Configure the Rx descriptor ring after a reset.

.. _`fm10k_update_rx_drop_en`:

fm10k_update_rx_drop_en
=======================

.. c:function:: void fm10k_update_rx_drop_en(struct fm10k_intfc *interface)

    Configures the drop enable bits for Rx rings

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_update_rx_drop_en.description`:

Description
-----------

Configure the drop enable bits for the Rx rings.

.. _`fm10k_configure_dglort`:

fm10k_configure_dglort
======================

.. c:function:: void fm10k_configure_dglort(struct fm10k_intfc *interface)

    Configure Receive DGLORT after reset

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_configure_dglort.description`:

Description
-----------

Configure the DGLORT description and RSS tables.

.. _`fm10k_configure_rx`:

fm10k_configure_rx
==================

.. c:function:: void fm10k_configure_rx(struct fm10k_intfc *interface)

    Configure Receive Unit after Reset

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`fm10k_netpoll`:

fm10k_netpoll
=============

.. c:function:: void fm10k_netpoll(struct net_device *netdev)

    A Polling 'interrupt' handler

    :param struct net_device \*netdev:
        network interface device structure

.. _`fm10k_netpoll.description`:

Description
-----------

This is used by netconsole to send skbs without having to re-enable
interrupts. It's not called while the normal interrupt routine is executing.

.. _`fm10k_qv_free_irq`:

fm10k_qv_free_irq
=================

.. c:function:: void fm10k_qv_free_irq(struct fm10k_intfc *interface)

    release interrupts associated with queue vectors

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_qv_free_irq.description`:

Description
-----------

Release all interrupts associated with this interface

.. _`fm10k_qv_request_irq`:

fm10k_qv_request_irq
====================

.. c:function:: int fm10k_qv_request_irq(struct fm10k_intfc *interface)

    initialize interrupts for queue vectors

    :param struct fm10k_intfc \*interface:
        board private structure

.. _`fm10k_qv_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`fm10k_sw_init`:

fm10k_sw_init
=============

.. c:function:: int fm10k_sw_init(struct fm10k_intfc *interface, const struct pci_device_id *ent)

    Initialize general software structures

    :param struct fm10k_intfc \*interface:
        host interface private structure to initialize

    :param const struct pci_device_id \*ent:
        *undescribed*

.. _`fm10k_sw_init.description`:

Description
-----------

fm10k_sw_init initializes the interface private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`fm10k_probe`:

fm10k_probe
===========

.. c:function:: int fm10k_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in fm10k_pci_tbl

.. _`fm10k_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

fm10k_probe initializes an interface identified by a pci_dev structure.
The OS initialization, configuring of the interface private structure,
and a hardware reset occur.

.. _`fm10k_remove`:

fm10k_remove
============

.. c:function:: void fm10k_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`fm10k_remove.description`:

Description
-----------

fm10k_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`fm10k_resume`:

fm10k_resume
============

.. c:function:: int fm10k_resume(struct pci_dev *pdev)

    Restore device to pre-sleep state

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`fm10k_resume.description`:

Description
-----------

fm10k_resume is called after the system has powered back up from a sleep
state and is ready to resume operation.  This function is meant to restore
the device back to its pre-sleep state.

.. _`fm10k_suspend`:

fm10k_suspend
=============

.. c:function:: int fm10k_suspend(struct pci_dev *pdev, pm_message_t __always_unused state)

    Prepare the device for a system sleep state

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param pm_message_t __always_unused state:
        *undescribed*

.. _`fm10k_suspend.description`:

Description
-----------

fm10k_suspend is meant to shutdown the device prior to the system entering
a sleep state.  The fm10k hardware does not support wake on lan so the
driver simply needs to shut down the device so it is in a low power state.

.. _`fm10k_io_error_detected`:

fm10k_io_error_detected
=======================

.. c:function:: pci_ers_result_t fm10k_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param pci_channel_state_t state:
        The current pci connection state

.. _`fm10k_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`fm10k_io_slot_reset`:

fm10k_io_slot_reset
===================

.. c:function:: pci_ers_result_t fm10k_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`fm10k_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.

.. _`fm10k_io_resume`:

fm10k_io_resume
===============

.. c:function:: void fm10k_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param struct pci_dev \*pdev:
        Pointer to PCI device

.. _`fm10k_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation.

.. _`fm10k_io_reset_notify`:

fm10k_io_reset_notify
=====================

.. c:function:: void fm10k_io_reset_notify(struct pci_dev *pdev, bool prepare)

    called when PCI function is reset

    :param struct pci_dev \*pdev:
        Pointer to PCI device

    :param bool prepare:
        *undescribed*

.. _`fm10k_io_reset_notify.description`:

Description
-----------

This callback is called when the PCI function is reset such as from
/sys/class/net/<enpX>/device/reset or similar. When prepare is true, it
means we should prepare for a function reset. If prepare is false, it means
the function reset just occurred.

.. _`fm10k_register_pci_driver`:

fm10k_register_pci_driver
=========================

.. c:function:: int fm10k_register_pci_driver( void)

    register driver interface

    :param  void:
        no arguments

.. _`fm10k_register_pci_driver.description`:

Description
-----------

This function is called on module load in order to register the driver.

.. _`fm10k_unregister_pci_driver`:

fm10k_unregister_pci_driver
===========================

.. c:function:: void fm10k_unregister_pci_driver( void)

    unregister driver interface

    :param  void:
        no arguments

.. _`fm10k_unregister_pci_driver.description`:

Description
-----------

This function is called on module unload in order to remove the driver.

.. This file was automatic generated / don't edit.

