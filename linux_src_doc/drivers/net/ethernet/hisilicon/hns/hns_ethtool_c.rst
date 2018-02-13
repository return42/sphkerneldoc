.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_ethtool.c

.. _`hns_nic_get_link`:

hns_nic_get_link
================

.. c:function:: u32 hns_nic_get_link(struct net_device *net_dev)

    get current link status \ ``net_dev``\ : net_device retuen 0 - success , negative --fail

    :param struct net_device \*net_dev:
        *undescribed*

.. _`hns_nic_get_link_ksettings`:

hns_nic_get_link_ksettings
==========================

.. c:function:: int hns_nic_get_link_ksettings(struct net_device *net_dev, struct ethtool_link_ksettings *cmd)

    implement ethtool get link ksettings \ ``net_dev``\ : net_device \ ``cmd``\ : ethtool_link_ksettings retuen 0 - success , negative --fail

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_link_ksettings \*cmd:
        *undescribed*

.. _`hns_nic_set_link_ksettings`:

hns_nic_set_link_ksettings
==========================

.. c:function:: int hns_nic_set_link_ksettings(struct net_device *net_dev, const struct ethtool_link_ksettings *cmd)

    implement ethtool set link ksettings \ ``net_dev``\ : net_device \ ``cmd``\ : ethtool_link_ksettings retuen 0 - success , negative --fail

    :param struct net_device \*net_dev:
        *undescribed*

    :param const struct ethtool_link_ksettings \*cmd:
        *undescribed*

.. _`__lb_run_test`:

\__lb_run_test
==============

.. c:function:: int __lb_run_test(struct net_device *ndev, enum hnae_loop loop_mode)

    run loopback test

    :param struct net_device \*ndev:
        *undescribed*

    :param enum hnae_loop loop_mode:
        *undescribed*

.. _`hns_nic_self_test`:

hns_nic_self_test
=================

.. c:function:: void hns_nic_self_test(struct net_device *ndev, struct ethtool_test *eth_test, u64 *data)

    self test

    :param struct net_device \*ndev:
        *undescribed*

    :param struct ethtool_test \*eth_test:
        test cmd

    :param u64 \*data:
        test result

.. _`hns_nic_get_drvinfo`:

hns_nic_get_drvinfo
===================

.. c:function:: void hns_nic_get_drvinfo(struct net_device *net_dev, struct ethtool_drvinfo *drvinfo)

    get net driver info

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_drvinfo \*drvinfo:
        driver info

.. _`hns_get_ringparam`:

hns_get_ringparam
=================

.. c:function:: void hns_get_ringparam(struct net_device *net_dev, struct ethtool_ringparam *param)

    get ring parameter

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_ringparam \*param:
        ethtool parameter

.. _`hns_get_pauseparam`:

hns_get_pauseparam
==================

.. c:function:: void hns_get_pauseparam(struct net_device *net_dev, struct ethtool_pauseparam *param)

    get pause parameter

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_pauseparam \*param:
        pause parameter

.. _`hns_set_pauseparam`:

hns_set_pauseparam
==================

.. c:function:: int hns_set_pauseparam(struct net_device *net_dev, struct ethtool_pauseparam *param)

    set pause parameter

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_pauseparam \*param:
        pause parameter

.. _`hns_set_pauseparam.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`hns_get_coalesce`:

hns_get_coalesce
================

.. c:function:: int hns_get_coalesce(struct net_device *net_dev, struct ethtool_coalesce *ec)

    get coalesce info.

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_coalesce \*ec:
        coalesce info.

.. _`hns_get_coalesce.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_set_coalesce`:

hns_set_coalesce
================

.. c:function:: int hns_set_coalesce(struct net_device *net_dev, struct ethtool_coalesce *ec)

    set coalesce info.

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_coalesce \*ec:
        coalesce info.

.. _`hns_set_coalesce.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_get_channels`:

hns_get_channels
================

.. c:function:: void hns_get_channels(struct net_device *net_dev, struct ethtool_channels *ch)

    get channel info.

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_channels \*ch:
        channel info.

.. _`hns_get_ethtool_stats`:

hns_get_ethtool_stats
=====================

.. c:function:: void hns_get_ethtool_stats(struct net_device *netdev, struct ethtool_stats *stats, u64 *data)

    get detail statistics.

    :param struct net_device \*netdev:
        *undescribed*

    :param struct ethtool_stats \*stats:
        statistics info.

    :param u64 \*data:
        statistics data.

.. _`hns_get_strings`:

hns_get_strings
===============

.. c:function:: void hns_get_strings(struct net_device *netdev, u32 stringset, u8 *data)

    Return a set of strings that describe the requested objects

    :param struct net_device \*netdev:
        *undescribed*

    :param u32 stringset:
        *undescribed*

    :param u8 \*data:
        objects data.

.. _`hns_get_sset_count`:

hns_get_sset_count
==================

.. c:function:: int hns_get_sset_count(struct net_device *netdev, int stringset)

    get string set count witch returned by nic_get_strings.

    :param struct net_device \*netdev:
        *undescribed*

    :param int stringset:
        string set index, 0: self test string; 1: statistics string.

.. _`hns_get_sset_count.description`:

Description
-----------

Return string set count.

.. _`hns_phy_led_set`:

hns_phy_led_set
===============

.. c:function:: int hns_phy_led_set(struct net_device *netdev, int value)

    set phy LED status.

    :param struct net_device \*netdev:
        *undescribed*

    :param int value:
        LED state.

.. _`hns_phy_led_set.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_set_phys_id`:

hns_set_phys_id
===============

.. c:function:: int hns_set_phys_id(struct net_device *netdev, enum ethtool_phys_id_state state)

    set phy identify LED.

    :param struct net_device \*netdev:
        *undescribed*

    :param enum ethtool_phys_id_state state:
        LED state.

.. _`hns_set_phys_id.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`hns_get_regs`:

hns_get_regs
============

.. c:function:: void hns_get_regs(struct net_device *net_dev, struct ethtool_regs *cmd, void *data)

    get net device register

    :param struct net_device \*net_dev:
        *undescribed*

    :param struct ethtool_regs \*cmd:
        ethtool cmd

    :param void \*data:
        *undescribed*

.. _`hns_get_regs_len`:

hns_get_regs_len
================

.. c:function:: int hns_get_regs_len(struct net_device *net_dev)

    get total register len.

    :param struct net_device \*net_dev:
        *undescribed*

.. _`hns_get_regs_len.description`:

Description
-----------

Return total register len.

.. _`hns_nic_nway_reset`:

hns_nic_nway_reset
==================

.. c:function:: int hns_nic_nway_reset(struct net_device *netdev)

    nway reset

    :param struct net_device \*netdev:
        *undescribed*

.. _`hns_nic_nway_reset.description`:

Description
-----------

Return 0 on success, negative on failure

.. This file was automatic generated / don't edit.

