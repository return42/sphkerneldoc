.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-linked:

=====================
snd_pcm_stream_linked
=====================

*man snd_pcm_stream_linked(9)*

*4.6.0-rc5*

Check whether the substream is linked with others


Synopsis
========

.. c:function:: int snd_pcm_stream_linked( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    substream to check


Description
===========

Returns true if the given substream is being linked with others.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
