.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/vnic.h

.. _`hfi1_vnic_sdma`:

struct hfi1_vnic_sdma
=====================

.. c:type:: struct hfi1_vnic_sdma

    VNIC per Tx ring SDMA information \ ``dd``\  - device data pointer \ ``sde``\  - sdma engine \ ``vinfo``\  - vnic info pointer \ ``wait``\  - iowait structure \ ``stx``\  - sdma tx request \ ``state``\  - vnic Tx ring SDMA state \ ``q_idx``\  - vnic Tx queue index

.. _`hfi1_vnic_sdma.definition`:

Definition
----------

.. code-block:: c

    struct hfi1_vnic_sdma {
        struct hfi1_devdata *dd;
        struct sdma_engine *sde;
        struct hfi1_vnic_vport_info *vinfo;
        struct iowait wait;
        struct sdma_txreq stx;
        unsigned int state;
        u8 q_idx;
        bool pkts_sent;
    }

.. _`hfi1_vnic_sdma.members`:

Members
-------

dd
    *undescribed*

sde
    *undescribed*

vinfo
    *undescribed*

wait
    *undescribed*

stx
    *undescribed*

state
    *undescribed*

q_idx
    *undescribed*

pkts_sent
    *undescribed*

.. _`hfi1_vnic_rx_queue`:

struct hfi1_vnic_rx_queue
=========================

.. c:type:: struct hfi1_vnic_rx_queue

    HFI1 VNIC receive queue

.. _`hfi1_vnic_rx_queue.definition`:

Definition
----------

.. code-block:: c

    struct hfi1_vnic_rx_queue {
        u8 idx;
        struct hfi1_vnic_vport_info *vinfo;
        struct net_device *netdev;
        struct napi_struct napi;
        struct sk_buff_head skbq;
    }

.. _`hfi1_vnic_rx_queue.members`:

Members
-------

idx
    queue index

vinfo
    pointer to vport information

netdev
    network device

napi
    netdev napi structure

skbq
    queue of received socket buffers

.. _`hfi1_vnic_vport_info`:

struct hfi1_vnic_vport_info
===========================

.. c:type:: struct hfi1_vnic_vport_info

    HFI1 VNIC virtual port information

.. _`hfi1_vnic_vport_info.definition`:

Definition
----------

.. code-block:: c

    struct hfi1_vnic_vport_info {
        struct hfi1_devdata *dd;
        struct net_device *netdev;
        unsigned long flags;
        struct mutex lock;
        u8 num_tx_q;
        u8 num_rx_q;
        u16 vesw_id;
        struct hfi1_vnic_rx_queue rxq;
        struct opa_vnic_stats stats;
        struct hfi1_vnic_sdma sdma;
    }

.. _`hfi1_vnic_vport_info.members`:

Members
-------

dd
    device data pointer

netdev
    net device pointer

flags
    state flags

lock
    vport lock

num_tx_q
    number of transmit queues

num_rx_q
    number of receive queues

vesw_id
    virtual switch id

rxq
    Array of receive queues

stats
    per queue stats

sdma
    VNIC SDMA structure per TXQ

.. This file was automatic generated / don't edit.

