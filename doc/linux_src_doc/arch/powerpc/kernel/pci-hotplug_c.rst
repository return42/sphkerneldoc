.. -*- coding: utf-8; mode: rst -*-

=============
pci-hotplug.c
=============


.. _`pcibios_release_device`:

pcibios_release_device
======================

.. c:function:: void pcibios_release_device (struct pci_dev *dev)

    release PCI device

    :param struct pci_dev \*dev:
        PCI device



.. _`pcibios_release_device.description`:

Description
-----------

The function is called before releasing the indicated PCI device.



.. _`pcibios_remove_pci_devices`:

pcibios_remove_pci_devices
==========================

.. c:function:: void pcibios_remove_pci_devices (struct pci_bus *bus)

    remove all devices under this bus

    :param struct pci_bus \*bus:
        the indicated PCI bus



.. _`pcibios_remove_pci_devices.description`:

Description
-----------

Remove all of the PCI devices under this bus both from the
linux pci device tree, and from the powerpc EEH address cache.



.. _`pcibios_add_pci_devices`:

pcibios_add_pci_devices
=======================

.. c:function:: void pcibios_add_pci_devices (struct pci_bus *bus)

    adds new pci devices to bus

    :param struct pci_bus \*bus:
        the indicated PCI bus



.. _`pcibios_add_pci_devices.description`:

Description
-----------

This routine will find and fixup new pci devices under
the indicated bus. This routine presumes that there
might already be some devices under this bridge, so
it carefully tries to add only new devices.  (And that
is how this routine differs from other, similar pcibios
routines.)

