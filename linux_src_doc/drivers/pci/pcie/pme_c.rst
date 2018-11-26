.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/pme.c

.. _`pcie_pme_interrupt_enable`:

pcie_pme_interrupt_enable
=========================

.. c:function:: void pcie_pme_interrupt_enable(struct pci_dev *dev, bool enable)

    Enable/disable PCIe PME interrupt generation.

    :param dev:
        PCIe root port or event collector.
    :type dev: struct pci_dev \*

    :param enable:
        Enable or disable the interrupt.
    :type enable: bool

.. _`pcie_pme_walk_bus`:

pcie_pme_walk_bus
=================

.. c:function:: bool pcie_pme_walk_bus(struct pci_bus *bus)

    Scan a PCI bus for devices asserting PME#.

    :param bus:
        PCI bus to scan.
    :type bus: struct pci_bus \*

.. _`pcie_pme_walk_bus.description`:

Description
-----------

Scan given PCI bus and all buses under it for devices asserting PME#.

.. _`pcie_pme_from_pci_bridge`:

pcie_pme_from_pci_bridge
========================

.. c:function:: bool pcie_pme_from_pci_bridge(struct pci_bus *bus, u8 devfn)

    Check if PCIe-PCI bridge generated a PME.

    :param bus:
        Secondary bus of the bridge.
    :type bus: struct pci_bus \*

    :param devfn:
        Device/function number to check.
    :type devfn: u8

.. _`pcie_pme_from_pci_bridge.description`:

Description
-----------

PME from PCI devices under a PCIe-PCI bridge may be converted to an in-band
PCIe PME message.  In such that case the bridge should use the Requester ID
of device/function number 0 on its secondary bus.

.. _`pcie_pme_handle_request`:

pcie_pme_handle_request
=======================

.. c:function:: void pcie_pme_handle_request(struct pci_dev *port, u16 req_id)

    Find device that generated PME and handle it.

    :param port:
        Root port or event collector that generated the PME interrupt.
    :type port: struct pci_dev \*

    :param req_id:
        PCIe Requester ID of the device that generated the PME.
    :type req_id: u16

.. _`pcie_pme_work_fn`:

pcie_pme_work_fn
================

.. c:function:: void pcie_pme_work_fn(struct work_struct *work)

    Work handler for PCIe PME interrupt.

    :param work:
        Work structure giving access to service data.
    :type work: struct work_struct \*

.. _`pcie_pme_irq`:

pcie_pme_irq
============

.. c:function:: irqreturn_t pcie_pme_irq(int irq, void *context)

    Interrupt handler for PCIe root port PME interrupt.

    :param irq:
        Interrupt vector.
    :type irq: int

    :param context:
        Interrupt context pointer.
    :type context: void \*

.. _`pcie_pme_can_wakeup`:

pcie_pme_can_wakeup
===================

.. c:function:: int pcie_pme_can_wakeup(struct pci_dev *dev, void *ign)

    Set the wakeup capability flag.

    :param dev:
        PCI device to handle.
    :type dev: struct pci_dev \*

    :param ign:
        Ignored.
    :type ign: void \*

.. _`pcie_pme_mark_devices`:

pcie_pme_mark_devices
=====================

.. c:function:: void pcie_pme_mark_devices(struct pci_dev *port)

    Set the wakeup flag for devices below a port.

    :param port:
        PCIe root port or event collector to handle.
    :type port: struct pci_dev \*

.. _`pcie_pme_mark_devices.description`:

Description
-----------

For each device below given root port, including the port itself (or for each
root complex integrated endpoint if \ ``port``\  is a root complex event collector)
set the flag indicating that it can signal run-time wake-up events.

.. _`pcie_pme_probe`:

pcie_pme_probe
==============

.. c:function:: int pcie_pme_probe(struct pcie_device *srv)

    Initialize PCIe PME service for given root port.

    :param srv:
        PCIe service to initialize.
    :type srv: struct pcie_device \*

.. _`pcie_pme_suspend`:

pcie_pme_suspend
================

.. c:function:: int pcie_pme_suspend(struct pcie_device *srv)

    Suspend PCIe PME service device.

    :param srv:
        PCIe service device to suspend.
    :type srv: struct pcie_device \*

.. _`pcie_pme_resume`:

pcie_pme_resume
===============

.. c:function:: int pcie_pme_resume(struct pcie_device *srv)

    Resume PCIe PME service device. \ ``srv``\  - PCIe service device to resume.

    :param srv:
        *undescribed*
    :type srv: struct pcie_device \*

.. _`pcie_pme_remove`:

pcie_pme_remove
===============

.. c:function:: void pcie_pme_remove(struct pcie_device *srv)

    Prepare PCIe PME service device for removal. \ ``srv``\  - PCIe service device to remove.

    :param srv:
        *undescribed*
    :type srv: struct pcie_device \*

.. _`pcie_pme_init`:

pcie_pme_init
=============

.. c:function:: int pcie_pme_init( void)

    Register the PCIe PME service driver.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

