.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/stm32-timers.c

.. _`stm32_timers_dma_burst_read`:

stm32_timers_dma_burst_read
===========================

.. c:function:: int stm32_timers_dma_burst_read(struct device *dev, u32 *buf, enum stm32_timers_dmas id, u32 reg, unsigned int num_reg, unsigned int bursts, unsigned long tmo_ms)

    Read from timers registers using DMA.

    :param struct device \*dev:
        reference to stm32_timers MFD device

    :param u32 \*buf:
        DMA'able destination buffer

    :param enum stm32_timers_dmas id:
        stm32_timers_dmas event identifier (ch[1..4], up, trig or com)

    :param u32 reg:
        registers start offset for DMA to read from (like CCRx for capture)

    :param unsigned int num_reg:
        number of registers to read upon each DMA request, starting \ ``reg``\ .

    :param unsigned int bursts:
        number of bursts to read (e.g. like two for pwm period capture)

    :param unsigned long tmo_ms:
        timeout (milliseconds)

.. _`stm32_timers_dma_burst_read.description`:

Description
-----------

Read from STM32 timers registers using DMA on a single event.

.. This file was automatic generated / don't edit.

