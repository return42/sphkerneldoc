.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/stm32-timers.c

.. _`stm32_timers_dma_burst_read`:

stm32_timers_dma_burst_read
===========================

.. c:function:: int stm32_timers_dma_burst_read(struct device *dev, u32 *buf, enum stm32_timers_dmas id, u32 reg, unsigned int num_reg, unsigned int bursts, unsigned long tmo_ms)

    Read from timers registers using DMA.

    :param dev:
        reference to stm32_timers MFD device
    :type dev: struct device \*

    :param buf:
        DMA'able destination buffer
    :type buf: u32 \*

    :param id:
        stm32_timers_dmas event identifier (ch[1..4], up, trig or com)
    :type id: enum stm32_timers_dmas

    :param reg:
        registers start offset for DMA to read from (like CCRx for capture)
    :type reg: u32

    :param num_reg:
        number of registers to read upon each DMA request, starting \ ``reg``\ .
    :type num_reg: unsigned int

    :param bursts:
        number of bursts to read (e.g. like two for pwm period capture)
    :type bursts: unsigned int

    :param tmo_ms:
        timeout (milliseconds)
    :type tmo_ms: unsigned long

.. _`stm32_timers_dma_burst_read.description`:

Description
-----------

Read from STM32 timers registers using DMA on a single event.

.. This file was automatic generated / don't edit.

