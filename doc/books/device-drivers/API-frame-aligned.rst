.. -*- coding: utf-8; mode: rst -*-

.. _API-frame-aligned:

=============
frame_aligned
=============

*man frame_aligned(9)*

*4.6.0-rc5*

Check whether the byte size is aligned to frames


Synopsis
========

.. c:function:: int frame_aligned( struct snd_pcm_runtime * runtime, ssize_t bytes )

Arguments
=========

``runtime``
    PCM runtime instance

``bytes``
    size in bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
