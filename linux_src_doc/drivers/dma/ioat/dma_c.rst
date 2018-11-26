.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ioat/dma.c

.. _`ioat_dma_do_interrupt`:

ioat_dma_do_interrupt
=====================

.. c:function:: irqreturn_t ioat_dma_do_interrupt(int irq, void *data)

    handler used for single vector interrupt mode

    :param irq:
        interrupt id
    :type irq: int

    :param data:
        interrupt data
    :type data: void \*

.. _`ioat_dma_do_interrupt_msix`:

ioat_dma_do_interrupt_msix
==========================

.. c:function:: irqreturn_t ioat_dma_do_interrupt_msix(int irq, void *data)

    handler used for vector-per-channel interrupt mode

    :param irq:
        interrupt id
    :type irq: int

    :param data:
        interrupt data
    :type data: void \*

.. _`ioat_update_pending`:

ioat_update_pending
===================

.. c:function:: void ioat_update_pending(struct ioatdma_chan *ioat_chan)

    log pending descriptors

    :param ioat_chan:
        *undescribed*
    :type ioat_chan: struct ioatdma_chan \*

.. _`ioat_update_pending.description`:

Description
-----------

Check if the number of unsubmitted descriptors has exceeded the
watermark.  Called with prep_lock held

.. _`ioat_check_space_lock`:

ioat_check_space_lock
=====================

.. c:function:: int ioat_check_space_lock(struct ioatdma_chan *ioat_chan, int num_descs)

    verify space and grab ring producer lock

    :param ioat_chan:
        *undescribed*
    :type ioat_chan: struct ioatdma_chan \*

    :param num_descs:
        allocation length
    :type num_descs: int

.. _`__cleanup`:

\__cleanup
==========

.. c:function:: void __cleanup(struct ioatdma_chan *ioat_chan, dma_addr_t phys_complete)

    reclaim used descriptors

    :param ioat_chan:
        *undescribed*
    :type ioat_chan: struct ioatdma_chan \*

    :param phys_complete:
        *undescribed*
    :type phys_complete: dma_addr_t

.. This file was automatic generated / don't edit.

