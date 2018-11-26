.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns3/hns3_ethtool.c

.. _`hns3_lp_run_test`:

hns3_lp_run_test
================

.. c:function:: int hns3_lp_run_test(struct net_device *ndev, enum hnae3_loop mode)

    run loopback test

    :param ndev:
        net device
    :type ndev: struct net_device \*

    :param mode:
        loopback type
    :type mode: enum hnae3_loop

.. _`hns3_self_test`:

hns3_self_test
==============

.. c:function:: void hns3_self_test(struct net_device *ndev, struct ethtool_test *eth_test, u64 *data)

    self test

    :param ndev:
        net device
    :type ndev: struct net_device \*

    :param eth_test:
        test cmd
    :type eth_test: struct ethtool_test \*

    :param data:
        test result
    :type data: u64 \*

.. This file was automatic generated / don't edit.

