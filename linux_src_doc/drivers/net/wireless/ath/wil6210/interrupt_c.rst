.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/wil6210/interrupt.c

.. _`wil6210_irq_disable`:

WIL6210_IRQ_DISABLE
===================

.. c:function::  WIL6210_IRQ_DISABLE()

.. _`wil6210_irq_disable.description`:

Description
-----------

There is ISR pseudo-cause register,
dma_rgf->DMA_RGF.PSEUDO_CAUSE.PSEUDO_CAUSE
Its bits represents OR'ed bits from 3 real ISR registers:
TX, RX, and MISC.

Registers may be configured to either "write 1 to clear" or
"clear on read" mode

When handling interrupt, one have to mask/unmask interrupts for the
real ISR registers, or hardware may malfunction.

.. _`wil6210_thread_irq`:

wil6210_thread_irq
==================

.. c:function:: irqreturn_t wil6210_thread_irq(int irq, void *cookie)

    :param irq:
        *undescribed*
    :type irq: int

    :param cookie:
        *undescribed*
    :type cookie: void \*

.. This file was automatic generated / don't edit.

