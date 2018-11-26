.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rapidio/devices/tsi721_dma.c

.. _`tsi721_bdma_msix`:

tsi721_bdma_msix
================

.. c:function:: irqreturn_t tsi721_bdma_msix(int irq, void *ptr)

    MSI-X interrupt handler for BDMA channels

    :param irq:
        Linux interrupt number
    :type irq: int

    :param ptr:
        Pointer to interrupt-specific data (BDMA channel structure)
    :type ptr: void \*

.. _`tsi721_bdma_msix.description`:

Description
-----------

Handles BDMA channel interrupts signaled using MSI-X.

.. This file was automatic generated / don't edit.

