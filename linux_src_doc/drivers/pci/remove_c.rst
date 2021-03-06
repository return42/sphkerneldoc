.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/remove.c

.. _`pci_stop_and_remove_bus_device`:

pci_stop_and_remove_bus_device
==============================

.. c:function:: void pci_stop_and_remove_bus_device(struct pci_dev *dev)

    remove a PCI device and any children

    :param dev:
        the device to remove
    :type dev: struct pci_dev \*

.. _`pci_stop_and_remove_bus_device.description`:

Description
-----------

Remove a PCI device from the device lists, informing the drivers
that the device has been removed.  We also remove any subordinate
buses and children in a depth-first manner.

For each device we remove, delete the device structure from the
device lists, remove the /proc entry, and notify userspace
(/sbin/hotplug).

.. This file was automatic generated / don't edit.

