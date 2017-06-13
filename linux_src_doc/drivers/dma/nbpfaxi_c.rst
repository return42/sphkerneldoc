.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/nbpfaxi.c

.. _`nbpf_desc`:

struct nbpf_desc
================

.. c:type:: struct nbpf_desc

    DMA transfer descriptor

.. _`nbpf_desc.definition`:

Definition
----------

.. code-block:: c

    struct nbpf_desc {
        struct dma_async_tx_descriptor async_tx;
        bool user_wait;
        size_t length;
        struct nbpf_channel *chan;
        struct list_head sg;
        struct list_head node;
    }

.. _`nbpf_desc.members`:

Members
-------

async_tx
    dmaengine object

user_wait
    waiting for a user ack

length
    total transfer length

chan
    *undescribed*

sg
    list of hardware descriptors, represented by struct nbpf_link_desc

node
    member in channel descriptor lists

.. _`nbpf_channel`:

struct nbpf_channel
===================

.. c:type:: struct nbpf_channel

    one DMAC channel

.. _`nbpf_channel.definition`:

Definition
----------

.. code-block:: c

    struct nbpf_channel {
        struct dma_chan dma_chan;
        struct tasklet_struct tasklet;
        void __iomem *base;
        struct nbpf_device *nbpf;
        char name;
        int irq;
        dma_addr_t slave_src_addr;
        size_t slave_src_width;
        size_t slave_src_burst;
        dma_addr_t slave_dst_addr;
        size_t slave_dst_width;
        size_t slave_dst_burst;
        unsigned int terminal;
        u32 dmarq_cfg;
        unsigned long flags;
        spinlock_t lock;
        struct list_head free_links;
        struct list_head free;
        struct list_head queued;
        struct list_head active;
        struct list_head done;
        struct list_head desc_page;
        struct nbpf_desc *running;
        bool paused;
    }

.. _`nbpf_channel.members`:

Members
-------

dma_chan
    standard dmaengine channel object

tasklet
    *undescribed*

base
    register address base

nbpf
    DMAC

name
    IRQ name

irq
    IRQ number

slave_src_addr
    *undescribed*

slave_src_width
    *undescribed*

slave_src_burst
    *undescribed*

slave_dst_addr
    *undescribed*

slave_dst_width
    *undescribed*

slave_dst_burst
    *undescribed*

terminal
    DMA terminal, assigned to this channel

dmarq_cfg
    DMA request line configuration - high / low, edge / level for NBPF_CHAN_CFG

flags
    configuration flags from DT

lock
    protect descriptor lists

free_links
    list of free link descriptors

free
    list of free descriptors

queued
    list of queued descriptors

active
    list of descriptors, scheduled for processing

done
    list of completed descriptors, waiting post-processing

desc_page
    list of additionally allocated descriptor pages - if any

running
    *undescribed*

paused
    *undescribed*

.. This file was automatic generated / don't edit.

