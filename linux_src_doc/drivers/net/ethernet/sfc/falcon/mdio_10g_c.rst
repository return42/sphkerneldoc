.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/mdio_10g.c

.. _`ef4_mdio_set_settings`:

ef4_mdio_set_settings
=====================

.. c:function:: int ef4_mdio_set_settings(struct ef4_nic *efx, struct ethtool_cmd *ecmd)

    Set (some of) the PHY settings over MDIO.

    :param struct ef4_nic \*efx:
        Efx NIC

    :param struct ethtool_cmd \*ecmd:
        New settings

.. _`ef4_mdio_an_reconfigure`:

ef4_mdio_an_reconfigure
=======================

.. c:function:: void ef4_mdio_an_reconfigure(struct ef4_nic *efx)

    Push advertising flags and restart autonegotiation

    :param struct ef4_nic \*efx:
        Efx NIC

.. This file was automatic generated / don't edit.

