
.. _API-snd-pcm-new-internal:

====================
snd_pcm_new_internal
====================

*man snd_pcm_new_internal(9)*

*4.6.0-rc1*

create a new internal PCM instance


Synopsis
========

.. c:function:: int snd_pcm_new_internal( struct snd_card * card, const char * id, int device, int playback_count, int capture_count, struct snd_pcm ** rpcm )

Arguments
=========

``card``
    the card instance

``id``
    the id string

``device``
    the device index (zero based - shared with normal PCMs)

``playback_count``
    the number of substreams for playback

``capture_count``
    the number of substreams for capture

``rpcm``
    the pointer to store the new pcm instance


Description
===========

Creates a new internal PCM instance with no userspace device or procfs entries. This is used by ASoC Back End PCMs in order to create a PCM that will only be used internally by
kernel drivers. i.e. it cannot be opened by userspace. It provides existing ASoC components drivers with a substream and access to any private data.

The pcm operators have to be set afterwards to the new instance via ``snd_pcm_set_ops``.


Return
======

Zero if successful, or a negative error code on failure.
