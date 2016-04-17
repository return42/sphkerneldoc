.. -*- coding: utf-8; mode: rst -*-

============
s3c-i2s-v2.h
============


.. _`s3c_i2sv2_info`:

struct s3c_i2sv2_info
=====================

.. c:type:: s3c_i2sv2_info

    S3C I2S-V2 information


.. _`s3c_i2sv2_info.definition`:

Definition
----------

.. code-block:: c

  struct s3c_i2sv2_info {
    struct device * dev;
    void __iomem * regs;
    u32 feature;
    unsigned char master;
    struct s3c_dma_params * dma_playback;
    struct s3c_dma_params * dma_capture;
    u32 suspend_iismod;
    u32 suspend_iiscon;
    u32 suspend_iispsr;
  };


.. _`s3c_i2sv2_info.members`:

Members
-------

:``dev``:
    The parent device passed to use from the probe.

:``regs``:
    The pointer to the device registe block.

:``feature``:
    Set of bit-flags indicating features of the controller.

:``master``:
    True if the I2S core is the I2S bit clock master.

:``dma_playback``:
    DMA information for playback channel.

:``dma_capture``:
    DMA information for capture channel.

:``suspend_iismod``:
    PM save for the IISMOD register.

:``suspend_iiscon``:
    PM save for the IISCON register.

:``suspend_iispsr``:
    PM save for the IISPSR register.




.. _`s3c_i2sv2_info.description`:

Description
-----------

This is the private codec state for the hardware associated with an
I2S channel such as the register mappings and clock sources.



.. _`s3c_i2sv2_probe`:

s3c_i2sv2_probe
===============

.. c:function:: int s3c_i2sv2_probe (struct snd_soc_dai *dai, struct s3c_i2sv2_info *i2s, unsigned long base)

    probe for i2s device helper

    :param struct snd_soc_dai \*dai:
        The ASoC DAI structure supplied to the original probe.

    :param struct s3c_i2sv2_info \*i2s:
        Our local i2s structure to fill in.

    :param unsigned long base:
        The base address for the registers.



.. _`s3c_i2sv2_register_component`:

s3c_i2sv2_register_component
============================

.. c:function:: int s3c_i2sv2_register_component (struct device *dev, int id, const struct snd_soc_component_driver *cmp_drv, struct snd_soc_dai_driver *dai_drv)

    register component and dai with soc core

    :param struct device \*dev:
        DAI device

    :param int id:
        DAI ID

    :param const struct snd_soc_component_driver \*cmp_drv:

        *undescribed*

    :param struct snd_soc_dai_driver \*dai_drv:

        *undescribed*



.. _`s3c_i2sv2_register_component.description`:

Description
-----------

Fill in any missing fields and then register the given dai with the
soc core.

