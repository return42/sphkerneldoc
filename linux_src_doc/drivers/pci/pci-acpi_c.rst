.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci-acpi.c

.. _`pciehp_is_native`:

pciehp_is_native
================

.. c:function:: bool pciehp_is_native(struct pci_dev *bridge)

    Check whether a hotplug port is handled by the OS

    :param bridge:
        Hotplug port to check
    :type bridge: struct pci_dev \*

.. _`pciehp_is_native.description`:

Description
-----------

Returns true if the given \ ``bridge``\  is handled by the native PCIe hotplug
driver.

.. _`shpchp_is_native`:

shpchp_is_native
================

.. c:function:: bool shpchp_is_native(struct pci_dev *bridge)

    Check whether a hotplug port is handled by the OS

    :param bridge:
        Hotplug port to check
    :type bridge: struct pci_dev \*

.. _`shpchp_is_native.description`:

Description
-----------

Returns true if the given \ ``bridge``\  is handled by the native SHPC hotplug
driver.

.. _`pci_acpi_wake_bus`:

pci_acpi_wake_bus
=================

.. c:function:: void pci_acpi_wake_bus(struct acpi_device_wakeup_context *context)

    Root bus wakeup notification fork function.

    :param context:
        Device wakeup context.
    :type context: struct acpi_device_wakeup_context \*

.. _`pci_acpi_wake_dev`:

pci_acpi_wake_dev
=================

.. c:function:: void pci_acpi_wake_dev(struct acpi_device_wakeup_context *context)

    PCI device wakeup notification work function.

    :param context:
        Device wakeup context.
    :type context: struct acpi_device_wakeup_context \*

.. _`pci_acpi_add_bus_pm_notifier`:

pci_acpi_add_bus_pm_notifier
============================

.. c:function:: acpi_status pci_acpi_add_bus_pm_notifier(struct acpi_device *dev)

    Register PM notifier for root PCI bus.

    :param dev:
        PCI root bridge ACPI device.
    :type dev: struct acpi_device \*

.. _`pci_acpi_add_pm_notifier`:

pci_acpi_add_pm_notifier
========================

.. c:function:: acpi_status pci_acpi_add_pm_notifier(struct acpi_device *dev, struct pci_dev *pci_dev)

    Register PM notifier for given PCI device.

    :param dev:
        ACPI device to add the notifier for.
    :type dev: struct acpi_device \*

    :param pci_dev:
        PCI device to check for the PME status if an event is signaled.
    :type pci_dev: struct pci_dev \*

.. _`pci_acpi_optimize_delay`:

pci_acpi_optimize_delay
=======================

.. c:function:: void pci_acpi_optimize_delay(struct pci_dev *pdev, acpi_handle handle)

    optimize PCI D3 and D3cold delay from ACPI

    :param pdev:
        the PCI device whose delay is to be updated
    :type pdev: struct pci_dev \*

    :param handle:
        ACPI handle of this device
    :type handle: acpi_handle

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

    :param bus:
        The PCI host bridge bus.
    :type bus: struct pci_bus \*

.. _`pci_host_bridge_acpi_msi_domain.description`:

Description
-----------

This function uses the callback function registered by
\ :c:func:`pci_msi_register_fwnode_provider`\  to retrieve the irq_domain with
type DOMAIN_BUS_PCI_MSI of the specified host bridge bus.
This returns NULL on error or when the domain is not found.

.. This file was automatic generated / don't edit.

