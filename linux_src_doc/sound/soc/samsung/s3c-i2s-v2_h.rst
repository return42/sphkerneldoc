.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/samsung/s3c-i2s-v2.h

.. _`s3c_i2sv2_info`:

struct s3c_i2sv2_info
=====================

.. c:type:: struct s3c_i2sv2_info

    S3C I2S-V2 information

.. _`s3c_i2sv2_info.definition`:

Definition
----------

.. code-block:: c

    struct s3c_i2sv2_info {
        struct device *dev;
        void __iomem *regs;
        u32 feature;
        struct clk *iis_pclk;
        struct clk *iis_cclk;
        unsigned char master;
        struct snd_dmaengine_dai_dma_data *dma_playback;
        struct snd_dmaengine_dai_dma_data *dma_capture;
        u32 suspend_iismod;
        u32 suspend_iiscon;
        u32 suspend_iispsr;
        unsigned long base;
    }

.. _`s3c_i2sv2_info.members`:

Members
-------

dev
    The parent device passed to use from the probe.

regs
    The pointer to the device registe block.

feature
    Set of bit-flags indicating features of the controller.

iis_pclk
    *undescribed*

iis_cclk
    *undescribed*

master
    True if the I2S core is the I2S bit clock master.

dma_playback
    DMA information for playback channel.

dma_capture
    DMA information for capture channel.

suspend_iismod
    PM save for the IISMOD register.

suspend_iiscon
    PM save for the IISCON register.

suspend_iispsr
    PM save for the IISPSR register.

base
    *undescribed*

.. _`s3c_i2sv2_info.description`:

Description
-----------

This is the private codec state for the hardware associated with an
I2S channel such as the register mappings and clock sources.

.. _`s3c_i2sv2_probe`:

s3c_i2sv2_probe
===============

.. c:function:: int s3c_i2sv2_probe(struct snd_soc_dai *dai, struct s3c_i2sv2_info *i2s, unsigned long base)

    probe for i2s device helper

    :param dai:
        The ASoC DAI structure supplied to the original probe.
    :type dai: struct snd_soc_dai \*

    :param i2s:
        Our local i2s structure to fill in.
    :type i2s: struct s3c_i2sv2_info \*

    :param base:
        The base address for the registers.
    :type base: unsigned long

.. _`s3c_i2sv2_cleanup`:

s3c_i2sv2_cleanup
=================

.. c:function:: void s3c_i2sv2_cleanup(struct snd_soc_dai *dai, struct s3c_i2sv2_info *i2s)

    cleanup resources allocated in s3c_i2sv2_probe

    :param dai:
        The ASoC DAI structure supplied to the original probe.
    :type dai: struct snd_soc_dai \*

    :param i2s:
        Our local i2s structure to fill in.
    :type i2s: struct s3c_i2sv2_info \*

.. _`s3c_i2sv2_register_component`:

s3c_i2sv2_register_component
============================

.. c:function:: int s3c_i2sv2_register_component(struct device *dev, int id, const struct snd_soc_component_driver *cmp_drv, struct snd_soc_dai_driver *dai_drv)

    register component and dai with soc core

    :param dev:
        DAI device
    :type dev: struct device \*

    :param id:
        DAI ID
    :type id: int

    :param cmp_drv:
        *undescribed*
    :type cmp_drv: const struct snd_soc_component_driver \*

    :param dai_drv:
        *undescribed*
    :type dai_drv: struct snd_soc_dai_driver \*

.. _`s3c_i2sv2_register_component.description`:

Description
-----------

Fill in any missing fields and then register the given dai with the
soc core.

.. This file was automatic generated / don't edit.

