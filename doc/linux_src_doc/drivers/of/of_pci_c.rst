.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_pci.c

.. _`of_pci_get_devfn`:

of_pci_get_devfn
================

.. c:function:: int of_pci_get_devfn(struct device_node *np)

    Get device and function numbers for a device node

    :param struct device_node \*np:
        device node

.. _`of_pci_get_devfn.description`:

Description
-----------

Parses a standard 5-cell PCI resource and returns an 8-bit value that can
be passed to the \ :c:func:`PCI_SLOT`\  and \ :c:func:`PCI_FUNC`\  macros to extract the device
and function numbers respectively. On error a negative error code is
returned.

.. _`of_pci_parse_bus_range`:

of_pci_parse_bus_range
======================

.. c:function:: int of_pci_parse_bus_range(struct device_node *node, struct resource *res)

    parse the bus-range property of a PCI device

    :param struct device_node \*node:
        device node

    :param struct resource \*res:
        address to a struct resource to return the bus-range

.. _`of_pci_parse_bus_range.description`:

Description
-----------

Returns 0 on success or a negative error-code on failure.

.. _`of_get_pci_domain_nr`:

of_get_pci_domain_nr
====================

.. c:function:: int of_get_pci_domain_nr(struct device_node *node)

    finding a property called "linux,pci-domain" of the given device node.

    :param struct device_node \*node:
        device tree node with the domain information

.. _`of_get_pci_domain_nr.description`:

Description
-----------

Returns the associated domain number from DT in the range [0-0xffff], or
a negative value if the required property is not found.

.. _`of_pci_check_probe_only`:

of_pci_check_probe_only
=======================

.. c:function:: void of_pci_check_probe_only( void)

    Setup probe only mode if linux,pci-probe-only is present and valid

    :param  void:
        no arguments

.. _`of_pci_get_host_bridge_resources`:

of_pci_get_host_bridge_resources
================================

.. c:function:: int of_pci_get_host_bridge_resources(struct device_node *dev, unsigned char busno, unsigned char bus_max, struct list_head *resources, resource_size_t *io_base)

    Parse PCI host bridge resources from DT

    :param struct device_node \*dev:
        device node of the host bridge having the range property

    :param unsigned char busno:
        bus number associated with the bridge root bus

    :param unsigned char bus_max:
        maximum number of buses for this bridge

    :param struct list_head \*resources:
        list where the range of resources will be added after DT parsing

    :param resource_size_t \*io_base:
        pointer to a variable that will contain on return the physical
        address for the start of the I/O range. Can be NULL if the caller doesn't
        expect IO ranges to be present in the device tree.

.. _`of_pci_get_host_bridge_resources.description`:

Description
-----------

It is the caller's job to free the \ ``resources``\  list.

This function will parse the "ranges" property of a PCI host bridge device
node and setup the resource mapping based on its content. It is expected
that the property conforms with the Power ePAPR document.

It returns zero if the range parsing has been successful or a standard error
value if it failed.

.. This file was automatic generated / don't edit.

