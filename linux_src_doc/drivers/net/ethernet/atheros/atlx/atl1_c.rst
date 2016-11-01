.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/atheros/atlx/atl1.c

.. _`atl1_check_options`:

atl1_check_options
==================

.. c:function:: void atl1_check_options(struct atl1_adapter *adapter)

    Range Checking for Command Line Parameters

    :param struct atl1_adapter \*adapter:
        board private structure

.. _`atl1_check_options.description`:

Description
-----------

This routine checks all command line parameters for valid user
input.  If an invalid value is given, or if no user specified
value exists, a default value is used.  The final value is stored
in a variable in the adapter structure.

.. _`atl1_sw_init`:

atl1_sw_init
============

.. c:function:: int atl1_sw_init(struct atl1_adapter *adapter)

    Initialize general software structures (struct atl1_adapter)

    :param struct atl1_adapter \*adapter:
        board private structure to initialize

.. _`atl1_sw_init.description`:

Description
-----------

atl1_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`atl1_setup_ring_resources`:

atl1_setup_ring_resources
=========================

.. c:function:: s32 atl1_setup_ring_resources(struct atl1_adapter *adapter)

    allocate Tx / RX descriptor resources

    :param struct atl1_adapter \*adapter:
        board private structure

.. _`atl1_setup_ring_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`atl1_clean_rx_ring`:

atl1_clean_rx_ring
==================

.. c:function:: void atl1_clean_rx_ring(struct atl1_adapter *adapter)

    Free RFD Buffers

    :param struct atl1_adapter \*adapter:
        board private structure

.. _`atl1_clean_tx_ring`:

atl1_clean_tx_ring
==================

.. c:function:: void atl1_clean_tx_ring(struct atl1_adapter *adapter)

    Free Tx Buffers

    :param struct atl1_adapter \*adapter:
        board private structure

.. _`atl1_free_ring_resources`:

atl1_free_ring_resources
========================

.. c:function:: void atl1_free_ring_resources(struct atl1_adapter *adapter)

    Free Tx / RX descriptor Resources

    :param struct atl1_adapter \*adapter:
        board private structure

.. _`atl1_free_ring_resources.description`:

Description
-----------

Free all transmit software resources

.. _`atl1_configure`:

atl1_configure
==============

.. c:function:: u32 atl1_configure(struct atl1_adapter *adapter)

    Configure Transmit&Receive Unit after Reset

    :param struct atl1_adapter \*adapter:
        board private structure

.. _`atl1_configure.description`:

Description
-----------

Configure the Tx /Rx unit of the MAC after a reset.

.. _`atl1_alloc_rx_buffers`:

atl1_alloc_rx_buffers
=====================

.. c:function:: u16 atl1_alloc_rx_buffers(struct atl1_adapter *adapter)

    Replace used receive buffers

    :param struct atl1_adapter \*adapter:
        address of board private structure

.. _`atl1_intr`:

atl1_intr
=========

.. c:function:: irqreturn_t atl1_intr(int irq, void *data)

    Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`atl1_phy_config`:

atl1_phy_config
===============

.. c:function:: void atl1_phy_config(unsigned long data)

    Timer Call-back

    :param unsigned long data:
        pointer to netdev cast into an unsigned long

.. _`atl1_change_mtu`:

atl1_change_mtu
===============

.. c:function:: int atl1_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`atl1_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`atl1_open`:

atl1_open
=========

.. c:function:: int atl1_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`atl1_close`:

atl1_close
==========

.. c:function:: int atl1_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl1_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`atl1_probe`:

atl1_probe
==========

.. c:function:: int atl1_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in atl1_pci_tbl

.. _`atl1_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

atl1_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`atl1_remove`:

atl1_remove
===========

.. c:function:: void atl1_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`atl1_remove.description`:

Description
-----------

atl1_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. This file was automatic generated / don't edit.

