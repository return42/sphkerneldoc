.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/mdio_10g.c

.. _`efx_mdio_set_settings`:

efx_mdio_set_settings
=====================

.. c:function:: int efx_mdio_set_settings(struct efx_nic *efx, struct ethtool_cmd *ecmd)

    Set (some of) the PHY settings over MDIO.

    :param struct efx_nic \*efx:
        Efx NIC

    :param struct ethtool_cmd \*ecmd:
        New settings

.. _`efx_mdio_an_reconfigure`:

efx_mdio_an_reconfigure
=======================

.. c:function:: void efx_mdio_an_reconfigure(struct efx_nic *efx)

    Push advertising flags and restart autonegotiation

    :param struct efx_nic \*efx:
        Efx NIC

.. This file was automatic generated / don't edit.

