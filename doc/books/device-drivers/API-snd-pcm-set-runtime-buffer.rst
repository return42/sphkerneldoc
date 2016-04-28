.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-set-runtime-buffer:

==========================
snd_pcm_set_runtime_buffer
==========================

*man snd_pcm_set_runtime_buffer(9)*

*4.6.0-rc5*

Set the PCM runtime buffer


Synopsis
========

.. c:function:: void snd_pcm_set_runtime_buffer( struct snd_pcm_substream * substream, struct snd_dma_buffer * bufp )

Arguments
=========

``substream``
    PCM substream to set

``bufp``
    the buffer information, NULL to clear


Description
===========

Copy the buffer information to runtime->dma_buffer when ``bufp`` is
non-NULL. Otherwise it clears the current buffer information.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
