.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/huawei/hinic/hinic_rx.c

.. _`hinic_rxq_clean_stats`:

hinic_rxq_clean_stats
=====================

.. c:function:: void hinic_rxq_clean_stats(struct hinic_rxq *rxq)

    Clean the statistics of specific queue

    :param rxq:
        Logical Rx Queue
    :type rxq: struct hinic_rxq \*

.. _`hinic_rxq_get_stats`:

hinic_rxq_get_stats
===================

.. c:function:: void hinic_rxq_get_stats(struct hinic_rxq *rxq, struct hinic_rxq_stats *stats)

    get statistics of Rx Queue

    :param rxq:
        Logical Rx Queue
    :type rxq: struct hinic_rxq \*

    :param stats:
        return updated stats here
    :type stats: struct hinic_rxq_stats \*

.. _`rxq_stats_init`:

rxq_stats_init
==============

.. c:function:: void rxq_stats_init(struct hinic_rxq *rxq)

    Initialize the statistics of specific queue

    :param rxq:
        Logical Rx Queue
    :type rxq: struct hinic_rxq \*

.. _`rx_alloc_skb`:

rx_alloc_skb
============

.. c:function:: struct sk_buff *rx_alloc_skb(struct hinic_rxq *rxq, dma_addr_t *dma_addr)

    allocate skb and map it to dma address

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

    :param dma_addr:
        returned dma address for the skb
    :type dma_addr: dma_addr_t \*

.. _`rx_alloc_skb.description`:

Description
-----------

Return skb

.. _`rx_unmap_skb`:

rx_unmap_skb
============

.. c:function:: void rx_unmap_skb(struct hinic_rxq *rxq, dma_addr_t dma_addr)

    unmap the dma address of the skb

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

    :param dma_addr:
        dma address of the skb
    :type dma_addr: dma_addr_t

.. _`rx_free_skb`:

rx_free_skb
===========

.. c:function:: void rx_free_skb(struct hinic_rxq *rxq, struct sk_buff *skb, dma_addr_t dma_addr)

    unmap and free skb

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

    :param skb:
        skb to free
    :type skb: struct sk_buff \*

    :param dma_addr:
        dma address of the skb
    :type dma_addr: dma_addr_t

.. _`rx_alloc_pkts`:

rx_alloc_pkts
=============

.. c:function:: int rx_alloc_pkts(struct hinic_rxq *rxq)

    allocate pkts in rx queue

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

.. _`rx_alloc_pkts.description`:

Description
-----------

Return number of skbs allocated

.. _`free_all_rx_skbs`:

free_all_rx_skbs
================

.. c:function:: void free_all_rx_skbs(struct hinic_rxq *rxq)

    free all skbs in rx queue

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

.. _`rx_alloc_task`:

rx_alloc_task
=============

.. c:function:: void rx_alloc_task(unsigned long data)

    tasklet for queue allocation

    :param data:
        rx queue
    :type data: unsigned long

.. _`rx_recv_jumbo_pkt`:

rx_recv_jumbo_pkt
=================

.. c:function:: int rx_recv_jumbo_pkt(struct hinic_rxq *rxq, struct sk_buff *head_skb, unsigned int left_pkt_len, u16 ci)

    Rx handler for jumbo pkt

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

    :param head_skb:
        the first skb in the list
    :type head_skb: struct sk_buff \*

    :param left_pkt_len:
        left size of the pkt exclude head skb
    :type left_pkt_len: unsigned int

    :param ci:
        consumer index
    :type ci: u16

.. _`rx_recv_jumbo_pkt.description`:

Description
-----------

Return number of wqes that used for the left of the pkt

.. _`rxq_recv`:

rxq_recv
========

.. c:function:: int rxq_recv(struct hinic_rxq *rxq, int budget)

    Rx handler

    :param rxq:
        rx queue
    :type rxq: struct hinic_rxq \*

    :param budget:
        maximum pkts to process
    :type budget: int

.. _`rxq_recv.description`:

Description
-----------

Return number of pkts received

.. _`hinic_init_rxq`:

hinic_init_rxq
==============

.. c:function:: int hinic_init_rxq(struct hinic_rxq *rxq, struct hinic_rq *rq, struct net_device *netdev)

    Initialize the Rx Queue

    :param rxq:
        Logical Rx Queue
    :type rxq: struct hinic_rxq \*

    :param rq:
        Hardware Rx Queue to connect the Logical queue with
    :type rq: struct hinic_rq \*

    :param netdev:
        network device to connect the Logical queue with
    :type netdev: struct net_device \*

.. _`hinic_init_rxq.description`:

Description
-----------

Return 0 - Success, negative - Failure

.. _`hinic_clean_rxq`:

hinic_clean_rxq
===============

.. c:function:: void hinic_clean_rxq(struct hinic_rxq *rxq)

    Clean the Rx Queue

    :param rxq:
        Logical Rx Queue
    :type rxq: struct hinic_rxq \*

.. This file was automatic generated / don't edit.

