.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/stm/stm32_spdifrx.c

.. _`stm32_spdifrx_data`:

struct stm32_spdifrx_data
=========================

.. c:type:: struct stm32_spdifrx_data

    private data of SPDIFRX

.. _`stm32_spdifrx_data.definition`:

Definition
----------

.. code-block:: c

    struct stm32_spdifrx_data {
        struct platform_device *pdev;
        void __iomem *base;
        struct regmap *regmap;
        const struct regmap_config *regmap_conf;
        struct completion cs_completion;
        struct clk *kclk;
        struct snd_dmaengine_dai_dma_data dma_params;
        struct snd_pcm_substream *substream;
        struct snd_dma_buffer *dmab;
        struct dma_chan *ctrl_chan;
        struct dma_async_tx_descriptor *desc;
        struct dma_slave_config slave_config;
        dma_addr_t phys_addr;
        spinlock_t lock;
        unsigned char cs[SPDIFRX_CS_BYTES_NB];
        unsigned char ub[SPDIFRX_UB_BYTES_NB];
        int irq;
        int refcount;
    }

.. _`stm32_spdifrx_data.members`:

Members
-------

pdev
    device data pointer

base
    mmio register base virtual address

regmap
    SPDIFRX register map pointer

regmap_conf
    SPDIFRX register map configuration pointer

cs_completion
    channel status retrieving completion

kclk
    kernel clock feeding the SPDIFRX clock generator

dma_params
    dma configuration data for rx channel

substream
    PCM substream data pointer

dmab
    dma buffer info pointer

ctrl_chan
    dma channel for S/PDIF control bits

desc
    dma async transaction descriptor

slave_config
    dma slave channel runtime config pointer

phys_addr
    SPDIFRX registers physical base address

lock
    synchronization enabling lock

cs
    channel status buffer

ub
    user data buffer

irq
    SPDIFRX interrupt line

refcount
    keep count of opened DMA channels

.. This file was automatic generated / don't edit.

