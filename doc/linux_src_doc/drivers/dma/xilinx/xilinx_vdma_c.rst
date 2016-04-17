.. -*- coding: utf-8; mode: rst -*-

=============
xilinx_vdma.c
=============


.. _`xilinx_vdma_desc_hw`:

struct xilinx_vdma_desc_hw
==========================

.. c:type:: xilinx_vdma_desc_hw

    Hardware Descriptor


.. _`xilinx_vdma_desc_hw.definition`:

Definition
----------

.. code-block:: c

  struct xilinx_vdma_desc_hw {
    u32 next_desc;
    u32 pad1;
    u32 buf_addr;
    u32 pad2;
    u32 vsize;
    u32 hsize;
    u32 stride;
  };


.. _`xilinx_vdma_desc_hw.members`:

Members
-------

:``next_desc``:
    Next Descriptor Pointer ``0x00``

:``pad1``:
    Reserved ``0x04``

:``buf_addr``:
    Buffer address ``0x08``

:``pad2``:
    Reserved ``0x0C``

:``vsize``:
    Vertical Size ``0x10``

:``hsize``:
    Horizontal Size ``0x14``

:``stride``:
    Number of bytes between the first
    pixels of each horizontal line ``0x18``




.. _`xilinx_vdma_tx_segment`:

struct xilinx_vdma_tx_segment
=============================

.. c:type:: xilinx_vdma_tx_segment

    Descriptor segment


.. _`xilinx_vdma_tx_segment.definition`:

Definition
----------

.. code-block:: c

  struct xilinx_vdma_tx_segment {
    struct xilinx_vdma_desc_hw hw;
    struct list_head node;
    dma_addr_t phys;
  };


.. _`xilinx_vdma_tx_segment.members`:

Members
-------

:``hw``:
    Hardware descriptor

:``node``:
    Node in the descriptor segments list

:``phys``:
    Physical address of segment




.. _`xilinx_vdma_tx_descriptor`:

struct xilinx_vdma_tx_descriptor
================================

.. c:type:: xilinx_vdma_tx_descriptor

    Per Transaction structure


.. _`xilinx_vdma_tx_descriptor.definition`:

Definition
----------

.. code-block:: c

  struct xilinx_vdma_tx_descriptor {
    struct dma_async_tx_descriptor async_tx;
    struct list_head segments;
    struct list_head node;
  };


.. _`xilinx_vdma_tx_descriptor.members`:

Members
-------

:``async_tx``:
    Async transaction descriptor

:``segments``:
    TX segments list

:``node``:
    Node in the channel descriptors list




.. _`xilinx_vdma_chan`:

struct xilinx_vdma_chan
=======================

.. c:type:: xilinx_vdma_chan

    Driver specific VDMA channel structure


.. _`xilinx_vdma_chan.definition`:

Definition
----------

.. code-block:: c

  struct xilinx_vdma_chan {
    struct xilinx_vdma_device * xdev;
    u32 ctrl_offset;
    u32 desc_offset;
    spinlock_t lock;
    struct list_head pending_list;
    struct list_head active_list;
    struct list_head done_list;
    struct dma_chan common;
    struct dma_pool * desc_pool;
    struct device * dev;
    int irq;
    int id;
    enum dma_transfer_direction direction;
    int num_frms;
    bool has_sg;
    bool genlock;
    bool err;
    struct tasklet_struct tasklet;
    struct xilinx_vdma_config config;
    bool flush_on_fsync;
    u32 desc_pendingcount;
  };


.. _`xilinx_vdma_chan.members`:

Members
-------

:``xdev``:
    Driver specific device structure

:``ctrl_offset``:
    Control registers offset

:``desc_offset``:
    TX descriptor registers offset

:``lock``:
    Descriptor operation lock

:``pending_list``:
    Descriptors waiting

:``active_list``:
    Descriptors ready to submit

:``done_list``:
    Complete descriptors

:``common``:
    DMA common channel

:``desc_pool``:
    Descriptors pool

:``dev``:
    The dma device

:``irq``:
    Channel IRQ

:``id``:
    Channel ID

:``direction``:
    Transfer direction

:``num_frms``:
    Number of frames

:``has_sg``:
    Support scatter transfers

:``genlock``:
    Support genlock mode

:``err``:
    Channel has errors

:``tasklet``:
    Cleanup work after irq

:``config``:
    Device configuration info

:``flush_on_fsync``:
    Flush on Frame sync

:``desc_pendingcount``:
    Descriptor pending count




.. _`xilinx_vdma_device`:

struct xilinx_vdma_device
=========================

.. c:type:: xilinx_vdma_device

    VDMA device structure


.. _`xilinx_vdma_device.definition`:

Definition
----------

.. code-block:: c

  struct xilinx_vdma_device {
    void __iomem * regs;
    struct device * dev;
    struct dma_device common;
    struct xilinx_vdma_chan * chan[XILINX_VDMA_MAX_CHANS_PER_DEVICE];
    bool has_sg;
    u32 flush_on_fsync;
  };


.. _`xilinx_vdma_device.members`:

Members
-------

:``regs``:
    I/O mapped base address

:``dev``:
    Device Structure

:``common``:
    DMA device structure

:``chan[XILINX_VDMA_MAX_CHANS_PER_DEVICE]``:
    Driver specific VDMA channel

:``has_sg``:
    Specifies whether Scatter-Gather is present or not

:``flush_on_fsync``:
    Flush on frame sync




.. _`xilinx_vdma_alloc_tx_segment`:

xilinx_vdma_alloc_tx_segment
============================

.. c:function:: struct xilinx_vdma_tx_segment *xilinx_vdma_alloc_tx_segment (struct xilinx_vdma_chan *chan)

    Allocate transaction segment

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_alloc_tx_segment.return`:

Return
------

The allocated segment on success and NULL on failure.



.. _`xilinx_vdma_free_tx_segment`:

xilinx_vdma_free_tx_segment
===========================

.. c:function:: void xilinx_vdma_free_tx_segment (struct xilinx_vdma_chan *chan, struct xilinx_vdma_tx_segment *segment)

    Free transaction segment

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel

    :param struct xilinx_vdma_tx_segment \*segment:
        VDMA transaction segment



.. _`xilinx_vdma_alloc_tx_descriptor`:

xilinx_vdma_alloc_tx_descriptor
===============================

.. c:function:: struct xilinx_vdma_tx_descriptor *xilinx_vdma_alloc_tx_descriptor (struct xilinx_vdma_chan *chan)

    Allocate transaction descriptor

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_alloc_tx_descriptor.return`:

Return
------

The allocated descriptor on success and NULL on failure.



.. _`xilinx_vdma_free_tx_descriptor`:

xilinx_vdma_free_tx_descriptor
==============================

.. c:function:: void xilinx_vdma_free_tx_descriptor (struct xilinx_vdma_chan *chan, struct xilinx_vdma_tx_descriptor *desc)

    Free transaction descriptor

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel

    :param struct xilinx_vdma_tx_descriptor \*desc:
        VDMA transaction descriptor



.. _`xilinx_vdma_free_desc_list`:

xilinx_vdma_free_desc_list
==========================

.. c:function:: void xilinx_vdma_free_desc_list (struct xilinx_vdma_chan *chan, struct list_head *list)

    Free descriptors list

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel

    :param struct list_head \*list:
        List to parse and delete the descriptor



.. _`xilinx_vdma_free_descriptors`:

xilinx_vdma_free_descriptors
============================

.. c:function:: void xilinx_vdma_free_descriptors (struct xilinx_vdma_chan *chan)

    Free channel descriptors

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_free_chan_resources`:

xilinx_vdma_free_chan_resources
===============================

.. c:function:: void xilinx_vdma_free_chan_resources (struct dma_chan *dchan)

    Free channel resources

    :param struct dma_chan \*dchan:
        DMA channel



.. _`xilinx_vdma_chan_desc_cleanup`:

xilinx_vdma_chan_desc_cleanup
=============================

.. c:function:: void xilinx_vdma_chan_desc_cleanup (struct xilinx_vdma_chan *chan)

    Clean channel descriptors

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_do_tasklet`:

xilinx_vdma_do_tasklet
======================

.. c:function:: void xilinx_vdma_do_tasklet (unsigned long data)

    Schedule completion tasklet

    :param unsigned long data:
        Pointer to the Xilinx VDMA channel structure



.. _`xilinx_vdma_alloc_chan_resources`:

xilinx_vdma_alloc_chan_resources
================================

.. c:function:: int xilinx_vdma_alloc_chan_resources (struct dma_chan *dchan)

    Allocate channel resources

    :param struct dma_chan \*dchan:
        DMA channel



.. _`xilinx_vdma_alloc_chan_resources.return`:

Return
------

'0' on success and failure value on error



.. _`xilinx_vdma_tx_status`:

xilinx_vdma_tx_status
=====================

.. c:function:: enum dma_status xilinx_vdma_tx_status (struct dma_chan *dchan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    Get VDMA transaction status

    :param struct dma_chan \*dchan:
        DMA channel

    :param dma_cookie_t cookie:
        Transaction identifier

    :param struct dma_tx_state \*txstate:
        Transaction state



.. _`xilinx_vdma_tx_status.return`:

Return
------

DMA transaction status



.. _`xilinx_vdma_is_running`:

xilinx_vdma_is_running
======================

.. c:function:: bool xilinx_vdma_is_running (struct xilinx_vdma_chan *chan)

    Check if VDMA channel is running

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_is_running.return`:

Return
------

'1' if running, '0' if not.



.. _`xilinx_vdma_is_idle`:

xilinx_vdma_is_idle
===================

.. c:function:: bool xilinx_vdma_is_idle (struct xilinx_vdma_chan *chan)

    Check if VDMA channel is idle

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_is_idle.return`:

Return
------

'1' if idle, '0' if not.



.. _`xilinx_vdma_halt`:

xilinx_vdma_halt
================

.. c:function:: void xilinx_vdma_halt (struct xilinx_vdma_chan *chan)

    Halt VDMA channel

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_start`:

xilinx_vdma_start
=================

.. c:function:: void xilinx_vdma_start (struct xilinx_vdma_chan *chan)

    Start VDMA channel

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_start_transfer`:

xilinx_vdma_start_transfer
==========================

.. c:function:: void xilinx_vdma_start_transfer (struct xilinx_vdma_chan *chan)

    Starts VDMA transfer

    :param struct xilinx_vdma_chan \*chan:
        Driver specific channel struct pointer



.. _`xilinx_vdma_issue_pending`:

xilinx_vdma_issue_pending
=========================

.. c:function:: void xilinx_vdma_issue_pending (struct dma_chan *dchan)

    Issue pending transactions

    :param struct dma_chan \*dchan:
        DMA channel



.. _`xilinx_vdma_complete_descriptor`:

xilinx_vdma_complete_descriptor
===============================

.. c:function:: void xilinx_vdma_complete_descriptor (struct xilinx_vdma_chan *chan)

    Mark the active descriptor as complete

    :param struct xilinx_vdma_chan \*chan:
        xilinx DMA channel



.. _`xilinx_vdma_complete_descriptor.context`:

CONTEXT
-------

hardirq



.. _`xilinx_vdma_reset`:

xilinx_vdma_reset
=================

.. c:function:: int xilinx_vdma_reset (struct xilinx_vdma_chan *chan)

    Reset VDMA channel

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_reset.return`:

Return
------

'0' on success and failure value on error



.. _`xilinx_vdma_chan_reset`:

xilinx_vdma_chan_reset
======================

.. c:function:: int xilinx_vdma_chan_reset (struct xilinx_vdma_chan *chan)

    Reset VDMA channel and enable interrupts

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_chan_reset.return`:

Return
------

'0' on success and failure value on error



.. _`xilinx_vdma_irq_handler`:

xilinx_vdma_irq_handler
=======================

.. c:function:: irqreturn_t xilinx_vdma_irq_handler (int irq, void *data)

    VDMA Interrupt handler

    :param int irq:
        IRQ number

    :param void \*data:
        Pointer to the Xilinx VDMA channel structure



.. _`xilinx_vdma_irq_handler.return`:

Return
------

IRQ_HANDLED/IRQ_NONE



.. _`append_desc_queue`:

append_desc_queue
=================

.. c:function:: void append_desc_queue (struct xilinx_vdma_chan *chan, struct xilinx_vdma_tx_descriptor *desc)

    Queuing descriptor

    :param struct xilinx_vdma_chan \*chan:
        Driver specific dma channel

    :param struct xilinx_vdma_tx_descriptor \*desc:
        dma transaction descriptor



.. _`xilinx_vdma_tx_submit`:

xilinx_vdma_tx_submit
=====================

.. c:function:: dma_cookie_t xilinx_vdma_tx_submit (struct dma_async_tx_descriptor *tx)

    Submit DMA transaction

    :param struct dma_async_tx_descriptor \*tx:
        Async transaction descriptor



.. _`xilinx_vdma_tx_submit.return`:

Return
------

cookie value on success and failure value on error



.. _`xilinx_vdma_dma_prep_interleaved`:

xilinx_vdma_dma_prep_interleaved
================================

.. c:function:: struct dma_async_tx_descriptor *xilinx_vdma_dma_prep_interleaved (struct dma_chan *dchan, struct dma_interleaved_template *xt, unsigned long flags)

    prepare a descriptor for a DMA_SLAVE transaction

    :param struct dma_chan \*dchan:
        DMA channel

    :param struct dma_interleaved_template \*xt:
        Interleaved template pointer

    :param unsigned long flags:
        transfer ack flags



.. _`xilinx_vdma_dma_prep_interleaved.return`:

Return
------

Async transaction descriptor on success and NULL on failure



.. _`xilinx_vdma_terminate_all`:

xilinx_vdma_terminate_all
=========================

.. c:function:: int xilinx_vdma_terminate_all (struct dma_chan *dchan)

    Halt the channel and free descriptors

    :param struct dma_chan \*dchan:

        *undescribed*



.. _`xilinx_vdma_channel_set_config`:

xilinx_vdma_channel_set_config
==============================

.. c:function:: int xilinx_vdma_channel_set_config (struct dma_chan *dchan, struct xilinx_vdma_config *cfg)

    Configure VDMA channel Run-time configuration for Axi VDMA, supports: . halt the channel . configure interrupt coalescing and inter-packet delay threshold . start/stop parking . enable genlock

    :param struct dma_chan \*dchan:
        DMA channel

    :param struct xilinx_vdma_config \*cfg:
        VDMA device configuration pointer



.. _`xilinx_vdma_channel_set_config.return`:

Return
------

'0' on success and failure value on error



.. _`xilinx_vdma_chan_remove`:

xilinx_vdma_chan_remove
=======================

.. c:function:: void xilinx_vdma_chan_remove (struct xilinx_vdma_chan *chan)

    Per Channel remove function

    :param struct xilinx_vdma_chan \*chan:
        Driver specific VDMA channel



.. _`xilinx_vdma_chan_probe`:

xilinx_vdma_chan_probe
======================

.. c:function:: int xilinx_vdma_chan_probe (struct xilinx_vdma_device *xdev, struct device_node *node)

    Per Channel Probing It get channel features from the device tree entry and initialize special channel handling routines

    :param struct xilinx_vdma_device \*xdev:
        Driver specific device structure

    :param struct device_node \*node:
        Device node



.. _`xilinx_vdma_chan_probe.return`:

Return
------

'0' on success and failure value on error



.. _`of_dma_xilinx_xlate`:

of_dma_xilinx_xlate
===================

.. c:function:: struct dma_chan *of_dma_xilinx_xlate (struct of_phandle_args *dma_spec, struct of_dma *ofdma)

    Translation function

    :param struct of_phandle_args \*dma_spec:
        Pointer to DMA specifier as found in the device tree

    :param struct of_dma \*ofdma:
        Pointer to DMA controller data



.. _`of_dma_xilinx_xlate.return`:

Return
------

DMA channel pointer on success and NULL on error



.. _`xilinx_vdma_probe`:

xilinx_vdma_probe
=================

.. c:function:: int xilinx_vdma_probe (struct platform_device *pdev)

    Driver probe function

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure



.. _`xilinx_vdma_probe.return`:

Return
------

'0' on success and failure value on error



.. _`xilinx_vdma_remove`:

xilinx_vdma_remove
==================

.. c:function:: int xilinx_vdma_remove (struct platform_device *pdev)

    Driver remove function

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure



.. _`xilinx_vdma_remove.return`:

Return
------

Always '0'

