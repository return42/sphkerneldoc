.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/samsung/sxgbe/sxgbe_mdio.c

.. _`sxgbe_mdio_read`:

sxgbe_mdio_read
===============

.. c:function:: int sxgbe_mdio_read(struct mii_bus *bus, int phyaddr, int phyreg)

    :param bus:
        points to the mii_bus structure
    :type bus: struct mii_bus \*

    :param phyaddr:
        address of phy port
    :type phyaddr: int

    :param phyreg:
        address of register with in phy register
    :type phyreg: int

.. _`sxgbe_mdio_read.description`:

Description
-----------

this function used for C45 and C22 MDIO Read

.. _`sxgbe_mdio_write`:

sxgbe_mdio_write
================

.. c:function:: int sxgbe_mdio_write(struct mii_bus *bus, int phyaddr, int phyreg, u16 phydata)

    :param bus:
        points to the mii_bus structure
    :type bus: struct mii_bus \*

    :param phyaddr:
        address of phy port
    :type phyaddr: int

    :param phyreg:
        address of phy registers
    :type phyreg: int

    :param phydata:
        data to be written into phy register
    :type phydata: u16

.. _`sxgbe_mdio_write.description`:

Description
-----------

this function is used for C45 and C22 MDIO write

.. This file was automatic generated / don't edit.

