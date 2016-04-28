.. -*- coding: utf-8; mode: rst -*-

.. _API-samples-to-bytes:

================
samples_to_bytes
================

*man samples_to_bytes(9)*

*4.6.0-rc5*

Unit conversion of the size from samples to bytes


Synopsis
========

.. c:function:: ssize_t samples_to_bytes( struct snd_pcm_runtime * runtime, ssize_t size )

Arguments
=========

``runtime``
    PCM runtime instance

``size``
    size in samples


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
