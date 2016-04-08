
.. _API-snd-dmaengine-pcm-register:

==========================
snd_dmaengine_pcm_register
==========================

*man snd_dmaengine_pcm_register(9)*

*4.6.0-rc1*

Register a dmaengine based PCM device


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_register( struct device * dev, const struct snd_dmaengine_pcm_config * config, unsigned int flags )

Arguments
=========

``dev``
    The parent device for the PCM device

``config``
    Platform specific PCM configuration

``flags``
    Platform specific quirks
