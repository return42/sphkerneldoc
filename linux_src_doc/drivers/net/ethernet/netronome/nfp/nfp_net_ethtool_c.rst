.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_ethtool.c

.. _`nfp_net_get_link_ksettings`:

nfp_net_get_link_ksettings
==========================

.. c:function:: int nfp_net_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *cmd)

    Get Link Speed settings

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param cmd:
        ethtool command
    :type cmd: struct ethtool_link_ksettings \*

.. _`nfp_net_get_link_ksettings.description`:

Description
-----------

Reports speed settings based on info in the BAR provided by the fw.

.. This file was automatic generated / don't edit.

