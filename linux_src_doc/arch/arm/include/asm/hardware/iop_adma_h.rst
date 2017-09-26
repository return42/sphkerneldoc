.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/hardware/iop_adma.h

.. _`iop_adma_device`:

struct iop_adma_device
======================

.. c:type:: struct iop_adma_device

    internal representation of an ADMA device

.. _`iop_adma_device.definition`:

Definition
----------

.. code-block:: c

    struct iop_adma_device {
        struct platform_device *pdev;
        int id;
        dma_addr_t dma_desc_pool;
        void *dma_desc_pool_virt;
        struct dma_device common;
    }

.. _`iop_adma_device.members`:

Members
-------

pdev
    Platform device

id
    HW ADMA Device selector

dma_desc_pool
    base of DMA descriptor region (DMA address)

dma_desc_pool_virt
    base of DMA descriptor region (CPU address)

common
    embedded struct dma_device

.. _`iop_adma_chan`:

struct iop_adma_chan
====================

.. c:type:: struct iop_adma_chan

    internal representation of an ADMA device

.. _`iop_adma_chan.definition`:

Definition
----------

.. code-block:: c

    struct iop_adma_chan {
        int pending;
        spinlock_t lock;
        void __iomem *mmr_base;
        struct list_head chain;
        struct iop_adma_device *device;
        struct dma_chan common;
        struct iop_adma_desc_slot *last_used;
        struct list_head all_slots;
        int slots_allocated;
        struct tasklet_struct irq_tasklet;
    }

.. _`iop_adma_chan.members`:

Members
-------

pending
    allows batching of hardware operations

lock
    serializes enqueue/dequeue operations to the slot pool

mmr_base
    memory mapped register base

chain
    device chain view of the descriptors

device
    parent device

common
    common dmaengine channel object members

last_used
    place holder for allocation to continue from where it left off

all_slots
    complete domain of slots usable by the channel

slots_allocated
    records the actual size of the descriptor slot pool

irq_tasklet
    bottom half where iop_adma_slot_cleanup runs

.. _`iop_adma_desc_slot`:

struct iop_adma_desc_slot
=========================

.. c:type:: struct iop_adma_desc_slot

    IOP-ADMA software descriptor

.. _`iop_adma_desc_slot.definition`:

Definition
----------

.. code-block:: c

    struct iop_adma_desc_slot {
        struct list_head slot_node;
        struct list_head chain_node;
        void *hw_desc;
        struct iop_adma_desc_slot *group_head;
        u16 slot_cnt;
        u16 slots_per_op;
        u16 idx;
        struct list_head tx_list;
        struct dma_async_tx_descriptor async_tx;
        union {
            u32 *xor_check_result;
            u32 *crc32_result;
            u32 *pq_check_result;
        } ;
    }

.. _`iop_adma_desc_slot.members`:

Members
-------

slot_node
    node on the iop_adma_chan.all_slots list

chain_node
    node on the op_adma_chan.chain list

hw_desc
    virtual address of the hardware descriptor chain

group_head
    first operation in a transaction

slot_cnt
    total slots used in an transaction (group of operations)

slots_per_op
    number of slots per operation

idx
    pool index

tx_list
    list of descriptors that are associated with one operation

async_tx
    support for the async_tx api

{unnamed_union}
    anonymous

xor_check_result
    result of zero sum

crc32_result
    result crc calculation

pq_check_result
    *undescribed*

.. This file was automatic generated / don't edit.

