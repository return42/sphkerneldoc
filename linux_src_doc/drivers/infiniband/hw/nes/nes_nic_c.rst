.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_nic.c

.. _`nes_netdev_poll`:

nes_netdev_poll
===============

.. c:function:: int nes_netdev_poll(struct napi_struct *napi, int budget)

    :param napi:
        *undescribed*
    :type napi: struct napi_struct \*

    :param budget:
        *undescribed*
    :type budget: int

.. _`nes_netdev_open`:

nes_netdev_open
===============

.. c:function:: int nes_netdev_open(struct net_device *netdev)

    Activate the network interface; ifconfig ethx up.

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_netdev_stop`:

nes_netdev_stop
===============

.. c:function:: int nes_netdev_stop(struct net_device *netdev)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_nic_send`:

nes_nic_send
============

.. c:function:: bool nes_nic_send(struct sk_buff *skb, struct net_device *netdev)

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_netdev_start_xmit`:

nes_netdev_start_xmit
=====================

.. c:function:: netdev_tx_t nes_netdev_start_xmit(struct sk_buff *skb, struct net_device *netdev)

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_netdev_get_stats`:

nes_netdev_get_stats
====================

.. c:function:: struct net_device_stats *nes_netdev_get_stats(struct net_device *netdev)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_netdev_tx_timeout`:

nes_netdev_tx_timeout
=====================

.. c:function:: void nes_netdev_tx_timeout(struct net_device *netdev)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_netdev_set_mac_address`:

nes_netdev_set_mac_address
==========================

.. c:function:: int nes_netdev_set_mac_address(struct net_device *netdev, void *p)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param p:
        *undescribed*
    :type p: void \*

.. _`nes_netdev_set_multicast_list`:

nes_netdev_set_multicast_list
=============================

.. c:function:: void nes_netdev_set_multicast_list(struct net_device *netdev)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_netdev_change_mtu`:

nes_netdev_change_mtu
=====================

.. c:function:: int nes_netdev_change_mtu(struct net_device *netdev, int new_mtu)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param new_mtu:
        *undescribed*
    :type new_mtu: int

.. _`nes_netdev_get_sset_count`:

nes_netdev_get_sset_count
=========================

.. c:function:: int nes_netdev_get_sset_count(struct net_device *netdev, int stringset)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param stringset:
        *undescribed*
    :type stringset: int

.. _`nes_netdev_get_strings`:

nes_netdev_get_strings
======================

.. c:function:: void nes_netdev_get_strings(struct net_device *netdev, u32 stringset, u8 *ethtool_strings)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param stringset:
        *undescribed*
    :type stringset: u32

    :param ethtool_strings:
        *undescribed*
    :type ethtool_strings: u8 \*

.. _`nes_netdev_get_ethtool_stats`:

nes_netdev_get_ethtool_stats
============================

.. c:function:: void nes_netdev_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *target_ethtool_stats, u64 *target_stat_values)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param target_ethtool_stats:
        *undescribed*
    :type target_ethtool_stats: struct ethtool_stats \*

    :param target_stat_values:
        *undescribed*
    :type target_stat_values: u64 \*

.. _`nes_netdev_get_drvinfo`:

nes_netdev_get_drvinfo
======================

.. c:function:: void nes_netdev_get_drvinfo(struct net_device *netdev, struct ethtool_drvinfo *drvinfo)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param drvinfo:
        *undescribed*
    :type drvinfo: struct ethtool_drvinfo \*

.. _`nes_netdev_set_coalesce`:

nes_netdev_set_coalesce
=======================

.. c:function:: int nes_netdev_set_coalesce(struct net_device *netdev, struct ethtool_coalesce *et_coalesce)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param et_coalesce:
        *undescribed*
    :type et_coalesce: struct ethtool_coalesce \*

.. _`nes_netdev_get_coalesce`:

nes_netdev_get_coalesce
=======================

.. c:function:: int nes_netdev_get_coalesce(struct net_device *netdev, struct ethtool_coalesce *et_coalesce)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param et_coalesce:
        *undescribed*
    :type et_coalesce: struct ethtool_coalesce \*

.. _`nes_netdev_get_pauseparam`:

nes_netdev_get_pauseparam
=========================

.. c:function:: void nes_netdev_get_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *et_pauseparam)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param et_pauseparam:
        *undescribed*
    :type et_pauseparam: struct ethtool_pauseparam \*

.. _`nes_netdev_set_pauseparam`:

nes_netdev_set_pauseparam
=========================

.. c:function:: int nes_netdev_set_pauseparam(struct net_device *netdev, struct ethtool_pauseparam *et_pauseparam)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param et_pauseparam:
        *undescribed*
    :type et_pauseparam: struct ethtool_pauseparam \*

.. _`nes_netdev_get_link_ksettings`:

nes_netdev_get_link_ksettings
=============================

.. c:function:: int nes_netdev_get_link_ksettings(struct net_device *netdev, struct ethtool_link_ksettings *cmd)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param cmd:
        *undescribed*
    :type cmd: struct ethtool_link_ksettings \*

.. _`nes_netdev_set_link_ksettings`:

nes_netdev_set_link_ksettings
=============================

.. c:function:: int nes_netdev_set_link_ksettings(struct net_device *netdev, const struct ethtool_link_ksettings *cmd)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param cmd:
        *undescribed*
    :type cmd: const struct ethtool_link_ksettings \*

.. _`nes_netdev_init`:

nes_netdev_init
===============

.. c:function:: struct net_device *nes_netdev_init(struct nes_device *nesdev, void __iomem *mmio_addr)

    initialize network device

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param mmio_addr:
        *undescribed*
    :type mmio_addr: void __iomem \*

.. _`nes_netdev_destroy`:

nes_netdev_destroy
==================

.. c:function:: void nes_netdev_destroy(struct net_device *netdev)

    destroy network device structure

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`nes_nic_cm_xmit`:

nes_nic_cm_xmit
===============

.. c:function:: int nes_nic_cm_xmit(struct sk_buff *skb, struct net_device *netdev)

    - CM calls this to send out pkts

    :param skb:
        *undescribed*
    :type skb: struct sk_buff \*

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. This file was automatic generated / don't edit.

