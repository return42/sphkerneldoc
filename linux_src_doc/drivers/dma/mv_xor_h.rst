.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/mv_xor.h

.. _`mv_xor_chan`:

struct mv_xor_chan
==================

.. c:type:: struct mv_xor_chan

    internal representation of a XOR channel

.. _`mv_xor_chan.definition`:

Definition
----------

.. code-block:: c

    struct mv_xor_chan {
        int pending;
        spinlock_t lock;
        void __iomem *mmr_base;
        void __iomem *mmr_high_base;
        unsigned int idx;
        int irq;
        struct list_head chain;
        struct list_head free_slots;
        struct list_head allocated_slots;
        struct list_head completed_slots;
        dma_addr_t dma_desc_pool;
        void *dma_desc_pool_virt;
        size_t pool_size;
        struct dma_device dmadev;
        struct dma_chan dmachan;
        int slots_allocated;
        struct tasklet_struct irq_tasklet;
        int op_in_desc;
        char dummy_src;
        char dummy_dst;
        dma_addr_t dummy_src_addr;
        dma_addr_t dummy_dst_addr;
        u32 saved_config_reg;
        u32 saved_int_mask_reg;
        struct mv_xor_device *xordev;
    }

.. _`mv_xor_chan.members`:

Members
-------

pending
    allows batching of hardware operations

lock
    serializes enqueue/dequeue operations to the descriptors pool

mmr_base
    memory mapped register base

mmr_high_base
    *undescribed*

idx
    the index of the xor channel

irq
    *undescribed*

chain
    device chain view of the descriptors

free_slots
    free slots usable by the channel

allocated_slots
    slots allocated by the driver

completed_slots
    slots completed by HW but still need to be acked

dma_desc_pool
    *undescribed*

dma_desc_pool_virt
    *undescribed*

pool_size
    *undescribed*

dmadev
    *undescribed*

dmachan
    *undescribed*

slots_allocated
    records the actual size of the descriptor slot pool

irq_tasklet
    bottom half where mv_xor_slot_cleanup runs

op_in_desc
    new mode of driver, each op is writen to descriptor.

dummy_src
    *undescribed*

dummy_dst
    *undescribed*

dummy_src_addr
    *undescribed*

dummy_dst_addr
    *undescribed*

saved_config_reg
    *undescribed*

saved_int_mask_reg
    *undescribed*

xordev
    *undescribed*

.. _`mv_xor_desc_slot`:

struct mv_xor_desc_slot
=======================

.. c:type:: struct mv_xor_desc_slot

    software descriptor

.. _`mv_xor_desc_slot.definition`:

Definition
----------

.. code-block:: c

    struct mv_xor_desc_slot {
        struct list_head node;
        struct list_head sg_tx_list;
        enum dma_transaction_type type;
        void *hw_desc;
        u16 idx;
        struct dma_async_tx_descriptor async_tx;
    }

.. _`mv_xor_desc_slot.members`:

Members
-------

node
    node on the mv_xor_chan lists

sg_tx_list
    *undescribed*

type
    *undescribed*

hw_desc
    virtual address of the hardware descriptor chain

idx
    pool index

async_tx
    support for the async_tx api

.. This file was automatic generated / don't edit.

