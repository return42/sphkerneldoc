.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/owl-dma.c

.. _`owl_dma_lli_hw`:

struct owl_dma_lli_hw
=====================

.. c:type:: struct owl_dma_lli_hw

    Hardware link list for dma transfer

.. _`owl_dma_lli_hw.definition`:

Definition
----------

.. code-block:: c

    struct owl_dma_lli_hw {
        u32 next_lli;
        u32 saddr;
        u32 daddr;
        u32 flen:20;
        u32 fcnt:12;
        u32 src_stride;
        u32 dst_stride;
        u32 ctrla;
        u32 ctrlb;
        u32 const_num;
    }

.. _`owl_dma_lli_hw.members`:

Members
-------

next_lli
    physical address of the next link list

saddr
    source physical address

daddr
    destination physical address

flen
    frame length

fcnt
    frame count

src_stride
    source stride

dst_stride
    destination stride

ctrla
    dma_mode and linklist ctrl config

ctrlb
    interrupt config

const_num
    data for constant fill

.. _`owl_dma_lli`:

struct owl_dma_lli
==================

.. c:type:: struct owl_dma_lli

    Link list for dma transfer

.. _`owl_dma_lli.definition`:

Definition
----------

.. code-block:: c

    struct owl_dma_lli {
        struct owl_dma_lli_hw hw;
        dma_addr_t phys;
        struct list_head node;
    }

.. _`owl_dma_lli.members`:

Members
-------

hw
    hardware link list

phys
    physical address of hardware link list

node
    node for txd's lli_list

.. _`owl_dma_txd`:

struct owl_dma_txd
==================

.. c:type:: struct owl_dma_txd

    Wrapper for struct dma_async_tx_descriptor

.. _`owl_dma_txd.definition`:

Definition
----------

.. code-block:: c

    struct owl_dma_txd {
        struct virt_dma_desc vd;
        struct list_head lli_list;
        bool cyclic;
    }

.. _`owl_dma_txd.members`:

Members
-------

vd
    virtual DMA descriptor

lli_list
    link list of lli nodes

cyclic
    flag to indicate cyclic transfers

.. _`owl_dma_pchan`:

struct owl_dma_pchan
====================

.. c:type:: struct owl_dma_pchan

    Holder for the physical channels

.. _`owl_dma_pchan.definition`:

Definition
----------

.. code-block:: c

    struct owl_dma_pchan {
        u32 id;
        void __iomem *base;
        struct owl_dma_vchan *vchan;
        spinlock_t lock;
    }

.. _`owl_dma_pchan.members`:

Members
-------

id
    physical index to this channel

base
    virtual memory base for the dma channel

vchan
    the virtual channel currently being served by this physical channel

lock
    a lock to use when altering an instance of this struct

.. _`owl_dma_vchan`:

struct owl_dma_vchan
====================

.. c:type:: struct owl_dma_vchan

    Wrapper for DMA ENGINE channel

.. _`owl_dma_vchan.definition`:

Definition
----------

.. code-block:: c

    struct owl_dma_vchan {
        struct virt_dma_chan vc;
        struct owl_dma_pchan *pchan;
        struct owl_dma_txd *txd;
        struct dma_slave_config cfg;
        u8 drq;
    }

.. _`owl_dma_vchan.members`:

Members
-------

vc
    wrappped virtual channel

pchan
    the physical channel utilized by this channel

txd
    active transaction on this channel

cfg
    slave configuration for this channel

drq
    physical DMA request ID for this channel

.. _`owl_dma`:

struct owl_dma
==============

.. c:type:: struct owl_dma

    Holder for the Owl DMA controller

.. _`owl_dma.definition`:

Definition
----------

.. code-block:: c

    struct owl_dma {
        struct dma_device dma;
        void __iomem *base;
        struct clk *clk;
        spinlock_t lock;
        struct dma_pool *lli_pool;
        int irq;
        unsigned int nr_pchans;
        struct owl_dma_pchan *pchans;
        unsigned int nr_vchans;
        struct owl_dma_vchan *vchans;
    }

.. _`owl_dma.members`:

Members
-------

dma
    dma engine for this instance

base
    virtual memory base for the DMA controller

clk
    clock for the DMA controller

lock
    a lock to use when change DMA controller global register

lli_pool
    a pool for the LLI descriptors

irq
    interrupt ID for the DMA controller

nr_pchans
    the number of physical channels

pchans
    array of data for the physical channels

nr_vchans
    the number of physical channels

vchans
    array of data for the physical channels

.. This file was automatic generated / don't edit.

