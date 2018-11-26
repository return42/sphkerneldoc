.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/pci-hotplug.c

.. _`pcibios_release_device`:

pcibios_release_device
======================

.. c:function:: void pcibios_release_device(struct pci_dev *dev)

    release PCI device

    :param dev:
        PCI device
    :type dev: struct pci_dev \*

.. _`pcibios_release_device.description`:

Description
-----------

The function is called before releasing the indicated PCI device.

.. _`pci_hp_remove_devices`:

pci_hp_remove_devices
=====================

.. c:function:: void pci_hp_remove_devices(struct pci_bus *bus)

    remove all devices under this bus

    :param bus:
        the indicated PCI bus
    :type bus: struct pci_bus \*

.. _`pci_hp_remove_devices.description`:

Description
-----------

Remove all of the PCI devices under this bus both from the
linux pci device tree, and from the powerpc EEH address cache.

.. _`pci_hp_add_devices`:

pci_hp_add_devices
==================

.. c:function:: void pci_hp_add_devices(struct pci_bus *bus)

    adds new pci devices to bus

    :param bus:
        the indicated PCI bus
    :type bus: struct pci_bus \*

.. _`pci_hp_add_devices.description`:

Description
-----------

This routine will find and fixup new pci devices under
the indicated bus. This routine presumes that there
might already be some devices under this bridge, so
it carefully tries to add only new devices.  (And that
is how this routine differs from other, similar pcibios
routines.)

.. This file was automatic generated / don't edit.

