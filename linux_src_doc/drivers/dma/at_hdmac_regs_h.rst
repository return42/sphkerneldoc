.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/at_hdmac_regs.h

.. _`at_desc`:

struct at_desc
==============

.. c:type:: struct at_desc

    software descriptor

.. _`at_desc.definition`:

Definition
----------

.. code-block:: c

    struct at_desc {
        struct at_lli lli;
        struct list_head tx_list;
        struct dma_async_tx_descriptor txd;
        struct list_head desc_node;
        size_t len;
        size_t total_len;
        size_t boundary;
        size_t dst_hole;
        size_t src_hole;
        bool memset_buffer;
        dma_addr_t memset_paddr;
        int *memset_vaddr;
    }

.. _`at_desc.members`:

Members
-------

lli
    *undescribed*

tx_list
    *undescribed*

txd
    support for the async_tx api

desc_node
    node on the channed descriptors list

len
    descriptor byte count

total_len
    total transaction byte count

boundary
    *undescribed*

dst_hole
    *undescribed*

src_hole
    *undescribed*

memset_buffer
    *undescribed*

memset_paddr
    *undescribed*

memset_vaddr
    *undescribed*

.. _`at_dma_chan`:

struct at_dma_chan
==================

.. c:type:: struct at_dma_chan

    internal representation of an Atmel HDMAC channel

.. _`at_dma_chan.definition`:

Definition
----------

.. code-block:: c

    struct at_dma_chan {
        struct dma_chan chan_common;
        struct at_dma *device;
        void __iomem *ch_regs;
        u8 mask;
        u8 per_if;
        u8 mem_if;
        unsigned long status;
        struct tasklet_struct tasklet;
        u32 save_cfg;
        u32 save_dscr;
        struct dma_slave_config dma_sconfig;
        spinlock_t lock;
        struct list_head active_list;
        struct list_head queue;
        struct list_head free_list;
        unsigned int descs_allocated;
    }

.. _`at_dma_chan.members`:

Members
-------

chan_common
    common dmaengine channel object members

device
    parent device

ch_regs
    memory mapped register base

mask
    channel index in a mask

per_if
    peripheral interface

mem_if
    memory interface

status
    transmit status information from irq/prep\* functions
    to tasklet (use atomic operations)

tasklet
    bottom half to finish transaction work

save_cfg
    configuration register that is saved on suspend/resume cycle

save_dscr
    for cyclic operations, preserve next descriptor address in
    the cyclic list on suspend/resume cycle

dma_sconfig
    configuration for slave transfers, passed via
    .device_config

lock
    serializes enqueue/dequeue operations to descriptors lists

active_list
    list of descriptors dmaengine is being running on

queue
    list of descriptors ready to be submitted to engine

free_list
    list of descriptors usable by the channel

descs_allocated
    records the actual size of the descriptor pool

.. _`at_dma`:

struct at_dma
=============

.. c:type:: struct at_dma

    internal representation of an Atmel HDMA Controller

.. _`at_dma.definition`:

Definition
----------

.. code-block:: c

    struct at_dma {
        struct dma_device dma_common;
        void __iomem *regs;
        struct clk *clk;
        u32 save_imr;
        u8 all_chan_mask;
        struct dma_pool *dma_desc_pool;
        struct dma_pool *memset_pool;
        struct at_dma_chan chan[0];
    }

.. _`at_dma.members`:

Members
-------

dma_common
    *undescribed*

regs
    *undescribed*

clk
    dma controller clock

save_imr
    interrupt mask register that is saved on suspend/resume cycle

all_chan_mask
    all channels availlable in a mask

dma_desc_pool
    base of DMA descriptor region (DMA address)

memset_pool
    *undescribed*

chan
    channels table to store at_dma_chan structures

.. _`atc_chan_is_enabled`:

atc_chan_is_enabled
===================

.. c:function:: int atc_chan_is_enabled(struct at_dma_chan *atchan)

    test if given channel is enabled

    :param struct at_dma_chan \*atchan:
        channel we want to test status

.. _`atc_chan_is_paused`:

atc_chan_is_paused
==================

.. c:function:: int atc_chan_is_paused(struct at_dma_chan *atchan)

    test channel pause/resume status

    :param struct at_dma_chan \*atchan:
        channel we want to test status

.. _`atc_chan_is_cyclic`:

atc_chan_is_cyclic
==================

.. c:function:: int atc_chan_is_cyclic(struct at_dma_chan *atchan)

    test if given channel has cyclic property set

    :param struct at_dma_chan \*atchan:
        channel we want to test status

.. _`set_desc_eol`:

set_desc_eol
============

.. c:function:: void set_desc_eol(struct at_desc *desc)

    set end-of-link to descriptor so it will end transfer

    :param struct at_desc \*desc:
        descriptor, signle or at the end of a chain, to end chain on

.. This file was automatic generated / don't edit.

