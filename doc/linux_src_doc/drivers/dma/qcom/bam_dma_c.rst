.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/qcom/bam_dma.c

.. _`bam_addr`:

bam_addr
========

.. c:function:: void __iomem *bam_addr(struct bam_device *bdev, u32 pipe, enum bam_reg reg)

    returns BAM register address

    :param struct bam_device \*bdev:
        bam device

    :param u32 pipe:
        pipe instance (ignored when register doesn't have multiple instances)

    :param enum bam_reg reg:
        register enum

.. _`bam_reset_channel`:

bam_reset_channel
=================

.. c:function:: void bam_reset_channel(struct bam_chan *bchan)

    Reset individual BAM DMA channel

    :param struct bam_chan \*bchan:
        bam channel

.. _`bam_reset_channel.description`:

Description
-----------

This function resets a specific BAM channel

.. _`bam_chan_init_hw`:

bam_chan_init_hw
================

.. c:function:: void bam_chan_init_hw(struct bam_chan *bchan, enum dma_transfer_direction dir)

    Initialize channel hardware

    :param struct bam_chan \*bchan:
        bam channel

    :param enum dma_transfer_direction dir:
        *undescribed*

.. _`bam_chan_init_hw.description`:

Description
-----------

This function resets and initializes the BAM channel

.. _`bam_alloc_chan`:

bam_alloc_chan
==============

.. c:function:: int bam_alloc_chan(struct dma_chan *chan)

    Allocate channel resources for DMA channel.

    :param struct dma_chan \*chan:
        specified channel

.. _`bam_alloc_chan.description`:

Description
-----------

This function allocates the FIFO descriptor memory

.. _`bam_free_chan`:

bam_free_chan
=============

.. c:function:: void bam_free_chan(struct dma_chan *chan)

    Frees dma resources associated with specific channel

    :param struct dma_chan \*chan:
        specified channel

.. _`bam_free_chan.description`:

Description
-----------

Free the allocated fifo descriptor memory and channel resources

.. _`bam_slave_config`:

bam_slave_config
================

.. c:function:: int bam_slave_config(struct dma_chan *chan, struct dma_slave_config *cfg)

    set slave configuration for channel

    :param struct dma_chan \*chan:
        dma channel

    :param struct dma_slave_config \*cfg:
        slave configuration

.. _`bam_slave_config.description`:

Description
-----------

Sets slave configuration for channel

.. _`bam_prep_slave_sg`:

bam_prep_slave_sg
=================

.. c:function:: struct dma_async_tx_descriptor *bam_prep_slave_sg(struct dma_chan *chan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction direction, unsigned long flags, void *context)

    Prep slave sg transaction

    :param struct dma_chan \*chan:
        dma channel

    :param struct scatterlist \*sgl:
        scatter gather list

    :param unsigned int sg_len:
        length of sg

    :param enum dma_transfer_direction direction:
        DMA transfer direction

    :param unsigned long flags:
        DMA flags

    :param void \*context:
        transfer context (unused)

.. _`bam_dma_terminate_all`:

bam_dma_terminate_all
=====================

.. c:function:: int bam_dma_terminate_all(struct dma_chan *chan)

    terminate all transactions on a channel

    :param struct dma_chan \*chan:
        *undescribed*

.. _`bam_dma_terminate_all.description`:

Description
-----------

Dequeues and frees all transactions
No callbacks are done

.. _`bam_pause`:

bam_pause
=========

.. c:function:: int bam_pause(struct dma_chan *chan)

    Pause DMA channel

    :param struct dma_chan \*chan:
        dma channel

.. _`bam_resume`:

bam_resume
==========

.. c:function:: int bam_resume(struct dma_chan *chan)

    Resume DMA channel operations

    :param struct dma_chan \*chan:
        dma channel

.. _`process_channel_irqs`:

process_channel_irqs
====================

.. c:function:: u32 process_channel_irqs(struct bam_device *bdev)

    processes the channel interrupts

    :param struct bam_device \*bdev:
        bam controller

.. _`process_channel_irqs.description`:

Description
-----------

This function processes the channel interrupts

.. _`bam_dma_irq`:

bam_dma_irq
===========

.. c:function:: irqreturn_t bam_dma_irq(int irq, void *data)

    irq handler for bam controller

    :param int irq:
        IRQ of interrupt

    :param void \*data:
        callback data

.. _`bam_dma_irq.description`:

Description
-----------

IRQ handler for the bam controller

.. _`bam_tx_status`:

bam_tx_status
=============

.. c:function:: enum dma_status bam_tx_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    returns status of transaction

    :param struct dma_chan \*chan:
        dma channel

    :param dma_cookie_t cookie:
        transaction cookie

    :param struct dma_tx_state \*txstate:
        DMA transaction state

.. _`bam_tx_status.description`:

Description
-----------

Return status of dma transaction

.. _`bam_apply_new_config`:

bam_apply_new_config
====================

.. c:function:: void bam_apply_new_config(struct bam_chan *bchan, enum dma_transfer_direction dir)

    :param struct bam_chan \*bchan:
        bam dma channel

    :param enum dma_transfer_direction dir:
        DMA direction

.. _`bam_start_dma`:

bam_start_dma
=============

.. c:function:: void bam_start_dma(struct bam_chan *bchan)

    start next transaction \ ``bchan``\  - bam dma channel

    :param struct bam_chan \*bchan:
        *undescribed*

.. _`dma_tasklet`:

dma_tasklet
===========

.. c:function:: void dma_tasklet(unsigned long data)

    DMA IRQ tasklet

    :param unsigned long data:
        tasklet argument (bam controller structure)

.. _`dma_tasklet.description`:

Description
-----------

Sets up next DMA operation and then processes all completed transactions

.. _`bam_issue_pending`:

bam_issue_pending
=================

.. c:function:: void bam_issue_pending(struct dma_chan *chan)

    starts pending transactions

    :param struct dma_chan \*chan:
        dma channel

.. _`bam_issue_pending.description`:

Description
-----------

Calls tasklet directly which in turn starts any pending transactions

.. _`bam_dma_free_desc`:

bam_dma_free_desc
=================

.. c:function:: void bam_dma_free_desc(struct virt_dma_desc *vd)

    free descriptor memory

    :param struct virt_dma_desc \*vd:
        virtual descriptor

.. _`bam_init`:

bam_init
========

.. c:function:: int bam_init(struct bam_device *bdev)

    :param struct bam_device \*bdev:
        bam device

.. _`bam_init.description`:

Description
-----------

Initialization helper for global bam registers

.. This file was automatic generated / don't edit.

