.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/xilinx/xilinx_dma.c

.. _`xilinx_vdma_desc_hw`:

struct xilinx_vdma_desc_hw
==========================

.. c:type:: struct xilinx_vdma_desc_hw

    Hardware Descriptor

.. _`xilinx_vdma_desc_hw.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_vdma_desc_hw {
        u32 next_desc;
        u32 pad1;
        u32 buf_addr;
        u32 buf_addr_msb;
        u32 vsize;
        u32 hsize;
        u32 stride;
    }

.. _`xilinx_vdma_desc_hw.members`:

Members
-------

next_desc
    Next Descriptor Pointer \ ``0x00``\ 

pad1
    Reserved \ ``0x04``\ 

buf_addr
    Buffer address \ ``0x08``\ 

buf_addr_msb
    MSB of Buffer address \ ``0x0C``\ 

vsize
    Vertical Size \ ``0x10``\ 

hsize
    Horizontal Size \ ``0x14``\ 

stride
    Number of bytes between the first
    pixels of each horizontal line \ ``0x18``\ 

.. _`xilinx_axidma_desc_hw`:

struct xilinx_axidma_desc_hw
============================

.. c:type:: struct xilinx_axidma_desc_hw

    Hardware Descriptor for AXI DMA

.. _`xilinx_axidma_desc_hw.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_axidma_desc_hw {
        u32 next_desc;
        u32 next_desc_msb;
        u32 buf_addr;
        u32 buf_addr_msb;
        u32 mcdma_control;
        u32 vsize_stride;
        u32 control;
        u32 status;
        u32 app[XILINX_DMA_NUM_APP_WORDS];
    }

.. _`xilinx_axidma_desc_hw.members`:

Members
-------

next_desc
    Next Descriptor Pointer \ ``0x00``\ 

next_desc_msb
    MSB of Next Descriptor Pointer \ ``0x04``\ 

buf_addr
    Buffer address \ ``0x08``\ 

buf_addr_msb
    MSB of Buffer address \ ``0x0C``\ 

mcdma_control
    Control field for mcdma \ ``0x10``\ 

vsize_stride
    Vsize and Stride field for mcdma \ ``0x14``\ 

control
    Control field \ ``0x18``\ 

status
    Status field \ ``0x1C``\ 

app
    APP Fields \ ``0x20``\  - 0x30

.. _`xilinx_cdma_desc_hw`:

struct xilinx_cdma_desc_hw
==========================

.. c:type:: struct xilinx_cdma_desc_hw

    Hardware Descriptor

.. _`xilinx_cdma_desc_hw.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_cdma_desc_hw {
        u32 next_desc;
        u32 next_desc_msb;
        u32 src_addr;
        u32 src_addr_msb;
        u32 dest_addr;
        u32 dest_addr_msb;
        u32 control;
        u32 status;
    }

.. _`xilinx_cdma_desc_hw.members`:

Members
-------

next_desc
    Next Descriptor Pointer \ ``0x00``\ 

next_desc_msb
    Next Descriptor Pointer MSB \ ``0x04``\ 

src_addr
    Source address \ ``0x08``\ 

src_addr_msb
    Source address MSB \ ``0x0C``\ 

dest_addr
    Destination address \ ``0x10``\ 

dest_addr_msb
    Destination address MSB \ ``0x14``\ 

control
    Control field \ ``0x18``\ 

status
    Status field \ ``0x1C``\ 

.. _`xilinx_vdma_tx_segment`:

struct xilinx_vdma_tx_segment
=============================

.. c:type:: struct xilinx_vdma_tx_segment

    Descriptor segment

.. _`xilinx_vdma_tx_segment.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_vdma_tx_segment {
        struct xilinx_vdma_desc_hw hw;
        struct list_head node;
        dma_addr_t phys;
    }

.. _`xilinx_vdma_tx_segment.members`:

Members
-------

hw
    Hardware descriptor

node
    Node in the descriptor segments list

phys
    Physical address of segment

.. _`xilinx_axidma_tx_segment`:

struct xilinx_axidma_tx_segment
===============================

.. c:type:: struct xilinx_axidma_tx_segment

    Descriptor segment

.. _`xilinx_axidma_tx_segment.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_axidma_tx_segment {
        struct xilinx_axidma_desc_hw hw;
        struct list_head node;
        dma_addr_t phys;
    }

.. _`xilinx_axidma_tx_segment.members`:

Members
-------

hw
    Hardware descriptor

node
    Node in the descriptor segments list

phys
    Physical address of segment

.. _`xilinx_cdma_tx_segment`:

struct xilinx_cdma_tx_segment
=============================

.. c:type:: struct xilinx_cdma_tx_segment

    Descriptor segment

.. _`xilinx_cdma_tx_segment.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_cdma_tx_segment {
        struct xilinx_cdma_desc_hw hw;
        struct list_head node;
        dma_addr_t phys;
    }

.. _`xilinx_cdma_tx_segment.members`:

Members
-------

hw
    Hardware descriptor

node
    Node in the descriptor segments list

phys
    Physical address of segment

.. _`xilinx_dma_tx_descriptor`:

struct xilinx_dma_tx_descriptor
===============================

.. c:type:: struct xilinx_dma_tx_descriptor

    Per Transaction structure

.. _`xilinx_dma_tx_descriptor.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_dma_tx_descriptor {
        struct dma_async_tx_descriptor async_tx;
        struct list_head segments;
        struct list_head node;
        bool cyclic;
    }

.. _`xilinx_dma_tx_descriptor.members`:

Members
-------

async_tx
    Async transaction descriptor

segments
    TX segments list

node
    Node in the channel descriptors list

cyclic
    Check for cyclic transfers.

.. _`xilinx_dma_chan`:

struct xilinx_dma_chan
======================

.. c:type:: struct xilinx_dma_chan

    Driver specific DMA channel structure

.. _`xilinx_dma_chan.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_dma_chan {
        struct xilinx_dma_device *xdev;
        u32 ctrl_offset;
        u32 desc_offset;
        spinlock_t lock;
        struct list_head pending_list;
        struct list_head active_list;
        struct list_head done_list;
        struct list_head free_seg_list;
        struct dma_chan common;
        struct dma_pool *desc_pool;
        struct device *dev;
        int irq;
        int id;
        enum dma_transfer_direction direction;
        int num_frms;
        bool has_sg;
        bool cyclic;
        bool genlock;
        bool err;
        bool idle;
        struct tasklet_struct tasklet;
        struct xilinx_vdma_config config;
        bool flush_on_fsync;
        u32 desc_pendingcount;
        bool ext_addr;
        u32 desc_submitcount;
        u32 residue;
        struct xilinx_axidma_tx_segment *seg_v;
        dma_addr_t seg_p;
        struct xilinx_axidma_tx_segment *cyclic_seg_v;
        dma_addr_t cyclic_seg_p;
        void (*start_transfer)(struct xilinx_dma_chan *chan);
        int (*stop_transfer)(struct xilinx_dma_chan *chan);
        u16 tdest;
        bool has_vflip;
    }

.. _`xilinx_dma_chan.members`:

Members
-------

xdev
    Driver specific device structure

ctrl_offset
    Control registers offset

desc_offset
    TX descriptor registers offset

lock
    Descriptor operation lock

pending_list
    Descriptors waiting

active_list
    Descriptors ready to submit

done_list
    Complete descriptors

free_seg_list
    Free descriptors

common
    DMA common channel

desc_pool
    Descriptors pool

dev
    The dma device

irq
    Channel IRQ

id
    Channel ID

direction
    Transfer direction

num_frms
    Number of frames

has_sg
    Support scatter transfers

cyclic
    Check for cyclic transfers.

genlock
    Support genlock mode

err
    Channel has errors

idle
    Check for channel idle

tasklet
    Cleanup work after irq

config
    Device configuration info

flush_on_fsync
    Flush on Frame sync

desc_pendingcount
    Descriptor pending count

ext_addr
    Indicates 64 bit addressing is supported by dma channel

desc_submitcount
    Descriptor h/w submitted count

residue
    Residue for AXI DMA

seg_v
    Statically allocated segments base

seg_p
    Physical allocated segments base

cyclic_seg_v
    Statically allocated segment base for cyclic transfers

cyclic_seg_p
    Physical allocated segments base for cyclic dma

start_transfer
    Differentiate b/w DMA IP's transfer

stop_transfer
    Differentiate b/w DMA IP's quiesce

tdest
    TDEST value for mcdma

has_vflip
    S2MM vertical flip

.. _`xdma_ip_type`:

enum xdma_ip_type
=================

.. c:type:: enum xdma_ip_type

    DMA IP type.

.. _`xdma_ip_type.definition`:

Definition
----------

.. code-block:: c

    enum xdma_ip_type {
        XDMA_TYPE_AXIDMA,
        XDMA_TYPE_CDMA,
        XDMA_TYPE_VDMA
    };

.. _`xdma_ip_type.constants`:

Constants
---------

XDMA_TYPE_AXIDMA
    Axi dma ip.

XDMA_TYPE_CDMA
    Axi cdma ip.

XDMA_TYPE_VDMA
    Axi vdma ip.

.. _`xilinx_dma_device`:

struct xilinx_dma_device
========================

.. c:type:: struct xilinx_dma_device

    DMA device structure

.. _`xilinx_dma_device.definition`:

Definition
----------

.. code-block:: c

    struct xilinx_dma_device {
        void __iomem *regs;
        struct device *dev;
        struct dma_device common;
        struct xilinx_dma_chan *chan[XILINX_DMA_MAX_CHANS_PER_DEVICE];
        bool has_sg;
        bool mcdma;
        u32 flush_on_fsync;
        bool ext_addr;
        struct platform_device *pdev;
        const struct xilinx_dma_config *dma_config;
        struct clk *axi_clk;
        struct clk *tx_clk;
        struct clk *txs_clk;
        struct clk *rx_clk;
        struct clk *rxs_clk;
        u32 nr_channels;
        u32 chan_id;
    }

.. _`xilinx_dma_device.members`:

Members
-------

regs
    I/O mapped base address

dev
    Device Structure

common
    DMA device structure

chan
    Driver specific DMA channel

has_sg
    Specifies whether Scatter-Gather is present or not

mcdma
    Specifies whether Multi-Channel is present or not

flush_on_fsync
    Flush on frame sync

ext_addr
    Indicates 64 bit addressing is supported by dma device

pdev
    Platform device structure pointer

dma_config
    DMA config structure

axi_clk
    DMA Axi4-lite interace clock

tx_clk
    DMA mm2s clock

txs_clk
    DMA mm2s stream clock

rx_clk
    DMA s2mm clock

rxs_clk
    DMA s2mm stream clock

nr_channels
    Number of channels DMA device supports

chan_id
    DMA channel identifier

.. _`vdma_desc_write_64`:

vdma_desc_write_64
==================

.. c:function:: void vdma_desc_write_64(struct xilinx_dma_chan *chan, u32 reg, u32 value_lsb, u32 value_msb)

    64-bit descriptor write

    :param chan:
        Driver specific VDMA channel
    :type chan: struct xilinx_dma_chan \*

    :param reg:
        Register to write
    :type reg: u32

    :param value_lsb:
        lower address of the descriptor.
    :type value_lsb: u32

    :param value_msb:
        upper address of the descriptor.
    :type value_msb: u32

.. _`vdma_desc_write_64.description`:

Description
-----------

Since vdma driver is trying to write to a register offset which is not a
multiple of 64 bits(ex : 0x5c), we are writing as two separate 32 bits
instead of a single 64 bit register write.

.. _`xilinx_vdma_alloc_tx_segment`:

xilinx_vdma_alloc_tx_segment
============================

.. c:function:: struct xilinx_vdma_tx_segment *xilinx_vdma_alloc_tx_segment(struct xilinx_dma_chan *chan)

    Allocate transaction segment

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_vdma_alloc_tx_segment.return`:

Return
------

The allocated segment on success and NULL on failure.

.. _`xilinx_cdma_alloc_tx_segment`:

xilinx_cdma_alloc_tx_segment
============================

.. c:function:: struct xilinx_cdma_tx_segment *xilinx_cdma_alloc_tx_segment(struct xilinx_dma_chan *chan)

    Allocate transaction segment

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_cdma_alloc_tx_segment.return`:

Return
------

The allocated segment on success and NULL on failure.

.. _`xilinx_axidma_alloc_tx_segment`:

xilinx_axidma_alloc_tx_segment
==============================

.. c:function:: struct xilinx_axidma_tx_segment *xilinx_axidma_alloc_tx_segment(struct xilinx_dma_chan *chan)

    Allocate transaction segment

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_axidma_alloc_tx_segment.return`:

Return
------

The allocated segment on success and NULL on failure.

.. _`xilinx_dma_free_tx_segment`:

xilinx_dma_free_tx_segment
==========================

.. c:function:: void xilinx_dma_free_tx_segment(struct xilinx_dma_chan *chan, struct xilinx_axidma_tx_segment *segment)

    Free transaction segment

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

    :param segment:
        DMA transaction segment
    :type segment: struct xilinx_axidma_tx_segment \*

.. _`xilinx_cdma_free_tx_segment`:

xilinx_cdma_free_tx_segment
===========================

.. c:function:: void xilinx_cdma_free_tx_segment(struct xilinx_dma_chan *chan, struct xilinx_cdma_tx_segment *segment)

    Free transaction segment

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

    :param segment:
        DMA transaction segment
    :type segment: struct xilinx_cdma_tx_segment \*

.. _`xilinx_vdma_free_tx_segment`:

xilinx_vdma_free_tx_segment
===========================

.. c:function:: void xilinx_vdma_free_tx_segment(struct xilinx_dma_chan *chan, struct xilinx_vdma_tx_segment *segment)

    Free transaction segment

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

    :param segment:
        DMA transaction segment
    :type segment: struct xilinx_vdma_tx_segment \*

.. _`xilinx_dma_alloc_tx_descriptor`:

xilinx_dma_alloc_tx_descriptor
==============================

.. c:function:: struct xilinx_dma_tx_descriptor *xilinx_dma_alloc_tx_descriptor(struct xilinx_dma_chan *chan)

    Allocate transaction descriptor

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_alloc_tx_descriptor.return`:

Return
------

The allocated descriptor on success and NULL on failure.

.. _`xilinx_dma_free_tx_descriptor`:

xilinx_dma_free_tx_descriptor
=============================

.. c:function:: void xilinx_dma_free_tx_descriptor(struct xilinx_dma_chan *chan, struct xilinx_dma_tx_descriptor *desc)

    Free transaction descriptor

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

    :param desc:
        DMA transaction descriptor
    :type desc: struct xilinx_dma_tx_descriptor \*

.. _`xilinx_dma_free_desc_list`:

xilinx_dma_free_desc_list
=========================

.. c:function:: void xilinx_dma_free_desc_list(struct xilinx_dma_chan *chan, struct list_head *list)

    Free descriptors list

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

    :param list:
        List to parse and delete the descriptor
    :type list: struct list_head \*

.. _`xilinx_dma_free_descriptors`:

xilinx_dma_free_descriptors
===========================

.. c:function:: void xilinx_dma_free_descriptors(struct xilinx_dma_chan *chan)

    Free channel descriptors

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_free_chan_resources`:

xilinx_dma_free_chan_resources
==============================

.. c:function:: void xilinx_dma_free_chan_resources(struct dma_chan *dchan)

    Free channel resources

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

.. _`xilinx_dma_chan_handle_cyclic`:

xilinx_dma_chan_handle_cyclic
=============================

.. c:function:: void xilinx_dma_chan_handle_cyclic(struct xilinx_dma_chan *chan, struct xilinx_dma_tx_descriptor *desc, unsigned long *flags)

    Cyclic dma callback

    :param chan:
        Driver specific dma channel
    :type chan: struct xilinx_dma_chan \*

    :param desc:
        dma transaction descriptor
    :type desc: struct xilinx_dma_tx_descriptor \*

    :param flags:
        flags for spin lock
    :type flags: unsigned long \*

.. _`xilinx_dma_chan_desc_cleanup`:

xilinx_dma_chan_desc_cleanup
============================

.. c:function:: void xilinx_dma_chan_desc_cleanup(struct xilinx_dma_chan *chan)

    Clean channel descriptors

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_do_tasklet`:

xilinx_dma_do_tasklet
=====================

.. c:function:: void xilinx_dma_do_tasklet(unsigned long data)

    Schedule completion tasklet

    :param data:
        Pointer to the Xilinx DMA channel structure
    :type data: unsigned long

.. _`xilinx_dma_alloc_chan_resources`:

xilinx_dma_alloc_chan_resources
===============================

.. c:function:: int xilinx_dma_alloc_chan_resources(struct dma_chan *dchan)

    Allocate channel resources

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

.. _`xilinx_dma_alloc_chan_resources.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_tx_status`:

xilinx_dma_tx_status
====================

.. c:function:: enum dma_status xilinx_dma_tx_status(struct dma_chan *dchan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    Get DMA transaction status

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param cookie:
        Transaction identifier
    :type cookie: dma_cookie_t

    :param txstate:
        Transaction state
    :type txstate: struct dma_tx_state \*

.. _`xilinx_dma_tx_status.return`:

Return
------

DMA transaction status

.. _`xilinx_dma_stop_transfer`:

xilinx_dma_stop_transfer
========================

.. c:function:: int xilinx_dma_stop_transfer(struct xilinx_dma_chan *chan)

    Halt DMA channel

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_stop_transfer.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_cdma_stop_transfer`:

xilinx_cdma_stop_transfer
=========================

.. c:function:: int xilinx_cdma_stop_transfer(struct xilinx_dma_chan *chan)

    Wait for the current transfer to complete

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_cdma_stop_transfer.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_start`:

xilinx_dma_start
================

.. c:function:: void xilinx_dma_start(struct xilinx_dma_chan *chan)

    Start DMA channel

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_vdma_start_transfer`:

xilinx_vdma_start_transfer
==========================

.. c:function:: void xilinx_vdma_start_transfer(struct xilinx_dma_chan *chan)

    Starts VDMA transfer

    :param chan:
        Driver specific channel struct pointer
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_cdma_start_transfer`:

xilinx_cdma_start_transfer
==========================

.. c:function:: void xilinx_cdma_start_transfer(struct xilinx_dma_chan *chan)

    Starts cdma transfer

    :param chan:
        Driver specific channel struct pointer
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_start_transfer`:

xilinx_dma_start_transfer
=========================

.. c:function:: void xilinx_dma_start_transfer(struct xilinx_dma_chan *chan)

    Starts DMA transfer

    :param chan:
        Driver specific channel struct pointer
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_issue_pending`:

xilinx_dma_issue_pending
========================

.. c:function:: void xilinx_dma_issue_pending(struct dma_chan *dchan)

    Issue pending transactions

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

.. _`xilinx_dma_complete_descriptor`:

xilinx_dma_complete_descriptor
==============================

.. c:function:: void xilinx_dma_complete_descriptor(struct xilinx_dma_chan *chan)

    Mark the active descriptor as complete

    :param chan:
        xilinx DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_complete_descriptor.context`:

Context
-------

hardirq

.. _`xilinx_dma_reset`:

xilinx_dma_reset
================

.. c:function:: int xilinx_dma_reset(struct xilinx_dma_chan *chan)

    Reset DMA channel

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_reset.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_chan_reset`:

xilinx_dma_chan_reset
=====================

.. c:function:: int xilinx_dma_chan_reset(struct xilinx_dma_chan *chan)

    Reset DMA channel and enable interrupts

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_chan_reset.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_irq_handler`:

xilinx_dma_irq_handler
======================

.. c:function:: irqreturn_t xilinx_dma_irq_handler(int irq, void *data)

    DMA Interrupt handler

    :param irq:
        IRQ number
    :type irq: int

    :param data:
        Pointer to the Xilinx DMA channel structure
    :type data: void \*

.. _`xilinx_dma_irq_handler.return`:

Return
------

IRQ_HANDLED/IRQ_NONE

.. _`append_desc_queue`:

append_desc_queue
=================

.. c:function:: void append_desc_queue(struct xilinx_dma_chan *chan, struct xilinx_dma_tx_descriptor *desc)

    Queuing descriptor

    :param chan:
        Driver specific dma channel
    :type chan: struct xilinx_dma_chan \*

    :param desc:
        dma transaction descriptor
    :type desc: struct xilinx_dma_tx_descriptor \*

.. _`xilinx_dma_tx_submit`:

xilinx_dma_tx_submit
====================

.. c:function:: dma_cookie_t xilinx_dma_tx_submit(struct dma_async_tx_descriptor *tx)

    Submit DMA transaction

    :param tx:
        Async transaction descriptor
    :type tx: struct dma_async_tx_descriptor \*

.. _`xilinx_dma_tx_submit.return`:

Return
------

cookie value on success and failure value on error

.. _`xilinx_vdma_dma_prep_interleaved`:

xilinx_vdma_dma_prep_interleaved
================================

.. c:function:: struct dma_async_tx_descriptor *xilinx_vdma_dma_prep_interleaved(struct dma_chan *dchan, struct dma_interleaved_template *xt, unsigned long flags)

    prepare a descriptor for a DMA_SLAVE transaction

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param xt:
        Interleaved template pointer
    :type xt: struct dma_interleaved_template \*

    :param flags:
        transfer ack flags
    :type flags: unsigned long

.. _`xilinx_vdma_dma_prep_interleaved.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`xilinx_cdma_prep_memcpy`:

xilinx_cdma_prep_memcpy
=======================

.. c:function:: struct dma_async_tx_descriptor *xilinx_cdma_prep_memcpy(struct dma_chan *dchan, dma_addr_t dma_dst, dma_addr_t dma_src, size_t len, unsigned long flags)

    prepare descriptors for a memcpy transaction

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param dma_dst:
        destination address
    :type dma_dst: dma_addr_t

    :param dma_src:
        source address
    :type dma_src: dma_addr_t

    :param len:
        transfer length
    :type len: size_t

    :param flags:
        transfer ack flags
    :type flags: unsigned long

.. _`xilinx_cdma_prep_memcpy.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`xilinx_dma_prep_slave_sg`:

xilinx_dma_prep_slave_sg
========================

.. c:function:: struct dma_async_tx_descriptor *xilinx_dma_prep_slave_sg(struct dma_chan *dchan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction direction, unsigned long flags, void *context)

    prepare descriptors for a DMA_SLAVE transaction

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param sgl:
        scatterlist to transfer to/from
    :type sgl: struct scatterlist \*

    :param sg_len:
        number of entries in \ ``scatterlist``\ 
    :type sg_len: unsigned int

    :param direction:
        DMA direction
    :type direction: enum dma_transfer_direction

    :param flags:
        transfer ack flags
    :type flags: unsigned long

    :param context:
        APP words of the descriptor
    :type context: void \*

.. _`xilinx_dma_prep_slave_sg.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`xilinx_dma_prep_dma_cyclic`:

xilinx_dma_prep_dma_cyclic
==========================

.. c:function:: struct dma_async_tx_descriptor *xilinx_dma_prep_dma_cyclic(struct dma_chan *dchan, dma_addr_t buf_addr, size_t buf_len, size_t period_len, enum dma_transfer_direction direction, unsigned long flags)

    prepare descriptors for a DMA_SLAVE transaction

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param buf_addr:
        Physical address of the buffer
    :type buf_addr: dma_addr_t

    :param buf_len:
        Total length of the cyclic buffers
    :type buf_len: size_t

    :param period_len:
        length of individual cyclic buffer
    :type period_len: size_t

    :param direction:
        DMA direction
    :type direction: enum dma_transfer_direction

    :param flags:
        transfer ack flags
    :type flags: unsigned long

.. _`xilinx_dma_prep_dma_cyclic.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`xilinx_dma_prep_interleaved`:

xilinx_dma_prep_interleaved
===========================

.. c:function:: struct dma_async_tx_descriptor *xilinx_dma_prep_interleaved(struct dma_chan *dchan, struct dma_interleaved_template *xt, unsigned long flags)

    prepare a descriptor for a DMA_SLAVE transaction

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param xt:
        Interleaved template pointer
    :type xt: struct dma_interleaved_template \*

    :param flags:
        transfer ack flags
    :type flags: unsigned long

.. _`xilinx_dma_prep_interleaved.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`xilinx_dma_terminate_all`:

xilinx_dma_terminate_all
========================

.. c:function:: int xilinx_dma_terminate_all(struct dma_chan *dchan)

    Halt the channel and free descriptors

    :param dchan:
        Driver specific DMA Channel pointer
    :type dchan: struct dma_chan \*

.. _`xilinx_dma_terminate_all.return`:

Return
------

'0' always.

.. _`xilinx_vdma_channel_set_config`:

xilinx_vdma_channel_set_config
==============================

.. c:function:: int xilinx_vdma_channel_set_config(struct dma_chan *dchan, struct xilinx_vdma_config *cfg)

    Configure VDMA channel Run-time configuration for Axi VDMA, supports: . halt the channel . configure interrupt coalescing and inter-packet delay threshold . start/stop parking . enable genlock

    :param dchan:
        DMA channel
    :type dchan: struct dma_chan \*

    :param cfg:
        VDMA device configuration pointer
    :type cfg: struct xilinx_vdma_config \*

.. _`xilinx_vdma_channel_set_config.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_chan_remove`:

xilinx_dma_chan_remove
======================

.. c:function:: void xilinx_dma_chan_remove(struct xilinx_dma_chan *chan)

    Per Channel remove function

    :param chan:
        Driver specific DMA channel
    :type chan: struct xilinx_dma_chan \*

.. _`xilinx_dma_chan_probe`:

xilinx_dma_chan_probe
=====================

.. c:function:: int xilinx_dma_chan_probe(struct xilinx_dma_device *xdev, struct device_node *node, int chan_id)

    Per Channel Probing It get channel features from the device tree entry and initialize special channel handling routines

    :param xdev:
        Driver specific device structure
    :type xdev: struct xilinx_dma_device \*

    :param node:
        Device node
    :type node: struct device_node \*

    :param chan_id:
        DMA Channel id
    :type chan_id: int

.. _`xilinx_dma_chan_probe.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_child_probe`:

xilinx_dma_child_probe
======================

.. c:function:: int xilinx_dma_child_probe(struct xilinx_dma_device *xdev, struct device_node *node)

    Per child node probe It get number of dma-channels per child node from device-tree and initializes all the channels.

    :param xdev:
        Driver specific device structure
    :type xdev: struct xilinx_dma_device \*

    :param node:
        Device node
    :type node: struct device_node \*

.. _`xilinx_dma_child_probe.return`:

Return
------

0 always.

.. _`of_dma_xilinx_xlate`:

of_dma_xilinx_xlate
===================

.. c:function:: struct dma_chan *of_dma_xilinx_xlate(struct of_phandle_args *dma_spec, struct of_dma *ofdma)

    Translation function

    :param dma_spec:
        Pointer to DMA specifier as found in the device tree
    :type dma_spec: struct of_phandle_args \*

    :param ofdma:
        Pointer to DMA controller data
    :type ofdma: struct of_dma \*

.. _`of_dma_xilinx_xlate.return`:

Return
------

DMA channel pointer on success and NULL on error

.. _`xilinx_dma_probe`:

xilinx_dma_probe
================

.. c:function:: int xilinx_dma_probe(struct platform_device *pdev)

    Driver probe function

    :param pdev:
        Pointer to the platform_device structure
    :type pdev: struct platform_device \*

.. _`xilinx_dma_probe.return`:

Return
------

'0' on success and failure value on error

.. _`xilinx_dma_remove`:

xilinx_dma_remove
=================

.. c:function:: int xilinx_dma_remove(struct platform_device *pdev)

    Driver remove function

    :param pdev:
        Pointer to the platform_device structure
    :type pdev: struct platform_device \*

.. _`xilinx_dma_remove.return`:

Return
------

Always '0'

.. This file was automatic generated / don't edit.

