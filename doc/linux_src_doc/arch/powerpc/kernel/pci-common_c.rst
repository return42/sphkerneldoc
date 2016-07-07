.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/pci-common.c

.. _`pci_process_bridge_of_ranges`:

pci_process_bridge_OF_ranges
============================

.. c:function:: void pci_process_bridge_OF_ranges(struct pci_controller *hose, struct device_node *dev, int primary)

    Parse PCI bridge resources from device tree

    :param struct pci_controller \*hose:
        newly allocated pci_controller to be setup

    :param struct device_node \*dev:
        device node of the host bridge

    :param int primary:
        set if primary bus (32 bits only, soon to be deprecated)

.. _`pci_process_bridge_of_ranges.description`:

Description
-----------

This function will parse the "ranges" property of a PCI host bridge device
node and setup the resource mapping of a pci controller based on its
content.

Life would be boring if it wasn't for a few issues that we have to deal

.. _`pci_process_bridge_of_ranges.with-here`:

with here
---------


- We can only cope with one IO space range and up to 3 Memory space
ranges. However, some machines (thanks Apple !) tend to split their
space into lots of small contiguous ranges. So we have to coalesce.

- Some busses have IO space not starting at 0, which causes trouble with
the way we do our IO resource renumbering. The code somewhat deals with
it for 64 bits but I would expect problems on 32 bits.

- Some 32 bits platforms such as 4xx can have physical space larger than
32 bits so we need to use 64 bits values for the parsing

.. _`pcibios_scan_phb`:

pcibios_scan_phb
================

.. c:function:: void pcibios_scan_phb(struct pci_controller *hose)

    Given a pci_controller, setup and scan the PCI bus

    :param struct pci_controller \*hose:
        Pointer to the PCI host controller instance structure

.. This file was automatic generated / don't edit.

