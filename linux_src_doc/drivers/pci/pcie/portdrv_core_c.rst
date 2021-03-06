.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pcie/portdrv_core.c

.. _`release_pcie_device`:

release_pcie_device
===================

.. c:function:: void release_pcie_device(struct device *dev)

    free PCI Express port service device structure

    :param dev:
        Port service device to release
    :type dev: struct device \*

.. _`release_pcie_device.description`:

Description
-----------

Invoked automatically when device is being removed in response to
device_unregister(dev).  Release all resources being claimed.

.. _`pcie_port_enable_irq_vec`:

pcie_port_enable_irq_vec
========================

.. c:function:: int pcie_port_enable_irq_vec(struct pci_dev *dev, int *irqs, int mask)

    try to set up MSI-X or MSI as interrupt mode for given port

    :param dev:
        PCI Express port to handle
    :type dev: struct pci_dev \*

    :param irqs:
        Array of interrupt vectors to populate
    :type irqs: int \*

    :param mask:
        Bitmask of port capabilities returned by \ :c:func:`get_port_device_capability`\ 
    :type mask: int

.. _`pcie_port_enable_irq_vec.return-value`:

Return value
------------

0 on success, error code on failure

.. _`pcie_init_service_irqs`:

pcie_init_service_irqs
======================

.. c:function:: int pcie_init_service_irqs(struct pci_dev *dev, int *irqs, int mask)

    initialize irqs for PCI Express port services

    :param dev:
        PCI Express port to handle
    :type dev: struct pci_dev \*

    :param irqs:
        Array of irqs to populate
    :type irqs: int \*

    :param mask:
        Bitmask of port capabilities returned by \ :c:func:`get_port_device_capability`\ 
    :type mask: int

.. _`pcie_init_service_irqs.return-value`:

Return value
------------

Interrupt mode associated with the port

.. _`get_port_device_capability`:

get_port_device_capability
==========================

.. c:function:: int get_port_device_capability(struct pci_dev *dev)

    discover capabilities of a PCI Express port

    :param dev:
        PCI Express port to examine
    :type dev: struct pci_dev \*

.. _`get_port_device_capability.description`:

Description
-----------

The capabilities are read from the port's PCI Express configuration registers
as described in PCI Express Base Specification 1.0a sections 7.8.2, 7.8.9 and
7.9 - 7.11.

.. _`get_port_device_capability.return-value`:

Return value
------------

Bitmask of discovered port capabilities

.. _`pcie_device_init`:

pcie_device_init
================

.. c:function:: int pcie_device_init(struct pci_dev *pdev, int service, int irq)

    allocate and initialize PCI Express port service device

    :param pdev:
        PCI Express port to associate the service device with
    :type pdev: struct pci_dev \*

    :param service:
        Type of service to associate with the service device
    :type service: int

    :param irq:
        Interrupt vector to associate with the service device
    :type irq: int

.. _`pcie_port_device_register`:

pcie_port_device_register
=========================

.. c:function:: int pcie_port_device_register(struct pci_dev *dev)

    register PCI Express port

    :param dev:
        PCI Express port to register
    :type dev: struct pci_dev \*

.. _`pcie_port_device_register.description`:

Description
-----------

Allocate the port extension structure and register services associated with
the port.

.. _`pcie_port_device_suspend`:

pcie_port_device_suspend
========================

.. c:function:: int pcie_port_device_suspend(struct device *dev)

    suspend port services associated with a PCIe port

    :param dev:
        PCI Express port to handle
    :type dev: struct device \*

.. _`pcie_port_device_resume`:

pcie_port_device_resume
=======================

.. c:function:: int pcie_port_device_resume(struct device *dev)

    resume port services associated with a PCIe port

    :param dev:
        PCI Express port to handle
    :type dev: struct device \*

.. _`pcie_port_device_runtime_suspend`:

pcie_port_device_runtime_suspend
================================

.. c:function:: int pcie_port_device_runtime_suspend(struct device *dev)

    runtime suspend port services

    :param dev:
        PCI Express port to handle
    :type dev: struct device \*

.. _`pcie_port_device_runtime_resume`:

pcie_port_device_runtime_resume
===============================

.. c:function:: int pcie_port_device_runtime_resume(struct device *dev)

    runtime resume port services

    :param dev:
        PCI Express port to handle
    :type dev: struct device \*

.. _`pcie_port_find_service`:

pcie_port_find_service
======================

.. c:function:: struct pcie_port_service_driver *pcie_port_find_service(struct pci_dev *dev, u32 service)

    find the service driver

    :param dev:
        PCI Express port the service is associated with
    :type dev: struct pci_dev \*

    :param service:
        Service to find
    :type service: u32

.. _`pcie_port_find_service.description`:

Description
-----------

Find PCI Express port service driver associated with given service

.. _`pcie_port_find_device`:

pcie_port_find_device
=====================

.. c:function:: struct device *pcie_port_find_device(struct pci_dev *dev, u32 service)

    find the struct device

    :param dev:
        PCI Express port the service is associated with
    :type dev: struct pci_dev \*

    :param service:
        For the service to find
    :type service: u32

.. _`pcie_port_find_device.description`:

Description
-----------

Find the struct device associated with given service on a pci_dev

.. _`pcie_port_device_remove`:

pcie_port_device_remove
=======================

.. c:function:: void pcie_port_device_remove(struct pci_dev *dev)

    unregister PCI Express port service devices

    :param dev:
        PCI Express port the service devices to unregister are associated with
    :type dev: struct pci_dev \*

.. _`pcie_port_device_remove.description`:

Description
-----------

Remove PCI Express port service devices associated with given port and
disable MSI-X or MSI for the port.

.. _`pcie_port_probe_service`:

pcie_port_probe_service
=======================

.. c:function:: int pcie_port_probe_service(struct device *dev)

    probe driver for given PCI Express port service

    :param dev:
        PCI Express port service device to probe against
    :type dev: struct device \*

.. _`pcie_port_probe_service.description`:

Description
-----------

If PCI Express port service driver is registered with
\ :c:func:`pcie_port_service_register`\ , this function will be called by the driver core
whenever match is found between the driver and a port service device.

.. _`pcie_port_remove_service`:

pcie_port_remove_service
========================

.. c:function:: int pcie_port_remove_service(struct device *dev)

    detach driver from given PCI Express port service

    :param dev:
        PCI Express port service device to handle
    :type dev: struct device \*

.. _`pcie_port_remove_service.description`:

Description
-----------

If PCI Express port service driver is registered with
\ :c:func:`pcie_port_service_register`\ , this function will be called by the driver core
when \ :c:func:`device_unregister`\  is called for the port service device associated
with the driver.

.. _`pcie_port_shutdown_service`:

pcie_port_shutdown_service
==========================

.. c:function:: void pcie_port_shutdown_service(struct device *dev)

    shut down given PCI Express port service

    :param dev:
        PCI Express port service device to handle
    :type dev: struct device \*

.. _`pcie_port_shutdown_service.description`:

Description
-----------

If PCI Express port service driver is registered with
\ :c:func:`pcie_port_service_register`\ , this function will be called by the driver core
when \ :c:func:`device_shutdown`\  is called for the port service device associated
with the driver.

.. _`pcie_port_service_register`:

pcie_port_service_register
==========================

.. c:function:: int pcie_port_service_register(struct pcie_port_service_driver *new)

    register PCI Express port service driver

    :param new:
        PCI Express port service driver to register
    :type new: struct pcie_port_service_driver \*

.. _`pcie_port_service_unregister`:

pcie_port_service_unregister
============================

.. c:function:: void pcie_port_service_unregister(struct pcie_port_service_driver *drv)

    unregister PCI Express port service driver

    :param drv:
        PCI Express port service driver to unregister
    :type drv: struct pcie_port_service_driver \*

.. This file was automatic generated / don't edit.

