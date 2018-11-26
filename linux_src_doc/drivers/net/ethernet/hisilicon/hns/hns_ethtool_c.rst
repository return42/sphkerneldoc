.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_ethtool.c

.. _`hns_nic_get_link`:

hns_nic_get_link
================

.. c:function:: u32 hns_nic_get_link(struct net_device *net_dev)

    get current link status \ ``net_dev``\ : net_device retuen 0 - success , negative --fail

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

.. _`hns_nic_get_link_ksettings`:

hns_nic_get_link_ksettings
==========================

.. c:function:: int hns_nic_get_link_ksettings(struct net_device *net_dev, struct ethtool_link_ksettings *cmd)

    implement ethtool get link ksettings \ ``net_dev``\ : net_device \ ``cmd``\ : ethtool_link_ksettings retuen 0 - success , negative --fail

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param cmd:
        *undescribed*
    :type cmd: struct ethtool_link_ksettings \*

.. _`hns_nic_set_link_ksettings`:

hns_nic_set_link_ksettings
==========================

.. c:function:: int hns_nic_set_link_ksettings(struct net_device *net_dev, const struct ethtool_link_ksettings *cmd)

    implement ethtool set link ksettings \ ``net_dev``\ : net_device \ ``cmd``\ : ethtool_link_ksettings retuen 0 - success , negative --fail

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param cmd:
        *undescribed*
    :type cmd: const struct ethtool_link_ksettings \*

.. _`__lb_run_test`:

\__lb_run_test
==============

.. c:function:: int __lb_run_test(struct net_device *ndev, enum hnae_loop loop_mode)

    run loopback test

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

    :param loop_mode:
        *undescribed*
    :type loop_mode: enum hnae_loop

.. _`hns_nic_self_test`:

hns_nic_self_test
=================

.. c:function:: void hns_nic_self_test(struct net_device *ndev, struct ethtool_test *eth_test, u64 *data)

    self test

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

    :param eth_test:
        test cmd
    :type eth_test: struct ethtool_test \*

    :param data:
        test result
    :type data: u64 \*

.. _`hns_nic_get_drvinfo`:

hns_nic_get_drvinfo
===================

.. c:function:: void hns_nic_get_drvinfo(struct net_device *net_dev, struct ethtool_drvinfo *drvinfo)

    get net driver info

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param drvinfo:
        driver info
    :type drvinfo: struct ethtool_drvinfo \*

.. _`hns_get_ringparam`:

hns_get_ringparam
=================

.. c:function:: void hns_get_ringparam(struct net_device *net_dev, struct ethtool_ringparam *param)

    get ring parameter

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param param:
        ethtool parameter
    :type param: struct ethtool_ringparam \*

.. _`hns_get_pauseparam`:

hns_get_pauseparam
==================

.. c:function:: void hns_get_pauseparam(struct net_device *net_dev, struct ethtool_pauseparam *param)

    get pause parameter

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param param:
        pause parameter
    :type param: struct ethtool_pauseparam \*

.. _`hns_set_pauseparam`:

hns_set_pauseparam
==================

.. c:function:: int hns_set_pauseparam(struct net_device *net_dev, struct ethtool_pauseparam *param)

    set pause parameter

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param param:
        pause parameter
    :type param: struct ethtool_pauseparam \*

.. _`hns_set_pauseparam.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`hns_get_coalesce`:

hns_get_coalesce
================

.. c:function:: int hns_get_coalesce(struct net_device *net_dev, struct ethtool_coalesce *ec)

    get coalesce info.

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param ec:
        coalesce info.
    :type ec: struct ethtool_coalesce \*

.. _`hns_get_coalesce.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_set_coalesce`:

hns_set_coalesce
================

.. c:function:: int hns_set_coalesce(struct net_device *net_dev, struct ethtool_coalesce *ec)

    set coalesce info.

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param ec:
        coalesce info.
    :type ec: struct ethtool_coalesce \*

.. _`hns_set_coalesce.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_get_channels`:

hns_get_channels
================

.. c:function:: void hns_get_channels(struct net_device *net_dev, struct ethtool_channels *ch)

    get channel info.

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param ch:
        channel info.
    :type ch: struct ethtool_channels \*

.. _`hns_get_ethtool_stats`:

hns_get_ethtool_stats
=====================

.. c:function:: void hns_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *stats, u64 *data)

    get detail statistics.

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param stats:
        statistics info.
    :type stats: struct ethtool_stats \*

    :param data:
        statistics data.
    :type data: u64 \*

.. _`hns_get_strings`:

hns_get_strings
===============

.. c:function:: void hns_get_strings(struct net_device *netdev, u32 stringset, u8 *data)

    Return a set of strings that describe the requested objects

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param stringset:
        *undescribed*
    :type stringset: u32

    :param data:
        objects data.
    :type data: u8 \*

.. _`hns_get_sset_count`:

hns_get_sset_count
==================

.. c:function:: int hns_get_sset_count(struct net_device *netdev, int stringset)

    get string set count witch returned by nic_get_strings.

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param stringset:
        string set index, 0: self test string; 1: statistics string.
    :type stringset: int

.. _`hns_get_sset_count.description`:

Description
-----------

Return string set count.

.. _`hns_phy_led_set`:

hns_phy_led_set
===============

.. c:function:: int hns_phy_led_set(struct net_device *netdev, int value)

    set phy LED status.

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param value:
        LED state.
    :type value: int

.. _`hns_phy_led_set.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_set_phys_id`:

hns_set_phys_id
===============

.. c:function:: int hns_set_phys_id(struct net_device *netdev, enum ethtool_phys_id_state state)

    set phy identify LED.

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param state:
        LED state.
    :type state: enum ethtool_phys_id_state

.. _`hns_set_phys_id.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_get_regs`:

hns_get_regs
============

.. c:function:: void hns_get_regs(struct net_device *net_dev, struct ethtool_regs *cmd, void *data)

    get net device register

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

    :param cmd:
        ethtool cmd
    :type cmd: struct ethtool_regs \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`hns_get_regs_len`:

hns_get_regs_len
================

.. c:function:: int hns_get_regs_len(struct net_device *net_dev)

    get total register len.

    :param net_dev:
        *undescribed*
    :type net_dev: struct net_device \*

.. _`hns_get_regs_len.description`:

Description
-----------

Return total register len.

.. _`hns_nic_nway_reset`:

hns_nic_nway_reset
==================

.. c:function:: int hns_nic_nway_reset(struct net_device *netdev)

    nway reset

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

.. _`hns_nic_nway_reset.description`:

Description
-----------

Return 0 on success, negative on failure

.. This file was automatic generated / don't edit.

