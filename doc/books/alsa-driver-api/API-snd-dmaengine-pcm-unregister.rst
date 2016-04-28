.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-unregister:

============================
snd_dmaengine_pcm_unregister
============================

*man snd_dmaengine_pcm_unregister(9)*

*4.6.0-rc5*

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

Removes a dmaengine based PCM device previously registered with
snd_dmaengine_pcm_register.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
