.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns3/hns3_ethtool.c

.. _`hns3_lp_run_test`:

hns3_lp_run_test
================

.. c:function:: int hns3_lp_run_test(struct net_device *ndev, enum hnae3_loop mode)

    run loopback test

    :param struct net_device \*ndev:
        net device

    :param enum hnae3_loop mode:
        loopback type

.. _`hns3_self_test`:

hns3_self_test
==============

.. c:function:: void hns3_self_test(struct net_device *ndev, struct ethtool_test *eth_test, u64 *data)

    self test

    :param struct net_device \*ndev:
        net device

    :param struct ethtool_test \*eth_test:
        test cmd

    :param u64 \*data:
        test result

.. This file was automatic generated / don't edit.

