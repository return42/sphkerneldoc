.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/samsung/sxgbe/sxgbe_mdio.c

.. _`sxgbe_mdio_read`:

sxgbe_mdio_read
===============

.. c:function:: int sxgbe_mdio_read(struct mii_bus *bus, int phyaddr, int phyreg)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

    :param int phyaddr:
        address of phy port

    :param int phyreg:
        address of register with in phy register

.. _`sxgbe_mdio_read.description`:

Description
-----------

this function used for C45 and C22 MDIO Read

.. _`sxgbe_mdio_write`:

sxgbe_mdio_write
================

.. c:function:: int sxgbe_mdio_write(struct mii_bus *bus, int phyaddr, int phyreg, u16 phydata)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

    :param int phyaddr:
        address of phy port

    :param int phyreg:
        address of phy registers

    :param u16 phydata:
        data to be written into phy register

.. _`sxgbe_mdio_write.description`:

Description
-----------

this function is used for C45 and C22 MDIO write

.. This file was automatic generated / don't edit.

