.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/xilinx/xilinx_axienet_mdio.c

.. _`axienet_mdio_read`:

axienet_mdio_read
=================

.. c:function:: int axienet_mdio_read(struct mii_bus *bus, int phy_id, int reg)

    MDIO interface read function

    :param struct mii_bus \*bus:
        Pointer to mii bus structure

    :param int phy_id:
        Address of the PHY device

    :param int reg:
        PHY register to read

.. _`axienet_mdio_read.return`:

Return
------

The register contents on success, -ETIMEDOUT on a timeout

Reads the contents of the requested register from the requested PHY
address by first writing the details into MCR register. After a while
the register MRD is read to obtain the PHY register content.

.. _`axienet_mdio_write`:

axienet_mdio_write
==================

.. c:function:: int axienet_mdio_write(struct mii_bus *bus, int phy_id, int reg, u16 val)

    MDIO interface write function

    :param struct mii_bus \*bus:
        Pointer to mii bus structure

    :param int phy_id:
        Address of the PHY device

    :param int reg:
        PHY register to write to

    :param u16 val:
        Value to be written into the register

.. _`axienet_mdio_write.return`:

Return
------

0 on success, -ETIMEDOUT on a timeout

Writes the value to the requested register by first writing the value
into MWD register. The the MCR register is then appropriately setup
to finish the write operation.

.. _`axienet_mdio_setup`:

axienet_mdio_setup
==================

.. c:function:: int axienet_mdio_setup(struct axienet_local *lp, struct device_node *np)

    MDIO setup function

    :param struct axienet_local \*lp:
        Pointer to axienet local data structure.

    :param struct device_node \*np:
        Pointer to device node

.. _`axienet_mdio_setup.return`:

Return
------

0 on success, -ETIMEDOUT on a timeout, -ENOMEM when
mdiobus_alloc (to allocate memory for mii bus structure) fails.

Sets up the MDIO interface by initializing the MDIO clock and enabling the
MDIO interface in hardware. Register the MDIO interface.

.. _`axienet_mdio_teardown`:

axienet_mdio_teardown
=====================

.. c:function:: void axienet_mdio_teardown(struct axienet_local *lp)

    MDIO remove function

    :param struct axienet_local \*lp:
        Pointer to axienet local data structure.

.. _`axienet_mdio_teardown.description`:

Description
-----------

Unregisters the MDIO and frees any associate memory for mii bus.

.. This file was automatic generated / don't edit.

