.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/qualcomm/emac/emac-phy.c

.. _`emac_phy_mdio_autopoll_disable`:

emac_phy_mdio_autopoll_disable
==============================

.. c:function:: int emac_phy_mdio_autopoll_disable(struct emac_adapter *adpt)

    disable mdio autopoll

    :param struct emac_adapter \*adpt:
        the emac adapter

.. _`emac_phy_mdio_autopoll_disable.description`:

Description
-----------

The autopoll feature takes over the MDIO bus.  In order for
the PHY driver to be able to talk to the PHY over the MDIO
bus, we need to temporarily disable the autopoll feature.

.. _`emac_phy_mdio_autopoll_enable`:

emac_phy_mdio_autopoll_enable
=============================

.. c:function:: void emac_phy_mdio_autopoll_enable(struct emac_adapter *adpt)

    disable mdio autopoll

    :param struct emac_adapter \*adpt:
        the emac adapter

.. _`emac_phy_mdio_autopoll_enable.description`:

Description
-----------

The EMAC has the ability to poll the external PHY on the MDIO
bus for link state changes.  This eliminates the need for the
driver to poll the phy.  If if the link state does change,
the EMAC issues an interrupt on behalf of the PHY.

.. This file was automatic generated / don't edit.

