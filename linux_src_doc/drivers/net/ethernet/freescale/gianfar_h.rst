.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/freescale/gianfar.h

.. _`gfar_priv_tx_q`:

struct gfar_priv_tx_q
=====================

.. c:type:: struct gfar_priv_tx_q

    per tx queue structure

.. _`gfar_priv_tx_q.definition`:

Definition
----------

.. code-block:: c

    struct gfar_priv_tx_q {
        spinlock_t txlock __attribute__ ((aligned (SMP_CACHE_BYTES)));
        struct txbd8 *tx_bd_base;
        struct txbd8 *cur_tx;
        unsigned int num_txbdfree;
        unsigned short skb_curtx;
        unsigned short tx_ring_size;
        struct tx_q_stats stats;
        struct gfar_priv_grp *grp;
        struct net_device *dev;
        struct sk_buff **tx_skbuff;
        struct txbd8 *dirty_tx;
        unsigned short skb_dirtytx;
        unsigned short qindex;
        unsigned int txcoalescing;
        unsigned long txic;
        dma_addr_t tx_bd_dma_base;
    }

.. _`gfar_priv_tx_q.members`:

Members
-------

txlock
    per queue tx spin lock

tx_bd_base
    First tx buffer descriptor

cur_tx
    Next free ring entry

num_txbdfree
    number of free TxBds

skb_curtx
    to be used skb pointer

tx_ring_size
    Tx ring size

stats
    bytes/packets stats

grp
    back pointer to the group to which this queue belongs

dev
    back pointer to the dev structure

tx_skbuff
    skb pointers

dirty_tx
    First buffer in line to be transmitted

skb_dirtytx
    the last used skb pointer

qindex
    index of this queue

txcoalescing
    enable/disable tx coalescing

txic
    transmit interrupt coalescing value

tx_bd_dma_base
    *undescribed*

.. _`gfar_priv_rx_q`:

struct gfar_priv_rx_q
=====================

.. c:type:: struct gfar_priv_rx_q

    per rx queue structure

.. _`gfar_priv_rx_q.definition`:

Definition
----------

.. code-block:: c

    struct gfar_priv_rx_q {
        struct gfar_rx_buff *rx_buff __aligned(SMP_CACHE_BYTES);
        struct rxbd8 *rx_bd_base;
        struct net_device *ndev;
        struct device *dev;
        u16 rx_ring_size;
        u16 qindex;
        struct gfar_priv_grp *grp;
        u16 next_to_clean;
        u16 next_to_use;
        u16 next_to_alloc;
        struct sk_buff *skb;
        struct rx_q_stats stats;
        u32 __iomem *rfbptr;
        unsigned char rxcoalescing;
        unsigned long rxic;
        dma_addr_t rx_bd_dma_base;
    }

.. _`gfar_priv_rx_q.members`:

Members
-------

rx_buff
    Array of buffer info metadata structs

rx_bd_base
    First rx buffer descriptor

ndev
    back pointer to net_device

dev
    *undescribed*

rx_ring_size
    Rx ring size

qindex
    index of this queue

grp
    *undescribed*

next_to_clean
    index of the next buffer to be cleaned

next_to_use
    index of the next buffer to be alloc'd

next_to_alloc
    *undescribed*

skb
    *undescribed*

stats
    *undescribed*

rfbptr
    *undescribed*

rxcoalescing
    enable/disable rx-coalescing

rxic
    receive interrupt coalescing vlaue

rx_bd_dma_base
    *undescribed*

.. _`gfar_priv_grp`:

struct gfar_priv_grp
====================

.. c:type:: struct gfar_priv_grp

    per group structure

.. _`gfar_priv_grp.definition`:

Definition
----------

.. code-block:: c

    struct gfar_priv_grp {
        spinlock_t grplock __aligned(SMP_CACHE_BYTES);
        struct napi_struct napi_rx;
        struct napi_struct napi_tx;
        struct gfar __iomem *regs;
        struct gfar_priv_tx_q *tx_queue;
        struct gfar_priv_rx_q *rx_queue;
        unsigned int tstat;
        unsigned int rstat;
        struct gfar_private *priv;
        unsigned long num_tx_queues;
        unsigned long tx_bit_map;
        unsigned long num_rx_queues;
        unsigned long rx_bit_map;
        struct gfar_irqinfo *irqinfo[GFAR_NUM_IRQS];
    }

.. _`gfar_priv_grp.members`:

Members
-------

grplock
    *undescribed*

napi_rx
    *undescribed*

napi_tx
    *undescribed*

regs
    the ioremapped register space for this group

tx_queue
    *undescribed*

rx_queue
    *undescribed*

tstat
    *undescribed*

rstat
    *undescribed*

priv
    back pointer to the priv structure

num_tx_queues
    *undescribed*

tx_bit_map
    *undescribed*

num_rx_queues
    *undescribed*

rx_bit_map
    *undescribed*

irqinfo
    TX/RX/ER irq data for this group

.. This file was automatic generated / don't edit.

