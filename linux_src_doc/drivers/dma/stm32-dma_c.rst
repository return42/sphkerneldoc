.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/stm32-dma.c

.. _`stm32_dma_cfg`:

struct stm32_dma_cfg
====================

.. c:type:: struct stm32_dma_cfg

    STM32 DMA custom configuration

.. _`stm32_dma_cfg.definition`:

Definition
----------

.. code-block:: c

    struct stm32_dma_cfg {
        u32 channel_id;
        u32 request_line;
        u32 stream_config;
        u32 features;
    }

.. _`stm32_dma_cfg.members`:

Members
-------

channel_id
    channel ID

request_line
    DMA request

stream_config
    32bit mask specifying the DMA channel configuration

features
    32bit mask specifying the DMA Feature list

.. This file was automatic generated / don't edit.

