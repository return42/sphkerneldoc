.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_mdio.c

.. _`stmmac_mdio_read`:

stmmac_mdio_read
================

.. c:function:: int stmmac_mdio_read(struct mii_bus *bus, int phyaddr, int phyreg)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

    :param int phyaddr:
        MII addr reg bits 15-11

    :param int phyreg:
        MII addr reg bits 10-6

.. _`stmmac_mdio_read.description`:

Description
-----------

it reads data from the MII register from within the phy device.
For the 7111 GMAC, we must set the bit 0 in the MII address register while
accessing the PHY registers.
Fortunately, it seems this has no drawback for the 7109 MAC.

.. _`stmmac_mdio_write`:

stmmac_mdio_write
=================

.. c:function:: int stmmac_mdio_write(struct mii_bus *bus, int phyaddr, int phyreg, u16 phydata)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

    :param int phyaddr:
        MII addr reg bits 15-11

    :param int phyreg:
        MII addr reg bits 10-6

    :param u16 phydata:
        phy data

.. _`stmmac_mdio_write.description`:

Description
-----------

it writes the data into the MII register from within the device.

.. _`stmmac_mdio_read_gmac4`:

stmmac_mdio_read_gmac4
======================

.. c:function:: int stmmac_mdio_read_gmac4(struct mii_bus *bus, int phyaddr, int phyreg)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

    :param int phyaddr:
        MII addr reg bits 25-21

    :param int phyreg:
        MII addr reg bits 20-16

.. _`stmmac_mdio_read_gmac4.description`:

Description
-----------

it reads data from the MII register of GMAC4 from within
the phy device.

.. _`stmmac_mdio_write_gmac4`:

stmmac_mdio_write_gmac4
=======================

.. c:function:: int stmmac_mdio_write_gmac4(struct mii_bus *bus, int phyaddr, int phyreg, u16 phydata)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

    :param int phyaddr:
        MII addr reg bits 25-21

    :param int phyreg:
        MII addr reg bits 20-16

    :param u16 phydata:
        phy data

.. _`stmmac_mdio_write_gmac4.description`:

Description
-----------

it writes the data into the MII register of GMAC4 from within
the device.

.. _`stmmac_mdio_reset`:

stmmac_mdio_reset
=================

.. c:function:: int stmmac_mdio_reset(struct mii_bus *bus)

    :param struct mii_bus \*bus:
        points to the mii_bus structure

.. _`stmmac_mdio_reset.description`:

Description
-----------

reset the MII bus

.. _`stmmac_mdio_register`:

stmmac_mdio_register
====================

.. c:function:: int stmmac_mdio_register(struct net_device *ndev)

    :param struct net_device \*ndev:
        net device structure

.. _`stmmac_mdio_register.description`:

Description
-----------

it registers the MII bus

.. _`stmmac_mdio_unregister`:

stmmac_mdio_unregister
======================

.. c:function:: int stmmac_mdio_unregister(struct net_device *ndev)

    :param struct net_device \*ndev:
        net device structure

.. _`stmmac_mdio_unregister.description`:

Description
-----------

it unregisters the MII bus

.. This file was automatic generated / don't edit.

