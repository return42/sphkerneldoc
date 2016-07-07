.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/samsung/pcm.c

.. _`s3c_pcm_info`:

struct s3c_pcm_info
===================

.. c:type:: struct s3c_pcm_info

    S3C PCM Controller information

.. _`s3c_pcm_info.definition`:

Definition
----------

.. code-block:: c

    struct s3c_pcm_info {
        spinlock_t lock;
        struct device *dev;
        void __iomem *regs;
        unsigned int sclk_per_fs;
        unsigned int idleclk;
        struct clk *pclk;
        struct clk *cclk;
        struct s3c_dma_params *dma_playback;
        struct s3c_dma_params *dma_capture;
    }

.. _`s3c_pcm_info.members`:

Members
-------

lock
    *undescribed*

dev
    The parent device passed to use from the probe.

regs
    The pointer to the device register block.

sclk_per_fs
    *undescribed*

idleclk
    *undescribed*

pclk
    *undescribed*

cclk
    *undescribed*

dma_playback
    DMA information for playback channel.

dma_capture
    DMA information for capture channel.

.. This file was automatic generated / don't edit.

