.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/bus.c

.. _`pci_bus_alloc_resource`:

pci_bus_alloc_resource
======================

.. c:function:: int pci_bus_alloc_resource(struct pci_bus *bus, struct resource *res, resource_size_t size, resource_size_t align, resource_size_t min, unsigned long type_mask, resource_size_t (*alignf)(void *, const struct resource *, resource_size_t, resource_size_t), void *alignf_data)

    allocate a resource from a parent bus

    :param bus:
        PCI bus
    :type bus: struct pci_bus \*

    :param res:
        resource to allocate
    :type res: struct resource \*

    :param size:
        size of resource to allocate
    :type size: resource_size_t

    :param align:
        alignment of resource to allocate
    :type align: resource_size_t

    :param min:
        minimum /proc/iomem address to allocate
    :type min: resource_size_t

    :param type_mask:
        IORESOURCE_* type flags
    :type type_mask: unsigned long

    :param resource_size_t (\*alignf)(void \*, const struct resource \*, resource_size_t, resource_size_t):
        resource alignment function

    :param alignf_data:
        data argument for resource alignment function
    :type alignf_data: void \*

.. _`pci_bus_alloc_resource.description`:

Description
-----------

Given the PCI bus a device resides on, the size, minimum address,
alignment and type, try to find an acceptable resource allocation
for a specific device resource.

.. _`pci_bus_add_device`:

pci_bus_add_device
==================

.. c:function:: void pci_bus_add_device(struct pci_dev *dev)

    start driver for a single device

    :param dev:
        device to add
    :type dev: struct pci_dev \*

.. _`pci_bus_add_device.description`:

Description
-----------

This adds add sysfs entries and start device drivers

.. _`pci_bus_add_devices`:

pci_bus_add_devices
===================

.. c:function:: void pci_bus_add_devices(const struct pci_bus *bus)

    start driver for PCI devices

    :param bus:
        bus to check for new devices
    :type bus: const struct pci_bus \*

.. _`pci_bus_add_devices.description`:

Description
-----------

Start driver for PCI devices and add some sysfs entries.

.. This file was automatic generated / don't edit.

