.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-sgbuf-get-ptr:

=====================
snd_pcm_sgbuf_get_ptr
=====================

*man snd_pcm_sgbuf_get_ptr(9)*

*4.6.0-rc5*

Get the virtual address at the corresponding offset


Synopsis
========

.. c:function:: void * snd_pcm_sgbuf_get_ptr( struct snd_pcm_substream * substream, unsigned int ofs )

Arguments
=========

``substream``
    PCM substream

``ofs``
    byte offset


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
