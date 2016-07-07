.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/platform.c

.. _`of_find_device_by_node`:

of_find_device_by_node
======================

.. c:function:: struct platform_device *of_find_device_by_node(struct device_node *np)

    Find the platform_device associated with a node

    :param struct device_node \*np:
        Pointer to device tree node

.. _`of_find_device_by_node.description`:

Description
-----------

Returns platform_device pointer, or NULL if not found

.. _`of_device_make_bus_id`:

of_device_make_bus_id
=====================

.. c:function:: void of_device_make_bus_id(struct device *dev)

    Use the device node data to assign a unique name

    :param struct device \*dev:
        pointer to device structure that is linked to a device tree node

.. _`of_device_make_bus_id.description`:

Description
-----------

This routine will first try using the translated bus address to
derive a unique name. If it cannot, then it will prepend names from
parent nodes until a unique name can be derived.

.. _`of_device_alloc`:

of_device_alloc
===============

.. c:function:: struct platform_device *of_device_alloc(struct device_node *np, const char *bus_id, struct device *parent)

    Allocate and initialize an of_device

    :param struct device_node \*np:
        device node to assign to device

    :param const char \*bus_id:
        Name to assign to the device.  May be null to use default name.

    :param struct device \*parent:
        Parent device.

.. _`of_platform_device_create_pdata`:

of_platform_device_create_pdata
===============================

.. c:function:: struct platform_device *of_platform_device_create_pdata(struct device_node *np, const char *bus_id, void *platform_data, struct device *parent)

    Alloc, initialize and register an of_device

    :param struct device_node \*np:
        pointer to node to create device for

    :param const char \*bus_id:
        name to assign device

    :param void \*platform_data:
        pointer to populate platform_data pointer with

    :param struct device \*parent:
        Linux device model parent device.

.. _`of_platform_device_create_pdata.description`:

Description
-----------

Returns pointer to created platform device, or NULL if a device was not
registered.  Unavailable devices will not get registered.

.. _`of_platform_device_create`:

of_platform_device_create
=========================

.. c:function:: struct platform_device *of_platform_device_create(struct device_node *np, const char *bus_id, struct device *parent)

    Alloc, initialize and register an of_device

    :param struct device_node \*np:
        pointer to node to create device for

    :param const char \*bus_id:
        name to assign device

    :param struct device \*parent:
        Linux device model parent device.

.. _`of_platform_device_create.description`:

Description
-----------

Returns pointer to created platform device, or NULL if a device was not
registered.  Unavailable devices will not get registered.

.. _`of_dev_lookup`:

of_dev_lookup
=============

.. c:function:: const struct of_dev_auxdata *of_dev_lookup(const struct of_dev_auxdata *lookup, struct device_node *np)

    Given a device node, lookup the preferred Linux name

    :param const struct of_dev_auxdata \*lookup:
        *undescribed*

    :param struct device_node \*np:
        *undescribed*

.. _`of_platform_bus_create`:

of_platform_bus_create
======================

.. c:function:: int of_platform_bus_create(struct device_node *bus, const struct of_device_id *matches, const struct of_dev_auxdata *lookup, struct device *parent, bool strict)

    Create a device for a node and its children.

    :param struct device_node \*bus:
        device node of the bus to instantiate

    :param const struct of_device_id \*matches:
        match table for bus nodes

    :param const struct of_dev_auxdata \*lookup:
        auxdata table for matching id and platform_data with device nodes

    :param struct device \*parent:
        parent for new device, or NULL for top level.

    :param bool strict:
        require compatible property

.. _`of_platform_bus_create.description`:

Description
-----------

Creates a platform_device for the provided device_node, and optionally
recursively create devices for all the child nodes.

.. _`of_platform_bus_probe`:

of_platform_bus_probe
=====================

.. c:function:: int of_platform_bus_probe(struct device_node *root, const struct of_device_id *matches, struct device *parent)

    Probe the device-tree for platform buses

    :param struct device_node \*root:
        parent of the first level to probe or NULL for the root of the tree

    :param const struct of_device_id \*matches:
        match table for bus nodes

    :param struct device \*parent:
        parent to hook devices from, NULL for toplevel

.. _`of_platform_bus_probe.description`:

Description
-----------

Note that children of the provided root are not instantiated as devices
unless the specified root itself matches the bus list and is not NULL.

.. _`of_platform_populate`:

of_platform_populate
====================

.. c:function:: int of_platform_populate(struct device_node *root, const struct of_device_id *matches, const struct of_dev_auxdata *lookup, struct device *parent)

    Populate platform_devices from device tree data

    :param struct device_node \*root:
        parent of the first level to probe or NULL for the root of the tree

    :param const struct of_device_id \*matches:
        match table, NULL to use the default

    :param const struct of_dev_auxdata \*lookup:
        auxdata table for matching id and platform_data with device nodes

    :param struct device \*parent:
        parent to hook devices from, NULL for toplevel

.. _`of_platform_populate.description`:

Description
-----------

Similar to \ :c:func:`of_platform_bus_probe`\ , this function walks the device tree
and creates devices from nodes.  It differs in that it follows the modern
convention of requiring all device nodes to have a 'compatible' property,
and it is suitable for creating devices which are children of the root
node (of_platform_bus_probe will only create children of the root which
are selected by the \ ``matches``\  argument).

New board support should be using this function instead of
\ :c:func:`of_platform_bus_probe`\ .

Returns 0 on success, < 0 on failure.

.. _`of_platform_depopulate`:

of_platform_depopulate
======================

.. c:function:: void of_platform_depopulate(struct device *parent)

    Remove devices populated from device tree

    :param struct device \*parent:
        device which children will be removed

.. _`of_platform_depopulate.description`:

Description
-----------

Complementary to \ :c:func:`of_platform_populate`\ , this function removes children
of the given device (and, recurrently, their children) that have been
created from their respective device tree nodes (and only those,
leaving others - eg. manually created - unharmed).

Returns 0 when all children devices have been removed or
-EBUSY when some children remained.

.. This file was automatic generated / don't edit.

