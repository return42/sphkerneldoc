.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-chmap-substream:

=======================
snd_pcm_chmap_substream
=======================

*man snd_pcm_chmap_substream(9)*

*4.6.0-rc5*

get the PCM substream assigned to the given chmap info


Synopsis
========

.. c:function:: struct snd_pcm_substream * snd_pcm_chmap_substream( struct snd_pcm_chmap * info, unsigned int idx )

Arguments
=========

``info``
    chmap information

``idx``
    the substream number index


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
