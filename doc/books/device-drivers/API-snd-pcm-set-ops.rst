.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-set-ops:

===============
snd_pcm_set_ops
===============

*man snd_pcm_set_ops(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
