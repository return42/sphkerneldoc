.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ppc4xx/adma.h

.. _`ppc440spe_adma_device`:

struct ppc440spe_adma_device
============================

.. c:type:: struct ppc440spe_adma_device

    internal representation of an ADMA device

.. _`ppc440spe_adma_device.definition`:

Definition
----------

.. code-block:: c

    struct ppc440spe_adma_device {
        struct device *dev;
        struct dma_regs __iomem *dma_reg;
        struct xor_regs __iomem *xor_reg;
        struct i2o_regs __iomem *i2o_reg;
        int id;
        void *dma_desc_pool_virt;
        dma_addr_t dma_desc_pool;
        size_t pool_size;
        int irq;
        int err_irq;
        struct dma_device common;
    }

.. _`ppc440spe_adma_device.members`:

Members
-------

dev
    device

dma_reg
    base for DMAx register access

xor_reg
    base for XOR register access

i2o_reg
    base for I2O register access

id
    HW ADMA Device selector

dma_desc_pool_virt
    base of DMA descriptor region (CPU address)

dma_desc_pool
    base of DMA descriptor region (DMA address)

pool_size
    size of the pool

irq
    DMAx or XOR irq number

err_irq
    DMAx error irq number

common
    embedded struct dma_device

.. _`ppc440spe_adma_chan`:

struct ppc440spe_adma_chan
==========================

.. c:type:: struct ppc440spe_adma_chan

    internal representation of an ADMA channel

.. _`ppc440spe_adma_chan.definition`:

Definition
----------

.. code-block:: c

    struct ppc440spe_adma_chan {
        spinlock_t lock;
        struct ppc440spe_adma_device *device;
        struct list_head chain;
        struct dma_chan common;
        struct list_head all_slots;
        struct ppc440spe_adma_desc_slot *last_used;
        int pending;
        int slots_allocated;
        int hw_chain_inited;
        struct tasklet_struct irq_tasklet;
        u8 needs_unmap;
        struct page *pdest_page;
        struct page *qdest_page;
        dma_addr_t pdest;
        dma_addr_t qdest;
    }

.. _`ppc440spe_adma_chan.members`:

Members
-------

lock
    serializes enqueue/dequeue operations to the slot pool

device
    parent device

chain
    device chain view of the descriptors

common
    common dmaengine channel object members

all_slots
    complete domain of slots usable by the channel

last_used
    *undescribed*

pending
    allows batching of hardware operations

slots_allocated
    records the actual size of the descriptor slot pool

hw_chain_inited
    h/w descriptor chain initialization flag

irq_tasklet
    bottom half where ppc440spe_adma_slot_cleanup runs

needs_unmap
    if buffers should not be unmapped upon final processing

pdest_page
    P destination page for async validate operation

qdest_page
    Q destination page for async validate operation

pdest
    P dma addr for async validate operation

qdest
    Q dma addr for async validate operation

.. _`ppc440spe_adma_desc_slot`:

struct ppc440spe_adma_desc_slot
===============================

.. c:type:: struct ppc440spe_adma_desc_slot

    PPC440SPE-ADMA software descriptor

.. _`ppc440spe_adma_desc_slot.definition`:

Definition
----------

.. code-block:: c

    struct ppc440spe_adma_desc_slot {
        dma_addr_t phys;
        struct ppc440spe_adma_desc_slot *group_head;
        struct ppc440spe_adma_desc_slot *hw_next;
        struct dma_async_tx_descriptor async_tx;
        struct list_head slot_node;
        struct list_head chain_node;
        struct list_head group_list;
        unsigned int unmap_len;
        void *hw_desc;
        u16 stride;
        u16 idx;
        u16 slot_cnt;
        u8 src_cnt;
        u8 dst_cnt;
        u8 slots_per_op;
        u8 descs_per_op;
        unsigned long flags;
        unsigned long reverse_flags[8];
    #define PPC440SPE_DESC_INT 0
    #define PPC440SPE_ZERO_P 1
    #define PPC440SPE_ZERO_Q 2
    #define PPC440SPE_COHERENT 3
    #define PPC440SPE_DESC_WXOR 4
    #define PPC440SPE_DESC_RXOR 5
    #define PPC440SPE_DESC_RXOR123 8
    #define PPC440SPE_DESC_RXOR124 9
    #define PPC440SPE_DESC_RXOR125 10
    #define PPC440SPE_DESC_RXOR12 11
    #define PPC440SPE_DESC_RXOR_REV 12
    #define PPC440SPE_DESC_PCHECK 13
    #define PPC440SPE_DESC_QCHECK 14
    #define PPC440SPE_DESC_RXOR_MSK 0x3
        struct ppc440spe_rxor rxor_cursor;
        union {unnamed_union};
    }

.. _`ppc440spe_adma_desc_slot.members`:

Members
-------

phys
    hardware address of the hardware descriptor chain

group_head
    first operation in a transaction

hw_next
    pointer to the next descriptor in chain

async_tx
    support for the async_tx api

slot_node
    node on the iop_adma_chan.all_slots list

chain_node
    node on the op_adma_chan.chain list

group_list
    list of slots that make up a multi-descriptor transaction
    for example transfer lengths larger than the supported hw max

unmap_len
    transaction bytecount

hw_desc
    virtual address of the hardware descriptor chain

stride
    currently chained or not

idx
    pool index

slot_cnt
    total slots used in an transaction (group of operations)

src_cnt
    number of sources set in this descriptor

dst_cnt
    number of destinations set in the descriptor

slots_per_op
    number of slots per operation

descs_per_op
    number of slot per P/Q operation see comment
    for ppc440spe_prep_dma_pqxor function

flags
    desc state/type

reverse_flags
    1 if a corresponding rxor address uses reversed address order

rxor_cursor
    *undescribed*

{unnamed_union}
    anonymous


.. This file was automatic generated / don't edit.

