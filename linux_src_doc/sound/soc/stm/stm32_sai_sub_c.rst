.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/stm/stm32_sai_sub.c

.. _`stm32_sai_sub_data`:

struct stm32_sai_sub_data
=========================

.. c:type:: struct stm32_sai_sub_data

    private data of SAI sub block (block A or B)

.. _`stm32_sai_sub_data.definition`:

Definition
----------

.. code-block:: c

    struct stm32_sai_sub_data {
        struct platform_device *pdev;
        struct regmap *regmap;
        const struct regmap_config *regmap_config;
        struct snd_dmaengine_dai_dma_data dma_params;
        struct snd_soc_dai_driver *cpu_dai_drv;
        struct snd_soc_dai *cpu_dai;
        struct snd_pcm_substream *substream;
        struct stm32_sai_data *pdata;
        struct device_node *np_sync_provider;
        struct clk *sai_ck;
        dma_addr_t phys_addr;
        unsigned int mclk_rate;
        unsigned int id;
        int dir;
        bool master;
        bool spdif;
        int fmt;
        int sync;
        int synco;
        int synci;
        int fs_length;
        int slots;
        int slot_width;
        int slot_mask;
        int data_size;
        unsigned int spdif_frm_cnt;
        unsigned char spdif_status_bits[SAI_IEC60958_STATUS_BYTES];
    }

.. _`stm32_sai_sub_data.members`:

Members
-------

pdev
    device data pointer

regmap
    SAI register map pointer

regmap_config
    SAI sub block register map configuration pointer

dma_params
    dma configuration data for rx or tx channel

cpu_dai_drv
    DAI driver data pointer

cpu_dai
    DAI runtime data pointer

substream
    PCM substream data pointer

pdata
    SAI block parent data pointer

np_sync_provider
    synchronization provider node

sai_ck
    kernel clock feeding the SAI clock generator

phys_addr
    SAI registers physical base address

mclk_rate
    SAI block master clock frequency (Hz). set at init

id
    SAI sub block id corresponding to sub-block A or B

dir
    SAI block direction (playback or capture). set at init

master
    SAI block mode flag. (true=master, false=slave) set at init

spdif
    SAI S/PDIF iec60958 mode flag. set at init

fmt
    SAI block format. relevant only for custom protocols. set at init

sync
    SAI block synchronization mode. (none, internal or external)

synco
    SAI block ext sync source (provider setting). (none, sub-block A/B)

synci
    SAI block ext sync source (client setting). (SAI sync provider index)

fs_length
    frame synchronization length. depends on protocol settings

slots
    rx or tx slot number

slot_width
    rx or tx slot width in bits

slot_mask
    rx or tx active slots mask. set at init or at runtime

data_size
    PCM data width. corresponds to PCM substream width.

spdif_frm_cnt
    S/PDIF playback frame counter

spdif_status_bits
    S/PDIF status bits

.. This file was automatic generated / don't edit.

