
.. _API-devm-snd-dmaengine-pcm-register:

===============================
devm_snd_dmaengine_pcm_register
===============================

*man devm_snd_dmaengine_pcm_register(9)*

*4.6.0-rc1*

resource managed dmaengine PCM registration


Synopsis
========

.. c:function:: int devm_snd_dmaengine_pcm_register( struct device * dev, const struct snd_dmaengine_pcm_config * config, unsigned int flags )

Arguments
=========

``dev``
    The parent device for the PCM device

``config``
    Platform specific PCM configuration

``flags``
    Platform specific quirks


Description
===========

Register a dmaengine based PCM device with automatic unregistration when the device is unregistered.
