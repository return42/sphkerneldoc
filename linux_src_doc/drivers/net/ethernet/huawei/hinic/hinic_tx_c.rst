.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_tx.c

.. _`hinic_txq_clean_stats`:

hinic_txq_clean_stats
=====================

.. c:function:: void hinic_txq_clean_stats(struct hinic_txq *txq)

    Clean the statistics of specific queue

    :param txq:
        Logical Tx Queue
    :type txq: struct hinic_txq \*

.. _`hinic_txq_get_stats`:

hinic_txq_get_stats
===================

.. c:function:: void hinic_txq_get_stats(struct hinic_txq *txq, struct hinic_txq_stats *stats)

    get statistics of Tx Queue

    :param txq:
        Logical Tx Queue
    :type txq: struct hinic_txq \*

    :param stats:
        return updated stats here
    :type stats: struct hinic_txq_stats \*

.. _`txq_stats_init`:

txq_stats_init
==============

.. c:function:: void txq_stats_init(struct hinic_txq *txq)

    Initialize the statistics of specific queue

    :param txq:
        Logical Tx Queue
    :type txq: struct hinic_txq \*

.. _`tx_map_skb`:

tx_map_skb
==========

.. c:function:: int tx_map_skb(struct hinic_dev *nic_dev, struct sk_buff *skb, struct hinic_sge *sges)

    dma mapping for skb and return sges

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param skb:
        the skb
    :type skb: struct sk_buff \*

    :param sges:
        returned sges
    :type sges: struct hinic_sge \*

.. _`tx_map_skb.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`tx_unmap_skb`:

tx_unmap_skb
============

.. c:function:: void tx_unmap_skb(struct hinic_dev *nic_dev, struct sk_buff *skb, struct hinic_sge *sges)

    unmap the dma address of the skb

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param skb:
        the skb
    :type skb: struct sk_buff \*

    :param sges:
        the sges that are connected to the skb
    :type sges: struct hinic_sge \*

.. _`tx_free_skb`:

tx_free_skb
===========

.. c:function:: void tx_free_skb(struct hinic_dev *nic_dev, struct sk_buff *skb, struct hinic_sge *sges)

    unmap and free skb

    :param nic_dev:
        nic device
    :type nic_dev: struct hinic_dev \*

    :param skb:
        the skb
    :type skb: struct sk_buff \*

    :param sges:
        the sges that are connected to the skb
    :type sges: struct hinic_sge \*

.. _`free_all_tx_skbs`:

free_all_tx_skbs
================

.. c:function:: void free_all_tx_skbs(struct hinic_txq *txq)

    free all skbs in tx queue

    :param txq:
        tx queue
    :type txq: struct hinic_txq \*

.. _`free_tx_poll`:

free_tx_poll
============

.. c:function:: int free_tx_poll(struct napi_struct *napi, int budget)

    free finished tx skbs in tx queue that connected to napi

    :param napi:
        napi
    :type napi: struct napi_struct \*

    :param budget:
        number of tx
    :type budget: int

.. _`free_tx_poll.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_init_txq`:

hinic_init_txq
==============

.. c:function:: int hinic_init_txq(struct hinic_txq *txq, struct hinic_sq *sq, struct net_device *netdev)

    Initialize the Tx Queue

    :param txq:
        Logical Tx Queue
    :type txq: struct hinic_txq \*

    :param sq:
        Hardware Tx Queue to connect the Logical queue with
    :type sq: struct hinic_sq \*

    :param netdev:
        network device to connect the Logical queue with
    :type netdev: struct net_device \*

.. _`hinic_init_txq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_txq`:

hinic_clean_txq
===============

.. c:function:: void hinic_clean_txq(struct hinic_txq *txq)

    Clean the Tx Queue

    :param txq:
        Logical Tx Queue
    :type txq: struct hinic_txq \*

.. This file was automatic generated / don't edit.

