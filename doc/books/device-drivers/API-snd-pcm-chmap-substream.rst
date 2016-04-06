
.. _API-snd-pcm-chmap-substream:

=======================
snd_pcm_chmap_substream
=======================

*man snd_pcm_chmap_substream(9)*

*4.6.0-rc1*

get the PCM substream assigned to the given chmap info


Synopsis
========

.. c:function:: struct snd_pcm_substream ⋆ snd_pcm_chmap_substream( struct snd_pcm_chmap * info, unsigned int idx )

Arguments
=========

``info``
    chmap information

``idx``
    the substream number index
