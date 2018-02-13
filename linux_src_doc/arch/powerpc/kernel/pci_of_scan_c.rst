.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/pci_of_scan.c

.. _`get_int_prop`:

get_int_prop
============

.. c:function:: u32 get_int_prop(struct device_node *np, const char *name, u32 def)

    Decode a u32 from a device tree property

    :param struct device_node \*np:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param u32 def:
        *undescribed*

.. _`pci_parse_of_flags`:

pci_parse_of_flags
==================

.. c:function:: unsigned int pci_parse_of_flags(u32 addr0, int bridge)

    Parse the flags cell of a device tree PCI address

    :param u32 addr0:
        value of 1st cell of a device tree PCI address.

    :param int bridge:
        Set this flag if the address is from a bridge 'ranges' property

.. _`of_pci_parse_addrs`:

of_pci_parse_addrs
==================

.. c:function:: void of_pci_parse_addrs(struct device_node *node, struct pci_dev *dev)

    Parse PCI addresses assigned in the device tree node

    :param struct device_node \*node:
        device tree node for the PCI device

    :param struct pci_dev \*dev:
        pci_dev structure for the device

.. _`of_pci_parse_addrs.description`:

Description
-----------

This function parses the 'assigned-addresses' property of a PCI devices'
device tree node and writes them into the associated pci_dev structure.

.. _`of_create_pci_dev`:

of_create_pci_dev
=================

.. c:function:: struct pci_dev *of_create_pci_dev(struct device_node *node, struct pci_bus *bus, int devfn)

    Given a device tree node on a pci bus, create a pci_dev

    :param struct device_node \*node:
        device tree node pointer

    :param struct pci_bus \*bus:
        bus the device is sitting on

    :param int devfn:
        PCI function number, extracted from device tree by caller.

.. _`of_scan_pci_bridge`:

of_scan_pci_bridge
==================

.. c:function:: void of_scan_pci_bridge(struct pci_dev *dev)

    Set up a PCI bridge and scan for child nodes

    :param struct pci_dev \*dev:
        pci_dev structure for the bridge

.. _`of_scan_pci_bridge.description`:

Description
-----------

\ :c:func:`of_scan_bus`\  calls this routine for each PCI bridge that it finds, and
this routine in turn call \ :c:func:`of_scan_bus`\  recusively to scan for more child
devices.

.. _`__of_scan_bus`:

\__of_scan_bus
==============

.. c:function:: void __of_scan_bus(struct device_node *node, struct pci_bus *bus, int rescan_existing)

    given a PCI bus node, setup bus and scan for child devices

    :param struct device_node \*node:
        device tree node for the PCI bus

    :param struct pci_bus \*bus:
        pci_bus structure for the PCI bus

    :param int rescan_existing:
        Flag indicating bus has already been set up

.. _`of_scan_bus`:

of_scan_bus
===========

.. c:function:: void of_scan_bus(struct device_node *node, struct pci_bus *bus)

    given a PCI bus node, setup bus and scan for child devices

    :param struct device_node \*node:
        device tree node for the PCI bus

    :param struct pci_bus \*bus:
        pci_bus structure for the PCI bus

.. _`of_rescan_bus`:

of_rescan_bus
=============

.. c:function:: void of_rescan_bus(struct device_node *node, struct pci_bus *bus)

    given a PCI bus node, scan for child devices

    :param struct device_node \*node:
        device tree node for the PCI bus

    :param struct pci_bus \*bus:
        pci_bus structure for the PCI bus

.. _`of_rescan_bus.description`:

Description
-----------

Same as of_scan_bus, but for a pci_bus structure that has already been
setup.

.. This file was automatic generated / don't edit.

