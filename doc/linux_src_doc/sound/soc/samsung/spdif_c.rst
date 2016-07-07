.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/samsung/spdif.c

.. _`samsung_spdif_info`:

struct samsung_spdif_info
=========================

.. c:type:: struct samsung_spdif_info

    Samsung S/PDIF Controller information

.. _`samsung_spdif_info.definition`:

Definition
----------

.. code-block:: c

    struct samsung_spdif_info {
        spinlock_t lock;
        struct device *dev;
        void __iomem *regs;
        unsigned long clk_rate;
        struct clk *pclk;
        struct clk *sclk;
        u32 saved_clkcon;
        u32 saved_con;
        u32 saved_cstas;
        struct s3c_dma_params *dma_playback;
    }

.. _`samsung_spdif_info.members`:

Members
-------

lock
    Spin lock for S/PDIF.

dev
    The parent device passed to use from the probe.

regs
    The pointer to the device register block.

clk_rate
    Current clock rate for calcurate ratio.

pclk
    The peri-clock pointer for spdif master operation.

sclk
    The source clock pointer for making sync signals.

saved_clkcon
    *undescribed*

saved_con
    *undescribed*

saved_cstas
    *undescribed*

dma_playback
    DMA information for playback channel.

.. This file was automatic generated / don't edit.

