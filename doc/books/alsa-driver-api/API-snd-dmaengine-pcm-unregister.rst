
.. _API-snd-dmaengine-pcm-unregister:

============================
snd_dmaengine_pcm_unregister
============================

*man snd_dmaengine_pcm_unregister(9)*

*4.6.0-rc1*

Removes a dmaengine based PCM device


Synopsis
========

.. c:function:: void snd_dmaengine_pcm_unregister( struct device * dev )

Arguments
=========

``dev``
    Parent device the PCM was register with


Description
===========

Removes a dmaengine based PCM device previously registered with snd_dmaengine_pcm_register.
