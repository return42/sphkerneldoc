.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/mdio_10g.c

.. _`ef4_mdio_set_link_ksettings`:

ef4_mdio_set_link_ksettings
===========================

.. c:function:: int ef4_mdio_set_link_ksettings(struct ef4_nic *efx, const struct ethtool_link_ksettings *cmd)

    Set (some of) the PHY settings over MDIO.

    :param efx:
        Efx NIC
    :type efx: struct ef4_nic \*

    :param cmd:
        New settings
    :type cmd: const struct ethtool_link_ksettings \*

.. _`ef4_mdio_an_reconfigure`:

ef4_mdio_an_reconfigure
=======================

.. c:function:: void ef4_mdio_an_reconfigure(struct ef4_nic *efx)

    Push advertising flags and restart autonegotiation

    :param efx:
        Efx NIC
    :type efx: struct ef4_nic \*

.. This file was automatic generated / don't edit.

