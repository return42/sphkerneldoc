.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/xilinx/zynqmp_dma.c

.. _`zynqmp_dma_desc_ll`:

struct zynqmp_dma_desc_ll
=========================

.. c:type:: struct zynqmp_dma_desc_ll

    Hw linked list descriptor

.. _`zynqmp_dma_desc_ll.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_dma_desc_ll {
        u64 addr;
        u32 size;
        u32 ctrl;
        u64 nxtdscraddr;
        u64 rsvd;
    }

.. _`zynqmp_dma_desc_ll.members`:

Members
-------

addr
    Buffer address

size
    Size of the buffer

ctrl
    Control word

nxtdscraddr
    Next descriptor base address

rsvd
    Reserved field and for Hw internal use.

.. _`zynqmp_dma_desc_sw`:

struct zynqmp_dma_desc_sw
=========================

.. c:type:: struct zynqmp_dma_desc_sw

    Per Transaction structure

.. _`zynqmp_dma_desc_sw.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_dma_desc_sw {
        u64 src;
        u64 dst;
        u32 len;
        struct list_head node;
        struct list_head tx_list;
        struct dma_async_tx_descriptor async_tx;
        struct zynqmp_dma_desc_ll *src_v;
        dma_addr_t src_p;
        struct zynqmp_dma_desc_ll *dst_v;
        dma_addr_t dst_p;
    }

.. _`zynqmp_dma_desc_sw.members`:

Members
-------

src
    Source address for simple mode dma

dst
    Destination address for simple mode dma

len
    Transfer length for simple mode dma

node
    Node in the channel descriptor list

tx_list
    List head for the current transfer

async_tx
    Async transaction descriptor

src_v
    Virtual address of the src descriptor

src_p
    Physical address of the src descriptor

dst_v
    Virtual address of the dst descriptor

dst_p
    Physical address of the dst descriptor

.. _`zynqmp_dma_chan`:

struct zynqmp_dma_chan
======================

.. c:type:: struct zynqmp_dma_chan

    Driver specific DMA channel structure

.. _`zynqmp_dma_chan.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_dma_chan {
        struct zynqmp_dma_device *zdev;
        void __iomem *regs;
        spinlock_t lock;
        struct list_head pending_list;
        struct list_head free_list;
        struct list_head active_list;
        struct zynqmp_dma_desc_sw *sw_desc_pool;
        struct list_head done_list;
        struct dma_chan common;
        void *desc_pool_v;
        dma_addr_t desc_pool_p;
        u32 desc_free_cnt;
        struct device *dev;
        int irq;
        bool is_dmacoherent;
        struct tasklet_struct tasklet;
        bool idle;
        u32 desc_size;
        bool err;
        u32 bus_width;
        u32 src_burst_len;
        u32 dst_burst_len;
    }

.. _`zynqmp_dma_chan.members`:

Members
-------

zdev
    Driver specific device structure

regs
    Control registers offset

lock
    Descriptor operation lock

pending_list
    Descriptors waiting

free_list
    Descriptors free

active_list
    Descriptors active

sw_desc_pool
    SW descriptor pool

done_list
    Complete descriptors

common
    DMA common channel

desc_pool_v
    Statically allocated descriptor base

desc_pool_p
    Physical allocated descriptor base

desc_free_cnt
    Descriptor available count

dev
    The dma device

irq
    Channel IRQ

is_dmacoherent
    Tells whether dma operations are coherent or not

tasklet
    Cleanup work after irq

idle
    Channel status;

desc_size
    Size of the low level descriptor

err
    Channel has errors

bus_width
    Bus width

src_burst_len
    Source burst length

dst_burst_len
    Dest burst length

.. _`zynqmp_dma_device`:

struct zynqmp_dma_device
========================

.. c:type:: struct zynqmp_dma_device

    DMA device structure

.. _`zynqmp_dma_device.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_dma_device {
        struct device *dev;
        struct dma_device common;
        struct zynqmp_dma_chan *chan;
        struct clk *clk_main;
        struct clk *clk_apb;
    }

.. _`zynqmp_dma_device.members`:

Members
-------

dev
    Device Structure

common
    DMA device structure

chan
    Driver specific DMA channel

clk_main
    Pointer to main clock

clk_apb
    Pointer to apb clock

.. _`zynqmp_dma_update_desc_to_ctrlr`:

zynqmp_dma_update_desc_to_ctrlr
===============================

.. c:function:: void zynqmp_dma_update_desc_to_ctrlr(struct zynqmp_dma_chan *chan, struct zynqmp_dma_desc_sw *desc)

    Updates descriptor to the controller

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA DMA channel pointer

    :param struct zynqmp_dma_desc_sw \*desc:
        Transaction descriptor pointer

.. _`zynqmp_dma_desc_config_eod`:

zynqmp_dma_desc_config_eod
==========================

.. c:function:: void zynqmp_dma_desc_config_eod(struct zynqmp_dma_chan *chan, void *desc)

    Mark the descriptor as end descriptor

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

    :param void \*desc:
        Hw descriptor pointer

.. _`zynqmp_dma_config_sg_ll_desc`:

zynqmp_dma_config_sg_ll_desc
============================

.. c:function:: void zynqmp_dma_config_sg_ll_desc(struct zynqmp_dma_chan *chan, struct zynqmp_dma_desc_ll *sdesc, dma_addr_t src, dma_addr_t dst, size_t len, struct zynqmp_dma_desc_ll *prev)

    Configure the linked list descriptor

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

    :param struct zynqmp_dma_desc_ll \*sdesc:
        Hw descriptor pointer

    :param dma_addr_t src:
        Source buffer address

    :param dma_addr_t dst:
        Destination buffer address

    :param size_t len:
        Transfer length

    :param struct zynqmp_dma_desc_ll \*prev:
        Previous hw descriptor pointer

.. _`zynqmp_dma_init`:

zynqmp_dma_init
===============

.. c:function:: void zynqmp_dma_init(struct zynqmp_dma_chan *chan)

    Initialize the channel

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_tx_submit`:

zynqmp_dma_tx_submit
====================

.. c:function:: dma_cookie_t zynqmp_dma_tx_submit(struct dma_async_tx_descriptor *tx)

    Submit DMA transaction

    :param struct dma_async_tx_descriptor \*tx:
        Async transaction descriptor pointer

.. _`zynqmp_dma_tx_submit.return`:

Return
------

cookie value

.. _`zynqmp_dma_get_descriptor`:

zynqmp_dma_get_descriptor
=========================

.. c:function:: struct zynqmp_dma_desc_sw *zynqmp_dma_get_descriptor(struct zynqmp_dma_chan *chan)

    Get the sw descriptor from the pool

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_get_descriptor.return`:

Return
------

The sw descriptor

.. _`zynqmp_dma_free_descriptor`:

zynqmp_dma_free_descriptor
==========================

.. c:function:: void zynqmp_dma_free_descriptor(struct zynqmp_dma_chan *chan, struct zynqmp_dma_desc_sw *sdesc)

    Issue pending transactions

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

    :param struct zynqmp_dma_desc_sw \*sdesc:
        Transaction descriptor pointer

.. _`zynqmp_dma_free_desc_list`:

zynqmp_dma_free_desc_list
=========================

.. c:function:: void zynqmp_dma_free_desc_list(struct zynqmp_dma_chan *chan, struct list_head *list)

    Free descriptors list

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

    :param struct list_head \*list:
        List to parse and delete the descriptor

.. _`zynqmp_dma_alloc_chan_resources`:

zynqmp_dma_alloc_chan_resources
===============================

.. c:function:: int zynqmp_dma_alloc_chan_resources(struct dma_chan *dchan)

    Allocate channel resources

    :param struct dma_chan \*dchan:
        DMA channel

.. _`zynqmp_dma_alloc_chan_resources.return`:

Return
------

Number of descriptors on success and failure value on error

.. _`zynqmp_dma_start`:

zynqmp_dma_start
================

.. c:function:: void zynqmp_dma_start(struct zynqmp_dma_chan *chan)

    Start DMA channel

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_handle_ovfl_int`:

zynqmp_dma_handle_ovfl_int
==========================

.. c:function:: void zynqmp_dma_handle_ovfl_int(struct zynqmp_dma_chan *chan, u32 status)

    Process the overflow interrupt

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

    :param u32 status:
        Interrupt status value

.. _`zynqmp_dma_device_config`:

zynqmp_dma_device_config
========================

.. c:function:: int zynqmp_dma_device_config(struct dma_chan *dchan, struct dma_slave_config *config)

    Zynqmp dma device configuration

    :param struct dma_chan \*dchan:
        DMA channel

    :param struct dma_slave_config \*config:
        DMA device config

.. _`zynqmp_dma_device_config.return`:

Return
------

0 always

.. _`zynqmp_dma_start_transfer`:

zynqmp_dma_start_transfer
=========================

.. c:function:: void zynqmp_dma_start_transfer(struct zynqmp_dma_chan *chan)

    Initiate the new transfer

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_chan_desc_cleanup`:

zynqmp_dma_chan_desc_cleanup
============================

.. c:function:: void zynqmp_dma_chan_desc_cleanup(struct zynqmp_dma_chan *chan)

    Cleanup the completed descriptors

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel

.. _`zynqmp_dma_complete_descriptor`:

zynqmp_dma_complete_descriptor
==============================

.. c:function:: void zynqmp_dma_complete_descriptor(struct zynqmp_dma_chan *chan)

    Mark the active descriptor as complete

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_issue_pending`:

zynqmp_dma_issue_pending
========================

.. c:function:: void zynqmp_dma_issue_pending(struct dma_chan *dchan)

    Issue pending transactions

    :param struct dma_chan \*dchan:
        DMA channel pointer

.. _`zynqmp_dma_free_descriptors`:

zynqmp_dma_free_descriptors
===========================

.. c:function:: void zynqmp_dma_free_descriptors(struct zynqmp_dma_chan *chan)

    Free channel descriptors

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_free_chan_resources`:

zynqmp_dma_free_chan_resources
==============================

.. c:function:: void zynqmp_dma_free_chan_resources(struct dma_chan *dchan)

    Free channel resources

    :param struct dma_chan \*dchan:
        DMA channel pointer

.. _`zynqmp_dma_reset`:

zynqmp_dma_reset
================

.. c:function:: void zynqmp_dma_reset(struct zynqmp_dma_chan *chan)

    Reset the channel

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_irq_handler`:

zynqmp_dma_irq_handler
======================

.. c:function:: irqreturn_t zynqmp_dma_irq_handler(int irq, void *data)

    ZynqMP DMA Interrupt handler

    :param int irq:
        IRQ number

    :param void \*data:
        Pointer to the ZynqMP DMA channel structure

.. _`zynqmp_dma_irq_handler.return`:

Return
------

IRQ_HANDLED/IRQ_NONE

.. _`zynqmp_dma_do_tasklet`:

zynqmp_dma_do_tasklet
=====================

.. c:function:: void zynqmp_dma_do_tasklet(unsigned long data)

    Schedule completion tasklet

    :param unsigned long data:
        Pointer to the ZynqMP DMA channel structure

.. _`zynqmp_dma_device_terminate_all`:

zynqmp_dma_device_terminate_all
===============================

.. c:function:: int zynqmp_dma_device_terminate_all(struct dma_chan *dchan)

    Aborts all transfers on a channel

    :param struct dma_chan \*dchan:
        DMA channel pointer

.. _`zynqmp_dma_device_terminate_all.return`:

Return
------

Always '0'

.. _`zynqmp_dma_prep_memcpy`:

zynqmp_dma_prep_memcpy
======================

.. c:function:: struct dma_async_tx_descriptor *zynqmp_dma_prep_memcpy(struct dma_chan *dchan, dma_addr_t dma_dst, dma_addr_t dma_src, size_t len, ulong flags)

    prepare descriptors for memcpy transaction

    :param struct dma_chan \*dchan:
        DMA channel

    :param dma_addr_t dma_dst:
        Destination buffer address

    :param dma_addr_t dma_src:
        Source buffer address

    :param size_t len:
        Transfer length

    :param ulong flags:
        transfer ack flags

.. _`zynqmp_dma_prep_memcpy.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`zynqmp_dma_chan_remove`:

zynqmp_dma_chan_remove
======================

.. c:function:: void zynqmp_dma_chan_remove(struct zynqmp_dma_chan *chan)

    Channel remove function

    :param struct zynqmp_dma_chan \*chan:
        ZynqMP DMA channel pointer

.. _`zynqmp_dma_chan_probe`:

zynqmp_dma_chan_probe
=====================

.. c:function:: int zynqmp_dma_chan_probe(struct zynqmp_dma_device *zdev, struct platform_device *pdev)

    Per Channel Probing

    :param struct zynqmp_dma_device \*zdev:
        Driver specific device structure

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`zynqmp_dma_chan_probe.return`:

Return
------

'0' on success and failure value on error

.. _`of_zynqmp_dma_xlate`:

of_zynqmp_dma_xlate
===================

.. c:function:: struct dma_chan *of_zynqmp_dma_xlate(struct of_phandle_args *dma_spec, struct of_dma *ofdma)

    Translation function

    :param struct of_phandle_args \*dma_spec:
        Pointer to DMA specifier as found in the device tree

    :param struct of_dma \*ofdma:
        Pointer to DMA controller data

.. _`of_zynqmp_dma_xlate.return`:

Return
------

DMA channel pointer on success and NULL on error

.. _`zynqmp_dma_suspend`:

zynqmp_dma_suspend
==================

.. c:function:: int __maybe_unused zynqmp_dma_suspend(struct device *dev)

    Suspend method for the driver

    :param struct device \*dev:
        Address of the device structure

.. _`zynqmp_dma_suspend.description`:

Description
-----------

Put the driver into low power mode.

.. _`zynqmp_dma_suspend.return`:

Return
------

0 on success and failure value on error

.. _`zynqmp_dma_resume`:

zynqmp_dma_resume
=================

.. c:function:: int __maybe_unused zynqmp_dma_resume(struct device *dev)

    Resume from suspend

    :param struct device \*dev:
        Address of the device structure

.. _`zynqmp_dma_resume.description`:

Description
-----------

Resume operation after suspend.

.. _`zynqmp_dma_resume.return`:

Return
------

0 on success and failure value on error

.. _`zynqmp_dma_runtime_suspend`:

zynqmp_dma_runtime_suspend
==========================

.. c:function:: int __maybe_unused zynqmp_dma_runtime_suspend(struct device *dev)

    Runtime suspend method for the driver

    :param struct device \*dev:
        Address of the device structure

.. _`zynqmp_dma_runtime_suspend.description`:

Description
-----------

Put the driver into low power mode.

.. _`zynqmp_dma_runtime_suspend.return`:

Return
------

0 always

.. _`zynqmp_dma_runtime_resume`:

zynqmp_dma_runtime_resume
=========================

.. c:function:: int __maybe_unused zynqmp_dma_runtime_resume(struct device *dev)

    Runtime suspend method for the driver

    :param struct device \*dev:
        Address of the device structure

.. _`zynqmp_dma_runtime_resume.description`:

Description
-----------

Put the driver into low power mode.

.. _`zynqmp_dma_runtime_resume.return`:

Return
------

0 always

.. _`zynqmp_dma_probe`:

zynqmp_dma_probe
================

.. c:function:: int zynqmp_dma_probe(struct platform_device *pdev)

    Driver probe function

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`zynqmp_dma_probe.return`:

Return
------

'0' on success and failure value on error

.. _`zynqmp_dma_remove`:

zynqmp_dma_remove
=================

.. c:function:: int zynqmp_dma_remove(struct platform_device *pdev)

    Driver remove function

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`zynqmp_dma_remove.return`:

Return
------

Always '0'

.. This file was automatic generated / don't edit.

