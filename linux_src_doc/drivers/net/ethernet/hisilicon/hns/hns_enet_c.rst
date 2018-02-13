.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/hisilicon/hns/hns_enet.c

.. _`hns_nic_get_headlen`:

hns_nic_get_headlen
===================

.. c:function:: unsigned int hns_nic_get_headlen(unsigned char *data, u32 flag, unsigned int max_size)

    determine size of header for RSC/LRO/GRO/FCOE

    :param unsigned char \*data:
        pointer to the start of the headers

    :param u32 flag:
        *undescribed*

    :param unsigned int max_size:
        *undescribed*

.. _`hns_nic_get_headlen.description`:

Description
-----------

This function is meant to determine the length of headers that will
be recognized by hardware for LRO, GRO, and RSC offloads.  The main
motivation of doing this is to only perform one pull for IPv4 TCP
packets so that we can do basic things like calculating the gso_size
based on the average data per packet.

.. _`smooth_alg`:

smooth_alg
==========

.. c:function:: u32 smooth_alg(u32 new_param, u32 old_param)

    smoothing algrithm for adjusting coalesce parameter

    :param u32 new_param:
        *undescribed*

    :param u32 old_param:
        *undescribed*

.. _`hns_nic_adpt_coalesce`:

hns_nic_adpt_coalesce
=====================

.. c:function:: void hns_nic_adpt_coalesce(struct hns_nic_ring_data *ring_data)

    self adapte coalesce according to rx rate

    :param struct hns_nic_ring_data \*ring_data:
        pointer to hns_nic_ring_data

.. _`hns_nic_adjust_link`:

hns_nic_adjust_link
===================

.. c:function:: void hns_nic_adjust_link(struct net_device *ndev)

    adjust net work mode by the phy stat or new param \ ``ndev``\ : net device

    :param struct net_device \*ndev:
        *undescribed*

.. _`hns_nic_init_phy`:

hns_nic_init_phy
================

.. c:function:: int hns_nic_init_phy(struct net_device *ndev, struct hnae_handle *h)

    init phy \ ``ndev``\ : net device \ ``h``\ : ae handle Return 0 on success, negative on failure

    :param struct net_device \*ndev:
        *undescribed*

    :param struct hnae_handle \*h:
        *undescribed*

.. _`hns_nic_clear_all_rx_fetch`:

hns_nic_clear_all_rx_fetch
==========================

.. c:function:: int hns_nic_clear_all_rx_fetch(struct net_device *ndev)

    clear the chip fetched descriptions. The function as follows: 1. if one rx ring has found the page_offset is not equal 0 between head and tail, it means that the chip fetched the wrong descs for the ring which buffer size is 4096. 2. we set the chip serdes loopback and set rss indirection to the ring. 3. construct 64-bytes ip broadcast packages, wait the associated rx ring recieving all packages and it will fetch new descriptions. 4. recover to the original state.

    :param struct net_device \*ndev:
        *undescribed*

.. _`hns_nic_clear_all_rx_fetch.description`:

Description
-----------

\ ``ndev``\ : net device

.. _`hns_set_multicast_list`:

hns_set_multicast_list
======================

.. c:function:: void hns_set_multicast_list(struct net_device *ndev)

    set mutl mac address

    :param struct net_device \*ndev:
        *undescribed*

.. _`hns_set_multicast_list.description`:

Description
-----------

return void

.. _`hns_tx_timeout_reset`:

hns_tx_timeout_reset
====================

.. c:function:: void hns_tx_timeout_reset(struct hns_nic_priv *priv)

    initiate reset due to Tx timeout

    :param struct hns_nic_priv \*priv:
        driver private struct

.. This file was automatic generated / don't edit.

