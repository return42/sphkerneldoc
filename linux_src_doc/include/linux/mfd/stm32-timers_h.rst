.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/stm32-timers.h

.. _`stm32_timers_dma`:

struct stm32_timers_dma
=======================

.. c:type:: struct stm32_timers_dma

    STM32 timer DMA handling.

.. _`stm32_timers_dma.definition`:

Definition
----------

.. code-block:: c

    struct stm32_timers_dma {
        struct completion completion;
        phys_addr_t phys_base;
        struct mutex lock;
        struct dma_chan *chan;
        struct dma_chan *chans[STM32_TIMERS_MAX_DMAS];
    }

.. _`stm32_timers_dma.members`:

Members
-------

completion
    end of DMA transfer completion

phys_base
    control registers physical base address

lock
    protect DMA access

chan
    DMA channel in use

chans
    DMA channels available for this timer instance

.. This file was automatic generated / don't edit.

