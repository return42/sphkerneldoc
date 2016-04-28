.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-sgbuf-get-chunk-size:

============================
snd_pcm_sgbuf_get_chunk_size
============================

*man snd_pcm_sgbuf_get_chunk_size(9)*

*4.6.0-rc5*

Compute the max size that fits within the contig. page from the given
size


Synopsis
========

.. c:function:: unsigned int snd_pcm_sgbuf_get_chunk_size( struct snd_pcm_substream * substream, unsigned int ofs, unsigned int size )

Arguments
=========

``substream``
    PCM substream

``ofs``
    byte offset

``size``
    byte size to examine


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
