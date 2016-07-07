.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/irq.c

.. _`irq_of_parse_and_map`:

irq_of_parse_and_map
====================

.. c:function:: unsigned int irq_of_parse_and_map(struct device_node *dev, int index)

    Parse and map an interrupt into linux virq space

    :param struct device_node \*dev:
        Device node of the device whose interrupt is to be mapped

    :param int index:
        Index of the interrupt to map

.. _`irq_of_parse_and_map.description`:

Description
-----------

This function is a wrapper that chains \ :c:func:`of_irq_parse_one`\  and
\ :c:func:`irq_create_of_mapping`\  to make things easier to callers

.. _`of_irq_find_parent`:

of_irq_find_parent
==================

.. c:function:: struct device_node *of_irq_find_parent(struct device_node *child)

    Given a device node, find its interrupt parent node

    :param struct device_node \*child:
        pointer to device node

.. _`of_irq_find_parent.description`:

Description
-----------

Returns a pointer to the interrupt parent node, or NULL if the interrupt
parent could not be determined.

.. _`of_irq_parse_raw`:

of_irq_parse_raw
================

.. c:function:: int of_irq_parse_raw(const __be32 *addr, struct of_phandle_args *out_irq)

    Low level interrupt tree parsing

    :param const __be32 \*addr:
        address specifier (start of "reg" property of the device) in be32 format

    :param struct of_phandle_args \*out_irq:
        structure of_irq updated by this function

.. _`of_irq_parse_raw.description`:

Description
-----------

Returns 0 on success and a negative number on error

This function is a low-level interrupt tree walking function. It
can be used to do a partial walk with synthetized reg and interrupts
properties, for example when resolving PCI interrupts when no device
node exist for the parent. It takes an interrupt specifier structure as
input, walks the tree looking for any interrupt-map properties, translates
the specifier for each map, and then returns the translated map.

.. _`of_irq_parse_one`:

of_irq_parse_one
================

.. c:function:: int of_irq_parse_one(struct device_node *device, int index, struct of_phandle_args *out_irq)

    Resolve an interrupt for a device

    :param struct device_node \*device:
        the device whose interrupt is to be resolved

    :param int index:
        index of the interrupt to resolve

    :param struct of_phandle_args \*out_irq:
        structure of_irq filled by this function

.. _`of_irq_parse_one.description`:

Description
-----------

This function resolves an interrupt for a node by walking the interrupt tree,
finding which interrupt controller node it is attached to, and returning the
interrupt specifier that can be used to retrieve a Linux IRQ number.

.. _`of_irq_to_resource`:

of_irq_to_resource
==================

.. c:function:: int of_irq_to_resource(struct device_node *dev, int index, struct resource *r)

    Decode a node's IRQ and return it as a resource

    :param struct device_node \*dev:
        pointer to device tree node

    :param int index:
        zero-based index of the irq

    :param struct resource \*r:
        pointer to resource structure to return result into.

.. _`of_irq_get`:

of_irq_get
==========

.. c:function:: int of_irq_get(struct device_node *dev, int index)

    Decode a node's IRQ and return it as a Linux irq number

    :param struct device_node \*dev:
        pointer to device tree node

    :param int index:
        zero-based index of the irq

.. _`of_irq_get.description`:

Description
-----------

Returns Linux irq number on success, or -EPROBE_DEFER if the irq domain
is not yet created.

.. _`of_irq_get_byname`:

of_irq_get_byname
=================

.. c:function:: int of_irq_get_byname(struct device_node *dev, const char *name)

    Decode a node's IRQ and return it as a Linux irq number

    :param struct device_node \*dev:
        pointer to device tree node

    :param const char \*name:
        irq name

.. _`of_irq_get_byname.description`:

Description
-----------

Returns Linux irq number on success, or -EPROBE_DEFER if the irq domain
is not yet created, or error code in case of any other failure.

.. _`of_irq_count`:

of_irq_count
============

.. c:function:: int of_irq_count(struct device_node *dev)

    Count the number of IRQs a node uses

    :param struct device_node \*dev:
        pointer to device tree node

.. _`of_irq_to_resource_table`:

of_irq_to_resource_table
========================

.. c:function:: int of_irq_to_resource_table(struct device_node *dev, struct resource *res, int nr_irqs)

    Fill in resource table with node's IRQ info

    :param struct device_node \*dev:
        pointer to device tree node

    :param struct resource \*res:
        array of resources to fill in

    :param int nr_irqs:
        the number of IRQs (and upper bound for num of \ ``res``\  elements)

.. _`of_irq_to_resource_table.description`:

Description
-----------

Returns the size of the filled in table (up to \ ``nr_irqs``\ ).

.. _`of_irq_init`:

of_irq_init
===========

.. c:function:: void of_irq_init(const struct of_device_id *matches)

    Scan and init matching interrupt controllers in DT

    :param const struct of_device_id \*matches:
        0 terminated array of nodes to match and init function to call

.. _`of_irq_init.description`:

Description
-----------

This function scans the device tree for matching interrupt controller nodes,
and calls their initialization functions in order with parents first.

.. _`of_msi_map_rid`:

of_msi_map_rid
==============

.. c:function:: u32 of_msi_map_rid(struct device *dev, struct device_node *msi_np, u32 rid_in)

    Map a MSI requester ID for a device.

    :param struct device \*dev:
        device for which the mapping is to be done.

    :param struct device_node \*msi_np:
        device node of the expected msi controller.

    :param u32 rid_in:
        unmapped MSI requester ID for the device.

.. _`of_msi_map_rid.description`:

Description
-----------

Walk up the device hierarchy looking for devices with a "msi-map"
property.  If found, apply the mapping to \ ``rid_in``\ .

Returns the mapped MSI requester ID.

.. _`of_msi_map_get_device_domain`:

of_msi_map_get_device_domain
============================

.. c:function:: struct irq_domain *of_msi_map_get_device_domain(struct device *dev, u32 rid)

    Use msi-map to find the relevant MSI domain

    :param struct device \*dev:
        device for which the mapping is to be done.

    :param u32 rid:
        Requester ID for the device.

.. _`of_msi_map_get_device_domain.description`:

Description
-----------

Walk up the device hierarchy looking for devices with a "msi-map"
property.

.. _`of_msi_map_get_device_domain.return`:

Return
------

the MSI domain for this device (or NULL on failure)

.. _`of_msi_get_domain`:

of_msi_get_domain
=================

.. c:function:: struct irq_domain *of_msi_get_domain(struct device *dev, struct device_node *np, enum irq_domain_bus_token token)

    Use msi-parent to find the relevant MSI domain

    :param struct device \*dev:
        device for which the domain is requested

    :param struct device_node \*np:
        device node for \ ``dev``\ 

    :param enum irq_domain_bus_token token:
        bus type for this domain

.. _`of_msi_get_domain.description`:

Description
-----------

Parse the msi-parent property (both the simple and the complex
versions), and returns the corresponding MSI domain.

.. _`of_msi_get_domain.return`:

Return
------

the MSI domain for this device (or NULL on failure).

.. _`of_msi_configure`:

of_msi_configure
================

.. c:function:: void of_msi_configure(struct device *dev, struct device_node *np)

    Set the msi_domain field of a device

    :param struct device \*dev:
        device structure to associate with an MSI irq domain

    :param struct device_node \*np:
        device node for that device

.. This file was automatic generated / don't edit.

