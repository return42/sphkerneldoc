.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-snd-dmaengine-pcm-register:

===============================
devm_snd_dmaengine_pcm_register
===============================

*man devm_snd_dmaengine_pcm_register(9)*

*4.6.0-rc5*

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

Register a dmaengine based PCM device with automatic unregistration when
the device is unregistered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
