
.. _API-snd-pcm-sgbuf-get-ptr:

=====================
snd_pcm_sgbuf_get_ptr
=====================

*man snd_pcm_sgbuf_get_ptr(9)*

*4.6.0-rc1*

Get the virtual address at the corresponding offset


Synopsis
========

.. c:function:: void ⋆ snd_pcm_sgbuf_get_ptr( struct snd_pcm_substream * substream, unsigned int ofs )

Arguments
=========

``substream``
    PCM substream

``ofs``
    byte offset
