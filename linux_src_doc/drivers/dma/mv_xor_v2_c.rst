.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/mv_xor_v2.c

.. _`mv_xor_v2_descriptor`:

struct mv_xor_v2_descriptor
===========================

.. c:type:: struct mv_xor_v2_descriptor

    DMA HW descriptor

.. _`mv_xor_v2_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct mv_xor_v2_descriptor {
        u16 desc_id;
        u16 flags;
        u32 crc32_result;
        u32 desc_ctrl;
    #define DESC_NUM_ACTIVE_D_BUF_SHIFT 22
    #define DESC_OP_MODE_SHIFT 28
    #define DESC_OP_MODE_NOP 0
    #define DESC_OP_MODE_MEMCPY 1
    #define DESC_OP_MODE_MEMSET 2
    #define DESC_OP_MODE_MEMINIT 3
    #define DESC_OP_MODE_MEM_COMPARE 4
    #define DESC_OP_MODE_CRC32 5
    #define DESC_OP_MODE_XOR 6
    #define DESC_OP_MODE_RAID6 7
    #define DESC_OP_MODE_RAID6_REC 8
    #define DESC_Q_BUFFER_ENABLE BIT(16)
    #define DESC_P_BUFFER_ENABLE BIT(17)
    #define DESC_IOD BIT(27)
        u32 buff_size;
        u32 fill_pattern_src_addr;
        u32 data_buff_addr;
        u32 reserved;
    }

.. _`mv_xor_v2_descriptor.members`:

Members
-------

desc_id
    used by S/W and is not affected by H/W.

flags
    error and status flags

crc32_result
    CRC32 calculation result

desc_ctrl
    operation mode and control flags

buff_size
    amount of bytes to be processed

fill_pattern_src_addr
    Fill-Pattern or Source-Address and
    AW-Attributes

data_buff_addr
    Source (and might be RAID6 destination)
    addresses of data buffers in RAID5 and RAID6

reserved
    reserved

.. _`mv_xor_v2_device`:

struct mv_xor_v2_device
=======================

.. c:type:: struct mv_xor_v2_device

    implements a xor device

.. _`mv_xor_v2_device.definition`:

Definition
----------

.. code-block:: c

    struct mv_xor_v2_device {
        spinlock_t lock;
        void __iomem *dma_base;
        void __iomem *glob_base;
        struct clk *clk;
        struct tasklet_struct irq_tasklet;
        struct list_head free_sw_desc;
        struct dma_device dmadev;
        struct dma_chan dmachan;
        dma_addr_t hw_desq;
        struct mv_xor_v2_descriptor *hw_desq_virt;
        struct mv_xor_v2_sw_desc *sw_desq;
        int desc_size;
        unsigned int npendings;
        unsigned int hw_queue_idx;
    }

.. _`mv_xor_v2_device.members`:

Members
-------

lock
    lock for the engine

dma_base
    memory mapped DMA register base

glob_base
    memory mapped global register base

clk
    *undescribed*

irq_tasklet
    *undescribed*

free_sw_desc
    linked list of free SW descriptors

dmadev
    dma device

dmachan
    dma channel

hw_desq
    HW descriptors queue

hw_desq_virt
    virtual address of DESCQ

sw_desq
    SW descriptors queue

desc_size
    HW descriptor size

npendings
    number of pending descriptors (for which tx_submit has
    been called, but not yet issue_pending)

hw_queue_idx
    *undescribed*

.. _`mv_xor_v2_sw_desc`:

struct mv_xor_v2_sw_desc
========================

.. c:type:: struct mv_xor_v2_sw_desc

    implements a xor SW descriptor

.. _`mv_xor_v2_sw_desc.definition`:

Definition
----------

.. code-block:: c

    struct mv_xor_v2_sw_desc {
        int idx;
        struct dma_async_tx_descriptor async_tx;
        struct mv_xor_v2_descriptor hw_desc;
        struct list_head free_list;
    }

.. _`mv_xor_v2_sw_desc.members`:

Members
-------

idx
    descriptor index

async_tx
    support for the async_tx api

hw_desc
    assosiated HW descriptor

free_list
    node of the free SW descriprots list

.. This file was automatic generated / don't edit.

