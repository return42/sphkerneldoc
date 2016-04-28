.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-little-endian:

============================
snd_pcm_format_little_endian
============================

*man snd_pcm_format_little_endian(9)*

*4.6.0-rc5*

Check the PCM format is little-endian


Synopsis
========

.. c:function:: int snd_pcm_format_little_endian( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is little-endian, 0 if big-endian, or a
negative error code if endian not specified.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
