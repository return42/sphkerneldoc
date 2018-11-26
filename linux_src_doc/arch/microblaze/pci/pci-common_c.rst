.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/microblaze/pci/pci-common.c

.. _`pci_process_bridge_of_ranges`:

pci_process_bridge_OF_ranges
============================

.. c:function:: void pci_process_bridge_OF_ranges(struct pci_controller *hose, struct device_node *dev, int primary)

    Parse PCI bridge resources from device tree

    :param hose:
        newly allocated pci_controller to be setup
    :type hose: struct pci_controller \*

    :param dev:
        device node of the host bridge
    :type dev: struct device_node \*

    :param primary:
        set if primary bus (32 bits only, soon to be deprecated)
    :type primary: int

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

- We can only cope with all memory ranges having the same offset
between CPU addresses and PCI addresses. Unfortunately, some bridges
are setup for a large 1:1 mapping along with a small "window" which
maps PCI address 0 to some arbitrary high address of the CPU space in
order to give access to the ISA memory hole.
The way out of here that I've chosen for now is to always set the
offset based on the first resource found, then override it if we
have a different offset and the previous was set by an ISA hole.

- Some busses have IO space not starting at 0, which causes trouble with
the way we do our IO resource renumbering. The code somewhat deals with
it for 64 bits but I would expect problems on 32 bits.

- Some 32 bits platforms such as 4xx can have physical space larger than
32 bits so we need to use 64 bits values for the parsing

.. This file was automatic generated / don't edit.

