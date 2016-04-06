
.. _API-snd-pcm-set-ops:

===============
snd_pcm_set_ops
===============

*man snd_pcm_set_ops(9)*

*4.6.0-rc1*

set the PCM operators


Synopsis
========

.. c:function:: void snd_pcm_set_ops( struct snd_pcm * pcm, int direction, const struct snd_pcm_ops * ops )

Arguments
=========

``pcm``
    the pcm instance

``direction``
    stream direction, SNDRV_PCM_STREAM_XXX

``ops``
    the operator table


Description
===========

Sets the given PCM operators to the pcm instance.
