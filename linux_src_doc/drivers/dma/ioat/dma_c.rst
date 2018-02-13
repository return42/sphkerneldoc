.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ioat/dma.c

.. _`ioat_dma_do_interrupt`:

ioat_dma_do_interrupt
=====================

.. c:function:: irqreturn_t ioat_dma_do_interrupt(int irq, void *data)

    handler used for single vector interrupt mode

    :param int irq:
        interrupt id

    :param void \*data:
        interrupt data

.. _`ioat_dma_do_interrupt_msix`:

ioat_dma_do_interrupt_msix
==========================

.. c:function:: irqreturn_t ioat_dma_do_interrupt_msix(int irq, void *data)

    handler used for vector-per-channel interrupt mode

    :param int irq:
        interrupt id

    :param void \*data:
        interrupt data

.. _`ioat_update_pending`:

ioat_update_pending
===================

.. c:function:: void ioat_update_pending(struct ioatdma_chan *ioat_chan)

    log pending descriptors

    :param struct ioatdma_chan \*ioat_chan:
        *undescribed*

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

    :param struct ioatdma_chan \*ioat_chan:
        *undescribed*

    :param int num_descs:
        allocation length

.. _`__cleanup`:

\__cleanup
==========

.. c:function:: void __cleanup(struct ioatdma_chan *ioat_chan, dma_addr_t phys_complete)

    reclaim used descriptors

    :param struct ioatdma_chan \*ioat_chan:
        *undescribed*

    :param dma_addr_t phys_complete:
        *undescribed*

.. This file was automatic generated / don't edit.

