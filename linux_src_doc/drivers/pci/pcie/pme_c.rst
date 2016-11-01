.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/pme.c

.. _`pcie_pme_interrupt_enable`:

pcie_pme_interrupt_enable
=========================

.. c:function:: void pcie_pme_interrupt_enable(struct pci_dev *dev, bool enable)

    Enable/disable PCIe PME interrupt generation.

    :param struct pci_dev \*dev:
        PCIe root port or event collector.

    :param bool enable:
        Enable or disable the interrupt.

.. _`pcie_pme_walk_bus`:

pcie_pme_walk_bus
=================

.. c:function:: bool pcie_pme_walk_bus(struct pci_bus *bus)

    Scan a PCI bus for devices asserting PME#.

    :param struct pci_bus \*bus:
        PCI bus to scan.

.. _`pcie_pme_walk_bus.description`:

Description
-----------

Scan given PCI bus and all buses under it for devices asserting PME#.

.. _`pcie_pme_from_pci_bridge`:

pcie_pme_from_pci_bridge
========================

.. c:function:: bool pcie_pme_from_pci_bridge(struct pci_bus *bus, u8 devfn)

    Check if PCIe-PCI bridge generated a PME.

    :param struct pci_bus \*bus:
        Secondary bus of the bridge.

    :param u8 devfn:
        Device/function number to check.

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

    :param struct pci_dev \*port:
        Root port or event collector that generated the PME interrupt.

    :param u16 req_id:
        PCIe Requester ID of the device that generated the PME.

.. _`pcie_pme_work_fn`:

pcie_pme_work_fn
================

.. c:function:: void pcie_pme_work_fn(struct work_struct *work)

    Work handler for PCIe PME interrupt.

    :param struct work_struct \*work:
        Work structure giving access to service data.

.. _`pcie_pme_irq`:

pcie_pme_irq
============

.. c:function:: irqreturn_t pcie_pme_irq(int irq, void *context)

    Interrupt handler for PCIe root port PME interrupt.

    :param int irq:
        Interrupt vector.

    :param void \*context:
        Interrupt context pointer.

.. _`pcie_pme_set_native`:

pcie_pme_set_native
===================

.. c:function:: int pcie_pme_set_native(struct pci_dev *dev, void *ign)

    Set the PME interrupt flag for given device.

    :param struct pci_dev \*dev:
        PCI device to handle.

    :param void \*ign:
        Ignored.

.. _`pcie_pme_mark_devices`:

pcie_pme_mark_devices
=====================

.. c:function:: void pcie_pme_mark_devices(struct pci_dev *port)

    Set the PME interrupt flag for devices below a port.

    :param struct pci_dev \*port:
        PCIe root port or event collector to handle.

.. _`pcie_pme_mark_devices.description`:

Description
-----------

For each device below given root port, including the port itself (or for each
root complex integrated endpoint if \ ``port``\  is a root complex event collector)
set the flag indicating that it can signal run-time wake-up events via PCIe
PME interrupts.

.. _`pcie_pme_probe`:

pcie_pme_probe
==============

.. c:function:: int pcie_pme_probe(struct pcie_device *srv)

    Initialize PCIe PME service for given root port.

    :param struct pcie_device \*srv:
        PCIe service to initialize.

.. _`pcie_pme_suspend`:

pcie_pme_suspend
================

.. c:function:: int pcie_pme_suspend(struct pcie_device *srv)

    Suspend PCIe PME service device.

    :param struct pcie_device \*srv:
        PCIe service device to suspend.

.. _`pcie_pme_resume`:

pcie_pme_resume
===============

.. c:function:: int pcie_pme_resume(struct pcie_device *srv)

    Resume PCIe PME service device. \ ``srv``\  - PCIe service device to resume.

    :param struct pcie_device \*srv:
        *undescribed*

.. _`pcie_pme_service_init`:

pcie_pme_service_init
=====================

.. c:function:: int pcie_pme_service_init( void)

    Register the PCIe PME service driver.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

