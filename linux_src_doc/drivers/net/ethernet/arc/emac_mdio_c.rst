.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/arc/emac_mdio.c

.. _`arc_mdio_complete_wait`:

arc_mdio_complete_wait
======================

.. c:function:: int arc_mdio_complete_wait(struct arc_emac_priv *priv)

    Waits until MDIO transaction is completed.

    :param priv:
        Pointer to ARC EMAC private data structure.
    :type priv: struct arc_emac_priv \*

.. _`arc_mdio_complete_wait.return`:

Return
------

0 on success, -ETIMEDOUT on a timeout.

.. _`arc_mdio_read`:

arc_mdio_read
=============

.. c:function:: int arc_mdio_read(struct mii_bus *bus, int phy_addr, int reg_num)

    MDIO interface read function.

    :param bus:
        Pointer to MII bus structure.
    :type bus: struct mii_bus \*

    :param phy_addr:
        Address of the PHY device.
    :type phy_addr: int

    :param reg_num:
        PHY register to read.
    :type reg_num: int

.. _`arc_mdio_read.return`:

Return
------

The register contents on success, -ETIMEDOUT on a timeout.

Reads the contents of the requested register from the requested PHY
address.

.. _`arc_mdio_write`:

arc_mdio_write
==============

.. c:function:: int arc_mdio_write(struct mii_bus *bus, int phy_addr, int reg_num, u16 value)

    MDIO interface write function.

    :param bus:
        Pointer to MII bus structure.
    :type bus: struct mii_bus \*

    :param phy_addr:
        Address of the PHY device.
    :type phy_addr: int

    :param reg_num:
        PHY register to write to.
    :type reg_num: int

    :param value:
        Value to be written into the register.
    :type value: u16

.. _`arc_mdio_write.return`:

Return
------

0 on success, -ETIMEDOUT on a timeout.

Writes the value to the requested register.

.. _`arc_mdio_reset`:

arc_mdio_reset
==============

.. c:function:: int arc_mdio_reset(struct mii_bus *bus)

    :param bus:
        points to the mii_bus structure
    :type bus: struct mii_bus \*

.. _`arc_mdio_reset.description`:

Description
-----------

reset the MII bus

.. _`arc_mdio_probe`:

arc_mdio_probe
==============

.. c:function:: int arc_mdio_probe(struct arc_emac_priv *priv)

    MDIO probe function.

    :param priv:
        Pointer to ARC EMAC private data structure.
    :type priv: struct arc_emac_priv \*

.. _`arc_mdio_probe.return`:

Return
------

0 on success, -ENOMEM when mdiobus_alloc
(to allocate memory for MII bus structure) fails.

Sets up and registers the MDIO interface.

.. _`arc_mdio_remove`:

arc_mdio_remove
===============

.. c:function:: int arc_mdio_remove(struct arc_emac_priv *priv)

    MDIO remove function.

    :param priv:
        Pointer to ARC EMAC private data structure.
    :type priv: struct arc_emac_priv \*

.. _`arc_mdio_remove.description`:

Description
-----------

Unregisters the MDIO and frees any associate memory for MII bus.

.. This file was automatic generated / don't edit.

