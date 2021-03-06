.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/of.c

.. _`of_pci_get_devfn`:

of_pci_get_devfn
================

.. c:function:: int of_pci_get_devfn(struct device_node *np)

    Get device and function numbers for a device node

    :param np:
        device node
    :type np: struct device_node \*

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

    :param node:
        device node
    :type node: struct device_node \*

    :param res:
        address to a struct resource to return the bus-range
    :type res: struct resource \*

.. _`of_pci_parse_bus_range.description`:

Description
-----------

Returns 0 on success or a negative error-code on failure.

.. _`of_get_pci_domain_nr`:

of_get_pci_domain_nr
====================

.. c:function:: int of_get_pci_domain_nr(struct device_node *node)

    finding a property called "linux,pci-domain" of the given device node.

    :param node:
        device tree node with the domain information
    :type node: struct device_node \*

.. _`of_get_pci_domain_nr.description`:

Description
-----------

Returns the associated domain number from DT in the range [0-0xffff], or
a negative value if the required property is not found.

.. _`of_pci_get_max_link_speed`:

of_pci_get_max_link_speed
=========================

.. c:function:: int of_pci_get_max_link_speed(struct device_node *node)

    a property called "max-link-speed" of the given device node.

    :param node:
        device tree node with the max link speed information
    :type node: struct device_node \*

.. _`of_pci_get_max_link_speed.description`:

Description
-----------

Returns the associated max link speed from DT, or a negative value if the
required property is not found or is invalid.

.. _`of_pci_check_probe_only`:

of_pci_check_probe_only
=======================

.. c:function:: void of_pci_check_probe_only( void)

    Setup probe only mode if linux,pci-probe-only is present and valid

    :param void:
        no arguments
    :type void: 

.. _`devm_of_pci_get_host_bridge_resources`:

devm_of_pci_get_host_bridge_resources
=====================================

.. c:function:: int devm_of_pci_get_host_bridge_resources(struct device *dev, unsigned char busno, unsigned char bus_max, struct list_head *resources, resource_size_t *io_base)

    Resource-managed parsing of PCI host bridge resources from DT

    :param dev:
        host bridge device
    :type dev: struct device \*

    :param busno:
        bus number associated with the bridge root bus
    :type busno: unsigned char

    :param bus_max:
        maximum number of buses for this bridge
    :type bus_max: unsigned char

    :param resources:
        list where the range of resources will be added after DT parsing
    :type resources: struct list_head \*

    :param io_base:
        pointer to a variable that will contain on return the physical
        address for the start of the I/O range. Can be NULL if the caller doesn't
        expect I/O ranges to be present in the device tree.
    :type io_base: resource_size_t \*

.. _`devm_of_pci_get_host_bridge_resources.description`:

Description
-----------

This function will parse the "ranges" property of a PCI host bridge device
node and setup the resource mapping based on its content. It is expected
that the property conforms with the Power ePAPR document.

It returns zero if the range parsing has been successful or a standard error
value if it failed.

.. _`of_irq_parse_pci`:

of_irq_parse_pci
================

.. c:function:: int of_irq_parse_pci(const struct pci_dev *pdev, struct of_phandle_args *out_irq)

    Resolve the interrupt for a PCI device

    :param pdev:
        the device whose interrupt is to be resolved
    :type pdev: const struct pci_dev \*

    :param out_irq:
        structure of_irq filled by this function
    :type out_irq: struct of_phandle_args \*

.. _`of_irq_parse_pci.description`:

Description
-----------

This function resolves the PCI interrupt for a given PCI device. If a
device-node exists for a given pci_dev, it will use normal OF tree
walking. If not, it will implement standard swizzling and walk up the
PCI tree until an device-node is found, at which point it will finish
resolving using the OF tree walking.

.. _`of_irq_parse_and_map_pci`:

of_irq_parse_and_map_pci
========================

.. c:function:: int of_irq_parse_and_map_pci(const struct pci_dev *dev, u8 slot, u8 pin)

    Decode a PCI IRQ from the device tree and map to a VIRQ

    :param dev:
        The PCI device needing an IRQ
    :type dev: const struct pci_dev \*

    :param slot:
        PCI slot number; passed when used as map_irq callback. Unused
    :type slot: u8

    :param pin:
        PCI IRQ pin number; passed when used as map_irq callback. Unused
    :type pin: u8

.. _`of_irq_parse_and_map_pci.description`:

Description
-----------

\ ``slot``\  and \ ``pin``\  are unused, but included in the function so that this
function can be used directly as the map_irq callback to
\ :c:func:`pci_assign_irq`\  and struct pci_host_bridge.map_irq pointer

.. This file was automatic generated / don't edit.

