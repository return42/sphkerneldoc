.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/qcom/bam_dma.c

.. _`bam_addr`:

bam_addr
========

.. c:function:: void __iomem *bam_addr(struct bam_device *bdev, u32 pipe, enum bam_reg reg)

    returns BAM register address

    :param bdev:
        bam device
    :type bdev: struct bam_device \*

    :param pipe:
        pipe instance (ignored when register doesn't have multiple instances)
    :type pipe: u32

    :param reg:
        register enum
    :type reg: enum bam_reg

.. _`bam_reset_channel`:

bam_reset_channel
=================

.. c:function:: void bam_reset_channel(struct bam_chan *bchan)

    Reset individual BAM DMA channel

    :param bchan:
        bam channel
    :type bchan: struct bam_chan \*

.. _`bam_reset_channel.description`:

Description
-----------

This function resets a specific BAM channel

.. _`bam_chan_init_hw`:

bam_chan_init_hw
================

.. c:function:: void bam_chan_init_hw(struct bam_chan *bchan, enum dma_transfer_direction dir)

    Initialize channel hardware

    :param bchan:
        bam channel
    :type bchan: struct bam_chan \*

    :param dir:
        DMA transfer direction
    :type dir: enum dma_transfer_direction

.. _`bam_chan_init_hw.description`:

Description
-----------

This function resets and initializes the BAM channel

.. _`bam_alloc_chan`:

bam_alloc_chan
==============

.. c:function:: int bam_alloc_chan(struct dma_chan *chan)

    Allocate channel resources for DMA channel.

    :param chan:
        specified channel
    :type chan: struct dma_chan \*

.. _`bam_alloc_chan.description`:

Description
-----------

This function allocates the FIFO descriptor memory

.. _`bam_free_chan`:

bam_free_chan
=============

.. c:function:: void bam_free_chan(struct dma_chan *chan)

    Frees dma resources associated with specific channel

    :param chan:
        specified channel
    :type chan: struct dma_chan \*

.. _`bam_free_chan.description`:

Description
-----------

Free the allocated fifo descriptor memory and channel resources

.. _`bam_slave_config`:

bam_slave_config
================

.. c:function:: int bam_slave_config(struct dma_chan *chan, struct dma_slave_config *cfg)

    set slave configuration for channel

    :param chan:
        dma channel
    :type chan: struct dma_chan \*

    :param cfg:
        slave configuration
    :type cfg: struct dma_slave_config \*

.. _`bam_slave_config.description`:

Description
-----------

Sets slave configuration for channel

.. _`bam_prep_slave_sg`:

bam_prep_slave_sg
=================

.. c:function:: struct dma_async_tx_descriptor *bam_prep_slave_sg(struct dma_chan *chan, struct scatterlist *sgl, unsigned int sg_len, enum dma_transfer_direction direction, unsigned long flags, void *context)

    Prep slave sg transaction

    :param chan:
        dma channel
    :type chan: struct dma_chan \*

    :param sgl:
        scatter gather list
    :type sgl: struct scatterlist \*

    :param sg_len:
        length of sg
    :type sg_len: unsigned int

    :param direction:
        DMA transfer direction
    :type direction: enum dma_transfer_direction

    :param flags:
        DMA flags
    :type flags: unsigned long

    :param context:
        transfer context (unused)
    :type context: void \*

.. _`bam_dma_terminate_all`:

bam_dma_terminate_all
=====================

.. c:function:: int bam_dma_terminate_all(struct dma_chan *chan)

    terminate all transactions on a channel

    :param chan:
        bam dma channel
    :type chan: struct dma_chan \*

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

    :param chan:
        dma channel
    :type chan: struct dma_chan \*

.. _`bam_resume`:

bam_resume
==========

.. c:function:: int bam_resume(struct dma_chan *chan)

    Resume DMA channel operations

    :param chan:
        dma channel
    :type chan: struct dma_chan \*

.. _`process_channel_irqs`:

process_channel_irqs
====================

.. c:function:: u32 process_channel_irqs(struct bam_device *bdev)

    processes the channel interrupts

    :param bdev:
        bam controller
    :type bdev: struct bam_device \*

.. _`process_channel_irqs.description`:

Description
-----------

This function processes the channel interrupts

.. _`bam_dma_irq`:

bam_dma_irq
===========

.. c:function:: irqreturn_t bam_dma_irq(int irq, void *data)

    irq handler for bam controller

    :param irq:
        IRQ of interrupt
    :type irq: int

    :param data:
        callback data
    :type data: void \*

.. _`bam_dma_irq.description`:

Description
-----------

IRQ handler for the bam controller

.. _`bam_tx_status`:

bam_tx_status
=============

.. c:function:: enum dma_status bam_tx_status(struct dma_chan *chan, dma_cookie_t cookie, struct dma_tx_state *txstate)

    returns status of transaction

    :param chan:
        dma channel
    :type chan: struct dma_chan \*

    :param cookie:
        transaction cookie
    :type cookie: dma_cookie_t

    :param txstate:
        DMA transaction state
    :type txstate: struct dma_tx_state \*

.. _`bam_tx_status.description`:

Description
-----------

Return status of dma transaction

.. _`bam_apply_new_config`:

bam_apply_new_config
====================

.. c:function:: void bam_apply_new_config(struct bam_chan *bchan, enum dma_transfer_direction dir)

    :param bchan:
        bam dma channel
    :type bchan: struct bam_chan \*

    :param dir:
        DMA direction
    :type dir: enum dma_transfer_direction

.. _`bam_start_dma`:

bam_start_dma
=============

.. c:function:: void bam_start_dma(struct bam_chan *bchan)

    start next transaction

    :param bchan:
        bam dma channel
    :type bchan: struct bam_chan \*

.. _`dma_tasklet`:

dma_tasklet
===========

.. c:function:: void dma_tasklet(unsigned long data)

    DMA IRQ tasklet

    :param data:
        tasklet argument (bam controller structure)
    :type data: unsigned long

.. _`dma_tasklet.description`:

Description
-----------

Sets up next DMA operation and then processes all completed transactions

.. _`bam_issue_pending`:

bam_issue_pending
=================

.. c:function:: void bam_issue_pending(struct dma_chan *chan)

    starts pending transactions

    :param chan:
        dma channel
    :type chan: struct dma_chan \*

.. _`bam_issue_pending.description`:

Description
-----------

Calls tasklet directly which in turn starts any pending transactions

.. _`bam_dma_free_desc`:

bam_dma_free_desc
=================

.. c:function:: void bam_dma_free_desc(struct virt_dma_desc *vd)

    free descriptor memory

    :param vd:
        virtual descriptor
    :type vd: struct virt_dma_desc \*

.. _`bam_init`:

bam_init
========

.. c:function:: int bam_init(struct bam_device *bdev)

    :param bdev:
        bam device
    :type bdev: struct bam_device \*

.. _`bam_init.description`:

Description
-----------

Initialization helper for global bam registers

.. This file was automatic generated / don't edit.

