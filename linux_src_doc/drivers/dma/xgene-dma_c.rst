.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/xgene-dma.c

.. _`xgene_dma_chan`:

struct xgene_dma_chan
=====================

.. c:type:: struct xgene_dma_chan

    internal representation of an X-Gene DMA channel

.. _`xgene_dma_chan.definition`:

Definition
----------

.. code-block:: c

    struct xgene_dma_chan {
        struct dma_chan dma_chan;
        struct xgene_dma *pdma;
        struct device *dev;
        int id;
        int rx_irq;
        char name;
        spinlock_t lock;
        int pending;
        int max_outstanding;
        struct list_head ld_pending;
        struct list_head ld_running;
        struct list_head ld_completed;
        struct dma_pool *desc_pool;
        struct tasklet_struct tasklet;
        struct xgene_dma_ring tx_ring;
        struct xgene_dma_ring rx_ring;
    }

.. _`xgene_dma_chan.members`:

Members
-------

dma_chan
    dmaengine channel object member

pdma
    X-Gene DMA device structure reference

dev
    struct device reference for dma mapping api

id
    raw id of this channel

rx_irq
    channel IRQ

name
    name of X-Gene DMA channel

lock
    serializes enqueue/dequeue operations to the descriptor pool

pending
    number of transaction request pushed to DMA controller for
    execution, but still waiting for completion,

max_outstanding
    max number of outstanding request we can push to channel

ld_pending
    descriptors which are queued to run, but have not yet been
    submitted to the hardware for execution

ld_running
    descriptors which are currently being executing by the hardware

ld_completed
    descriptors which have finished execution by the hardware.
    These descriptors have already had their cleanup actions run. They
    are waiting for the ACK bit to be set by the async tx API.

desc_pool
    descriptor pool for DMA operations

tasklet
    bottom half where all completed descriptors cleans

tx_ring
    transmit ring descriptor that we use to prepare actual
    descriptors for further executions

rx_ring
    receive ring descriptor that we use to get completed DMA
    descriptors during cleanup time

.. _`xgene_dma`:

struct xgene_dma
================

.. c:type:: struct xgene_dma

    internal representation of an X-Gene DMA device

.. _`xgene_dma.definition`:

Definition
----------

.. code-block:: c

    struct xgene_dma {
        struct device *dev;
        struct clk *clk;
        int err_irq;
        int ring_num;
        void __iomem *csr_dma;
        void __iomem *csr_ring;
        void __iomem *csr_ring_cmd;
        void __iomem *csr_efuse;
        struct dma_device dma_dev;
        struct xgene_dma_chan chan;
    }

.. _`xgene_dma.members`:

Members
-------

dev
    *undescribed*

clk
    *undescribed*

err_irq
    DMA error irq number

ring_num
    start id number for DMA ring

csr_dma
    base for DMA register access

csr_ring
    base for DMA ring register access

csr_ring_cmd
    base for DMA ring command register access

csr_efuse
    base for efuse register access

dma_dev
    embedded struct dma_device

chan
    reference to X-Gene DMA channels

.. _`xgene_dma_clean_completed_descriptor`:

xgene_dma_clean_completed_descriptor
====================================

.. c:function:: void xgene_dma_clean_completed_descriptor(struct xgene_dma_chan *chan)

    free all descriptors which has been completed and acked

    :param struct xgene_dma_chan \*chan:
        X-Gene DMA channel

.. _`xgene_dma_clean_completed_descriptor.description`:

Description
-----------

This function is used on all completed and acked descriptors.

.. _`xgene_dma_run_tx_complete_actions`:

xgene_dma_run_tx_complete_actions
=================================

.. c:function:: void xgene_dma_run_tx_complete_actions(struct xgene_dma_chan *chan, struct xgene_dma_desc_sw *desc)

    cleanup a single link descriptor

    :param struct xgene_dma_chan \*chan:
        X-Gene DMA channel

    :param struct xgene_dma_desc_sw \*desc:
        descriptor to cleanup and free

.. _`xgene_dma_run_tx_complete_actions.description`:

Description
-----------

This function is used on a descriptor which has been executed by the DMA
controller. It will run any callbacks, submit any dependencies.

.. _`xgene_dma_clean_running_descriptor`:

xgene_dma_clean_running_descriptor
==================================

.. c:function:: void xgene_dma_clean_running_descriptor(struct xgene_dma_chan *chan, struct xgene_dma_desc_sw *desc)

    move the completed descriptor from ld_running to ld_completed

    :param struct xgene_dma_chan \*chan:
        X-Gene DMA channel

    :param struct xgene_dma_desc_sw \*desc:
        the descriptor which is completed

.. _`xgene_dma_clean_running_descriptor.description`:

Description
-----------

Free the descriptor directly if acked by async_tx api,
else move it to queue ld_completed.

.. _`xgene_chan_xfer_ld_pending`:

xgene_chan_xfer_ld_pending
==========================

.. c:function:: void xgene_chan_xfer_ld_pending(struct xgene_dma_chan *chan)

    push any pending transactions to hw

    :param struct xgene_dma_chan \*chan:
        X-Gene DMA channel

.. _`xgene_chan_xfer_ld_pending.locking`:

LOCKING
-------

must hold chan->lock

.. _`xgene_dma_cleanup_descriptors`:

xgene_dma_cleanup_descriptors
=============================

.. c:function:: void xgene_dma_cleanup_descriptors(struct xgene_dma_chan *chan)

    cleanup link descriptors which are completed and move them to ld_completed to free until flag 'ack' is set

    :param struct xgene_dma_chan \*chan:
        X-Gene DMA channel

.. _`xgene_dma_cleanup_descriptors.description`:

Description
-----------

This function is used on descriptors which have been executed by the DMA
controller. It will run any callbacks, submit any dependencies, then
free these descriptors if flag 'ack' is set.

.. _`xgene_dma_free_desc_list`:

xgene_dma_free_desc_list
========================

.. c:function:: void xgene_dma_free_desc_list(struct xgene_dma_chan *chan, struct list_head *list)

    Free all descriptors in a queue

    :param struct xgene_dma_chan \*chan:
        X-Gene DMA channel

    :param struct list_head \*list:
        the list to free

.. _`xgene_dma_free_desc_list.locking`:

LOCKING
-------

must hold chan->lock

.. This file was automatic generated / don't edit.

