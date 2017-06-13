.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_ethtool.c

.. _`nfp_net_get_link_ksettings`:

nfp_net_get_link_ksettings
==========================

.. c:function:: int nfp_net_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *cmd)

    Get Link Speed settings

    :param struct net_device \*netdev:
        network interface device structure

    :param struct ethtool_link_ksettings \*cmd:
        ethtool command

.. _`nfp_net_get_link_ksettings.description`:

Description
-----------

Reports speed settings based on info in the BAR provided by the fw.

.. This file was automatic generated / don't edit.

