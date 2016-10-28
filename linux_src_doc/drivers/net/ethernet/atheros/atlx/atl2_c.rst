.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/atheros/atlx/atl2.c

.. _`atl2_sw_init`:

atl2_sw_init
============

.. c:function:: int atl2_sw_init(struct atl2_adapter *adapter)

    Initialize general software structures (struct atl2_adapter)

    :param struct atl2_adapter \*adapter:
        board private structure to initialize

.. _`atl2_sw_init.description`:

Description
-----------

atl2_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`atl2_set_multi`:

atl2_set_multi
==============

.. c:function:: void atl2_set_multi(struct net_device *netdev)

    Multicast and Promiscuous mode set

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl2_set_multi.description`:

Description
-----------

The set_multi entry point is called whenever the multicast address
list or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper multicast,
promiscuous mode, and all-multi behavior.

.. _`atl2_configure`:

atl2_configure
==============

.. c:function:: int atl2_configure(struct atl2_adapter *adapter)

    Configure Transmit\ :c:type:`struct Receive <Receive>` Unit after Reset

    :param struct atl2_adapter \*adapter:
        board private structure

.. _`atl2_configure.description`:

Description
-----------

Configure the Tx /Rx unit of the MAC after a reset.

.. _`atl2_setup_ring_resources`:

atl2_setup_ring_resources
=========================

.. c:function:: s32 atl2_setup_ring_resources(struct atl2_adapter *adapter)

    allocate Tx / RX descriptor resources

    :param struct atl2_adapter \*adapter:
        board private structure

.. _`atl2_setup_ring_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`atl2_irq_enable`:

atl2_irq_enable
===============

.. c:function:: void atl2_irq_enable(struct atl2_adapter *adapter)

    Enable default interrupt generation settings

    :param struct atl2_adapter \*adapter:
        board private structure

.. _`atl2_irq_disable`:

atl2_irq_disable
================

.. c:function:: void atl2_irq_disable(struct atl2_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param struct atl2_adapter \*adapter:
        board private structure

.. _`atl2_intr`:

atl2_intr
=========

.. c:function:: irqreturn_t atl2_intr(int irq, void *data)

    Interrupt Handler

    :param int irq:
        interrupt number

    :param void \*data:
        pointer to a network interface device structure

.. _`atl2_free_ring_resources`:

atl2_free_ring_resources
========================

.. c:function:: void atl2_free_ring_resources(struct atl2_adapter *adapter)

    Free Tx / RX descriptor Resources

    :param struct atl2_adapter \*adapter:
        board private structure

.. _`atl2_free_ring_resources.description`:

Description
-----------

Free all transmit software resources

.. _`atl2_open`:

atl2_open
=========

.. c:function:: int atl2_open(struct net_device *netdev)

    Called when a network interface is made active

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl2_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`atl2_close`:

atl2_close
==========

.. c:function:: int atl2_close(struct net_device *netdev)

    Disables a network interface

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl2_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the drivers control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`atl2_change_mtu`:

atl2_change_mtu
===============

.. c:function:: int atl2_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param struct net_device \*netdev:
        network interface device structure

    :param int new_mtu:
        new value for maximum frame size

.. _`atl2_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`atl2_set_mac`:

atl2_set_mac
============

.. c:function:: int atl2_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param struct net_device \*netdev:
        network interface device structure

    :param void \*p:
        pointer to an address structure

.. _`atl2_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`atl2_tx_timeout`:

atl2_tx_timeout
===============

.. c:function:: void atl2_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param struct net_device \*netdev:
        network interface device structure

.. _`atl2_watchdog`:

atl2_watchdog
=============

.. c:function:: void atl2_watchdog(unsigned long data)

    Timer Call-back

    :param unsigned long data:
        pointer to netdev cast into an unsigned long

.. _`atl2_phy_config`:

atl2_phy_config
===============

.. c:function:: void atl2_phy_config(unsigned long data)

    Timer Call-back

    :param unsigned long data:
        pointer to netdev cast into an unsigned long

.. _`atl2_link_chg_task`:

atl2_link_chg_task
==================

.. c:function:: void atl2_link_chg_task(struct work_struct *work)

    deal with link change event Out of interrupt context

    :param struct work_struct \*work:
        *undescribed*

.. _`atl2_probe`:

atl2_probe
==========

.. c:function:: int atl2_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

    :param const struct pci_device_id \*ent:
        entry in atl2_pci_tbl

.. _`atl2_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

atl2_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`atl2_remove`:

atl2_remove
===========

.. c:function:: void atl2_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param struct pci_dev \*pdev:
        PCI device information struct

.. _`atl2_remove.description`:

Description
-----------

atl2_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`atl2_init_module`:

atl2_init_module
================

.. c:function:: int atl2_init_module( void)

    Driver Registration Routine

    :param  void:
        no arguments

.. _`atl2_init_module.description`:

Description
-----------

atl2_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`atl2_exit_module`:

atl2_exit_module
================

.. c:function:: void __exit atl2_exit_module( void)

    Driver Exit Cleanup Routine

    :param  void:
        no arguments

.. _`atl2_exit_module.description`:

Description
-----------

atl2_exit_module is called just before the driver is removed
from memory.

.. _`atl2_check_options`:

atl2_check_options
==================

.. c:function:: void atl2_check_options(struct atl2_adapter *adapter)

    Range Checking for Command Line Parameters

    :param struct atl2_adapter \*adapter:
        board private structure

.. _`atl2_check_options.description`:

Description
-----------

This routine checks all command line parameters for valid user
input.  If an invalid value is given, or if no user specified
value exists, a default value is used.  The final value is stored
in a variable in the adapter structure.

.. This file was automatic generated / don't edit.

