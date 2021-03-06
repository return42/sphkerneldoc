.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/fm10k/fm10k_pci.c

.. _`fm10k_macvlan_schedule`:

fm10k_macvlan_schedule
======================

.. c:function:: void fm10k_macvlan_schedule(struct fm10k_intfc *interface)

    Schedule MAC/VLAN queue task

    :param interface:
        fm10k private interface structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_macvlan_schedule.description`:

Description
-----------

Schedule the MAC/VLAN queue monitor task. If the MAC/VLAN task cannot be
started immediately, request that it be restarted when possible.

.. _`fm10k_stop_macvlan_task`:

fm10k_stop_macvlan_task
=======================

.. c:function:: void fm10k_stop_macvlan_task(struct fm10k_intfc *interface)

    Stop the MAC/VLAN queue monitor

    :param interface:
        fm10k private interface structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_stop_macvlan_task.description`:

Description
-----------

Wait until the MAC/VLAN queue task has stopped, and cancel any future
requests.

.. _`fm10k_resume_macvlan_task`:

fm10k_resume_macvlan_task
=========================

.. c:function:: void fm10k_resume_macvlan_task(struct fm10k_intfc *interface)

    Restart the MAC/VLAN queue monitor

    :param interface:
        fm10k private interface structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_resume_macvlan_task.description`:

Description
-----------

Clear the \__FM10K_MACVLAN_DISABLE bit and, if a request occurred, schedule
the MAC/VLAN work monitor.

.. _`fm10k_service_timer`:

fm10k_service_timer
===================

.. c:function:: void fm10k_service_timer(struct timer_list *t)

    Timer Call-back

    :param t:
        pointer to timer data
    :type t: struct timer_list \*

.. _`fm10k_prepare_for_reset`:

fm10k_prepare_for_reset
=======================

.. c:function:: bool fm10k_prepare_for_reset(struct fm10k_intfc *interface)

    Prepare the driver and device for a pending reset

    :param interface:
        fm10k private data structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_prepare_for_reset.description`:

Description
-----------

This function prepares for a device reset by shutting as much down as we
can. It does nothing and returns false if \__FM10K_RESETTING was already set
prior to calling this function. It returns true if it actually did work.

.. _`fm10k_configure_swpri_map`:

fm10k_configure_swpri_map
=========================

.. c:function:: void fm10k_configure_swpri_map(struct fm10k_intfc *interface)

    Configure Receive SWPRI to PC mapping

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_configure_swpri_map.description`:

Description
-----------

Configure the SWPRI to PC mapping for the port.

.. _`fm10k_watchdog_update_host_state`:

fm10k_watchdog_update_host_state
================================

.. c:function:: void fm10k_watchdog_update_host_state(struct fm10k_intfc *interface)

    Update the link status based on host.

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_mbx_subtask`:

fm10k_mbx_subtask
=================

.. c:function:: void fm10k_mbx_subtask(struct fm10k_intfc *interface)

    Process upstream and downstream mailboxes

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_mbx_subtask.description`:

Description
-----------

This function will process both the upstream and downstream mailboxes.

.. _`fm10k_watchdog_host_is_ready`:

fm10k_watchdog_host_is_ready
============================

.. c:function:: void fm10k_watchdog_host_is_ready(struct fm10k_intfc *interface)

    Update netdev status based on host ready

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_watchdog_host_not_ready`:

fm10k_watchdog_host_not_ready
=============================

.. c:function:: void fm10k_watchdog_host_not_ready(struct fm10k_intfc *interface)

    Update netdev status based on host not ready

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_update_stats`:

fm10k_update_stats
==================

.. c:function:: void fm10k_update_stats(struct fm10k_intfc *interface)

    Update the board statistics counters.

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_watchdog_flush_tx`:

fm10k_watchdog_flush_tx
=======================

.. c:function:: void fm10k_watchdog_flush_tx(struct fm10k_intfc *interface)

    flush queues on host not ready

    :param interface:
        pointer to the device interface structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_watchdog_subtask`:

fm10k_watchdog_subtask
======================

.. c:function:: void fm10k_watchdog_subtask(struct fm10k_intfc *interface)

    check and bring link up

    :param interface:
        pointer to the device interface structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_check_hang_subtask`:

fm10k_check_hang_subtask
========================

.. c:function:: void fm10k_check_hang_subtask(struct fm10k_intfc *interface)

    check for hung queues and dropped interrupts

    :param interface:
        pointer to the device interface structure
    :type interface: struct fm10k_intfc \*

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

    :param work:
        pointer to work_struct containing our data
    :type work: struct work_struct \*

.. _`fm10k_macvlan_task`:

fm10k_macvlan_task
==================

.. c:function:: void fm10k_macvlan_task(struct work_struct *work)

    send queued MAC/VLAN requests to switch manager

    :param work:
        pointer to work_struct containing our data
    :type work: struct work_struct \*

.. _`fm10k_macvlan_task.description`:

Description
-----------

This work item handles sending MAC/VLAN updates to the switch manager. When
the interface is up, it will attempt to queue mailbox messages to the
switch manager requesting updates for MAC/VLAN pairs. If the Tx fifo of the
mailbox is full, it will reschedule itself to try again in a short while.
This ensures that the driver does not overload the switch mailbox with too
many simultaneous requests, causing an unnecessary reset.

.. _`fm10k_configure_tx_ring`:

fm10k_configure_tx_ring
=======================

.. c:function:: void fm10k_configure_tx_ring(struct fm10k_intfc *interface, struct fm10k_ring *ring)

    Configure Tx ring after Reset

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

    :param ring:
        structure containing ring specific data
    :type ring: struct fm10k_ring \*

.. _`fm10k_configure_tx_ring.description`:

Description
-----------

Configure the Tx descriptor ring after a reset.

.. _`fm10k_enable_tx_ring`:

fm10k_enable_tx_ring
====================

.. c:function:: void fm10k_enable_tx_ring(struct fm10k_intfc *interface, struct fm10k_ring *ring)

    Verify Tx ring is enabled after configuration

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

    :param ring:
        structure containing ring specific data
    :type ring: struct fm10k_ring \*

.. _`fm10k_enable_tx_ring.description`:

Description
-----------

Verify the Tx descriptor ring is ready for transmit.

.. _`fm10k_configure_tx`:

fm10k_configure_tx
==================

.. c:function:: void fm10k_configure_tx(struct fm10k_intfc *interface)

    Configure Transmit Unit after Reset

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`fm10k_configure_rx_ring`:

fm10k_configure_rx_ring
=======================

.. c:function:: void fm10k_configure_rx_ring(struct fm10k_intfc *interface, struct fm10k_ring *ring)

    Configure Rx ring after Reset

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

    :param ring:
        structure containing ring specific data
    :type ring: struct fm10k_ring \*

.. _`fm10k_configure_rx_ring.description`:

Description
-----------

Configure the Rx descriptor ring after a reset.

.. _`fm10k_update_rx_drop_en`:

fm10k_update_rx_drop_en
=======================

.. c:function:: void fm10k_update_rx_drop_en(struct fm10k_intfc *interface)

    Configures the drop enable bits for Rx rings

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_update_rx_drop_en.description`:

Description
-----------

Configure the drop enable bits for the Rx rings.

.. _`fm10k_configure_dglort`:

fm10k_configure_dglort
======================

.. c:function:: void fm10k_configure_dglort(struct fm10k_intfc *interface)

    Configure Receive DGLORT after reset

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_configure_dglort.description`:

Description
-----------

Configure the DGLORT description and RSS tables.

.. _`fm10k_configure_rx`:

fm10k_configure_rx
==================

.. c:function:: void fm10k_configure_rx(struct fm10k_intfc *interface)

    Configure Receive Unit after Reset

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`fm10k_qv_free_irq`:

fm10k_qv_free_irq
=================

.. c:function:: void fm10k_qv_free_irq(struct fm10k_intfc *interface)

    release interrupts associated with queue vectors

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

.. _`fm10k_qv_free_irq.description`:

Description
-----------

Release all interrupts associated with this interface

.. _`fm10k_qv_request_irq`:

fm10k_qv_request_irq
====================

.. c:function:: int fm10k_qv_request_irq(struct fm10k_intfc *interface)

    initialize interrupts for queue vectors

    :param interface:
        board private structure
    :type interface: struct fm10k_intfc \*

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

    :param interface:
        host interface private structure to initialize
    :type interface: struct fm10k_intfc \*

    :param ent:
        PCI device ID entry
    :type ent: const struct pci_device_id \*

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

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in fm10k_pci_tbl
    :type ent: const struct pci_device_id \*

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

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

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

.. c:function:: int __maybe_unused fm10k_resume(struct device *dev)

    Generic PM resume hook

    :param dev:
        generic device structure
    :type dev: struct device \*

.. _`fm10k_resume.description`:

Description
-----------

Generic PM hook used when waking the device from a low power state after
suspend or hibernation. This function does not need to handle lower PCIe
device state as the stack takes care of that for us.

.. _`fm10k_suspend`:

fm10k_suspend
=============

.. c:function:: int __maybe_unused fm10k_suspend(struct device *dev)

    Generic PM suspend hook

    :param dev:
        generic device structure
    :type dev: struct device \*

.. _`fm10k_suspend.description`:

Description
-----------

Generic PM hook used when setting the device into a low power state for
system suspend or hibernation. This function does not need to handle lower
PCIe device state as the stack takes care of that for us.

.. _`fm10k_io_error_detected`:

fm10k_io_error_detected
=======================

.. c:function:: pci_ers_result_t fm10k_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

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

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`fm10k_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot.

.. _`fm10k_io_resume`:

fm10k_io_resume
===============

.. c:function:: void fm10k_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`fm10k_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation.

.. _`fm10k_io_reset_prepare`:

fm10k_io_reset_prepare
======================

.. c:function:: void fm10k_io_reset_prepare(struct pci_dev *pdev)

    called when PCI function is about to be reset

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`fm10k_io_reset_prepare.description`:

Description
-----------

This callback is called when the PCI function is about to be reset,
allowing the device driver to prepare for it.

.. _`fm10k_io_reset_done`:

fm10k_io_reset_done
===================

.. c:function:: void fm10k_io_reset_done(struct pci_dev *pdev)

    called when PCI function has finished resetting

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`fm10k_io_reset_done.description`:

Description
-----------

This callback is called just after the PCI function is reset, such as via
/sys/class/net/<enpX>/device/reset or similar.

.. _`fm10k_register_pci_driver`:

fm10k_register_pci_driver
=========================

.. c:function:: int fm10k_register_pci_driver( void)

    register driver interface

    :param void:
        no arguments
    :type void: 

.. _`fm10k_register_pci_driver.description`:

Description
-----------

This function is called on module load in order to register the driver.

.. _`fm10k_unregister_pci_driver`:

fm10k_unregister_pci_driver
===========================

.. c:function:: void fm10k_unregister_pci_driver( void)

    unregister driver interface

    :param void:
        no arguments
    :type void: 

.. _`fm10k_unregister_pci_driver.description`:

Description
-----------

This function is called on module unload in order to remove the driver.

.. This file was automatic generated / don't edit.

