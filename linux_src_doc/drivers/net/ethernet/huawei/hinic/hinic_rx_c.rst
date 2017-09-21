.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_rx.c

.. _`hinic_rxq_clean_stats`:

hinic_rxq_clean_stats
=====================

.. c:function:: void hinic_rxq_clean_stats(struct hinic_rxq *rxq)

    Clean the statistics of specific queue

    :param struct hinic_rxq \*rxq:
        Logical Rx Queue

.. _`hinic_rxq_get_stats`:

hinic_rxq_get_stats
===================

.. c:function:: void hinic_rxq_get_stats(struct hinic_rxq *rxq, struct hinic_rxq_stats *stats)

    get statistics of Rx Queue

    :param struct hinic_rxq \*rxq:
        Logical Rx Queue

    :param struct hinic_rxq_stats \*stats:
        return updated stats here

.. _`rxq_stats_init`:

rxq_stats_init
==============

.. c:function:: void rxq_stats_init(struct hinic_rxq *rxq)

    Initialize the statistics of specific queue

    :param struct hinic_rxq \*rxq:
        Logical Rx Queue

.. _`rx_alloc_skb`:

rx_alloc_skb
============

.. c:function:: struct sk_buff *rx_alloc_skb(struct hinic_rxq *rxq, dma_addr_t *dma_addr)

    allocate skb and map it to dma address

    :param struct hinic_rxq \*rxq:
        rx queue

    :param dma_addr_t \*dma_addr:
        returned dma address for the skb

.. _`rx_alloc_skb.description`:

Description
-----------

Return skb

.. _`rx_unmap_skb`:

rx_unmap_skb
============

.. c:function:: void rx_unmap_skb(struct hinic_rxq *rxq, dma_addr_t dma_addr)

    unmap the dma address of the skb

    :param struct hinic_rxq \*rxq:
        rx queue

    :param dma_addr_t dma_addr:
        dma address of the skb

.. _`rx_free_skb`:

rx_free_skb
===========

.. c:function:: void rx_free_skb(struct hinic_rxq *rxq, struct sk_buff *skb, dma_addr_t dma_addr)

    unmap and free skb

    :param struct hinic_rxq \*rxq:
        rx queue

    :param struct sk_buff \*skb:
        skb to free

    :param dma_addr_t dma_addr:
        dma address of the skb

.. _`rx_alloc_pkts`:

rx_alloc_pkts
=============

.. c:function:: int rx_alloc_pkts(struct hinic_rxq *rxq)

    allocate pkts in rx queue

    :param struct hinic_rxq \*rxq:
        rx queue

.. _`rx_alloc_pkts.description`:

Description
-----------

Return number of skbs allocated

.. _`free_all_rx_skbs`:

free_all_rx_skbs
================

.. c:function:: void free_all_rx_skbs(struct hinic_rxq *rxq)

    free all skbs in rx queue

    :param struct hinic_rxq \*rxq:
        rx queue

.. _`rx_alloc_task`:

rx_alloc_task
=============

.. c:function:: void rx_alloc_task(unsigned long data)

    tasklet for queue allocation

    :param unsigned long data:
        rx queue

.. _`rx_recv_jumbo_pkt`:

rx_recv_jumbo_pkt
=================

.. c:function:: int rx_recv_jumbo_pkt(struct hinic_rxq *rxq, struct sk_buff *head_skb, unsigned int left_pkt_len, u16 ci)

    Rx handler for jumbo pkt

    :param struct hinic_rxq \*rxq:
        rx queue

    :param struct sk_buff \*head_skb:
        the first skb in the list

    :param unsigned int left_pkt_len:
        left size of the pkt exclude head skb

    :param u16 ci:
        consumer index

.. _`rx_recv_jumbo_pkt.description`:

Description
-----------

Return number of wqes that used for the left of the pkt

.. _`rxq_recv`:

rxq_recv
========

.. c:function:: int rxq_recv(struct hinic_rxq *rxq, int budget)

    Rx handler

    :param struct hinic_rxq \*rxq:
        rx queue

    :param int budget:
        maximum pkts to process

.. _`rxq_recv.description`:

Description
-----------

Return number of pkts received

.. _`hinic_init_rxq`:

hinic_init_rxq
==============

.. c:function:: int hinic_init_rxq(struct hinic_rxq *rxq, struct hinic_rq *rq, struct net_device *netdev)

    Initialize the Rx Queue

    :param struct hinic_rxq \*rxq:
        Logical Rx Queue

    :param struct hinic_rq \*rq:
        Hardware Rx Queue to connect the Logical queue with

    :param struct net_device \*netdev:
        network device to connect the Logical queue with

.. _`hinic_init_rxq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_rxq`:

hinic_clean_rxq
===============

.. c:function:: void hinic_clean_rxq(struct hinic_rxq *rxq)

    Clean the Rx Queue

    :param struct hinic_rxq \*rxq:
        Logical Rx Queue

.. This file was automatic generated / don't edit.

