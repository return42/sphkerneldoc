.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/altera-msgdma.c

.. _`msgdma_extended_desc`:

struct msgdma_extended_desc
===========================

.. c:type:: struct msgdma_extended_desc

    implements an extended descriptor

.. _`msgdma_extended_desc.definition`:

Definition
----------

.. code-block:: c

    struct msgdma_extended_desc {
        u32 read_addr_lo;
        u32 write_addr_lo;
        u32 len;
        u32 burst_seq_num;
        u32 stride;
        u32 read_addr_hi;
        u32 write_addr_hi;
        u32 control;
    }

.. _`msgdma_extended_desc.members`:

Members
-------

read_addr_lo
    data buffer source address low bits

write_addr_lo
    data buffer destination address low bits

len
    the number of bytes to transfer per descriptor

burst_seq_num
    bit 31:24 write burst
    bit 23:16 read burst
    bit 15:00 sequence number

stride
    bit 31:16 write stride
    bit 15:00 read stride

read_addr_hi
    data buffer source address high bits

write_addr_hi
    data buffer destination address high bits

control
    characteristics of the transfer

.. _`msgdma_sw_desc`:

struct msgdma_sw_desc
=====================

.. c:type:: struct msgdma_sw_desc

    implements a sw descriptor

.. _`msgdma_sw_desc.definition`:

Definition
----------

.. code-block:: c

    struct msgdma_sw_desc {
        struct dma_async_tx_descriptor async_tx;
        struct msgdma_extended_desc hw_desc;
        struct list_head node;
        struct list_head tx_list;
    }

.. _`msgdma_sw_desc.members`:

Members
-------

async_tx
    support for the async_tx api

hw_desc
    assosiated HW descriptor

node
    *undescribed*

tx_list
    *undescribed*

.. _`msgdma_device`:

struct msgdma_device
====================

.. c:type:: struct msgdma_device

    DMA device structure

.. _`msgdma_device.definition`:

Definition
----------

.. code-block:: c

    struct msgdma_device {
        spinlock_t lock;
        struct device *dev;
        struct tasklet_struct irq_tasklet;
        struct list_head pending_list;
        struct list_head free_list;
        struct list_head active_list;
        struct list_head done_list;
        u32 desc_free_cnt;
        bool idle;
        struct dma_device dmadev;
        struct dma_chan dmachan;
        dma_addr_t hw_desq;
        struct msgdma_sw_desc *sw_desq;
        unsigned int npendings;
        struct dma_slave_config slave_cfg;
        int irq;
        void __iomem *csr;
        void __iomem *desc;
        void __iomem *resp;
    }

.. _`msgdma_device.members`:

Members
-------

lock
    *undescribed*

dev
    *undescribed*

irq_tasklet
    *undescribed*

pending_list
    *undescribed*

free_list
    *undescribed*

active_list
    *undescribed*

done_list
    *undescribed*

desc_free_cnt
    *undescribed*

idle
    *undescribed*

dmadev
    *undescribed*

dmachan
    *undescribed*

hw_desq
    *undescribed*

sw_desq
    *undescribed*

npendings
    *undescribed*

slave_cfg
    *undescribed*

irq
    *undescribed*

csr
    *undescribed*

desc
    *undescribed*

resp
    *undescribed*

.. _`msgdma_get_descriptor`:

msgdma_get_descriptor
=====================

.. c:function:: struct msgdma_sw_desc *msgdma_get_descriptor(struct msgdma_device *mdev)

    Get the sw descriptor from the pool

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_get_descriptor.return`:

Return
------

The sw descriptor

.. _`msgdma_free_descriptor`:

msgdma_free_descriptor
======================

.. c:function:: void msgdma_free_descriptor(struct msgdma_device *mdev, struct msgdma_sw_desc *desc)

    Issue pending transactions

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

    :param struct msgdma_sw_desc \*desc:
        Transaction descriptor pointer

.. _`msgdma_free_desc_list`:

msgdma_free_desc_list
=====================

.. c:function:: void msgdma_free_desc_list(struct msgdma_device *mdev, struct list_head *list)

    Free descriptors list

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

    :param struct list_head \*list:
        List to parse and delete the descriptor

.. _`msgdma_desc_config`:

msgdma_desc_config
==================

.. c:function:: void msgdma_desc_config(struct msgdma_extended_desc *desc, dma_addr_t dst, dma_addr_t src, size_t len, u32 stride)

    Configure the descriptor

    :param struct msgdma_extended_desc \*desc:
        Hw descriptor pointer

    :param dma_addr_t dst:
        Destination buffer address

    :param dma_addr_t src:
        Source buffer address

    :param size_t len:
        Transfer length

    :param u32 stride:
        *undescribed*

.. _`msgdma_desc_config_eod`:

msgdma_desc_config_eod
======================

.. c:function:: void msgdma_desc_config_eod(struct msgdma_extended_desc *desc)

    Mark the descriptor as end descriptor

    :param struct msgdma_extended_desc \*desc:
        Hw descriptor pointer

.. _`msgdma_tx_submit`:

msgdma_tx_submit
================

.. c:function:: dma_cookie_t msgdma_tx_submit(struct dma_async_tx_descriptor *tx)

    Submit DMA transaction

    :param struct dma_async_tx_descriptor \*tx:
        Async transaction descriptor pointer

.. _`msgdma_tx_submit.return`:

Return
------

cookie value

.. _`msgdma_prep_memcpy`:

msgdma_prep_memcpy
==================

.. c:function:: struct dma_async_tx_descriptor *msgdma_prep_memcpy(struct dma_chan *dchan, dma_addr_t dma_dst, dma_addr_t dma_src, size_t len, ulong flags)

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

.. _`msgdma_prep_memcpy.return`:

Return
------

Async transaction descriptor on success and NULL on failure

.. _`msgdma_prep_slave_sg`:

msgdma_prep_slave_sg
====================

.. c:function:: struct dma_async_tx_descriptor *msgdma_prep_slave_sg(struct dma_chan *dchan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction dir, unsigned long flags, void *context)

    prepare descriptors for a slave sg transaction

    :param struct dma_chan \*dchan:
        DMA channel

    :param struct scatterlist \*sgl:
        Destination scatter list

    :param unsigned int sg_len:
        Number of entries in destination scatter list

    :param enum dma_transfer_direction dir:
        DMA transfer direction

    :param unsigned long flags:
        transfer ack flags

    :param void \*context:
        transfer context (unused)

.. _`msgdma_copy_desc_to_fifo`:

msgdma_copy_desc_to_fifo
========================

.. c:function:: void msgdma_copy_desc_to_fifo(struct msgdma_device *mdev, struct msgdma_sw_desc *desc)

    copy descriptor(s) into controller FIFO

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

    :param struct msgdma_sw_desc \*desc:
        Transaction descriptor pointer

.. _`msgdma_start_transfer`:

msgdma_start_transfer
=====================

.. c:function:: void msgdma_start_transfer(struct msgdma_device *mdev)

    Initiate the new transfer

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_issue_pending`:

msgdma_issue_pending
====================

.. c:function:: void msgdma_issue_pending(struct dma_chan *chan)

    Issue pending transactions

    :param struct dma_chan \*chan:
        DMA channel pointer

.. _`msgdma_chan_desc_cleanup`:

msgdma_chan_desc_cleanup
========================

.. c:function:: void msgdma_chan_desc_cleanup(struct msgdma_device *mdev)

    Cleanup the completed descriptors

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_complete_descriptor`:

msgdma_complete_descriptor
==========================

.. c:function:: void msgdma_complete_descriptor(struct msgdma_device *mdev)

    Mark the active descriptor as complete

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_free_descriptors`:

msgdma_free_descriptors
=======================

.. c:function:: void msgdma_free_descriptors(struct msgdma_device *mdev)

    Free channel descriptors

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_free_chan_resources`:

msgdma_free_chan_resources
==========================

.. c:function:: void msgdma_free_chan_resources(struct dma_chan *dchan)

    Free channel resources

    :param struct dma_chan \*dchan:
        DMA channel pointer

.. _`msgdma_alloc_chan_resources`:

msgdma_alloc_chan_resources
===========================

.. c:function:: int msgdma_alloc_chan_resources(struct dma_chan *dchan)

    Allocate channel resources

    :param struct dma_chan \*dchan:
        DMA channel

.. _`msgdma_alloc_chan_resources.return`:

Return
------

Number of descriptors on success and failure value on error

.. _`msgdma_tasklet`:

msgdma_tasklet
==============

.. c:function:: void msgdma_tasklet(unsigned long data)

    Schedule completion tasklet

    :param unsigned long data:
        Pointer to the Altera sSGDMA channel structure

.. _`msgdma_irq_handler`:

msgdma_irq_handler
==================

.. c:function:: irqreturn_t msgdma_irq_handler(int irq, void *data)

    Altera mSGDMA Interrupt handler

    :param int irq:
        IRQ number

    :param void \*data:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_irq_handler.return`:

Return
------

IRQ_HANDLED/IRQ_NONE

.. _`msgdma_dev_remove`:

msgdma_dev_remove
=================

.. c:function:: void msgdma_dev_remove(struct msgdma_device *mdev)

    Channel remove function

    :param struct msgdma_device \*mdev:
        Pointer to the Altera mSGDMA device structure

.. _`msgdma_probe`:

msgdma_probe
============

.. c:function:: int msgdma_probe(struct platform_device *pdev)

    Driver probe function

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`msgdma_probe.return`:

Return
------

'0' on success and failure value on error

.. _`msgdma_remove`:

msgdma_remove
=============

.. c:function:: int msgdma_remove(struct platform_device *pdev)

    Driver remove function

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`msgdma_remove.return`:

Return
------

Always '0'

.. This file was automatic generated / don't edit.

