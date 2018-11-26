.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/of_mdio.c

.. _`of_mdiobus_register`:

of_mdiobus_register
===================

.. c:function:: int of_mdiobus_register(struct mii_bus *mdio, struct device_node *np)

    Register mii_bus and create PHYs from the device tree

    :param mdio:
        pointer to mii_bus structure
    :type mdio: struct mii_bus \*

    :param np:
        pointer to device_node of MDIO bus.
    :type np: struct device_node \*

.. _`of_mdiobus_register.description`:

Description
-----------

This function registers the mii_bus structure and registers a phy_device
for each child node of \ ``np``\ .

.. _`of_phy_find_device`:

of_phy_find_device
==================

.. c:function:: struct phy_device *of_phy_find_device(struct device_node *phy_np)

    Give a PHY node, find the phy_device

    :param phy_np:
        Pointer to the phy's device tree node
    :type phy_np: struct device_node \*

.. _`of_phy_find_device.description`:

Description
-----------

If successful, returns a pointer to the phy_device with the embedded
struct device refcount incremented by one, or NULL on failure.

.. _`of_phy_connect`:

of_phy_connect
==============

.. c:function:: struct phy_device *of_phy_connect(struct net_device *dev, struct device_node *phy_np, void (*hndlr)(struct net_device *), u32 flags, phy_interface_t iface)

    Connect to the phy described in the device tree

    :param dev:
        pointer to net_device claiming the phy
    :type dev: struct net_device \*

    :param phy_np:
        Pointer to device tree node for the PHY
    :type phy_np: struct device_node \*

    :param void (\*hndlr)(struct net_device \*):
        Link state callback for the network device

    :param flags:
        flags to pass to the PHY
    :type flags: u32

    :param iface:
        PHY data interface type
    :type iface: phy_interface_t

.. _`of_phy_connect.description`:

Description
-----------

If successful, returns a pointer to the phy_device with the embedded
struct device refcount incremented by one, or NULL on failure. The
refcount must be dropped by calling \ :c:func:`phy_disconnect`\  or \ :c:func:`phy_detach`\ .

.. _`of_phy_get_and_connect`:

of_phy_get_and_connect
======================

.. c:function:: struct phy_device *of_phy_get_and_connect(struct net_device *dev, struct device_node *np, void (*hndlr)(struct net_device *))

    - Get phy node and connect to the phy described in the device tree

    :param dev:
        pointer to net_device claiming the phy
    :type dev: struct net_device \*

    :param np:
        Pointer to device tree node for the net_device claiming the phy
    :type np: struct device_node \*

    :param void (\*hndlr)(struct net_device \*):
        Link state callback for the network device

.. _`of_phy_get_and_connect.description`:

Description
-----------

If successful, returns a pointer to the phy_device with the embedded
struct device refcount incremented by one, or NULL on failure. The
refcount must be dropped by calling \ :c:func:`phy_disconnect`\  or \ :c:func:`phy_detach`\ .

.. _`of_phy_attach`:

of_phy_attach
=============

.. c:function:: struct phy_device *of_phy_attach(struct net_device *dev, struct device_node *phy_np, u32 flags, phy_interface_t iface)

    Attach to a PHY without starting the state machine

    :param dev:
        pointer to net_device claiming the phy
    :type dev: struct net_device \*

    :param phy_np:
        Node pointer for the PHY
    :type phy_np: struct device_node \*

    :param flags:
        flags to pass to the PHY
    :type flags: u32

    :param iface:
        PHY data interface type
    :type iface: phy_interface_t

.. _`of_phy_attach.description`:

Description
-----------

If successful, returns a pointer to the phy_device with the embedded
struct device refcount incremented by one, or NULL on failure. The
refcount must be dropped by calling \ :c:func:`phy_disconnect`\  or \ :c:func:`phy_detach`\ .

.. This file was automatic generated / don't edit.

