.. -*- coding: utf-8; mode: rst -*-

===========================
soc-generic-dmaengine-pcm.c
===========================

.. _`snd_dmaengine_pcm_prepare_slave_config`:

snd_dmaengine_pcm_prepare_slave_config
======================================

.. c:function:: int snd_dmaengine_pcm_prepare_slave_config (struct snd_pcm_substream *substream, struct snd_pcm_hw_params *params, struct dma_slave_config *slave_config)

    Generic prepare_slave_config callback

    :param struct snd_pcm_substream \*substream:
        PCM substream

    :param struct snd_pcm_hw_params \*params:
        hw_params

    :param struct dma_slave_config \*slave_config:
        DMA slave config to prepare


.. _`snd_dmaengine_pcm_prepare_slave_config.description`:

Description
-----------

This function can be used as a generic prepare_slave_config callback for
platforms which make use of the snd_dmaengine_dai_dma_data struct for their
DAI DMA data. Internally the function will first call
snd_hwparams_to_dma_slave_config to fill in the slave config based on the
hw_params, followed by snd_dmaengine_set_config_from_dai_data to fill in the
remaining fields based on the DAI DMA data.


.. _`snd_dmaengine_pcm_register`:

snd_dmaengine_pcm_register
==========================

.. c:function:: int snd_dmaengine_pcm_register (struct device *dev, const struct snd_dmaengine_pcm_config *config, unsigned int flags)

    Register a dmaengine based PCM device

    :param struct device \*dev:
        The parent device for the PCM device

    :param const struct snd_dmaengine_pcm_config \*config:
        Platform specific PCM configuration

    :param unsigned int flags:
        Platform specific quirks


.. _`snd_dmaengine_pcm_unregister`:

snd_dmaengine_pcm_unregister
============================

.. c:function:: void snd_dmaengine_pcm_unregister (struct device *dev)

    Removes a dmaengine based PCM device

    :param struct device \*dev:
        Parent device the PCM was register with


.. _`snd_dmaengine_pcm_unregister.description`:

Description
-----------

Removes a dmaengine based PCM device previously registered with
snd_dmaengine_pcm_register.

