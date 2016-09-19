.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci-acpi.c

.. _`pci_acpi_wake_bus`:

pci_acpi_wake_bus
=================

.. c:function:: void pci_acpi_wake_bus(struct work_struct *work)

    Root bus wakeup notification fork function.

    :param struct work_struct \*work:
        Work item to handle.

.. _`pci_acpi_wake_dev`:

pci_acpi_wake_dev
=================

.. c:function:: void pci_acpi_wake_dev(struct work_struct *work)

    PCI device wakeup notification work function.

    :param struct work_struct \*work:
        Work item to handle.

.. _`pci_acpi_add_bus_pm_notifier`:

pci_acpi_add_bus_pm_notifier
============================

.. c:function:: acpi_status pci_acpi_add_bus_pm_notifier(struct acpi_device *dev)

    Register PM notifier for root PCI bus.

    :param struct acpi_device \*dev:
        PCI root bridge ACPI device.

.. _`pci_acpi_add_pm_notifier`:

pci_acpi_add_pm_notifier
========================

.. c:function:: acpi_status pci_acpi_add_pm_notifier(struct acpi_device *dev, struct pci_dev *pci_dev)

    Register PM notifier for given PCI device.

    :param struct acpi_device \*dev:
        ACPI device to add the notifier for.

    :param struct pci_dev \*pci_dev:
        PCI device to check for the PME status if an event is signaled.

.. _`pci_acpi_optimize_delay`:

pci_acpi_optimize_delay
=======================

.. c:function:: void pci_acpi_optimize_delay(struct pci_dev *pdev, acpi_handle handle)

    optimize PCI D3 and D3cold delay from ACPI

    :param struct pci_dev \*pdev:
        the PCI device whose delay is to be updated

    :param acpi_handle handle:
        ACPI handle of this device

.. _`pci_acpi_optimize_delay.description`:

Description
-----------

Update the d3_delay and d3cold_delay of a PCI device from the ACPI \_DSM
control method of either the device itself or the PCI host bridge.

Function 8, "Reset Delay," applies to the entire hierarchy below a PCI
host bridge.  If it returns one, the OS may assume that all devices in
the hierarchy have already completed power-on reset delays.

Function 9, "Device Readiness Durations," applies only to the object
where it is located.  It returns delay durations required after various
events if the device requires less time than the spec requires.  Delays
from this function take precedence over the Reset Delay function.

These \_DSM functions are defined by the draft ECN of January 28, 2014,
titled "ACPI additions for FW latency optimizations."

.. _`pci_msi_register_fwnode_provider`:

pci_msi_register_fwnode_provider
================================

.. c:function:: void pci_msi_register_fwnode_provider(struct fwnode_handle *(*fn)(struct device *))

    Register callback to retrieve fwnode

    :param struct fwnode_handle \*(\*fn)(struct device \*):
        Callback matching a device to a fwnode that identifies a PCI
        MSI domain.

.. _`pci_msi_register_fwnode_provider.description`:

Description
-----------

This should be called by irqchip driver, which is the parent of
the MSI domain to provide callback interface to query fwnode.

.. _`pci_host_bridge_acpi_msi_domain`:

pci_host_bridge_acpi_msi_domain
===============================

.. c:function:: struct irq_domain *pci_host_bridge_acpi_msi_domain(struct pci_bus *bus)

    Retrieve MSI domain of a PCI host bridge

    :param struct pci_bus \*bus:
        The PCI host bridge bus.

.. _`pci_host_bridge_acpi_msi_domain.description`:

Description
-----------

This function uses the callback function registered by
\ :c:func:`pci_msi_register_fwnode_provider`\  to retrieve the irq_domain with
type DOMAIN_BUS_PCI_MSI of the specified host bridge bus.
This returns NULL on error or when the domain is not found.

.. This file was automatic generated / don't edit.

