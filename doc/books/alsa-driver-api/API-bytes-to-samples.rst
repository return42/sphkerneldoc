.. -*- coding: utf-8; mode: rst -*-

.. _API-bytes-to-samples:

================
bytes_to_samples
================

*man bytes_to_samples(9)*

*4.6.0-rc5*

Unit conversion of the size from bytes to samples


Synopsis
========

.. c:function:: ssize_t bytes_to_samples( struct snd_pcm_runtime * runtime, ssize_t size )

Arguments
=========

``runtime``
    PCM runtime instance

``size``
    size in bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
